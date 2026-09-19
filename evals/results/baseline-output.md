# Baseline task responses

## A. Backend function review

Two concrete findings in the supplied function:

- The guard rejects `percent == 100`, contrary to the explicitly inclusive requirement. `discount(200, 100)` must return zero but raises `ValueError`.
- A Python floating-point NaN is not a valid percentage in the stated range, but both comparisons are false, so it returns NaN instead of rejecting it. This matters if this function can receive NaN; whether the API's request parser already excludes it is unknown.

Minimal executable witness, using the original implementation unchanged:

```python
def discount(total, percent):
    if percent < 0 or percent >= 100:
        raise ValueError("invalid percent")
    return total * (1 - percent / 100)

for p in [0, 50, 100, -1, 101, float("nan")]:
    try:
        print(repr(p), "=>", discount(200, p))
    except Exception as e:
        print(repr(p), "=>", type(e).__name__, str(e))
```

Executed with the provided Python runtime through `rtk proxy`; exit code 0, output:

```text
0 => 200.0
50 => 100.0
100 => ValueError invalid percent
-1 => ValueError invalid percent
101 => ValueError invalid percent
nan => nan
```

The process completed successfully; that does not mean the function meets its requirement. The observed 100 and NaN results demonstrate defects. Corrective direction: permit the upper endpoint and reject values outside the finite numeric range under the API's intended type policy. Decimal-money rounding, coercion, and total validation need a contract before further findings can be asserted. Record the review in the existing `engineering/decisions.md` if later authorized; no phase records are needed and no implementation or project record was changed here.

Skills read specifically for A: none; direct code review and execution were sufficient. Limitation: supplied function only, no actual API request-path check.

## B. Existing frontend integration

Implement the account-settings page against the existing documented API and reviewed mockup, preserving the component library. Existing work does not need to have originated in this skill library. Reuse current project records and resolve only actual gaps in the save/error/retry contract; do not rebuild the backend or repeat design approval solely to satisfy a workflow.

Use the existing API through a typed service boundary. Cover idle/editing, saving, saved, field-validation errors, and recoverable network failures. Keep user input on failure, make error messages accessible, prevent duplicate submissions while saving, and let users retry deliberately. For an ambiguous timeout, use the API's idempotency/read-back behavior rather than assuming the save never happened. A retry must not create an unintended second operation.

Completion evidence: focused tests of state transitions and error mapping; actual API integration proving save and reload persistence; validation rejection and retry recovery; keyboard/focus and accessible feedback checks; rendered comparisons with the approved mockup at relevant viewports/states; relevant lint/build checks. Bind results to the implemented candidate. Mocks may inject failures but cannot replace proof of real API integration. Backend changes are unnecessary unless integration exposes a genuine contract defect.

Skills: `app-frontend`; references F1–F7 below. Checks here: approach reconciled against the supplied design/API facts; no implementation, API, or browser checks were executed.

## C. Pricing with weak evidence

The assumed delivery cost is `10 × 800 + 1,000 = 9,000`. At 15,000, the contribution before acquisition is 6,000, or 40% of revenue. Including the assumed 3,000 new-customer acquisition cost leaves 3,000, or 20%, before overhead, tax, rework, and other omitted costs. First-engagement break-even under these assumptions is 12,000. A further 3.75 delivery hours consumes the remaining 3,000. These are scenario calculations, not observed margins or market validation.

Useful initial architectures:

- A fixed-scope engagement at a provisional 15,000: define releases/environments, test scope, reporting, retest allowance, exclusions, and a separately approved change process. This offers a predictable budget but transfers overrun risk to the provider.
- A base package plus clearly priced optional work, with an agreed spend cap: maintains a predictable core while accommodating variable scope. Confirm additions before charging.
- A recurring subscription with defined included release capacity and rollover/overage terms: investigate only for buyers with recurring needs; it creates capacity and utilization risk. Do not assume subscriptions fit occasional buyers.

Use 15,000 as an internal pilot hypothesis, not an approved public price. Next, identify the target buyer and interview a small group about recent testing purchases, budget ownership, release frequency, surprise costs, and alternatives. Test concrete scoped proposals with qualified buyers and seek paid-pilot commitments. Measure actual hours, rework, direct costs, acquisition cost, and repeat demand. Customer preference and willingness to pay remain unknown. Recommend a fixed-scope paid pilot as the smallest test; the owner retains the commercial decision.

Skill: `discover`. Checks here: arithmetic derived from the supplied assumptions; no customer research, sales, or live financial evidence obtained.

## D. Homepage proposition and CTA

Draft for owner review, using the existing brand:

**Know what needs attention before your next release.**

We’re exploring a release-testing service for teams preparing to ship. Talk with us about your next release, the areas you need tested, and your budget constraints to help shape a suitable engagement.

**CTA: Discuss your next release**

