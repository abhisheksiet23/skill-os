# Per-use tracking pilot

## Boundary

Run one purposeful command from its owning project directory. The wrapper measures elapsed process time and exit status; it does not measure an entire agent task, judge correctness, or infer model/human effort. Select meaningful operations such as a validation suite rather than wrapping every search or tool call. Nothing runs automatically.

Use PowerShell 7, already required by the repository's migration helpers:

```powershell
& ./scripts/Measure-Use.ps1 -Task tracking-validation -Category validation `
  -Mechanism powershell -Rework initial -Executable pwsh `
  -ArgumentList @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', 'scripts/Test-UseTracking.ps1')
```

`Bypass` applies only to that child process, allowing local unsigned test scripts on this device; no machine policy is changed. For another executable, pass its arguments as an array. The executable must return a process exit code. Use `pwsh -File` or `pwsh -Command` to wrap PowerShell functions, pipelines or multiple dependent commands, ensuring the child returns the intended aggregate result. Choose a non-sensitive task ID and mechanism label, using letters, numbers, dots, underscores or hyphens. Categories: navigation, analysis, validation, build, other. Rework defaults to unknown; declare initial or correction only when known.

The caller's current directory identifies the project and receives `.use-tracking/uses.jsonl`. Start in the project root. For another authorized project, invoke this runner by its absolute path while keeping that project's directory current; keep its records and ignore rule there. The pilot does not install or modify other projects.

## Records and limits

Each JSON line holds a use ID, project directory's basename, task/category/mechanism labels, UTC interval, stopwatch duration in milliseconds, exit code, outcome and declared rework state. Outcomes distinguish success, failure and inability to launch. Measurement source and coverage gaps are explicit; provider tokens and cost are null, meaning unknown.

Command text, arguments, output, prompts, code, query results, environment values and absolute project paths are not copied into telemetry. Output still reaches the terminal. Labels and the project basename are user-selected metadata and must contain no secrets. Records are local and ignored by Git here; no upload is performed.

Nested wrappers inherit an environment marker and record only the outer operation. Separately launched operations can overlap: compare intervals and never sum their durations as wall-clock task time. Opt-in sampling cannot establish overall task frequency or total effort. Logging is best effort: write failures warn and preserve the underlying exit code. Concurrent appends are not guaranteed lossless. No dashboard, automatic aggregation or background collector is included.

## Verification and adoption boundary

`scripts/Test-UseTracking.ps1` supplies process checks for success/nonzero exits, unavailable executable, metadata without command/output capture, unknown metrics, inherited nesting, marker restoration and unwritable collection. Execute it for the selected candidate/environment before claiming a current pass. These synthetic runner checks do not establish ordinary-use value or migration readiness.

Collection is implemented; useful recurrence, collection overhead, application coverage, attributable provider usage and savings remain open. Command-output estimates do not establish billing. See [retained lessons](lessons-learned.md) and [environmental factors](environmental-factors.md) for the conclusions and execution constraints, without carrying pilot history into this usage contract.

## Next boundary

Use the collector on relevant operations in whichever authorized project is active next; no comparison application or benchmark campaign is required. Identify one repeated burden from those observations before expanding collection. Stop or simplify if annotation costs outweigh useful findings. The roadmap's broader tracking acceptance remains open until real application uses and collection overhead support adoption.
