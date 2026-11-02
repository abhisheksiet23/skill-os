#Requires -Version 7.0
[CmdletBinding()]
param(
    [switch]$Apply,
    [switch]$RetireLegacy,
    [string]$UserRoot = $env:USERPROFILE,
    [string]$Python = 'python',
    [string]$Codex = 'codex',
    [string]$Rtk = (Join-Path $env:USERPROFILE '.local/bin/rtk.exe')
)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
Import-Module (Join-Path $PSScriptRoot 'LegacySkills.psm1') -Force
$repo = Split-Path -Parent $PSScriptRoot
$source = Join-Path $repo 'skillmesh'
if (-not $UserRoot -or -not [IO.Path]::IsPathFullyQualified($UserRoot)) { throw 'UserRoot must be an absolute user directory.' }
$stage = Assert-ContainedPath (Join-Path $UserRoot 'plugins/skillmesh') (Join-Path $UserRoot 'plugins')
$marketplace = Assert-ContainedPath (Join-Path $UserRoot '.agents/plugins/marketplace.json') (Join-Path $UserRoot '.agents/plugins')
$helper = Join-Path $UserRoot '.codex/skills/.system/plugin-creator/scripts'
$hasHelpers = @('validate_plugin.py', 'read_marketplace_name.py', 'update_plugin_cachebuster.py', 'create_basic_plugin.py' | Where-Object { -not (Test-Path -LiteralPath (Join-Path $helper $_)) }).Count -eq 0
$legacy = @(Get-LegacySkillPlan $UserRoot)
Write-Host "Authoring source: $source"
Write-Host "Plugin release copy: $stage"
Write-Host "Personal marketplace: $marketplace"
Write-Host "Legacy copies found: $($legacy.Count); retirement requested: $RetireLegacy"
$legacy | Format-Table Name,Surface,Path | Out-Host
if (-not $Apply) { Write-Host 'Inspection only. Use -Apply to install; add -RetireLegacy to archive replaced copies after verification.'; return }

function Invoke-Native([string]$Executable, [string[]]$Arguments) {
    & $Rtk proxy $Executable @Arguments
    if ($LASTEXITCODE -ne 0) { throw "Command failed ($LASTEXITCODE): $Executable" }
}

