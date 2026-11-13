# Install SkillMesh and retire replaced copies

The plugin contains 23 independent skills and a bundled Serena stdio MCP connection. It does not replace TWG, document/media tools, Sites or system skills. [Code navigation setup and limits](serena.md) covers runtime preparation, project activation and fallback.

## Validate

From the repository, use Python 3.10+ and PowerShell 7:

```powershell
python scripts/validate_library.py
python -m unittest discover -s tests -v
pwsh -File scripts/Test-Migration.ps1
python "$env:USERPROFILE/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py" ./skillmesh
```

Run the system skill-creator `scripts/quick_validate.py` against each directory under `skillmesh/skills`. Official validators require PyYAML; install it in a local environment if absent. Do not confuse static validation with behavioral results; see [evaluation guidance](../evals/README.md). Historical committed results remain in Git history.

With no directory argument, `validate_library.py` also checks tracked and new non-ignored repository files for complete Git conflict-marker lines, including diff3 ancestor markers. It reports file/line diagnostics and fails if Git inventory is unavailable. Binary files are skipped; quote intentional marker examples inline. An explicit plugin-directory argument checks that package alone, including markers outside its skills, without requiring Git.

## Inspect, then install

```powershell
pwsh -File scripts/Install-SkillMesh.ps1
pwsh -File scripts/Install-SkillMesh.ps1 -Apply -RetireLegacy
```

Pass `-Python`, `-Codex` or `-Rtk` when executables are not on PATH. The script uses the official plugin-creator helpers already installed under the user's system skills. `-Apply` registers/installs; without it the script only displays the plan. `-RetireLegacy` archives exact matching website/app skill folders only after the native CLI confirms the expected enabled plugin version. Omit retirement if you only want installation, but avoid leaving duplicate skills active for normal use.

The authoring source remains `<repository>/skillmesh`. The installer stages a deployment copy under `~/plugins/skillmesh`, registers the default personal marketplace at `~/.agents/plugins/marketplace.json`, and uses `codex plugin add skillmesh@<marketplace-name>`. The personal marketplace is discovered implicitly; no marketplace-add command is needed. Existing marketplace names and unrelated entries are preserved.

Re-running the installer refreshes the deployment copy, updates the version cachebuster, then reinstalls. When the older bundled plugin-creator Python helpers are unavailable, the installer uses the repository packaging validator, preserves existing marketplace entries during registration, and adds a timestamp to the deployment version. It does not require those removed helpers. Do not edit deployed or cached copies. Start a new Codex task to pick up the installed skills; an existing task's captured skill list may remain stale.

The source now includes portable `plugin.json`/`mcp.json` and the existing compatibility overlay. Release-copy versions stay synchronized. Before replacing the active source, `Prepare-Serena.ps1` prepares uv/Python/Serena and available initial-stack language servers; network or prerequisite failure leaves the existing plugin installation intact. Native plugin registration is checked separately from the opt-in live catalog check: `python scripts/test_plugin_host.py`. If scripts are blocked by local signing policy, pass `-ExecutionPolicy Bypass` to the PowerShell process only.

Installation status is device-specific. If retaining a local record, use ignored `docs/installation-status.local.md` for the verification date, source revision or snapshot, installed version, checks and recovery paths. Verify each device independently; another device's installation record does not establish local deployment status. Keep reusable installation guidance here.

## What retirement means

The twelve replaced `website*` and `app-*` folders are moved out of both user discovery roots (`~/.codex/skills` and `~/.agents/skills`) when present, using an explicit name list. Local modifications travel with those folders. Unrecognized identities or linked resources stop automatic retirement for manual inspection.

Backups are kept under `~/.codex/skillmesh-backups/<timestamp-id>/`, including any prior deployment source and marketplace file. The legacy folders are under `legacy/codex/` and `legacy/agents/`. Old source repositories, specialized toolkit tools, `.claude` installations, global instructions and project records are not removed.

Installation failure before verification leaves legacy discovery intact. The complete replacement source is prepared and validated before replacing the old source; a failed local move restores the previous source when the destination is absent. A later CLI failure leaves a complete new source and preserves the old source in backup; legacy retirement has not started.

If the process is forcibly terminated during the source swap, inspect `~/plugins/skillmesh` and `<recovery directory>/plugin-source` before retrying. If the active source is missing, move that preserved prior source back to the exact active path using PowerShell `Move-Item -LiteralPath`, after verifying both paths. For any interrupted CLI operation, inspect native plugin status before another install. This is a bounded migration utility, not an atomic package manager.

## Roll back

Remove SkillMesh with the native CLI using the actual marketplace name, then restore the archived copies:

```powershell
codex plugin remove skillmesh@personal
pwsh -File scripts/Restore-LegacySkills.ps1 -BackupPath '<printed recovery directory>/legacy' -Apply
```

Use the marketplace name printed during installation if different from `personal`. Restore refuses to overwrite an existing skill and checks destinations before moving. A prior plugin deployment source is preserved separately for deliberate recovery. Do not overwrite marketplace configuration that changed after the backup; inspect it and use official tooling.

Project-specific skill copies and global instructions that explicitly name the old external OS may still need scoped cleanup when working in those projects. This migration intentionally does not rewrite every project or unrelated instruction file.
