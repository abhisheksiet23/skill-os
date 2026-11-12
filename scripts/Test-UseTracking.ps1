#Requires -Version 7.0
$ErrorActionPreference = 'Stop'
$runner = Join-Path $PSScriptRoot 'Measure-Use.ps1'
$root = Join-Path (Split-Path $PSScriptRoot) ".use-tracking/tests/$([guid]::NewGuid().ToString('N'))"
New-Item -ItemType Directory -Path $root -Force | Out-Null
function Assert([bool]$Condition, [string]$Message) { if (-not $Condition) { throw $Message } }
$pwsh = (Get-Command pwsh).Source
$previousParent = $env:SKILLMESH_TRACKED_USE
$env:SKILLMESH_TRACKED_USE = $null
Push-Location $root
try {
    & $runner -Task smoke -Category validation -Mechanism pwsh -Rework initial -Executable $pwsh -ArgumentList @('-NoProfile','-Command','Write-Output "private-payload"; exit 0')
    Assert ($LASTEXITCODE -eq 0) 'Successful exit changed.'
    $log = Join-Path $root '.use-tracking/uses.jsonl'
    $raw = Get-Content -LiteralPath $log -Raw
    $record = $raw | ConvertFrom-Json
    Assert ($record.task -eq 'smoke' -and $record.outcome -eq 'succeeded') 'Missing operation metadata.'
    Assert ($record.duration_ms -gt 0 -and $record.measurement_source -eq 'local-stopwatch-and-process-exit') 'Duration has no source.'
    Assert ($null -eq $record.provider_tokens -and $null -eq $record.cost) 'Unknown metrics became measurements.'
    Assert (-not $raw.Contains('private-payload') -and -not $raw.Contains('ArgumentList')) 'Command or output leaked.'
    & $runner -Task smoke -Category validation -Mechanism pwsh -Rework correction -Executable $pwsh -ArgumentList @('-NoProfile','-Command','exit 7')
    Assert ($LASTEXITCODE -eq 7) 'Failure exit changed.'
    $records = @(Get-Content -LiteralPath $log | ConvertFrom-Json)
    Assert ($records.Count -eq 2 -and $records[1].outcome -eq 'failed' -and $records[1].rework -eq 'correction') 'Failure/rework was not recorded.'
    & $runner -Task launch -Category validation -Mechanism unavailable -Executable 'skillmesh-nonexistent-executable'
    Assert ($LASTEXITCODE -ne 0) 'Launch failure reported success.'
    $records = @(Get-Content -LiteralPath $log | ConvertFrom-Json)
    Assert ($records[2].outcome -eq 'launch-failed') 'Launch failure disappeared.'
    $env:SKILLMESH_TRACKED_USE = 'parent'
    & $runner -Task nested -Category validation -Mechanism pwsh -Executable $pwsh -ArgumentList @('-NoProfile','-Command','exit 0')
    Assert (@(Get-Content -LiteralPath $log).Count -eq 3) 'Nested operation double-counted.'
    Assert ($env:SKILLMESH_TRACKED_USE -eq 'parent') 'Parent marker was not restored.'
    $env:SKILLMESH_TRACKED_USE = $null
    $nestedScript = Join-Path $root 'nested.ps1'
    @'
param([string]$RunnerPath)
& $RunnerPath -Task child -Category validation -Mechanism pwsh -Executable (Get-Command pwsh).Source -ArgumentList @('-NoProfile','-Command','exit 0')
exit $LASTEXITCODE
'@ | Set-Content -LiteralPath $nestedScript
    & $runner -Task parent -Category validation -Mechanism pwsh -Executable $pwsh -ArgumentList @('-NoProfile','-ExecutionPolicy','Bypass','-File',$nestedScript,'-RunnerPath',$runner)
    Assert ($LASTEXITCODE -eq 0) 'Nested subprocess failed.'
    $records = @(Get-Content -LiteralPath $log | ConvertFrom-Json)
    Assert ($records.Count -eq 4 -and $records[3].task -eq 'parent') 'Child process nesting double-counted.'
    Assert (-not $env:SKILLMESH_TRACKED_USE) 'Parent marker leaked after completion.'
    # Force collection failure using a file where the output directory should be.
    $blocked = Join-Path $root 'blocked'
    New-Item -ItemType Directory -Path $blocked | Out-Null
    Set-Content -LiteralPath (Join-Path $blocked '.use-tracking') -Value 'blocked'
    Push-Location $blocked
    try {
        & $runner -Task blocked -Category validation -Mechanism pwsh -Executable $pwsh -ArgumentList @('-NoProfile','-Command','exit 9')
        Assert ($LASTEXITCODE -eq 9) 'Collection failure masked program failure.'
        & $runner -Task blocked -Category validation -Mechanism pwsh -Executable $pwsh -ArgumentList @('-NoProfile','-Command','exit 0')
        Assert ($LASTEXITCODE -eq 0) 'Collection failure broke successful work.'
    } finally { Pop-Location }
} finally {
    Pop-Location
    $env:SKILLMESH_TRACKED_USE = $previousParent
    $fixtureBase = [IO.Path]::GetFullPath((Join-Path (Split-Path $PSScriptRoot) '.use-tracking/tests'))
    $fixturePath = [IO.Path]::GetFullPath($root)
    if ([IO.Path]::GetDirectoryName($fixturePath) -ne $fixtureBase) {
        throw 'Fixture cleanup refused: target is outside the expected test directory.'
    }
    Remove-Item -LiteralPath $fixturePath -Recurse -Force
}
Write-Host 'Use-tracking checks passed (success, failure, privacy, nesting, unavailable collector).'
