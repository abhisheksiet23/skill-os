#Requires -Version 7.0
<# Run one purposeful operation; persist metadata only, never its command or output. #>
[CmdletBinding()]
param(
    [Parameter(Mandatory)][ValidatePattern('^[a-zA-Z0-9][a-zA-Z0-9._-]{0,79}$')][string]$Task,
    [Parameter(Mandatory)][ValidateSet('navigation','analysis','validation','build','other')][string]$Category,
    [Parameter(Mandatory)][ValidatePattern('^[a-zA-Z0-9][a-zA-Z0-9._-]{0,79}$')][string]$Mechanism,
    [ValidateSet('unknown','initial','correction')][string]$Rework = 'unknown',
    [Parameter(Mandatory)][string]$Executable,
    [string[]]$ArgumentList = @()
)
$ErrorActionPreference = 'Stop'
# A failed native program is an observed outcome, even in callers enabling this preference.
$PSNativeCommandUseErrorActionPreference = $false
$projectRoot = (Get-Location).ProviderPath
$parentUse = $env:SKILLMESH_TRACKED_USE
$useId = [guid]::NewGuid().ToString('N')
$started = [DateTimeOffset]::UtcNow
$timer = [Diagnostics.Stopwatch]::StartNew()
$exitCode = 1
$outcome = 'launch-failed'
try {
    $env:SKILLMESH_TRACKED_USE = $useId
    $global:LASTEXITCODE = 0
    & $Executable @ArgumentList
    $exitCode = $LASTEXITCODE
    $outcome = if ($exitCode -eq 0) { 'succeeded' } else { 'failed' }
} catch {
    # Do not copy exception text (which may contain command arguments) into telemetry.
    Write-Warning 'Operation could not complete; command details were not recorded.'
} finally {
    $timer.Stop()
    $ended = [DateTimeOffset]::UtcNow
    $env:SKILLMESH_TRACKED_USE = $parentUse
}
if (-not $parentUse) {
    $record = [ordered]@{
        schema_version = 1
        use_id = $useId
        project = Split-Path -Leaf $projectRoot
        task = $Task
        category = $Category
        mechanism = $Mechanism
        started_utc = $started.ToString('o')
        ended_utc = $ended.ToString('o')
        duration_ms = [math]::Round($timer.Elapsed.TotalMilliseconds, 3)
        outcome = $outcome
        exit_code = $exitCode
        rework = $Rework
        measurement_source = 'local-stopwatch-and-process-exit'
        provider_tokens = $null
        cost = $null
        gaps = @('opt-in-command-coverage', 'human-and-model-effort-unmeasured',
            'exit-status-is-not-acceptance', 'overlapping-uses-not-additive',
            'provider-tokens-and-cost-unavailable')
    }
    try {
        $directory = Join-Path $projectRoot '.use-tracking'
        [IO.Directory]::CreateDirectory($directory) | Out-Null
        $line = ($record | ConvertTo-Json -Depth 3 -Compress) + [Environment]::NewLine
        [IO.File]::AppendAllText((Join-Path $directory 'uses.jsonl'), $line, [Text.UTF8Encoding]::new($false))
    } catch {
        Write-Warning 'Use record unavailable; preserving the operation exit status.'
    }
}
exit $exitCode
