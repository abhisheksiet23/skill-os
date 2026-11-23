import json
from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.test_plugin_host import MANIFESTS, verify_plugin, verify_serena


class PluginHostVerificationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name).resolve()
        self.candidate = root / "candidate"
        self.marketplace = root / "marketplace.json"
        self.marketplace.write_text('{"name": "personal"}', encoding="utf-8")
        self.codex_home = root / "codex"
        self.published = root / "published"
        self.version = "0.2.0+codex.20261123122504601"
        self.installed = self.codex_home / "plugins/cache/personal/skillmesh" / self.version
        self.write_manifests(self.candidate, "0.2.0")
        for name in ("first", "second"):
            definition = self.candidate / "skills" / name / "SKILL.md"
            definition.parent.mkdir(parents=True)
            definition.write_text(f"---\nname: {name}\n---\n", encoding="utf-8")
        reference = self.candidate / "skills/first/references/guide.md"
        reference.parent.mkdir()
        reference.write_text("candidate reference", encoding="utf-8")
        for package in (self.published, self.installed):
            shutil.copytree(self.candidate, package)
            self.write_manifests(package, self.version)
        self.details = {
            "marketplaceName": "personal",
            "marketplacePath": str(self.marketplace),
            "summary": {
                "id": "skillmesh@personal",
                "name": "skillmesh",
                "enabled": True,
                "installed": True,
                "localVersion": self.version,
                "source": {"type": "local", "path": str(self.published)},
            },
            "skills": [
                {"name": name, "path": str(self.published / "skills" / name / "SKILL.md"), "enabled": True}
                for name in ("first", "second")
            ],
            "mcpServers": ["serena"],
        }

    def write_manifests(self, package, version):
        for relative in MANIFESTS:
            path = package / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps({"name": "skillmesh", "version": version}), encoding="utf-8")

    def verify(self):
        return verify_plugin(self.details, self.candidate, self.marketplace, str(self.codex_home))

    def test_accepts_reordered_catalog_and_materialized_paths(self):
        self.details["skills"].reverse()
        for skill in self.details["skills"]:
            skill["path"] = str(self.installed / "skills" / skill["name"] / "SKILL.md")
        self.assertEqual(self.verify(), (self.version, 2))

    def test_accepts_marketplace_paths_for_matching_cache(self):
        self.assertEqual(self.verify(), (self.version, 2))

    def test_accepts_skillmesh_qualified_catalog_names(self):
        for skill in self.details["skills"]:
            skill["name"] = "skillmesh:" + skill["name"]
        self.assertEqual(self.verify(), (self.version, 2))

    def test_accepts_installer_replacing_candidate_build_metadata(self):
        self.write_manifests(self.candidate, "0.2.0+git.abc")
        self.assertEqual(self.verify(), (self.version, 2))

    def test_rejects_installer_stamp_for_different_release(self):
        self.write_manifests(self.candidate, "0.1.0+git.abc")
        with self.assertRaisesRegex(ValueError, "Marketplace version"):
            self.verify()

    def test_rejects_malformed_server_registrations(self):
        for servers in (None, "prefix-serena", {"serena": True}, [], ["serena", {}]):
            with self.subTest(servers=servers), self.assertRaisesRegex(ValueError, "register Serena"):
                self.details["mcpServers"] = servers
                self.verify()

    def test_rejects_empty_missing_unknown_and_duplicate_skills(self):
        first, second = self.details["skills"]
        cases = (
            ([], "missing"),
            ([first], "missing"),
            ([first, second, dict(second, name="unexpected")], "extra=.*unexpected"),
            ([first, dict(second, name="other:second")], "extra=.*other:second"),
            ([first, second, second], "duplicate=.*second"),
            ([first, second, dict(second, name="skillmesh:second")], "duplicate=.*second"),
        )
        for catalog, diagnostic in cases:
            with self.subTest(catalog=catalog), self.assertRaisesRegex(ValueError, diagnostic):
                self.details["skills"] = catalog
                self.verify()

    def test_rejects_missing_wrong_and_disabled_skill_paths(self):
        first = self.details["skills"][0]
        for changes in (
            {"path": None},
            {"path": str(self.candidate / "skills/first/SKILL.md")},
            {"path": str(self.published / "skills/second/SKILL.md")},
            {"enabled": False},
        ):
            with self.subTest(changes=changes), self.assertRaisesRegex(ValueError, "skill path|catalog entry"):
                self.details["skills"][0] = dict(first, **changes)
                self.verify()

    def test_rejects_unverifiable_catalog_identity(self):
        for catalog in (None, {}, [{}]):
            with self.subTest(catalog=catalog), self.assertRaisesRegex(ValueError, "without named entries"):
                self.details["skills"] = catalog
                self.verify()

    def test_rejects_missing_marketplace_and_codex_home_paths(self):
        with self.assertRaisesRegex(ValueError, "Codex home"):
            verify_plugin(self.details, self.candidate, self.marketplace, None)
        del self.details["marketplacePath"]
        with self.assertRaisesRegex(ValueError, "marketplace path"):
            self.verify()

    def test_rejects_unverifiable_installation(self):
        summary = self.details["summary"]
        for changes in (
            {"id": "skillmesh@other"},
            {"enabled": False},
            {"installed": False},
            {"localVersion": None},
            {"localVersion": "0.1.0"},
            {"source": {"type": "remote"}},
            {"source": {"type": "local", "path": None}},
        ):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.details["summary"] = dict(summary, **changes)
                self.verify()

    def test_rejects_missing_materialized_copy_even_with_matching_marketplace(self):
        shutil.rmtree(self.installed)
        with self.assertRaisesRegex(ValueError, "Cannot locate the materialized"):
            self.verify()

    def test_rejects_old_cache_content_with_same_catalog_and_version(self):
        reference = self.installed / "skills/first/references/guide.md"
        reference.write_text("stale reference", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Package content differs.*guide.md"):
            self.verify()

    def test_rejects_extra_cached_file(self):
        (self.installed / "extra.txt").touch()
        with self.assertRaisesRegex(ValueError, "extra=.*extra.txt"):
            self.verify()

    def test_rejects_manifest_edits_besides_installer_version(self):
        manifest = self.published / "plugin.json"
        manifest.write_text(json.dumps({
            "name": "skillmesh", "version": self.version, "description": "different",
        }), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Package content differs.*plugin.json"):
            self.verify()

    def test_requires_exact_version_for_stamped_candidate(self):
        self.write_manifests(self.candidate, "0.2.0+codex.20261023122504601")
        with self.assertRaisesRegex(ValueError, "Marketplace version"):
            self.verify()

    def test_rejects_manifest_boolean_changed_to_number(self):
        for package, flag in ((self.candidate, True), (self.installed, True), (self.published, 1)):
            manifest = package / "plugin.json"
            data = json.loads(manifest.read_text(encoding="utf-8"))
            data["flag"] = flag
            manifest.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, r"Package content differs.*published.*plugin.json"):
            self.verify()


class SerenaStatusTests(unittest.TestCase):
    def setUp(self):
        self.plugin_id = "skillmesh@personal"
        self.tools = {
            name: {"name": name, "inputSchema": {"type": "object"}} for name in (
                "initial_instructions", "activate_project", "get_current_config",
                "get_symbols_overview", "find_symbol", "find_referencing_symbols",
                "find_implementations",
            )
        }
        self.server = {"name": "serena", "pluginId": self.plugin_id, "tools": self.tools}

    def test_accepts_only_the_matching_registration_and_tools(self):
        status = {"data": [self.server], "nextCursor": None}
        self.assertEqual(verify_serena(status, self.plugin_id), sorted(self.tools))

    def test_rejects_unverifiable_registration(self):
        with self.assertRaisesRegex(ValueError, "registration"):
            verify_serena([], self.plugin_id)
        for servers, cursor in (
            (None, None),
            ({}, None),
            ([], None),
            (["serena"], None),
            ([self.server, self.server], None),
            ([dict(self.server, name="other")], None),
            ([dict(self.server, pluginId="other@personal")], None),
            ([self.server], "next"),
            ([self.server], ""),
        ):
            with self.subTest(servers=servers, cursor=cursor), self.assertRaisesRegex(ValueError, "registration"):
                verify_serena({"data": servers, "nextCursor": cursor}, self.plugin_id)

    def test_rejects_missing_and_extra_tools(self):
        missing = dict(self.tools)
        del missing["find_symbol"]
        for tools in (missing, dict(self.tools, extra={"name": "extra", "inputSchema": {}})):
            with self.subTest(tools=tools), self.assertRaisesRegex(ValueError, "Unexpected Serena tools"):
                verify_serena({"data": [dict(self.server, tools=tools)]}, self.plugin_id)

    def test_rejects_names_without_tool_definitions(self):
        for tools in (
            list(self.tools),
            dict.fromkeys(self.tools),
            dict(self.tools, find_symbol={}),
            dict(self.tools, find_symbol={"name": "other", "inputSchema": {}}),
        ):
            with self.subTest(tools=tools), self.assertRaisesRegex(ValueError, "named tool definitions"):
                verify_serena({"data": [dict(self.server, tools=tools)]}, self.plugin_id)
