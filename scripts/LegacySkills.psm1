Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Explicit migration scope, not a skill registry. Never infer retirement from a prefix.
$LegacyNames = @('app-analyze','app-backend','app-deliver','app-frontend','app-prototype','app-qa',
    'website','website-build','website-create','website-deliver','website-discover','website-review')

function Assert-ContainedPath([string]$Path, [string]$Root) {
    $absolute = [IO.Path]::GetFullPath($Path)
    $boundary = [IO.Path]::GetFullPath($Root).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
    if (-not $absolute.StartsWith($boundary + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Path is outside the intended directory: $absolute"
    }
    # Reject reparse-point ancestors as well as the final path before copy/move.
    $cursor = $absolute
    while ($cursor) {
        if (Test-Path -LiteralPath $cursor) {
            if ((Get-Item -LiteralPath $cursor -Force).Attributes -band [IO.FileAttributes]::ReparsePoint) {
                throw "Linked paths need manual migration: $cursor"
            }
        }
        $parent = Split-Path -Parent $cursor
        if ($parent -eq $cursor) { break }
        $cursor = $parent
    }
    return $absolute
}

function Get-LegacySkillPlan([string]$UserRoot) {
    foreach ($surface in @('codex','agents')) {
        $root = Join-Path $UserRoot ".$surface/skills"
        foreach ($name in $LegacyNames) {
            $path = Assert-ContainedPath (Join-Path $root $name) $root
            if (-not (Test-Path -LiteralPath $path)) { continue }
            $entry = Join-Path $path 'SKILL.md'
            if (-not (Test-Path -LiteralPath $entry -PathType Leaf)) { throw "Not a recognized skill: $path" }
            $text = Get-Content -LiteralPath $entry -Raw
            if ($text -notmatch "(?m)^name:\s*$([regex]::Escape($name))\s*$") { throw "Unexpected skill identity: $path" }
            # Reject nested links; archive should preserve only the named directory's contents.
            foreach ($child in Get-ChildItem -LiteralPath $path -Recurse -Force) {
                if ($child.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw "Linked resource needs manual migration: $($child.FullName)" }
            }
            [pscustomobject]@{ Name = $name; Surface = $surface; Path = $path }
        }
    }
}

function Move-LegacySkills([string]$UserRoot, [string]$BackupPath) {
    $backup = Assert-ContainedPath $BackupPath (Join-Path $UserRoot '.codex/skillmesh-backups')
    $plan = @(Get-LegacySkillPlan $UserRoot)
    foreach ($item in $plan) {
        $target = Assert-ContainedPath (Join-Path $backup "$($item.Surface)/$($item.Name)") $backup
        if (Test-Path -LiteralPath $target) { throw "Backup already contains $target" }
    }
    foreach ($item in $plan) {
        $target = Assert-ContainedPath (Join-Path $backup "$($item.Surface)/$($item.Name)") $backup
        $source = Assert-ContainedPath $item.Path (Join-Path $UserRoot ".$($item.Surface)/skills")
        New-Item -ItemType Directory -Path (Split-Path -Parent $target) -Force | Out-Null
        Move-Item -LiteralPath $source -Destination $target
        Write-Host "Archived $source -> $target"
    }
}

function Restore-LegacySkills([string]$UserRoot, [string]$BackupPath) {
    $backup = Assert-ContainedPath $BackupPath (Join-Path $UserRoot '.codex/skillmesh-backups')
    if (-not (Test-Path -LiteralPath $backup -PathType Container)) { throw "Backup not found: $backup" }
    $plan = @()
    foreach ($surface in @('codex','agents')) {
        foreach ($name in $LegacyNames) {
            $source = Assert-ContainedPath (Join-Path $backup "$surface/$name") $backup
            if (-not (Test-Path -LiteralPath $source)) { continue }
            $target = Assert-ContainedPath (Join-Path $UserRoot ".$surface/skills/$name") (Join-Path $UserRoot ".$surface/skills")
            if (Test-Path -LiteralPath $target) { throw "Refusing to overwrite an active skill: $target" }
            $plan += [pscustomobject]@{ Source = $source; Target = $target }
        }
    }
    foreach ($item in $plan) {
        New-Item -ItemType Directory -Path (Split-Path -Parent $item.Target) -Force | Out-Null
        Move-Item -LiteralPath $item.Source -Destination $item.Target
        Write-Host "Restored $($item.Target)"
    }
}

function Publish-PluginSource([string]$UserRoot, [string]$Prepared, [string]$Stage, [string]$Previous) {
    $preparedPath = Assert-ContainedPath $Prepared (Join-Path $UserRoot '.codex/skillmesh-backups')
    $stagePath = Assert-ContainedPath $Stage (Join-Path $UserRoot 'plugins')
    $previousPath = Assert-ContainedPath $Previous (Join-Path $UserRoot '.codex/skillmesh-backups')
    if (-not (Test-Path -LiteralPath (Join-Path $preparedPath '.codex-plugin/plugin.json') -PathType Leaf)) { throw 'Prepared plugin is incomplete.' }
    if (Test-Path -LiteralPath $previousPath) { throw 'Previous-source backup already exists.' }
    New-Item -ItemType Directory -Path (Split-Path -Parent $stagePath) -Force | Out-Null
    $movedOld = $false
    try {
        if (Test-Path -LiteralPath $stagePath) {
            Move-Item -LiteralPath $stagePath -Destination $previousPath
            $movedOld = $true
        }
        Move-Item -LiteralPath $preparedPath -Destination $stagePath
    } catch {
        # Recover a failed local swap; never replay an uncertain native install operation.
        if ($movedOld -and -not (Test-Path -LiteralPath $stagePath)) {
            Move-Item -LiteralPath $previousPath -Destination $stagePath
        }
        throw
    }
}

Export-ModuleMember -Function Assert-ContainedPath,Get-LegacySkillPlan,Move-LegacySkills,Restore-LegacySkills,Publish-PluginSource
