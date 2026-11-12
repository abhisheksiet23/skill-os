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

## Evidence as of 2026-11-12

- Before: `rtk gain --project --format json` reported zero commands, input/output estimates and duration on this device. RTK supplied no usable baseline. Its command-level output-size estimates would not establish provider billing or purposeful-use boundaries.
- After: the local pilot captured actual migration-validation failures and a successful tracking-validation operation in this repository. The first migration attempt was blocked by unsigned-script policy; a process-scoped policy override reached the migration tests, which then failed creating a junction with access denied. Neither failure is a migration pass. Correction is explicitly linked by the shared task label and rework flag.
- `scripts/Test-UseTracking.ps1` exercises success/nonzero exits, unavailable executable, metadata without command/output capture, unknown metrics, inherited nesting, marker restoration and unwritable collection. These are executed process tests using synthetic fixtures, separate from the real-use pilot.
- No skills or routing behavior changed. The before/after result is availability of useful local operation records, not an improvement in model behavior. Collection overhead, repeated-use usefulness, application coverage, provider usage and savings remain unmeasured.

## Next boundary

Use the collector on relevant operations in whichever authorized project is active next; no comparison application or benchmark campaign is required. Identify one repeated burden from those observations before expanding collection. Stop or simplify if annotation costs outweigh useful findings. The roadmap's broader tracking acceptance remains open until real application uses and collection overhead support adoption.