# All verification that can run before profile writes happens first.
Invoke-Native $Python @((Join-Path $repo 'scripts/validate_library.py'), $source)
if ($hasHelpers) { Invoke-Native $Python @((Join-Path $helper 'validate_plugin.py'), $source) }
else { Write-Host 'Bundled plugin helpers unavailable; using the repository validator and skills-only marketplace registration.' }
$marketplaceName = 'personal'
$registered = $false
if (Test-Path -LiteralPath $marketplace) {
    $marketplaceData = Get-Content -LiteralPath $marketplace -Raw | ConvertFrom-Json
    $marketplaceName = $marketplaceData.name
    $entries = @($marketplaceData.plugins | Where-Object name -EQ 'skillmesh')
    if ($entries.Count -gt 1) { throw 'Duplicate SkillMesh marketplace entries require resolution.' }
    $registered = $entries.Count -eq 1
    if ($registered -and ($entries[0].source.source -ne 'local' -or $entries[0].source.path -ne './plugins/skillmesh')) {
        throw 'Existing SkillMesh entry points elsewhere; refusing to replace it.'
    }
}
if ($marketplaceName -notmatch '^[A-Za-z0-9_-]+$') { throw 'Invalid marketplace identifier.' }
if (Test-Path -LiteralPath $stage) {
    $existing = Get-Content -LiteralPath (Join-Path $stage '.codex-plugin/plugin.json') -Raw | ConvertFrom-Json
    if ($existing.name -ne 'skillmesh') { throw 'The destination is not SkillMesh.' }
    foreach ($child in Get-ChildItem -LiteralPath $stage -Recurse -Force) {
        if ($child.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw 'Linked release copies require manual migration.' }
    }
}
$backup = Assert-ContainedPath (Join-Path $UserRoot ".codex/skillmesh-backups/$([DateTime]::UtcNow.ToString('yyyyMMdd-HHmmss'))-$([guid]::NewGuid().ToString('N').Substring(0,8))") (Join-Path $UserRoot '.codex/skillmesh-backups')
New-Item -ItemType Directory -Path $backup -Force | Out-Null
Write-Host "Recovery directory: $backup"
if (Test-Path -LiteralPath $marketplace) { Copy-Item -LiteralPath $marketplace -Destination (Join-Path $backup 'marketplace.json') }
# Prepare and validate the complete replacement before moving the active source.
$preparedParent = Assert-ContainedPath (Join-Path $backup 'prepared') $backup
New-Item -ItemType Directory -Path $preparedParent -Force | Out-Null
Copy-Item -LiteralPath $source -Destination $preparedParent -Recurse
$prepared = Join-Path $preparedParent 'skillmesh'
if ($registered) {
    if ($hasHelpers) { Invoke-Native $Python @((Join-Path $helper 'update_plugin_cachebuster.py'), $prepared) }
    else {
        $manifestPath = Join-Path $prepared '.codex-plugin/plugin.json'
        $manifest = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
        $manifest.version = ($manifest.version -split '\+')[0] + '+codex.' + [DateTime]::UtcNow.ToString('yyyyMMddHHmmssfff')
        $manifest | ConvertTo-Json -Depth 100 | Set-Content -LiteralPath $manifestPath -Encoding utf8
    }
}
if ($hasHelpers) { Invoke-Native $Python @((Join-Path $helper 'validate_plugin.py'), $prepared) }
else { Invoke-Native $Python @((Join-Path $repo 'scripts/validate_library.py'), $prepared) }
# Registration uses the official helper. Its throwaway scaffold cannot overwrite the release source.
if (-not $registered) {
    if ($hasHelpers) {
        Invoke-Native $Python @((Join-Path $helper 'create_basic_plugin.py'), 'skillmesh', '--path', (Join-Path $backup 'registration'), '--marketplace-path', $marketplace, '--with-marketplace', '--with-skills')
    } else {
        if (-not (Test-Path -LiteralPath $marketplace)) {
            $marketplaceData = [pscustomobject]@{ name = $marketplaceName; interface = @{ displayName = 'Personal' }; plugins = @() }
        }
        $marketplaceData.plugins = @($marketplaceData.plugins) + @([pscustomobject]@{
            name = 'skillmesh'; source = @{ source = 'local'; path = './plugins/skillmesh' }
            policy = @{ installation = 'AVAILABLE'; authentication = 'ON_INSTALL' }; category = 'Productivity'
        })
        New-Item -ItemType Directory -Path (Split-Path -Parent $marketplace) -Force | Out-Null
        $marketplaceData | ConvertTo-Json -Depth 100 | Set-Content -LiteralPath $marketplace -Encoding utf8
    }
}
Publish-PluginSource $UserRoot $prepared $stage (Join-Path $backup 'plugin-source')
$selector = "skillmesh@$marketplaceName"
Invoke-Native $Codex @('plugin', 'add', $selector, '--json')
$listing = (Invoke-Native $Codex @('plugin', 'list', '--json') | Out-String) | ConvertFrom-Json
$installed = @($listing.installed | Where-Object { $_.pluginId -eq $selector -and $_.installed -and $_.enabled })
$releaseManifest = Get-Content -LiteralPath (Join-Path $stage '.codex-plugin/plugin.json') -Raw | ConvertFrom-Json
if ($installed.Count -ne 1 -or $installed[0].version -ne $releaseManifest.version) { throw 'Native CLI did not confirm the expected enabled release; legacy skills were not retired.' }
if ($RetireLegacy) { Move-LegacySkills $UserRoot (Join-Path $backup 'legacy') }
Write-Host "Installed and verified $selector. Recovery directory: $backup"
Write-Host 'Start a new Codex task to pick up the plugin skills.'
