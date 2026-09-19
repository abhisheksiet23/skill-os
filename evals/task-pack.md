# Task pack

Treat the following as separate small user requests. Answer each with the useful deliverable; use skills only when helpful. Do not browse: all evidence available for these bounded tasks is provided. Do not contact people, install software, deploy, or edit project implementation. Record skill files actually read and limitations; no private reasoning is requested.

## A. Review a backend function

Review-only: our existing Python API uses this function to calculate a percent discount. The ticket says discounts may range from 0 through 100 inclusive; invalid percentages must be rejected. The project uses `engineering/decisions.md` and has no phase records. Identify concrete defects and provide a minimal executable witness, without changing implementation.

```python
def discount(total, percent):
    if percent < 0 or percent >= 100:
        raise ValueError("invalid percent")
    return total * (1 - percent / 100)
```

## B. Existing frontend integration

Produce a concise implementation approach, not code. We already have a reviewed mockup and a working, documented API for an account-settings page. The approved design preserves the existing component library. We need save, validation-error and network-retry states. Neither frontend nor backend was built with this skill library. What should happen next and what would prove completion?

## C. Pricing with weak evidence

Suggest initial pricing architecture for a release-testing service. A typical engagement is assumed to need 10 delivery hours at 800 currency units per hour, plus 1,000 direct tool costs and 3,000 acquisition cost per new customer. A proposed price is 15,000. Buyers have not been interviewed and no one has paid. Customers may want predictable budgets. Give useful options and the next evidence needed; do not invent market research.

## D. Transfer a business finding into website copy

An owner approved exploring a release-testing offer but has not approved public pricing or guarantees. Research found competitors advertising fixed testing packages; it did not establish their sales. Two prospective buyers said they disliked surprise invoices; no purchase occurred. Draft a homepage proposition and CTA, with a short note about what cannot yet be claimed. Use the existing brand and do not design or build a website.

## E. Conflicting views and stopping

Analysis one says usage pricing differentiates us, based on founder intuition. Analysis two says customers prefer predictable subscriptions, based on three interviews in a different segment. Reconcile these views and identify the smallest useful next investigation. Separately, we already have credible competitor evidence, 12 target-customer interviews, tested pricing and a simple financial model: should we commission another broad market scan merely to be thorough?

## F. Restraint

Give three possible names for a QA consulting service. No availability research requested.

## G. Release preparation with missing proof

Prepare a concise release-readiness decision from these facts. Deployment is authorized for a staging simulation only. Candidate revision B changes a database migration; all recorded checks and approvals refer to revision A. The engineer says the new migration is probably safe and wants to mark it complete because the gap is documented. No migration execution environment is available in this task. Do not execute a deployment.