This wording presents an exploratory offer without implying an established service, approved package price, guaranteed outcome, or operational commitment. Competitors advertising fixed packages demonstrate how they present offers, not that those packages sell. Two prospective buyers' dislike of surprise invoices is limited preference evidence, not validated demand or willingness to pay. No claims of proven savings, defect-free releases, customer traction, or fixed-price guarantees are supported. Owner permission to explore is not permission to publish pricing or guarantees. The draft is not published. No brand redesign is proposed; specific brand voice assets were not supplied.

Skill: `website-create`; references W1–W2. Checks here: claims traced to the task evidence; no site design, rendering, or implementation was performed.

## E. Conflicting views and stopping

The two analyses answer different questions with weakly matched evidence. Founder intuition supports a hypothesis about differentiation, not customer acceptance. Three interviews support a preference within a different segment, not necessarily this offer's target buyers. Usage billing and budget predictability can also coexist through capped usage or included allowances; they are not inherently incompatible.

Keep both hypotheses open. The smallest useful investigation is a focused comparison with a few actual target buyers using the same concrete scope and low/typical/high usage scenarios: usage billing, a fixed package, and a cap or allowance. Ask about their latest purchase and approval process, then seek a scoped paid-pilot commitment. Observe economic feasibility as well as preference. Do not declare a market-wide winner from these conversations.

Separately, do not commission another broad market scan merely for thoroughness when credible competitor evidence, 12 target interviews, tested pricing, and a simple financial model already support the current decision. First identify a remaining decision-changing uncertainty or stale assumption. If none exists, stop research and act on the existing evidence; if one exists, investigate only that gap.

Skill: `discover`, reused from C. Checks here: compared provenance, segment, and claim strength in supplied evidence; no new research executed.

## F. Three names

- Release Compass
- ClearSignal QA
- Test Harbor

Skills: none. No availability, trademark, or domain research performed or claimed.

## G. Release-readiness decision

**Revision B is not ready to be marked complete. Required migration proof is pending.** Checks and approvals for revision A do not establish the safety of B's changed migration. The engineer's confidence and a documented gap cannot substitute for execution evidence.

The authorization covers only a staging simulation. This task also explicitly prohibits deployment, so none was executed. No production authorization is inferred.

Prepare a candidate-specific follow-up: identify the A-to-B migration diff and affected schema/data consumers; review order, compatibility, locking and data-loss risks; define a suitable recovery or forward-fix path. In a representative migration environment, execute B's migration against relevant existing data and test resulting application behavior and data integrity. Exercise recovery as appropriate to the migration's reversibility, and rerun impacted integration/regression checks. Re-attest unaffected A evidence only after checking that it still applies to B. Record revision, environment, command, outcome, and applicable authorization together before reassessing readiness.

The execution environment is unavailable, so migration execution and recovery validation remain pending, not passed or N/A. A staging simulation, when available and authorized, would still need to be described as simulation evidence and would not establish a production deployment. Keep the release incomplete with the precise blocker and next action recorded.

Skill: `app-deliver`; references F1–F4 and F7. Checks here: candidate/evidence and authorization consistency review only. No migration, deployment, or recovery test executed.

## Actual reading and execution record

Task inputs read: `E:/aj/experiments/skill-os/evals/task-pack.md`, `E:/aj/experiments/skill-os/evals/baseline-catalog.md`, and shell conventions `C:/Users/Abhishek/.codex/RTK.md`.

Skill files actually read:

- `E:/aj/experiments/ai-product-engineering-os-v1.4/skills/app-frontend/SKILL.md`
- `E:/aj/experiments/shipwright/skills/discover/SKILL.md`
- `E:/aj/experiments/ai-driven-website/skills/website-create/SKILL.md`
- `E:/aj/experiments/ai-product-engineering-os-v1.4/skills/app-deliver/SKILL.md`

Referenced files actually read:

- F1: `C:/Users/Abhishek/.codex/product-engineering-os/kernel/bootstrap.md`
- F2: `C:/Users/Abhishek/.codex/product-engineering-os/kernel/evidence.md`
- F3: `C:/Users/Abhishek/.codex/product-engineering-os/disciplines/review.md`
- F4: `C:/Users/Abhishek/.codex/product-engineering-os/kernel/agent-trust.md`
- F5: `C:/Users/Abhishek/.codex/product-engineering-os/orchestration/planning.md`
- F6: `C:/Users/Abhishek/.codex/product-engineering-os/disciplines/testing.md`
- F7: `C:/Users/Abhishek/.codex/product-engineering-os/orchestration/change-classifier.md`
- W1: `E:/aj/experiments/ai-driven-website/skills/website/references/operating-rules.md`
- W2: `E:/aj/experiments/ai-driven-website/skills/website-create/references/creative-practice.md`

Read these files using PowerShell `Get-Content`. Executed the A witness via `C:/Users/Abhishek/.local/bin/rtk.exe proxy C:/Users/Abhishek/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe -c ...`. No other executable behavioral checks were run. No browsing, project implementation changes, external writes, deployments, or further delegation occurred. Only this response artifact was written. Broader skill workflows and project-record creation were scoped out in favor of the explicit bounded task requests. No measured token metrics are available.
