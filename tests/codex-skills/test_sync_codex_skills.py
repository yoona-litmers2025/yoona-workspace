import json
import importlib.util
import re
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "config" / "codex-skills.json"
SYNC_SCRIPT = ROOT / "scripts" / "sync-codex-skills.py"
CHECK_DEPS_SCRIPT = ROOT / "scripts" / "check-codex-skill-deps.py"
RUNTIME = ROOT / ".agents" / "skills" / "_shared" / "codex-runtime.md"

EXPECTED_SKILLS = {
    "change-brief",
    "client-chat",
    "create-srs",
    "daily-scrum",
    "dev-chat",
    "frontend-slides",
    "issue-ticket",
    "kickoff-prep",
    "meeting-note",
    "new-project",
    "nexus-daily",
    "qa-feedback",
    "qa-plan",
    "qa-request",
    "qa-update",
    "setup-workspace",
    "srs-translate",
    "sync-note",
    "to-spec",
    "today-brief",
    "todo",
    "weekly-report",
}

EXPLICIT_ONLY_RISKS = {"critical", "high", "low", "deprecated"}
SECRET_PATTERNS = (
    re.compile(r"Bearer\s+[A-Za-z0-9._~+/=-]{16,}", re.IGNORECASE),
    re.compile(r"(?:sk|ntn|nxs)_[A-Za-z0-9_-]{16,}"),
    re.compile(r"https://[^\s\"']*powerautomate[^\s\"']*sig=", re.IGNORECASE),
)


def load_manifest():
    with MANIFEST.open(encoding="utf-8") as handle:
        return json.load(handle)


class ManifestTests(unittest.TestCase):
    def test_manifest_covers_every_workspace_skill(self):
        manifest = load_manifest()
        entries = manifest["skills"]
        names = [entry["name"] for entry in entries]

        self.assertEqual(22, len(entries))
        self.assertEqual(EXPECTED_SKILLS, set(names))
        self.assertEqual(len(names), len(set(names)))

    def test_manifest_sources_and_metadata_are_valid(self):
        manifest = load_manifest()

        for entry in manifest["skills"]:
            with self.subTest(skill=entry["name"]):
                self.assertRegex(entry["name"], r"^[a-z0-9-]{1,64}$")
                self.assertTrue(entry["description"].startswith("Use when "))
                self.assertLessEqual(len(entry["description"]), 500)
                self.assertTrue((ROOT / entry["source"]).is_file())
                self.assertIn(
                    entry["risk"],
                    {"critical", "high", "medium", "low", "read-only", "deprecated"},
                )
                if entry["risk"] in EXPLICIT_ONLY_RISKS:
                    self.assertFalse(entry["allow_implicit_invocation"])

        total_description_chars = sum(
            len(entry["description"]) for entry in manifest["skills"]
        )
        self.assertLess(total_description_chars, 8000)

    def test_deprecated_commands_are_compatibility_aliases(self):
        entries = {entry["name"]: entry for entry in load_manifest()["skills"]}

        self.assertEqual("to-spec", entries["change-brief"]["replacement"])
        self.assertEqual("qa-update", entries["qa-feedback"]["replacement"])
        self.assertEqual("deprecated", entries["change-brief"]["risk"])
        self.assertEqual("deprecated", entries["qa-feedback"]["risk"])

    def test_runtime_policy_exists_and_covers_required_guards(self):
        content = RUNTIME.read_text(encoding="utf-8")

        self.assertIn("$ARGUMENTS", content)
        self.assertIn("PM Confirm Gate", content)
        self.assertIn("Never bypass", content)
        self.assertIn("semantic operation", content)
        self.assertIn("Do not copy credentials", content)


