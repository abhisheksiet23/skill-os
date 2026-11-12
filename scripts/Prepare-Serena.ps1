#Requires -Version 7.0
[CmdletBinding()]
param(
    [string]$UserRoot = [Environment]::GetFolderPath('UserProfile'),
    [string]$Rtk = 'rtk'
)
$ErrorActionPreference = 'Stop'
if (-not [IO.Path]::IsPathFullyQualified($UserRoot)) { throw 'UserRoot must be absolute.' }
$uvx = Get-Command uvx -ErrorAction SilentlyContinue
if ($uvx) { $uvxPath = $uvx.Source }
else {
    $localBin = Join-Path $UserRoot '.local/bin'
    $uvxPath = Join-Path $localBin $(if ($IsWindows) { 'uvx.exe' } else { 'uvx' })
    if (-not (Test-Path -LiteralPath $uvxPath -PathType Leaf)) {
        if (-not $IsWindows) { throw 'Install uv using https://docs.astral.sh/uv/getting-started/installation/ and rerun.' }
        # Use the upstream versioned installer, not a custom package manager.
        $scratch = Join-Path (Split-Path $PSScriptRoot) ".validation-deps/uv-bootstrap/$([guid]::NewGuid().ToString('N'))"
        New-Item -ItemType Directory -Path $scratch -Force | Out-Null
        $installer = Join-Path $scratch 'install.ps1'
        Invoke-WebRequest 'https://astral.sh/uv/0.13.7/install.ps1' -OutFile $installer
        $previousInstallDir = $env:UV_INSTALL_DIR
        $previousNoPath = $env:UV_NO_MODIFY_PATH
        try {
            $env:UV_INSTALL_DIR = $localBin
            $env:UV_NO_MODIFY_PATH = '1'
            & $Rtk proxy pwsh -NoProfile -ExecutionPolicy Bypass -File $installer
            if ($LASTEXITCODE -ne 0) { throw 'uv installation failed; SkillMesh was not installed.' }
        } finally {
            $env:UV_INSTALL_DIR = $previousInstallDir
            $env:UV_NO_MODIFY_PATH = $previousNoPath
        }
    }
    if (-not (Test-Path -LiteralPath $uvxPath -PathType Leaf)) { throw 'uvx is unavailable after setup.' }
    # Native MCP starts by executable name. Persist only the required bin path on Windows.
    if ($IsWindows -and ([IO.Path]::GetFullPath($UserRoot) -eq [IO.Path]::GetFullPath([Environment]::GetFolderPath('UserProfile')))) {
        $userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
        if ($localBin -notin ($userPath -split ';')) {
            [Environment]::SetEnvironmentVariable('Path', (([string]$userPath).TrimEnd(';') + ';' + $localBin), 'User')
        }
    }
    $env:PATH = $localBin + [IO.Path]::PathSeparator + $env:PATH
}
# Populate the same uvx cache and Python version used by the bundled MCP definition.
& $Rtk proxy $uvxPath --python 3.12 --from serena-agent==2.1.0 serena --version
if ($LASTEXITCODE -ne 0) { throw 'Serena preparation failed; existing plugin installation remains unchanged.' }
# Prewarm available initial-stack backends before simultaneous chats can race
# while extracting a shared cold language-server installation (observed with Roslyn).
$languages = @()
if (Get-Command node -ErrorAction SilentlyContinue) { $languages += @('typescript', 'angular') }
if (Get-Command dotnet -ErrorAction SilentlyContinue) {
    $sdks = & $Rtk proxy dotnet --list-sdks
    if ($LASTEXITCODE -eq 0 -and @($sdks | Where-Object { $_ -match '^(1[0-9]|[2-9][0-9])\.' }).Count -gt 0) { $languages += 'csharp' }
}
if ($languages.Count -gt 0) {
    $launcher = Join-Path (Split-Path $PSScriptRoot) 'skillmesh/serena/start.py'
    & $Rtk proxy $uvxPath --python 3.12 --from serena-agent==2.1.0 python $launcher download-ls-dependencies @languages
    if ($LASTEXITCODE -ne 0) { throw 'Language-server preparation failed; existing plugin installation remains unchanged.' }
}
Write-Host 'Serena dependency runner ready. Restart the app if uvx was newly added to PATH.'
