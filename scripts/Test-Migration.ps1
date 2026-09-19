#Requires -Version 7.0
$ErrorActionPreference = 'Stop'
Import-Module (Join-Path $PSScriptRoot 'LegacySkills.psm1') -Force
$testRoot = Join-Path (Split-Path -Parent $PSScriptRoot) ".migration-tests/$([guid]::NewGuid().ToString('N'))"
New-Item -ItemType Directory -Path $testRoot -Force | Out-Null
function Assert([bool]$Condition, [string]$Message) { if (-not $Condition) { throw $Message } }
function Must-Fail([scriptblock]$Action, [string]$Message) {
    $failed = $false
    try { & $Action | Out-Null } catch { $failed = $true }
    Assert $failed $Message
}
foreach ($surface in @('codex','agents')) {
    $skill = Join-Path $testRoot ".$surface/skills/app-analyze"
    New-Item -ItemType Directory -Path $skill -Force | Out-Null
    "---`nname: app-analyze`ndescription: Existing locally customized skill.`n---`nKeep my changes." | Set-Content -LiteralPath (Join-Path $skill 'SKILL.md')
    'local preference' | Set-Content -LiteralPath (Join-Path $skill 'notes.txt')
}
$unrelated = Join-Path $testRoot '.codex/skills/app-unrelated'
New-Item -ItemType Directory -Path $unrelated -Force | Out-Null
'keep unrelated skill' | Set-Content -LiteralPath (Join-Path $unrelated 'SKILL.md')
$backup = Join-Path $testRoot '.codex/skillmesh-backups/test/legacy'
Assert (@(Get-LegacySkillPlan $testRoot).Count -eq 2) 'Inspection must select only exact known names across both discovery roots.'
Assert (Test-Path -LiteralPath (Join-Path $testRoot '.codex/skills/app-analyze')) 'Inspection mutated a skill.'
Must-Fail { Assert-ContainedPath (Join-Path $testRoot '../escape') $testRoot } 'Parent traversal must fail.'
Must-Fail { Assert-ContainedPath ($testRoot + '-sibling/file') $testRoot } 'Prefix sibling escape must fail.'
Move-LegacySkills $testRoot $backup
Assert (@(Get-LegacySkillPlan $testRoot).Count -eq 0) 'Legacy copies remain discoverable after archive.'
Assert (Test-Path -LiteralPath $unrelated) 'Unrelated skill was moved.'
Assert ((Get-Content -LiteralPath (Join-Path $backup 'codex/app-analyze/notes.txt')) -eq 'local preference') 'Local modifications lost.'
Move-LegacySkills $testRoot $backup # Safe no-op after retirement.
Restore-LegacySkills $testRoot $backup
Assert (@(Get-LegacySkillPlan $testRoot).Count -eq 2) 'Restore did not recover both discovery roots.'
# Preflight every destination before any restore moves.
Move-LegacySkills $testRoot $backup
$collision = Join-Path $testRoot '.agents/skills/app-analyze'
New-Item -ItemType Directory -Path $collision -Force | Out-Null
Must-Fail { Restore-LegacySkills $testRoot $backup } 'Restore must refuse a collision.'
Assert (Test-Path -LiteralPath (Join-Path $backup 'codex/app-analyze')) 'Restore partially moved files before detecting collision.'
# Incorrect identity must block retirement before touching other entries.
'---`nname: unexpected`n---' | Set-Content -LiteralPath (Join-Path $collision 'SKILL.md')
Must-Fail { Get-LegacySkillPlan $testRoot } 'Unexpected identities must not be retired.'
# A linked marketplace branch must be rejected, including intermediate ancestors.
$outside = Join-Path $testRoot 'outside'
New-Item -ItemType Directory -Path $outside -Force | Out-Null
$marketplaceLink = Join-Path $testRoot '.agents/plugins'
New-Item -ItemType Junction -Path $marketplaceLink -Target $outside | Out-Null
Must-Fail { Assert-ContainedPath (Join-Path $marketplaceLink 'marketplace.json') $marketplaceLink } 'Marketplace junction must be rejected.'
# An incomplete prepared release must leave the previous source intact.
$stage = Join-Path $testRoot 'plugins/skillmesh'
New-Item -ItemType Directory -Path $stage -Force | Out-Null
'old source' | Set-Content -LiteralPath (Join-Path $stage 'keep.txt')
$prepared = Join-Path $testRoot '.codex/skillmesh-backups/update/prepared/skillmesh'
$previous = Join-Path $testRoot '.codex/skillmesh-backups/update/plugin-source'
Must-Fail { Publish-PluginSource $testRoot $prepared $stage $previous } 'Incomplete prepared release must fail.'
Assert (Test-Path -LiteralPath (Join-Path $stage 'keep.txt')) 'Preflight failure displaced source.'
New-Item -ItemType Directory -Path (Join-Path $prepared '.codex-plugin') -Force | Out-Null
'{"name":"skillmesh"}' | Set-Content -LiteralPath (Join-Path $prepared '.codex-plugin/plugin.json')
'new source' | Set-Content -LiteralPath (Join-Path $prepared 'new.txt')
Publish-PluginSource $testRoot $prepared $stage $previous
Assert (Test-Path -LiteralPath (Join-Path $stage 'new.txt')) 'Prepared source was not published.'
Assert (Test-Path -LiteralPath (Join-Path $previous 'keep.txt')) 'Previous source was not preserved.'
Write-Host "Migration checks passed. Isolated fixtures retained at $testRoot"
