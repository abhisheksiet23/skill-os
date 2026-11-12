# Bundled code navigation

SkillMesh 0.2.0 bundles Serena 2.1.0 as a local stdio MCP provider and the independently usable `code-navigation` skill. Installing through the repository helper prepares the runtime; start a new chat to load the updated plugin. No application project is selected during installation.

## Package and startup

The root `skillmesh/plugin.json` and `mcp.json` use the portable Agent Plugins format. The existing `.codex-plugin/plugin.json` remains a synchronized compatibility overlay. The installer updates both versions in its release copy; author source stays at the release version. This host's legacy-only MCP path did not expand plugin-root arguments, so a recognized plugin entry alone was insufficient. The portable package was verified through the native host's live tool catalog.

`uvx --python 3.12 --from serena-agent==2.1.0` runs the packaged launcher and upstream CLI. The launcher initializes provider settings under `~/.serena/skillmesh`, leaving an existing `~/.serena/serena_config.yml` untouched. `SKILLMESH_SERENA_HOME` overrides the managed location for isolated tests. A first-configuration file lock protects concurrent initialization. Upstream anonymous usage reporting is disabled in this process. Editing/interactive base-mode prompts are absent from the initial managed configuration; no dashboard or GUI is opened.

Seven operations are exposed: initial instructions, explicit project activation, current configuration, symbol overviews, symbol lookup, references and implementations. Shell execution, semantic edits, mode switching and memory tools are not in the configured surface. This is a navigation capability during the existing task, not a change to the task's authority or analysis/editing mode.

## Installation and dependencies

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/Install-SkillMesh.ps1 -Apply -Python <working-python-executable>
```

The process-scoped policy override is needed on devices that block unsigned local scripts. The existing installer keeps its inspection-only default, validation, recovery directory and native installation verification. No legacy retirement is needed for this update.

`Prepare-Serena.ps1` reuses available `uvx`; otherwise Windows setup uses Astral's versioned uv 0.13.7 installer. It adds the standard local binary directory to the current process and, for the actual Windows user profile, the existing user PATH without replacing unrelated entries. Other operating systems require uv to be available first. uv may download Python 3.12 and Serena's dependencies. Initial downloads require network access and disk space; transitive versions are governed by Serena's package constraints, not a repository-wide lock. [uv installation](https://docs.astral.sh/uv/getting-started/installation/), [pinned Serena package](https://github.com/oraios/serena/blob/v2.1.0/pyproject.toml).

Setup prewarms TypeScript/Angular backends when Node is available and Roslyn when a .NET 10+ SDK is available. This avoids simultaneous first-use extraction into a shared cold Roslyn cache, observed during testing. A preparation failure stops the installer before replacing the existing plugin; downloads may remain for retry. Other languages can need their own authorized dependencies and initial warmup. Readiness is established by a successful known-symbol lookup, not activation alone.

## Working in any active project

- Establish the actual repository/worktree root; never treat the plugin's directory as the application.
- Inspect existing project/local Serena settings before activation, particularly activation commands and language/ignore settings. Read the initial instructions and pass the returned session ID when activating the absolute root. Confirm current configuration.
- Use a separate stdio server instance per session; confirm binding after switching projects. Provider settings/cache locations are local state, not shared application authority. Activation may write provider configuration/cache files; preserve review-only/no-write scope by using search when needed.
- Confirm a known symbol resolves. Use native search and file reads for missing/unsupported results and relationships outside language-server coverage. Serena reports zero-based line numbers; verify one-based source links.

Angular uses its explicit `angular` backend rather than also registering overlapping TypeScript/HTML servers. Template support remains experimental and depends on project Angular packages; prewarming the language server does not install application dependencies or prove template coverage. C#'s Roslyn runtime requirement does not change the application's target framework. [Serena language support](https://oraios.github.io/serena/01-about/020_programming-languages.html).

## Verification and recovery

```powershell
python scripts/validate_library.py
python -m unittest discover -s tests -v
python scripts/test_plugin_host.py
# Requires Python with Serena's MCP client dependency; opt-in live backend downloads:
python scripts/test_serena_live.py --language typescript
python scripts/test_serena_live.py --language csharp
```

The live checks use disposable synthetic projects and ignored test caches. They exercise actual MCP definitions/references, independent process bindings, switching roots, a missing-root error and direct source fallback. They are integration checks, not model/skill behavioral scores or performance comparisons. The native host check reads the installed plugin and targets only Serena's catalog; it creates no chat, invokes no model and calls no application tools.

Disable the bundled server through the native plugin-server control under `plugins."skillmesh@personal".mcp_servers.serena.enabled = false` (use the actual marketplace ID), then refresh the client. Skills and ordinary search remain useful. Preserve provider caches if retrying an interrupted download. Removing SkillMesh does not remove the shared uv installation or provider caches. The installer's recovery directory retains the previous deployment source; follow [migration recovery](migration.md#roll-back) for plugin rollback. [Native plugin-server controls](https://developers.openai.com/codex/mcp).

As of 2026-11-12, Windows native catalog discovery and TypeScript/C# synthetic live paths have passed. Angular dependency preparation passed; template semantics and real-application usefulness remain unproved. A broad host inventory probe exhausted available memory; verification now targets only Serena. Provider-token, cost and speed savings remain unknown.