class GeneratorTests(unittest.TestCase):
    def run_sync(self, output_root: Path, *extra_args: str):
        return subprocess.run(
            [
                "python3",
                str(SYNC_SCRIPT),
                "--manifest",
                str(MANIFEST),
                "--output-root",
                str(output_root),
                *extra_args,
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_generator_creates_valid_adapters_and_metadata(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_root = Path(temp_dir) / "skills"
            result = self.run_sync(output_root)
            self.assertEqual(0, result.returncode, result.stderr)

            manifest = load_manifest()
            for entry in manifest["skills"]:
                with self.subTest(skill=entry["name"]):
                    skill_dir = output_root / entry["name"]
                    skill_md = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
                    openai_yaml = (skill_dir / "agents" / "openai.yaml").read_text(
                        encoding="utf-8"
                    )

                    self.assertRegex(
                        skill_md,
                        rf"\A---\nname: {re.escape(entry['name'])}\ndescription: .+\n---\n",
                    )
                    self.assertIn(entry["source"], skill_md)
                    self.assertIn(".agents/skills/_shared/codex-runtime.md", skill_md)
                    self.assertIn(
                        f"allow_implicit_invocation: {str(entry['allow_implicit_invocation']).lower()}",
                        openai_yaml,
                    )

                    if entry.get("replacement"):
                        self.assertIn(f"${entry['replacement']}", skill_md)

            generated_text = "\n".join(
                path.read_text(encoding="utf-8")
                for path in output_root.rglob("*")
                if path.is_file()
            )
            for pattern in SECRET_PATTERNS:
                self.assertIsNone(pattern.search(generated_text), pattern.pattern)

    def test_generation_is_idempotent_and_check_detects_drift(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_root = Path(temp_dir) / "skills"
            first = self.run_sync(output_root)
            self.assertEqual(0, first.returncode, first.stderr)

            snapshot = {
                path.relative_to(output_root): path.read_bytes()
                for path in output_root.rglob("*")
                if path.is_file()
            }
            second = self.run_sync(output_root)
            self.assertEqual(0, second.returncode, second.stderr)
            self.assertEqual(
                snapshot,
                {
                    path.relative_to(output_root): path.read_bytes()
                    for path in output_root.rglob("*")
                    if path.is_file()
                },
            )

            clean_check = self.run_sync(output_root, "--check")
            self.assertEqual(0, clean_check.returncode, clean_check.stderr)

            adapter = output_root / "dev-chat" / "SKILL.md"
            adapter.write_text(adapter.read_text(encoding="utf-8") + "\nDRIFT\n", encoding="utf-8")
            drift_check = self.run_sync(output_root, "--check")
            self.assertNotEqual(0, drift_check.returncode)
            self.assertIn("dev-chat/SKILL.md", drift_check.stderr)

    def test_source_digest_ignores_credential_rotation(self):
        spec = importlib.util.spec_from_file_location("sync_codex_skills", SYNC_SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        with tempfile.TemporaryDirectory() as temp_dir:
            first = Path(temp_dir) / "first.md"
            second = Path(temp_dir) / "second.md"
            first.write_text("AUTH_TOKEN: nxs_{}\n".format("a" * 16), encoding="utf-8")
            second.write_text("AUTH_TOKEN: nxs_{}\n".format("b" * 16), encoding="utf-8")

            self.assertEqual(module.source_digest(first), module.source_digest(second))


class DependencyCheckerTests(unittest.TestCase):
    MCP_LIST = """\
Name              Command  Args  Env  Cwd  Status   Auth
google-workspace  npx      -     -    -    enabled  Unsupported
playwright        npx      -     -    -    enabled  Unsupported

Name           Url                              Status   Auth
linear         https://mcp.linear.app/mcp       enabled  OAuth
nexus-os       https://nexus.example.test/mcp   enabled  Bearer token
notion-cigro   https://mcp.notion.com/mcp       enabled  OAuth
"""

    def run_checker(self, mcp_content: str, env_content: str):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            mcp_file = temp_path / "mcp-list.txt"
            teams_file = temp_path / ".env.teams"
            mcp_file.write_text(mcp_content, encoding="utf-8")
            teams_file.write_text(env_content, encoding="utf-8")
            return subprocess.run(
                [
                    "python3",
                    str(CHECK_DEPS_SCRIPT),
                    "--mcp-list-file",
                    str(mcp_file),
                    "--teams-env-file",
                    str(teams_file),
                    "--json",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )

    def test_dependency_checker_reports_ready_without_exposing_values(self):
        secret = "https://flow.example.test/run?sig=do-not-print-this"
        result = self.run_checker(
            self.MCP_LIST,
            "TEAMS_FLOW_URL={}\nTEAMS_CHAT_RAYEON_DEV=secret-chat-id\n".format(secret),
        )

        self.assertEqual(0, result.returncode, result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(payload["ready"])
        self.assertTrue(all(item["configured"] for item in payload["dependencies"]))
        self.assertNotIn(secret, result.stdout)
        self.assertNotIn("secret-chat-id", result.stdout)

    def test_dependency_checker_fails_when_required_dependency_is_missing(self):
        result = self.run_checker(
            self.MCP_LIST.replace(
                "linear         https://mcp.linear.app/mcp       enabled  OAuth\n", ""
            ),
            "TEAMS_FLOW_URL=configured\nTEAMS_CHAT_RAYEON_DEV=configured\n",
        )

        self.assertNotEqual(0, result.returncode)
        payload = json.loads(result.stdout)
        linear = next(
            item for item in payload["dependencies"] if item["name"] == "linear"
        )
        self.assertFalse(linear["configured"])
        self.assertFalse(payload["ready"])


if __name__ == "__main__":
    unittest.main()
