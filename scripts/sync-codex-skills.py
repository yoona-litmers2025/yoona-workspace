#!/usr/bin/env python3
"""Generate repo-scoped Codex skill adapters from the workspace manifest."""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Dict, Iterable, List


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "config" / "codex-skills.json"
DEFAULT_OUTPUT_ROOT = ROOT / ".agents" / "skills"
NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
VALID_RISKS = {"critical", "high", "medium", "low", "read-only", "deprecated"}
EXPLICIT_ONLY_RISKS = {"critical", "high", "low", "deprecated"}
SOURCE_SECRET_PATTERNS = (
    re.compile(r"Bearer\\s+[A-Za-z0-9._~+/=-]{16,}", re.IGNORECASE),
    re.compile(r"(?:sk|ntn|nxs)_[A-Za-z0-9_-]{16,}"),
    re.compile(r"https://[^\\s\"']*powerautomate[^\\s\"']*sig=[^\\s\"']+", re.IGNORECASE),
)

MCP_DEPENDENCIES: Dict[str, Dict[str, str]] = {
    "notion-cigro": {
        "description": "Cigro Notion workspace for PM documents, communication, tasks, and action items",
        "transport": "streamable_http",
        "url": "https://mcp.notion.com/mcp",
    },
    "linear": {
        "description": "Linear workspace for issue creation and project tracking",
        "transport": "streamable_http",
        "url": "https://mcp.linear.app/mcp",
    },
    "nexus-os": {
        "description": "Nexus OS project, task, daily-entry, and PM todo operations",
    },
    "google-workspace": {
        "description": "Google Workspace calendar and document operations",
    },
    "playwright": {
        "description": "Playwright browser inspection for read-only QA planning",
    },
}


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def source_digest(path: Path) -> str:
    content = path.read_text(encoding="utf-8")
    for pattern in SOURCE_SECRET_PATTERNS:
        content = pattern.sub("<redacted-credential>", content)
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def read_frontmatter(path: Path) -> Dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return {}

    metadata: Dict[str, str] = {}
    for line in lines[1:]:
        if line == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"')
    return metadata


def load_manifest(path: Path, repo_root: Path) -> List[Dict[str, object]]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError("Unable to read manifest {}: {}".format(path, exc)) from exc

    if payload.get("version") != 1 or not isinstance(payload.get("skills"), list):
        raise ValueError("Manifest must contain version=1 and a skills array")

    entries: List[Dict[str, object]] = payload["skills"]
    seen = set()
    for entry in entries:
        name = entry.get("name")
        description = entry.get("description")
        risk = entry.get("risk")
        source = entry.get("source")
        dependencies = entry.get("dependencies")

        if not isinstance(name, str) or not NAME_RE.fullmatch(name):
            raise ValueError("Invalid skill name: {!r}".format(name))
        if name in seen:
            raise ValueError("Duplicate skill name: {}".format(name))
        seen.add(name)
        if not isinstance(description, str) or not description.startswith("Use when "):
            raise ValueError("{} description must start with 'Use when '".format(name))
        if len(description) > 500:
            raise ValueError("{} description exceeds 500 characters".format(name))
        if risk not in VALID_RISKS:
            raise ValueError("{} has invalid risk {}".format(name, risk))
        if risk in EXPLICIT_ONLY_RISKS and entry.get("allow_implicit_invocation") is not False:
            raise ValueError("{} must disable implicit invocation".format(name))
        if not isinstance(source, str) or not (repo_root / source).is_file():
            raise ValueError("{} source does not exist: {}".format(name, source))
        if not isinstance(dependencies, list):
            raise ValueError("{} dependencies must be an array".format(name))
        unknown = set(dependencies) - set(MCP_DEPENDENCIES) - {"teams-flow"}
        if unknown:
            raise ValueError("{} has unknown dependencies: {}".format(name, sorted(unknown)))
        if risk == "deprecated" and not entry.get("replacement"):
            raise ValueError("{} deprecated adapter needs a replacement".format(name))

    return entries


def dependency_label(dependencies: Iterable[str]) -> str:
    values = list(dependencies)
    return ", ".join(values) if values else "none"


