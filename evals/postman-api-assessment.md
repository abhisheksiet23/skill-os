# Executable Postman upkeep assessment — 2026-10-20

Changed backend guidance from optional Postman creation to a default repository-owned runnable collection for HTTP APIs. The first API increment establishes it; contract changes update affected requests, examples and assertions. Compilation or internal-only changes do not cause cosmetic edits. A focused local reference covers real assertions, role/data setup, repeatable workflows, cleanup, runner compatibility, owner authorization and compact reports/failure-first diagnosis. Unit/database integration tests retain their distinct responsibilities. No new skill or test framework was added.

## Executed instruction exercise

Two separate performers answered the same three requests in `postman-api-tasks.md`. Baseline used HEAD `2833a89`; candidate used updated backend guidance/reference. They did not read peer outputs or assessment criteria. The author assessed both; this was not a blind assessment. Actual responses are retained locally in ignored `.eval-runs/postman/baseline.md` and `candidate.md`.

- First HTTP increment: baseline already selected Postman and generated a six-request illustrative collection with explicitly assumed transports and unresolved inputs. Its JSON parsed, but no requests/scripts ran. Candidate specified the default executable collection, scoped credentials/IDs, assertions, supported cleanup, local runner prerequisites and pending evidence; it declined to fabricate a runnable application collection from missing contract details. This outcome does not demonstrate artifact-production superiority or a working collection.
- Pagination contract change: both described replacing bare-array assertions with envelope/item checks, updating consumers/examples/extractors, preserving unrelated coverage and exercising boundary pages/authorization. Candidate emphasized in-place upkeep, compact reports and explicit runner compatibility.
- Internal-only refactor: both avoided collection churn and required applicable new-candidate evidence rather than presenting a prior green report as a fresh pass. Missing execution stayed pending.

The exercise supports comprehension of intended upkeep and boundaries but does not establish that generated collections stay synchronized on real projects. Future application evaluation should implement a real endpoint change, run the collection, deliberately break the contract and demonstrate failed assertions, then compare correction effort and context usage. No token saving is claimed here.

## Verification and limits

Library validator: 19 skills, zero packaging errors. Official backend skill validator and whitespace check passed. Postman CLI and Newman were not found on PATH. No runner installation, API server, real collection run, request/assertion execution, application/release build, SQL generation or production mutation occurred. No application repository was changed. Runtime pass rate, token cost and time savings are unknown.

Current official documentation was inspected: [Postman CLI local collection execution](https://learning.postman.com/docs/postman-cli/postman-cli-run-collection) and [Newman compatibility](https://learning.postman.com/latest-v-12/docs/reference/newman-cli/migrate-to-postman-cli). The reference preserves compatible existing Newman suites and calls for verifying version-specific OAuth/upload capabilities instead of uploading private data as a workaround.
