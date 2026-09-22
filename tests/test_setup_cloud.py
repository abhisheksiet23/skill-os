import tempfile
import unittest
from pathlib import Path

from scripts.setup_cloud import setup


class CloudSetupTests(unittest.TestCase):
    def make_repo(self, root):
        repo = Path(root)
        skill = repo / "skillmesh/skills/example"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text("example", encoding="utf-8")
        return repo, skill

    def test_link_resolves_source_and_repeat_is_safe(self):
        with tempfile.TemporaryDirectory() as root:
            repo, skill = self.make_repo(root)
            try:
                count = setup(repo)
            except OSError as exc:
                if getattr(exc, "winerror", None) == 1314:
                    self.skipTest("Windows symlink privilege unavailable; run in Linux cloud")
                raise
            self.assertEqual(count, 1)
            link = repo / ".agents/skills/example"
            self.assertTrue(link.is_symlink())
            self.assertEqual(link.resolve(), skill.resolve())
            self.assertEqual(setup(repo), 1)
            (skill / "SKILL.md").write_text("updated", encoding="utf-8")
            self.assertEqual((link / "SKILL.md").read_text(), "updated")

    def test_existing_skill_is_preserved(self):
        with tempfile.TemporaryDirectory() as root:
            repo, _ = self.make_repo(root)
            existing = repo / ".agents/skills/example"
            existing.mkdir(parents=True)
            marker = existing / "SKILL.md"
            marker.write_text("local", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "Existing skill"):
                setup(repo)
            self.assertEqual(marker.read_text(), "local")
