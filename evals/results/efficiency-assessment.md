# Delivery efficiency revision — assessment

Date: 2026-09-20. Scope: app-analyze, app-backend, app-frontend and app-qa. Historical motivation: Medcross analysis audit and later integration/QA findings. This is not a replay or timing comparison against the old Product Engineering OS.

## Method and limits

Two fresh independent evaluators received the same four bounded tasks in `../efficiency-tasks.md`, using respectively the pre-edit skills and revised skills. Each could load relevant references; neither received the intended answer or other output. Responses are preserved in `efficiency-before.md` and `efficiency-after.md`. Both used the parent model/settings without overrides. Cases were planning-only: no application, source, database or browser execution occurred in these evaluations. One sample per variant is insufficient for causal or general performance claims.

## Observations

| Case | Before | After | Assessment |
| --- | --- | --- | --- |
| Modernization | Already asks about widget scope before deep recovery; bounds session discovery | Explicit release boundary, one current contract and completion without consequential guesses | Both adequate. Candidate reinforces intended ordering; no demonstrated large improvement |
| Typo | Contained edit, existing checks, no new suite | Same restraint; no new analysis/design cycle | No observed process expansion |
| Repeated auth QA | Proposes reusable Node runner, real integration, production CSP checks and no premature MCP | Adds repeat execution, fresh contexts/cleanup, structured outcomes and setup/maintenance accounting | Useful specificity, without claiming tests were executed |
| Legacy integration | Starts with actual identity mappings and real boundary | More explicit thin path before expanding implementation | Both adequate; candidate preserves scope and proof boundaries |

Both variants preserved the material requirements in these supplied cases and distinguished proposed tests from execution. The candidate's preference for preserving seamless legacy authentication is a recommendation awaiting owner agreement, not permission; retain that distinction in real work. Neither evaluation establishes real-world defect escape or correction rates.

Reported partial evaluation intervals were 81 seconds before and 101 seconds after, excluding initial reads/final bookkeeping. They are not full task durations and do not show speed improvement. Token usage and monetary cost are unknown. Word counts are not token measurements. Do not claim numerical savings or general superiority.

## Separate executed QA pilot

Project-owned pilot in `E:/aj/experiments/medcross-admin/qa` uses the existing journey functions with Playwright Test 1.63.0 and installed Edge against the existing local HTTPS IIS site. Three anonymous checks passed in 4.898 seconds on the first run and again in a 5.856-second full invocation; the full invocation reported two authenticated cases blocked and exited 2 because credentials were absent. These timings cover runner execution, not initial implementation, dependency setup or visual review. Project evidence records candidate/environment and scope. Authenticated cases and original-CSRF-failure detection remain unproved. No deployment or application changes were made.

A browser-only negative control blocked CSS downloads. The initial `link.sheet` assertion incorrectly passed (3.931 seconds); a stylesheet object alone was inadequate evidence. The assertion was strengthened to require readable, populated CSS rules. The repeated negative control failed as intended (2 passed/1 failed, 3.818 seconds). After restoring normal browser requests, the final full run again reported 3 passed/2 blocked (5.805 seconds). The application/server was not changed for either probe. Initial and corrected negative-control summaries are retained separately in the project, rather than discarding the false positive. Desktop/mobile login validation screenshots were visually inspected; this does not establish authenticated or accessibility sign-off.

Repository packaging checks passed for all 18 skills, seven validator unit tests passed, the four edited skill entrypoints passed official validation, and isolated migration tests passed. The enabled installation was refreshed to `0.1.0+codex.20260920080937` with the prior deployment preserved by the installer. Static checks and installation are not behavioral performance evidence.

## Decision

Retain the narrow guidance changes for explicit decision ordering, evidence reuse, early real integration and repeatable QA. Do not create a universal workflow, mandatory test framework, MCP service or skill routing engine. Keep strategy/design/architectural depth when it prevents rework. Reassess on the next real modernization and repeated QA changes using total delivery effort, user corrections, omitted requirements, maintained test cost and escaped defects. Live repeated-run evidence supports the anonymous pilot's usability, not a full QA or token-efficiency claim.
