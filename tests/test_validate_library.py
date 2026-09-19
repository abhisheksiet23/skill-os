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
