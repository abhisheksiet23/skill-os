# Automation feedback evaluation — 2026-11-02

## Candidate and method

Owner authorized the narrow changes following the [feedback investigation](../docs/automation-run-feedback.md). Compared source baseline `e16ec158726e205bee6954c0cf93a04937b65368` with the uncommitted patch in five skills: analysis/clarification, solution-design feasibility and increment sizing, backend integration/discovery, frontend visual timing, and QA evidence use. Six skill files changed; no runtime, mandatory packet schema, plugin identity or installed copy changed.

Two fresh no-history performers used separate frozen skill snapshots and the same [four tasks](automation-feedback-tasks.md). The first task implemented and executed against a local boundary simulator. B/C/D were written responses, not browser/application execution. Neither performer read the author's feedback analysis, assessment key or peer outputs. Both selected backend/frontend for A and analysis for B; neither loaded solution design. Consequently, changed solution-design guidance has source-review coverage here, not a demonstrated independent behavioral comparison. Cases within each variant shared context. Host instructions, filesystem and tools remained shared; no isolation from those surfaces is claimed. The author assessed the outputs without a blind independent assessor.

Local frozen evidence is retained under ignored `.eval-runs/automation-feedback/{baseline,candidate}/`: skills, fixture, report and output artifacts. Snapshot digest is SHA-256 over sorted relative paths plus NUL, file contents plus NUL for all files under each `skills` folder:

- Baseline: `13579eaca6299a7bbcd6b1c3b21d349e2998f24073a05f4c8ade1e776dd1102a`.
- Candidate: `c6c8550ada5e5a4f49ace2c139baba8e8858664cf063de43c8fdb42cc0d5021e`.
- Fixed dependency fixture: `b3dccb45207fb3aa57c0e6f2c37c0d58768087de0f0c82c707c8a8b27b3fb86e`.

## Observed outcomes

| Case | Baseline | Candidate | Supported conclusion |
| --- | --- | --- | --- |
| A: first functional increment | Created app/UI/check files, then exercised the adapter during checks. Four final native checks passed. | Executed a thin login/worker/write/read-back probe before app/UI files existed; retained its unknown result in the UI journal. Six final native checks passed after correcting an initial test failure. | Candidate improved boundary-check ordering in this one comparison. Test counts are not comparable quality scores. |
| A: unknown external write | One create per unique owned operation; 500/unknown followed by 503/unavailable remained unresolved; no automatic replay. | Same unresolved outcome; preserved initial probe and blocked further creation while its outcome remained uncertain. Later fixture tests used separate owned operations/journals. | Both preserved important evidence and mutation limits. The fixture cannot establish successful create/reopen. |
| B: clarification | Asked target URL first, authentication next; used delegation and deferred later catalogue questions. | Comparable selection/timing, with explicit supported credential handoff. | No demonstrated reduction in owner questions relative to baseline in this case. |
| C: dense screen | Proposed early development rendering with realistic density and real integration despite no production bundle. | Explicitly placed rendering before layout expansion and separated development from production-host proof. | Both credible written approaches; no actual visual-quality advantage demonstrated. |
| D: typo | Bounded string correction with existing checks and rendered inspection. | Comparable restraint. | No new architecture, packet or integration phase imposed. |

Ordering evidence: baseline `app.py`/HTML/checks were created at approximately 15:25:23–24 UTC; the first recorded dependency operations occurred at 15:25:33 UTC. Candidate's probe/events were created at approximately 15:24:42 UTC; app/UI files at 15:25:55–56 UTC. These are local event and file observations corroborating performer reports, not provider timing or efficiency measurements. Both variants still built UI, supervision and persistent history; this run does **not** demonstrate smaller platform batches or that the new instructions eliminated dependent expansion. Some platform work remained useful under the explicit UI request; the narrower scope question needs observation in real continuation.

Candidate execution deviation: the initial tests used `TemporaryDirectory.cleanup()`, contrary to the exercise's no-recursive-deletion constraint, and failed with open SQLite handles. Some temporary files may have been removed before failure. The performer reported it, stopped cleanup attempts, retained later fixtures, fixed connection lifetimes and passed six tests. This is a visible candidate limitation, not a discarded failed run or a fault attributed causally to the skill changes. Baseline reported no deletion attempt. No production or application-project records were involved.

Both implementations used supervised threads and a simulated worker identity. Neither proves a real Windows subprocess identity, browser supervision, real HTTP transport/security, screenshot inspection, Postman execution or production serving. No real credentials existed in the fixture, so supported-reference use does not prove credential non-retention. There was no real remote write or application-root-cause diagnosis. B/C/D prose is not executed proof. One run per variant, shared host guidance and author assessment cannot establish general superiority or token/time/cost savings.

## Source and packaging checks

- Repository library validator: 20 skills, zero packaging errors.
- Repository unit suite: eight passed, one Windows symlink-privilege skip. Initial attempts failed because the PATH Python alias was inaccessible and the default sandbox temporary directory was unwritable. Using the bundled interpreter and a workspace-local temporary root completed the suite; no test code changed.
- Isolated migration suite passed. The first invocation was blocked by script-signing policy; process-scoped execution policy allowed execution, then the sandbox denied a junction. The authorized escalated run passed entirely within its isolated workspace fixtures.
- Official skill-creator validator could not run: bundled Python lacks PyYAML. The repository validator is separate packaging evidence, not a substitute official pass.
- Whitespace/diff validation passed. No commit, push, installation or application edit performed.

## Decision and continuation

Retain the focused source patch: an observed early-check ordering improvement, no observed clarification/contained-change regression in the matched cases, and explicit limitations support a bounded trial. Do not claim validated live effectiveness or universal performance improvement. Next evidence should come from the continuing application workstream: timing of its next critical capability check, amount of dependent work before proof, necessary versus avoidable owner questions, first populated-screen review, and use of the existing credential handoff during discovery. Keep application evidence there. Installation remains a separate owner action; current installed skills have not received this patch.
