import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_library import conflict_markers, repository_conflicts, validate


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "example"
        (self.root / ".codex-plugin").mkdir(parents=True)
        (self.root / ".codex-plugin/plugin.json").write_text(json.dumps({"name": "example", "skills": "./skills/"}), encoding="utf-8")
        self.skill = self.root / "skills/check"
        self.skill.mkdir(parents=True)
        self.entry = self.skill / "SKILL.md"
        self.entry.write_text("---\nname: check\ndescription: Check a concrete artifact when verification is requested.\n---\n\n# Check\n", encoding="utf-8")

    def test_valid_standalone_skill(self):
        self.assertEqual(validate(self.root)[0], [])

    def test_package_conflict_outside_skills_fails(self):
        (self.root / "mcp.json").write_text("<<<<<<< HEAD\n=======\n>>>>>>> incoming\n")
        errors, _ = validate(self.root)
        self.assertEqual(sum("unresolved conflict marker" in error for error in errors), 3)

    def add_mcp(self, argument="${PLUGIN_ROOT}/context.yml"):
        manifest_path = self.root / ".codex-plugin/plugin.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["mcpServers"] = "./.mcp.json"
        manifest_path.write_text(json.dumps(manifest))
        (self.root / ".mcp.json").write_text(json.dumps({"mcpServers": {
            "navigation": {"command": "uvx", "args": [argument]}}}))

    def test_mcp_asset_is_packaged(self):
        self.add_mcp()
        (self.root / "context.yml").write_text("prompt: ''")
        self.assertEqual(validate(self.root)[0], [])

    def test_missing_mcp_asset_fails(self):
        self.add_mcp()
        self.assertTrue(any("MCP asset" in e for e in validate(self.root)[0]))

    def test_mcp_asset_cannot_escape_plugin(self):
        (self.root.parent / "outside.yml").write_text("prompt: ''")
        self.add_mcp("${PLUGIN_ROOT}/../outside.yml")
        self.assertTrue(any("MCP asset" in e for e in validate(self.root)[0]))

    def test_missing_mcp_definition_fails(self):
        self.add_mcp()
        (self.root / ".mcp.json").unlink()
        self.assertTrue(validate(self.root)[0])

    def add_portable(self):
        path = self.root / ".codex-plugin/plugin.json"
        compatibility = json.loads(path.read_text())
        compatibility["version"] = "0.2.0"
        path.write_text(json.dumps(compatibility))
        portable = {"$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
                    "name": "example", "version": "0.2.0"}
        (self.root / "plugin.json").write_text(json.dumps(portable))
        return portable

    def test_portable_manifest_matches_compatibility(self):
        self.add_portable()
        self.assertEqual(validate(self.root)[0], [])

    def test_portable_version_drift_fails(self):
        portable = self.add_portable()
        portable["version"] = "0.3.0"
        (self.root / "plugin.json").write_text(json.dumps(portable))
        self.assertTrue(any("version differ" in e for e in validate(self.root)[0]))

    def test_portable_mcp_conventional_discovery_checks_assets(self):
        self.add_portable()
        (self.root / "mcp.json").write_text(json.dumps({"mcpServers": {
            "navigation": {"type": "stdio", "command": "uvx", "args": ["${PLUGIN_ROOT}/context.yml"]}}}))
        self.assertTrue(any("MCP asset" in e for e in validate(self.root)[0]))
        (self.root / "context.yml").write_text("prompt: ''")
        self.assertEqual(validate(self.root)[0], [])

    def test_local_missing_reference_fails(self):
        with self.entry.open("a", encoding="utf-8") as f:
            f.write("[Detail](references/missing.md)\n")
        self.assertTrue(any("missing reference" in e for e in validate(self.root)[0]))

    def test_sibling_dependency_fails_even_when_file_exists(self):
        sibling = self.root / "skills/other"
        sibling.mkdir()
        (sibling / "detail.md").write_text("Shared detail", encoding="utf-8")
        with self.entry.open("a", encoding="utf-8") as f:
            f.write("[Detail](../other/detail.md)\n")
        self.assertTrue(any("nonlocal" in e for e in validate(self.root)[0]))

    def test_encoded_escape_fails(self):
        with self.entry.open("a", encoding="utf-8") as f:
            f.write("[Detail](%2e%2e/outside.md)\n")
        self.assertTrue(any("nonlocal" in e for e in validate(self.root)[0]))

    def test_empty_metadata_fails(self):
        self.entry.write_text("---\nname: check\ndescription:\n---\n", encoding="utf-8")
        self.assertTrue(validate(self.root)[0])

    def test_mismatched_identifier_fails(self):
        self.entry.write_text(self.entry.read_text().replace("name: check", "name: wrong"), encoding="utf-8")
        self.assertTrue(any("mismatched" in e for e in validate(self.root)[0]))

    def test_local_and_https_links_allowed(self):
        (self.skill / "detail.md").write_text("Details", encoding="utf-8")
        with self.entry.open("a", encoding="utf-8") as f:
            f.write("[Local](detail.md#section) and [Web](https://example.org/docs)\n")
        self.assertEqual(validate(self.root)[0], [])


class ConflictTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_bom_crlf_orphan_and_diff3_markers_report_line_numbers(self):
        path = self.root / "checkpoint.md"
        path.write_bytes(b"\xef\xbb\xbf<<<<<<< HEAD\r\n||||||| base\r\n=======\r\n>>>>>>> incoming\r\n========\r\n")
        self.assertEqual(conflict_markers([path]), [
            f"{path}:{number}: unresolved conflict marker" for number in range(1, 6)
        ])

    def test_inline_examples_short_rules_and_binary_are_not_conflicts(self):
        text = self.root / "guide.md"
        text.write_text("Example: <<<<<<< HEAD\n`=======`\n---\n======\n> >>>>>>> incoming\n")
        binary = self.root / "image.bin"
        binary.write_bytes(b"\0\n<<<<<<< HEAD\n")
        self.assertEqual(conflict_markers([text, binary]), [])

    def test_repository_scan_covers_tracked_and_new_files_but_not_ignored_runs(self):
        subprocess.run(["git", "init", "-q", str(self.root)], check=True, capture_output=True)
        (self.root / ".gitignore").write_text(".eval-runs/\n")
        docs = self.root / "docs"
        docs.mkdir()
        tracked = docs / "checkpoint.md"
        tracked.write_text("settled\n")
        subprocess.run(["git", "-C", str(self.root), "add", "."], check=True, capture_output=True)
        tracked.write_text("<<<<<<< HEAD\n")
        new = self.root / "new script.py"
        new.write_text("=======\n")
        ignored = self.root / ".eval-runs"
        ignored.mkdir()
        (ignored / "old.md").write_text(">>>>>>> old\n")
        self.assertEqual(repository_conflicts(self.root), [
            f"{tracked}:1: unresolved conflict marker",
            f"{new}:1: unresolved conflict marker",
        ])
        tracked.write_text("resolved\n")
        new.write_text("resolved\n")
        self.assertEqual(repository_conflicts(self.root), [])

    def test_repository_scan_failure_is_not_a_clean_pass(self):
        self.assertTrue(repository_conflicts(self.root))


if __name__ == "__main__":
    unittest.main()
