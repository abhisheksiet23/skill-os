# Returning-reader evaluation — 2026-10-17

Subsequent owner feedback: regenerated code remains dense; readability is not accepted as fixed. The structural observations below are historical evidence, not owner acceptance. Follow-up spacing requirements and a new reviewable example are evaluated separately in `code-spacing-tasks.md`.

Later feedback on 2026-10-17 accepted the spacing example as more readable. That scoped review is closed in `code-spacing-assessment.md`; it does not retrospectively accept the earlier dense code or establish whole-application readability.

## Scope and method

Updated `app-frontend`, `app-backend` and `app-qa` to require readable implementation for a developer returning after six years. The standard concerns business-flow comprehension, visible contracts, structured values, meaningful boundaries and necessary explanations, without banning modern syntax or requiring tutorial comments.

Executed matched implementation requests against a captured Medcross approve-and-assign workflow. Baseline used frontend/backend instructions at `4bae659`; candidate used the revised instructions. Two separate performers inherited the same parent model/settings and received the same source and request. Neither saw the other output or assessment key. A third agent independently reviewed both implementations using revised `app-qa`, and executed its own handler checks. This is one paired trial, not a general benchmark or human usability study. A final edit generalized the backend naming example from the project-specific role to administrator access; it did not change the evaluated standard.

All code edits were isolated under ignored `.eval-runs/readability/`. The active Helpdesk implementation was not modified. Source snapshot identity is recorded below because that application was changing during the review.

## Observed results

| Area | Baseline output | Candidate output |
| --- | --- | --- |
| Selection representation | Expanded parsing but retained `userId|teamId` convention | Structured `Assignment` bound through Angular `ngValue` |
| Client contract | Expanded inferred fields; remembered payload remained `unknown` | Named `TicketActionFields` and `TicketActionRequest`, typed remembered state |
| Submission path | Expanded existing dialog dispatcher | Focused ticket-action handler with explicit payload, retry, request and recovery steps |
| Backend rules | Expanded assignment branch and named predicates | Coherent `AssignTicket` helper, while outer command retains authorization, transaction, history and receipt ownership |
| Mechanism explanations | Retry and cumulative team-access comments | Also explains retry reconciliation before version checks and approval scope per review cycle |
| Template | Approval controls expanded | Approval controls expanded and structured selection visible |

Both outputs improved the captured source. Independent source assessment favored the candidate's discoverable contract and removal of the hidden string convention; it found no introduced behavior regression. The candidate still has a multipurpose root component and generic dialog, plus unrelated anonymous responses and dense transport logic. These were not silently counted as solved, and whole-application restructuring was outside this bounded request.

## Executed checks

- Both performers compiled their actual frontend sources with strict TypeScript/Angular templates: passed.
- Both compiled captured backend sources as isolated .NET libraries with existing cached application packages: passed, zero warnings/errors. No host or database was started. Candidate initially hit unavailable network restore with an incorrect cache location, then passed with offline cached dependencies.
- Both executed the actual transpiled submission method with API doubles: exact approval payload/version, unchanged retry ID, changed-intent ID, conflict handling and busy cleanup passed. Candidate additionally checked refreshed version, authentication handling and success behavior.
- Independent reviewer executed the actual fixture, baseline and candidate method bodies against the same check: payload, network retry, changed fields, refreshed version, preserved entries, 409 recovery and lost action availability passed for all three.
- Source review checked retry reconciliation before stale-version rejection, existing visibility/action checks, eligibility, approval cycle, additive team grants, history and transaction ordering. Compilation and review do not prove SQL transaction behavior.
- Library packaging validation: 19 skills, zero errors. Official skill validator: all three changed skills passed. Git whitespace check passed.

No real SQL Server writes, authentication/CSRF integration, database concurrency/rollback, browser interaction or production deployment was exercised. Human comprehension and owner satisfaction remain unknown, as do provider token/cost metrics. This trial supports a concrete improvement in one generated workflow; it does not establish that every generated file now meets the standard.

## Local review artifacts and source identity

Actual code and commands: `.eval-runs/readability/baseline/`, `candidate/`, `baseline-result.md`, `candidate-result.md`, and `independent-assessment.md`. Evaluation request: `returning-reader-tasks.md`. These are evaluation artifacts, not production changes or installed plugin updates.

Captured source SHA-256 values:

| Source | SHA-256 |
| --- | --- |
| frontend/src/api.ts | ef93d564bca216649a7e900998078910eb50c6f02ac28299effdac3edd861de8 |
| frontend/src/app.html | 6c946aa9f3a62211f155d08a8b9cc2aa50c80c0eecd1aae2edc15e190b581fbf |
| frontend/src/main.ts | 58b97ae71f263ae0ef8416c5bee965b4d1bd5b997b118ad36cea0a8f33888089 |
| backend/Helpdesk.Api/AccountService.cs | ddef5da9846ff68cba0503c6dd105728de3cdef539ecf4fc3d481a9d775ffa00 |
| backend/Helpdesk.Api/Models.cs | fe6490bcdd192ed7919994f7dc11a72828a82e36882d9ca5f5cdbe64e1aedef6 |
| backend/Helpdesk.Api/TicketService.cs | 38a03633daf287b0afb6fce99620f0334bf41a06b25e4721a80144086a5e3555 |
