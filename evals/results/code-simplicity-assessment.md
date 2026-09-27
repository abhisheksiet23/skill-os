# Code simplicity instruction assessment

Date: 2026-09-27

Scope: `app-frontend` and `app-backend`. The user reported dense lines and unnecessarily complex generated code. No offending application source was supplied. The baseline is the repository version before this change; the candidate adds implementation and self-review guidance to each owning skill.

## Representative before/after review

This is a static instruction evaluation, not an independent model run or an executed application test. The same cases were reviewed against both versions. Baseline gaps do not prove that a model would produce poor code; candidate coverage does not prove improved output.

| Case and representative task | Baseline guidance | Candidate guidance and review finding |
| --- | --- | --- |
| Frontend: implement loading, error, empty and populated order-list states with a multi-step retry handler. | Requires meaningful states and avoids speculative abstractions; gives no explicit expression or handler readability guidance. | Explicit state branches, multiline JSX and named multi-step handlers address both dense rendering and hard-to-trace events. |
| Frontend: add local filtering to a small list using the existing component system. | Preserves conventions and performance, without criteria for effects, hooks or memoization. | Straightforward derived values and a concrete reason for memoization discourage duplicate state and premature machinery; established abstractions remain usable. |
| Backend: validate and authorize an order, persist it transactionally and handle a retry safely. | Strong correctness boundaries, but no guidance against compressed rule chains or unnecessary layers. | Explicit steps, domain names and purposeful helpers improve traceability while retaining transaction, authorization and idempotency requirements. |
| Backend: return a paginated list with related records under an established latency constraint. | Requires inspection of consequential queries and growth. | Keeps sensible queries and bounded work; permits justified optimization rather than making a simple-looking repeated-query loop the default. |
| Both: make a contained correction in code that already uses suitable project abstractions. | Establishes scope and project conventions. | Adds a changed-code readability pass while explicitly limiting cleanup to the requested change and preserving useful abstractions. |

## Limits and follow-up

The candidate covers the reported failure modes without prescribing line counts, maximum function lengths, a framework or a new shared dependency. Both skills retain their existing correctness and integration checks.

Live before/after code-generation quality, runtime correctness, human correction burden and token/runtime changes are unknown. To measure them, run the cases above as identical implementation requests in isolated application fixtures against each version, retain actual code and test outputs, and assess readability separately from behavioral correctness. No live behavioral pass is claimed here.
