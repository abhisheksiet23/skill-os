# Common experiment case: equipment reservations

**Decision, 2026-11-18:** use [ER-1](fixtures/equipment-reservations/brief.md) as the default continuing case for major and minor Skill OS experiments. It reuses the existing equipment-reservation scenario rather than inventing a new domain for every run. Its distinct continuing purpose is comparing changes against a stable shared product contract across analysis, design, implementation, QA and context work.

The brief is reusable input, not natural-use evidence. The owner-authorized [executable specimen](fixtures/equipment-reservations/specimen/README.md) now supports bounded synthetic T-08/T-09/T-10 experiments; it does not resolve the real-project dependency for T-06/T-04 or establish field benefit. Its rendered path explicitly combines ER-LIMIT and ER-DRAFT, while the canonical base brief retains its original facts and open choices. All fixture extensions are explicitly synthetic. The older [requirements case A](requirements-density-tasks.md#a-equipment-reservations) remains its original frozen task; use ER-1 as the current common-case authority instead of treating both versions as competing contracts.

## Run the relevant slice

Use the same domain by default; do not force every experiment through every stage or claim it can answer every question. Supplement ER-1 when it lacks the deciding evidence. A business-demand or external-provider claim, for example, needs its own supplied evidence. Broad transfer claims need materially different cases too.

| Experiment | Small useful slice | Required evidence boundary |
| --- | --- | --- |
| Analysis / contract traceability | Specify confirmation and own-reservation view; retain the unresolved draft choice; later supply ER-DRAFT | Distinct source facts, accepted fictional choices and proposals; trace changed behavior to checks |
| Prototype / frontend / microcopy | Asset/date selection, confirmation result, own list and an affected error state | Inspect rendered states, keyboard/focus and responsive behavior when claimed; mocks remain labelled |
| Backend / domain pattern, including T-08 | Date/eligibility rules and operation replay; compare recorder, camera and projector consumers | Implement real consumers inside the isolated specimen before judging extraction; test differing limits and camera-only training without awkward generic exceptions |
| Verification, including T-09 | Make a demonstrated recurring ER boundary executable in the specimen runner | Executed runner; check detects the relevant original fault; test count alone is not benefit |
| Rendered example, including T-10 | One actual gap such as date-conflict draft recovery after ER-DRAFT | Existing example check, observed gap, rendered candidate and upkeep; no gallery requirement |
| Navigation / context | Trace one implemented confirmation path or resume an ER change from project records | Requires actual specimen code/records and observed retrieval; no invented navigation failure or continuity pass |
| Discovery/loading, including T-11 | Follow actual skill/reference consultation during one ER task | Source-bound trace of a real miss or repeated irrelevant retrieval; scenario availability is not such a trace |
| Major cross-component change | ER-LIMIT plus affected UI, API/domain, persistence and checks where implemented | Trace one complete path, then affected consumers and regressions; source, mock, loopback and deployed evidence stay distinct |
| Recovery / release | ER-RECOVERY or ER-RACE against an executable candidate | Actual race/restart and required persistence/integration checks; release remains separately authorized |

## Keep comparisons interpretable

Before execution, identify the ER-1 version and file hash, selected slice/change, intended observation, frozen baseline/candidate skill and specimen revisions, tool/model environment, and actual write/execution scope. Resolve only gaps that block that slice. A small experiment can use one explicit task paragraph; no new record format or orchestration mechanism is required.

Give a performer the [brief](fixtures/equipment-reservations/brief.md), its selected task/change, adequate specimen sources and its assigned frozen skill variant. Keep this guide, assessment notes, peer outputs and prior conclusions out of the performer packet. Use fresh performer contexts only when available and authorized; otherwise disclose shared context. Shared filesystem and host instructions remain isolation limits.

Use equal starting state and the same relevant facts for baseline/candidate comparisons. Do not let one variant consume the other's generated design/code. Experiments that intentionally continue a specimen identify the prior snapshot they inherit; later runs are not independent replications. Record changed requirements separately from implementation changes, and invalidate only affected old evidence.

Keep temporary comparison/mutation copies under the existing ignored `.eval-runs/` area. The maintained [specimen and contract tests](fixtures/equipment-reservations/specimen/README.md) stay with this fixture because subsequent common-case experiments have a continuing consumer for them. If this becomes an actual application, create it in its own application directory and keep its code, records and application evidence there. No application build, installation, deployment, external service call or new tool spending is authorized merely by adopting this fixture; the owner separately authorized the local T-08 specimen experiment.

## Assessment checks — evaluator input

Select the checks affected by the task; the list is not a demand to build every layer for every minor change. A requirement below is an oracle, not a recorded pass.

| Boundary | Distinguishing observation |
| --- | --- |
| Inclusive duration and weekends | With the fixed clock: REC-01 on Nov 22–28 is seven days and permitted; Nov 22–29 exceeds its limit. CAM-01 for trained EMP-01 on Nov 18–20 is permitted; Nov 18–21 exceeds its limit. PROJ-01 on Nov 18–19 is permitted; Nov 18–20 exceeds the baseline limit. A same-day reservation counts as one day |
| Invalid dates | Start before Nov 18 or end before start is rejected without authoritative-state mutation |
| Training freshness | EMP-02 cannot create a camera reservation; EMP-01 losing training after catalogue display cannot create one either |
| Overlap endpoints | New REC-01 Nov 19–20 conflicts with the seed; Nov 21–22 also conflicts; Nov 22–23 does not. Another asset on the same dates does not conflict merely because the dates match |
| Concurrent confirmation | For a fresh contested slot, concurrent valid confirmations yield at most one new confirmation; inspect resulting state, not only response codes |
| Lost response / replay | Retry the successful operation with identical facts: same logical confirmation, no second booking. Different payload under that operation conflicts without mutation. Another employee cannot retrieve the first employee's result through replay |
| Read isolation | EMP-01 cannot see EMP-02's seed confirmation; rejected/forged reads do not disclose its details |
| Unresolved experience | Baseline outputs retain the open draft decision. ER-DRAFT changes only its stated behavior; do not quietly apply it to baseline or other errors |
| ER-LIMIT compatibility | New three-day projector confirmation succeeds; four days fails; recorder/camera rules stay unchanged; existing confirmation replay remains valid |
| Domain extraction | Real recorder/camera/projector paths use the candidate pattern; verify variation points and unchanged behavior against the same pre-extraction contract. Similar-looking code alone does not justify extraction |
| Recovery limits | Only actual restart with persistent state proves restart recovery; in-memory tests, simulation and sequential calls are labelled for what they establish |

Preserve rejection state, ownership and retry guarantees while improving readability, layout or abstraction. Use the existing [evaluation method](README.md#compare-useful-outcomes-and-total-execution-effort) and [rubric](deliverable-quality-rubric.md). Record passed/failed/blocked/untested boundaries, observed corrections and known preparation/upkeep. Time/provider usage/cost/savings remain unknown unless measured comparably. Fixtures, keys and this guide are public regression material, not held-out evidence; use independently prepared variations for a fresh comparison, and report familiarity.

**Current evidence, 2026-11-18:** [T-10](../docs/toolkit-session-assessments.md#t-10-rendered-conflict-example) adds one rendered conflict/recovery example: 32 Python/domain and actual loopback HTTP checks, plus nine Chromium scenarios and inspected screenshots at three widths. [T-09 ER-LIMIT](../docs/toolkit-session-assessments.md#t-09-er-limit-repeatable-verification) and [T-08](../docs/toolkit-session-assessments.md#t-08-synthetic-domain-pattern-experiment) retain their source-bound earlier rule-change/extraction evidence. These are author-run synthetic checks, not a before/after skill comparison, independent review, production integration, natural-use observation or measured benefit. Screen-reader, persistent restart and owner-comprehension evidence remain unavailable. Future source/requirement changes need affected revalidation.
