# Installed — 2026-09-19

Native Codex CLI confirms `skillmesh@personal`, version `0.1.0`, installed and enabled.

| Location | Purpose |
| --- | --- |
| `E:/aj/experiments/skill-os/skillmesh` | Authoritative source |
| `C:/Users/Abhishek/plugins/skillmesh` | Deployment source used by the personal marketplace |
| `C:/Users/Abhishek/.agents/plugins/marketplace.json` | Native personal-marketplace registration |
| `C:/Users/Abhishek/.codex/plugins/cache/personal/skillmesh/0.1.0` | Installed plugin cache |
| `C:/Users/Abhishek/.codex/skillmesh-backups/20260919-164356-e51bbcf3` | Migration recovery directory |

All 36 installed files were compared with authoring sources using SHA-256 and matched. Eighteen skills are packaged. Native plugin listing confirms the other installed plugins remain enabled.

Twelve superseded individual website/app skill folders were moved from `~/.codex/skills` to the recovery directory's `legacy/codex/` folder, preserving their complete contents. Neither user discovery root contains an active copy of those twelve legacy skills. System skills and `.agents/skills` integrations were not removed. The original source repositories, Claude installations and external product-engineering-os tools remain intact.

The official plugin and all eighteen official skill validations passed. Packaging and isolated migration tests passed before installation. The native installation, enabled-state check and cache-content comparison completed afterward. See [behavioral assessment](../evals/results/2026-09-19-assessment.md) for the narrower evidence about skill quality; this installation does not establish a general quality improvement.

Start a new Codex task to load the new plugin skills. This task's original skill catalog may remain stale. Edit authoring sources here and use [migration/update guidance](migration.md) to deploy later revisions; do not edit cached copies.

## Rollback command

Run only if intentionally reverting to the legacy skills:

```powershell
codex plugin remove skillmesh@personal
pwsh -File E:/aj/experiments/skill-os/scripts/Restore-LegacySkills.ps1 -BackupPath C:/Users/Abhishek/.codex/skillmesh-backups/20260919-164356-e51bbcf3/legacy -Apply
```

Restore refuses collisions. Review any later changes before reverting. No production project was changed by this migration.
