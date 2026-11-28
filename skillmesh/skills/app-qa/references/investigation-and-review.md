# Investigate quality beyond a passing test suite

Use the parts that affect the requested scope. A broad review earns breadth through coverage, not a checklist copied into the report. Deepen where a plausible failure could change the conclusion; do not impose a full security, performance or release audit on a contained correction.

## Build and challenge the explanation

Recover intended behavior from adequate requirements, contracts and actual consumers. Treat existing code and tests as evidence of implementation, not unquestionable product intent. Name the invariant at risk, the plausible failure mechanism and the observation that would distinguish it from correct behavior. For ambiguous symptoms, compare competing causes before choosing a fix. Seek counterexamples: a valid zero, missing record, stale version, repeated request, changed permission or partial completion may expose a rule hidden by happy-path data.

Read assertions and fixture setup, not just test names and counts. Ask whether a faulty implementation could pass, whether mocks erase the uncertain boundary, and whether expected values merely reproduce the production calculation. Add or run a discriminating check at the cheapest faithful layer. Report static reasoning, controlled fault injection and actual integrated behavior separately. Never simulate an execution result in a report.

## Review the implementation on its own merits

For unfamiliar applications, inventory the important surfaces and trace selected workflows from entry to authorization, validation, domain rules, durable state and external effect. Include background jobs, exports, admin paths and retained consumers when they can bypass the main journey. Record why sampled paths cover consequential boundaries and what remains unreviewed.

Investigate applicable risks:

| Boundary | Questions that change the assessment |
| --- | --- |
| Correctness and contracts | Are units, rounding, null/zero, limits and state transitions consistent across callers? Can errors become success or incomplete work become final? |
| Access and sensitive data | Is identity trusted and authorization enforced for the action and record scope on the server? Do direct IDs, exports, logs or filesystem paths bypass it? |
| State and concurrency | Who owns each write? What prevents lost updates, duplicate effects and invalid transitions? Are transactions, retries, cancellation and idempotency coherent across stores and services? |
| Structure and maintainability | Are responsibilities, names and contracts discoverable? Does coupling or duplication create a concrete divergence or change risk? Separate architectural trade-offs and style preferences from demonstrable defects. |
| Resources and operations | Are expensive queries, memory, file sizes, queues, timeouts and cleanup bounded where workload makes them consequential? Can operators detect partial failure and recover? Do configuration and dependency choices undermine a claimed guarantee? |
| Tests | Do assertions establish behavior under realistic invalid, boundary and failure conditions? What important guarantee has no meaningful check? |

Inspect dependency/configuration evidence when relevant. A scanner alert needs version, reachability and consequence triage; a clean scan does not establish security. Verify uncertain current vulnerability or library behavior against authoritative sources when needed. Do not prescribe a rewrite, abstraction or infrastructure merely because it is familiar. Recommend deeper architecture or specialist assessment only for an identified consequential uncertainty.

## Assess irreversible and high-impact operations

Before running migration, compression, cleanup, bulk rewrite or deletion, identify the authoritative copy, readers/writers, acceptable transformation and recovery mechanism. Read the actual command and reachable startup/cleanup paths. Use synthetic or appropriately de-identified disposable copies in an isolated environment; missing storage or credentials does not justify experimenting on the only live copy. Avoid copying sensitive records into reports or external services.

Trace the sequence through selection, read, transform, validate, durable write, reference switch and original retirement. Check guarantees rather than insist on one storage pattern:

- A failed transform, insufficient space or interrupted write must not destroy the only usable original. A temporary file, rename or transaction is not proof by itself: inspect the filesystem/object-store semantics and cross-store commit boundary.
- File and database state must remain reconcilable after a crash between steps. Establish what restart/retry will do with partial files, stale references and already-processed records. A database rollback cannot restore overwritten file bytes.
- Concurrent upload, read, edit or worker activity must not cause stale replacement, cross-record attachment or deletion of another operation's output. Check selection stability, ownership/version checks and collision handling as relevant.
- Verify recovery against a stated failure and selected environment. A backup label, untested restore command or same-storage snapshot does not establish an independent usable copy. When the operation can irreversibly damage the only copy and recovery is not demonstrated, recommend withholding that operation and state the smallest prerequisite. Continue safe inspection and disposable tests.

Choose fault injection from the actual sequence: transform failure, write/flush failure, full storage, interruption before/after the reference switch, retry and concurrent modification. Check both content integrity and identity/reference integrity after each selected failure. Mocking an exception can prove error-path logic; it cannot prove power-loss durability or actual storage behavior. Never deliberately exhaust shared storage or interrupt production to establish this evidence.

For transformations of images, documents or other meaningful content, technical readability is only one oracle. Determine format, dimensions, orientation, metadata, content fidelity and consumer compatibility requirements. Lossy clinical/diagnostic content needs qualified acceptance criteria and domain validation; do not invent a safe quality setting or infer clinical usability from a checksum, OCR score, perceptual metric or an image opening successfully. Lossless round-trip equality proves preserved bytes only for that tested path; it does not prove attachment correctness or safe replacement. Missing domain acceptance blocks that claim, not unrelated code investigation. Keep application-specific policies in the application.

## Deliver a decision someone can act on

Give each material finding an exact location, triggering conditions, observed or reasoned failure, consequence and focused correction. Include a reproducer when safely obtainable. Rank credible data loss, unauthorized disclosure and irreversible effects above cosmetic improvements. Do not inflate a hypothetical risk into an observed defect; also do not hide a well-supported source defect merely because production reproduction would be unsafe.

Separate implementation findings, behavioral evidence and operational prerequisites in the same coherent result. A request for perfection calls for an honest residual-risk statement and stronger relevant proof, not a guarantee. Review-only work ends with actionable findings and coverage limits; fixes and production execution require their own authority.
