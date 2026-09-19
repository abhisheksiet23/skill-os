# Candidate task outputs

Scope: seven separate bounded requests, using the supplied catalog and evidence only. No browsing, implementation edits, deployment, contacts, or external mutations. Read `C:/Users/Abhishek/.codex/RTK.md`, `evals/task-pack.md`, and `evals/candidate-catalog.md`. Skill paths below are relative to `E:/aj/experiments/skill-os/skillmesh/skills/`.

## A. Backend review

Two concrete findings in the supplied function:

- The guard at function line 2 rejects `percent == 100`, although the ticket explicitly permits it. `discount(200, 100)` raises `ValueError`; expected result is zero. Change the upper-bound comparison to reject values greater than 100.
- The same guard accepts floating-point NaN, which is not a percentage in the permitted interval. `discount(200, float('nan'))` returns NaN, propagating an invalid amount. Validate a supported numeric percentage as belonging to the closed interval, including rejecting NaN. Merely changing `>=` to `>` does not fix this.

Minimal executable witness (the function body is unchanged):

```python
def discount(total, percent):
    if percent < 0 or percent >= 100:
        raise ValueError("invalid percent")
    return total * (1 - percent / 100)

import math
try:
    discount(200, 100)
except ValueError:
    print("WITNESS CONFIRMED: valid 100 rejected")
else:
    raise AssertionError("boundary defect not reproduced")
assert math.isnan(discount(200, float('nan')))
print("WITNESS CONFIRMED: NaN accepted")
```

Executed this witness plus normal/invalid probes through PowerShell stdin using `& C:/Users/Abhishek/.local/bin/rtk.exe proxy C:/Users/Abhishek/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe -`. Exit code 0; both witness confirmations printed. Observed results for total 200: 0 → 200.0, 25 → 150.0, 100 → ValueError, -1 → ValueError, 101 → ValueError, NaN → NaN. The exit code confirms reproduction, not correctness of the implementation.

Read: `app-qa/SKILL.md`, `app-qa/references/verification.md`. Candidate is exactly the supplied snippet, not a checked-out API revision. API input parsing, supported numeric types, total validation and money-rounding rules were not supplied or tested. NaN reachability through the API remains unknown; acceptance by this Python function is demonstrated. Record the review in the project's existing `engineering/decisions.md` when doing project work; no phase records or new lifecycle are needed. No project records were edited here.

## B. Existing frontend integration

Proceed with production frontend integration using the approved mockup, existing components and documented real API. Their origin outside this library is immaterial. Inspect local conventions and the actual contract, then map initial load, edits, saving, saved confirmation, field/server validation and network failure/retry states onto that design. Preserve entered values on errors, associate messages with fields, manage focus accessibly and prevent accidental duplicate submissions. Establish retry behavior against the API's idempotency/concurrency rules; do not blindly replay an ambiguously successful save.

Completion requires an appropriate successful build, meaningful state-transition checks, and real API evidence that edits persist and reload correctly; validation errors retain values and identify actionable corrections; network recovery succeeds without unintended duplicate effects. Inspect rendered states at relevant widths against the approved mockup and check keyboard/focus behavior. Record the candidate, checks and gaps in existing project records. No new prototype, mock backend, backend rewrite or prerequisite skill history is required.

Read: `app-frontend/SKILL.md`. This is an implementation approach only; no repository, API, browser, build or integration checks executed.

## C. Initial pricing architecture

All figures are provisional currency units per engagement, with tax treatment unspecified. Delivery labour is 10 × 800 = 8,000; plus tools 1,000 gives delivery cost 9,000. Including assumed acquisition cost 3,000 gives 12,000 per new customer. At 15,000, the delivery contribution is 6,000 (40%); after acquisition it is 3,000 (20%), before overhead, idle capacity, tax and uncounted support. This is not net profit or evidence of willingness to pay. At 13.75 delivery hours the assumed new-customer contribution reaches zero: (15,000 − 1,000 − 3,000) / 800. Repeats could contribute 6,000 if acquisition is not incurred again and other assumptions hold.

Assumed payer to verify: the person accountable for a team's software release budget. Assumed purchased value: clearer release risk and actionable findings within an agreed testing scope.

| Option to test | Metric, package and provisional level | Trade-off and evidence test |
|---|---|---|
| Bounded release package — recommended first | 15,000 per agreed release scope; specify environments, flows, test window, findings report and bounded retest allowance; exclude extra releases, unagreed environments and unlimited support. Approve any extra scope and quote before work. | Predictable buyer budget but seller bears effort overruns. Reference is the assumed 12,000 cost, not market acceptance. Test concrete paid offers and track actual hours including retests. |
| Capped time-based engagement | Hypothesis: 1,500 per delivery hour, capped at 15,000 for up to 10 hours; scope/priorities stop at the cap unless buyer approves more. Define tool and retest inclusion. | Budget certainty can coexist with usage pricing, but unfinished coverage at the cap is an objection. At 10 hours economics match the package; smaller jobs may not recover fixed acquisition/tool costs. Test package choice and willingness to accept a scope boundary. |
| Recurring bounded package | Hypothesis: 15,000 per month for one defined release allowance, only for buyers with recurring need; specify expiry/rollover, retests, renewal/cancellation and separate quotes for excess usage. | Predictability and capacity reservation may help, but intermittent release cadence makes commitment unattractive. Do not promise unlimited releases. Test cadence, paid renewal and delivery load before offering discounts. |

