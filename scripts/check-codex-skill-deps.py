#!/usr/bin/env python3
"""Check whether external dependencies required by workspace Codex skills are configured."""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_MCP = (
    "notion-cigro",
    "linear",
    "nexus-os",
    "google-workspace",
    "playwright",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mcp-list-file",
        type=Path,
        help="Read captured `codex mcp list` output instead of invoking Codex.",
    )
    parser.add_argument(
        "--teams-env-file",
        type=Path,
        default=ROOT / ".env.teams",
        help="Teams environment file; only variable names and non-empty state are inspected.",
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    return parser.parse_args()


def read_mcp_list(path: Path = None) -> str:
    if path:
        return path.read_text(encoding="utf-8")

    result = subprocess.run(
        ["codex", "mcp", "list"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "`codex mcp list` failed")
    return result.stdout


def configured_mcp_servers(content: str) -> Dict[str, bool]:
    configured: Dict[str, bool] = {name: False for name in REQUIRED_MCP}
    for line in content.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        first = stripped.split(None, 1)[0]
        if first in configured:
            configured[first] = bool(re.search(r"\benabled\b", stripped, re.IGNORECASE))
    return configured


def configured_teams(path: Path) -> bool:
    if not path.is_file():
        return False

    keys: Dict[str, bool] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        keys[key.strip()] = bool(value.strip())

    has_flow = keys.get("TEAMS_FLOW_URL", False)
    has_dev_chat = any(
        key.startswith("TEAMS_CHAT_") and key.endswith("_DEV") and present
        for key, present in keys.items()
    )
    return has_flow and has_dev_chat


def build_result(mcp_content: str, teams_env_file: Path) -> Dict[str, object]:
    mcp = configured_mcp_servers(mcp_content)
    dependencies: List[Dict[str, object]] = [
        {"name": name, "configured": mcp[name]} for name in REQUIRED_MCP
    ]
    dependencies.append(
        {"name": "teams-flow", "configured": configured_teams(teams_env_file)}
    )
    return {
        "ready": all(item["configured"] for item in dependencies),
        "dependencies": dependencies,
    }


def main() -> int:
    args = parse_args()
    try:
        mcp_content = read_mcp_list(args.mcp_list_file)
        result = build_result(mcp_content, args.teams_env_file)
    except (OSError, RuntimeError) as exc:
        print("Dependency check failed: {}".format(exc), file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for item in result["dependencies"]:
            status = "configured" if item["configured"] else "missing"
            print("{:<18} {}".format(item["name"], status))
        print("ready              {}".format("yes" if result["ready"] else "no"))
    return 0 if result["ready"] else 1


if __name__ == "__main__":
    sys.exit(main())
