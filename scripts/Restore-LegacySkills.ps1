#Requires -Version 7.0
[CmdletBinding()]
param([Parameter(Mandatory)][string]$BackupPath, [string]$UserRoot = $env:USERPROFILE, [switch]$Apply)
$ErrorActionPreference = 'Stop'
Import-Module (Join-Path $PSScriptRoot 'LegacySkills.psm1') -Force
if (-not $Apply) { Write-Host "Inspection only. Restore from $BackupPath into $UserRoot with -Apply. Remove/disable SkillMesh first to avoid duplicate discovery."; return }
Restore-LegacySkills $UserRoot $BackupPath