Next evidence: interview target budget owners about their last release, actual testing spend/alternatives, invoice surprises, procurement and cadence. Then present a concrete scope and two credible packages. For a small initial test, predeclare a learning threshold such as at least two paid pilots among five qualified offers at the proposed price, with actual costs leaving positive contribution; this is a proposed test criterion, not a forecast or statistical validation. Repeated rejection on value/price or overruns would trigger revisions. Payment and repeat use are stronger evidence than interview preferences. Owner approval is still needed before adopting public prices or terms.

Read: `business-pricing/SKILL.md`. Checks: arithmetic calculated from supplied assumptions; no demand research, paid tests or market prices observed. Currency, tax treatment, true scope variability, acquisition attribution and buyer authority remain unknown.

## D. Homepage proposition and CTA

Draft for internal review, using the existing brand:

**Understand release risks before your next launch.**

We're exploring a focused release-testing service for software teams. Tell us what you're shipping and where you need more confidence, so we can discuss a useful testing scope and a clear budget before any work begins.

**CTA: Discuss your next release**

This conveys the exploratory status without announcing approved commercial terms. Do not claim established demand, proven sales, fixed public prices, guaranteed bug detection, defect-free releases or guaranteed outcomes. Competitor advertisements show package positioning, not their sales; two prospects' invoice concerns suggest a budgeting need, not purchase intent or validated pricing. The budget discussion is draft positioning, not an approved pricing guarantee. Preserve brand voice/styles when this copy is eventually placed; no design or build is requested.

Read: `website-create/SKILL.md`, applied only to the requested copy and evidence boundary. Its broader prototype/design workflow was outside the explicit scope, so no creative/artwork references were needed. Checks: claims compared with supplied evidence and approval limits; no publication, design, build or buyer test executed.

## E. Conflicting views and stopping

Preserve both claims: usage-based differentiation is founder intuition; subscription preference comes from three interviews in a different segment. Neither establishes what the intended segment will purchase. They address partly different questions—distinctiveness and budget predictability—and use unequal, limited evidence. A capped usage plan or fixed allowance could reconcile them, but that remains a hypothesis; do not silently choose subscriptions or treat differentiation as demand.

Smallest useful investigation: show a few qualified target-segment budget owners two otherwise comparable concrete offers, one capped usage and one fixed allowance, using realistic low/high usage bills. Ask about their recent spend and purchasing constraints, request a package choice and a credible paid-pilot commitment. Predefine the decision: favor the option producing actual commitments at viable economics; if both fail, revisit value/scope rather than declaring either pricing theory correct. Small-sample findings are directional and require observed delivery/renewal before scaling.

For the separate mature-evidence case, do not commission another broad scan merely for completeness. Existing credible competitors, 12 relevant interviews, tested pricing and a financial model justify acting on the actual decision unless a specific unresolved assumption, stale evidence or new market change could reverse it. Investigate that gap narrowly if it exists; otherwise stop researching.

Read: `business-challenge/SKILL.md`. Checks: reconciled supplied evidence types and segment scope; no fresh research or experiment executed.

## F. Three possible names

- Release Lantern
- ClearPass QA
- SteadyShip Consulting

Skills read for this task: none. Checks: none; availability was not researched or implied.

## G. Release-readiness decision

**Revision B is not ready for the authorized staging simulation; leave migration verification and release completion pending.** All recorded checks and approvals refer to A. B's migration change invalidates affected readiness evidence; an engineer's expectation and a documented gap do not constitute proof. Preserve unaffected A evidence where applicability can be established, but do not relabel it as B verification. No deployment is executed, and production deployment is outside the authorization.

Prepare a B-specific handoff now: exact revision/artifact identity, migration difference and affected data, compatibility with retained readers/writers, execution order, expected duration/locking, backup and tested restore or forward-recovery approach, and post-migration integrity/application smoke checks. A code rollback must not be assumed to reverse changed data. The actual migration contents were not supplied, so these remain required preparation items rather than completed technical findings.

Before the simulation proceeds, provide a migration execution environment and run B on representative existing data; assess schema/data correctness, affected integration, failure/recovery behavior and relevant regression checks. Bind results to B and obtain any B-specific review required by the existing release process; do not assume A's approvals cover the change. Existing authorization for staging simulation does not need to be requested again. Any later actual simulation must verify deployed revision and health before marking that scope complete.

Read: `app-deliver/SKILL.md`, `app-deliver/references/release.md`; used the candidate/evidence principles already read in `app-qa/references/verification.md`. Checks: compared supplied candidate and proof revisions. Migration execution, recovery proof and deployment verification are unavailable, not passed. No environment exists in this task and no deployment or project mutation occurred.

## Execution limits

Only the discount snippet was executed. B–G are requested bounded approaches, calculations, drafts and decisions using supplied facts, not live behavioral passes. No measured token counts or self-grades are claimed. The only file written is this report.
