import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "outline.py"


def run(*args):
    return subprocess.run([sys.executable, "-I", str(SCRIPT), *args], capture_output=True, text=True, encoding="utf-8")


class OutlineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, name, text):
        p = self.dir / name
        p.write_text(text, encoding="utf-8")
        return str(p)

    def test_markdown_outline_ranges_and_fences(self):
        f = self.write("a.md", "intro\n# One\ntext\n```\n# not a heading\n```\n## Two\nbody\n# Three\nend\n")
        out = run(f).stdout
        self.assertIn("L2-8", out)  # One spans through Two
        self.assertIn("L7-8", out)  # Two
        self.assertIn("L9-10", out)  # Three
        self.assertNotIn("not a heading", out)
        self.assertIn("(preamble)", out)

    def test_markdown_section_returns_only_that_section(self):
        f = self.write("a.md", "# One\naaa\n## Two\nbbb\n# Three\nccc\n")
        r = run(f, "--section", "two")
        self.assertEqual(0, r.returncode)
        self.assertIn("bbb", r.stdout)
        self.assertNotIn("ccc", r.stdout)
        self.assertNotIn("aaa", r.stdout)

    def test_unknown_section_fails_clearly(self):
        f = self.write("a.md", "# One\n")
        r = run(f, "--section", "nope")
        self.assertNotEqual(0, r.returncode)
        self.assertIn("no heading", r.stderr)

    def test_json_outline_and_path(self):
        f = self.write("a.json", json.dumps({"a": {"b": [1, 2, 3]}, "big": "x" * 500, "n": 7}))
        out = run(f).stdout
        self.assertIn("n: 7", out)
        self.assertIn("big: str", out)
        self.assertNotIn("xxxxx", out)
        self.assertIn("2", run(f, "--path", "a.b.1").stdout)

    def test_json_path_truncates(self):
        f = self.write("a.json", json.dumps({"big": "x" * 10000}))
        out = run(f, "--path", "big", "--max-chars", "100").stdout
        self.assertIn("[truncated]", out)
        self.assertLess(len(out), 200)

    def test_jsonl_outline_and_record_path(self):
        f = self.write("a.jsonl", '{"k": 1, "t": {"x": 2}}\n{"k": 5}\n')
        self.assertIn("2 records", run(f).stdout)
        self.assertIn("5", run(f, "--path", "1.k").stdout)

    def test_unsupported_type_is_refused(self):
        f = self.write("a.py", "x = 1\n")
        r = run(f)
        self.assertNotEqual(0, r.returncode)
        self.assertIn("unsupported", r.stderr)


if __name__ == "__main__":
    unittest.main()
