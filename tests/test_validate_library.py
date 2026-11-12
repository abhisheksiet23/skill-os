import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_library import validate


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


if __name__ == "__main__":
    unittest.main()