def render_skill(entry: Dict[str, object], repo_root: Path) -> str:
    name = str(entry["name"])
    description = str(entry["description"])
    display_name = str(entry["display_name"])
    source = str(entry["source"])
    digest = source_digest(repo_root / source)
    risk = str(entry["risk"])
    dependencies = [str(value) for value in entry["dependencies"]]
    frontmatter = (
        "---\n"
        "name: {}\n"
        "description: {}\n"
        "---\n".format(name, yaml_string(description))
    )

    if entry.get("replacement"):
        replacement = str(entry["replacement"])
        body = """# {display_name} Compatibility Alias

This adapter preserves an old command name without running the deprecated workflow.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Treat the current request payload as arguments for `${replacement}`.
3. Read `.agents/skills/{replacement}/SKILL.md` completely and follow it.
4. Tell the user that `${name}` was routed to `${replacement}`; do not execute `{source}`.

- Source record: `{source}`
- Source revision: `sha256:{digest}`
- Risk: `{risk}`
- Dependencies: {dependencies}
""".format(
            display_name=display_name,
            replacement=replacement,
            name=name,
            source=source,
            digest=digest,
            risk=risk,
            dependencies=dependency_label(dependencies),
        )
    else:
        source_kind_note = (
            "Resolve the source's supporting resource links from `frontend-slides/`."
            if entry.get("source_kind") == "agent-skill"
            else "Resolve workspace paths from the repository root unless the source says otherwise."
        )
        body = """# {display_name} Codex Adapter

Use the workspace workflow without duplicating its canonical instructions.

1. Read `.agents/skills/_shared/codex-runtime.md` completely.
2. Read `{source}` completely from the repository root before taking task actions.
3. Treat the payload supplied with `${name}` as the source command's `$ARGUMENTS`.
4. {source_kind_note}
5. Follow the source workflow, applying the runtime compatibility and safety rules first when host behavior differs.

- Source revision: `sha256:{digest}`
- Risk: `{risk}`
- Dependencies: {dependencies}
""".format(
            display_name=display_name,
            source=source,
            name=name,
            source_kind_note=source_kind_note,
            digest=digest,
            risk=risk,
            dependencies=dependency_label(dependencies),
        )

    return frontmatter + "\n" + body


def short_description(description: str) -> str:
    value = description[len("Use when ") :]
    value = value[0].upper() + value[1:]
    if len(value) > 120:
        value = value[:117].rstrip() + "..."
    return value


def render_openai_yaml(entry: Dict[str, object], source_path: Path) -> str:
    name = str(entry["name"])
    metadata = read_frontmatter(source_path)
    argument_hint = metadata.get("argument-hint", "")
    prompt = "Use ${}".format(name)
    if argument_hint and not argument_hint.startswith("("):
        prompt += " " + argument_hint

    lines = [
        "interface:",
        "  display_name: {}".format(yaml_string(str(entry["display_name"]))),
        "  short_description: {}".format(
            yaml_string(short_description(str(entry["description"])))
        ),
        "  default_prompt: {}".format(yaml_string(prompt)),
        "policy:",
        "  allow_implicit_invocation: {}".format(
            str(bool(entry["allow_implicit_invocation"])).lower()
        ),
    ]

    mcp_dependencies = [
        dependency
        for dependency in entry["dependencies"]
        if dependency in MCP_DEPENDENCIES
    ]
    if mcp_dependencies:
        lines.extend(["dependencies:", "  tools:"])
        for dependency in mcp_dependencies:
            details = MCP_DEPENDENCIES[str(dependency)]
            lines.extend(
                [
                    '    - type: "mcp"',
                    "      value: {}".format(yaml_string(str(dependency))),
                    "      description: {}".format(yaml_string(details["description"])),
                ]
            )
            if "transport" in details:
                lines.append("      transport: {}".format(yaml_string(details["transport"])))
            if "url" in details:
                lines.append("      url: {}".format(yaml_string(details["url"])))

    return "\n".join(lines) + "\n"


def expected_files(
    entries: Iterable[Dict[str, object]], repo_root: Path
) -> Dict[Path, str]:
    files: Dict[Path, str] = {}
    for entry in entries:
        name = str(entry["name"])
        source_path = repo_root / str(entry["source"])
        files[Path(name) / "SKILL.md"] = render_skill(entry, repo_root)
        files[Path(name) / "agents" / "openai.yaml"] = render_openai_yaml(
            entry, source_path
        )
    return files


def check_output(output_root: Path, files: Dict[Path, str]) -> List[str]:
    drift: List[str] = []
    for relative_path, expected in files.items():
        target = output_root / relative_path
        if not target.is_file() or target.read_text(encoding="utf-8") != expected:
            drift.append(str(relative_path))

    expected_skill_dirs = {path.parts[0] for path in files if path.name == "SKILL.md"}
    if output_root.is_dir():
        for skill_md in output_root.glob("*/SKILL.md"):
            if skill_md.parent.name not in expected_skill_dirs:
                drift.append(str(skill_md.relative_to(output_root)))
    return sorted(set(drift))


def write_output(output_root: Path, files: Dict[Path, str]) -> int:
    changed = 0
    for relative_path, content in files.items():
        target = output_root / relative_path
        if target.is_file() and target.read_text(encoding="utf-8") == content:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        changed += 1
    return changed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail when generated adapters are missing or differ; do not write files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest_path = args.manifest.resolve()
    try:
        entries = load_manifest(manifest_path, ROOT)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    files = expected_files(entries, ROOT)
    output_root = args.output_root.resolve()
    if args.check:
        drift = check_output(output_root, files)
        if drift:
            print("Codex skill adapter drift:", file=sys.stderr)
            for path in drift:
                print("- {}".format(path), file=sys.stderr)
            return 1
        print("Codex skill adapters are synchronized ({} skills).".format(len(entries)))
        return 0

    changed = write_output(output_root, files)
    print(
        "Synchronized {} Codex skills ({} files updated).".format(len(entries), changed)
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
