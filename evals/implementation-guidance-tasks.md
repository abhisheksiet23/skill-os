# Implementation-guidance regression cases

These cases exercise small implementation changes and asynchronous-action artifacts. Once used, they are regression inputs, not held-out evidence. For a new comparison use fresh cases that vary behavior and failure paths. Freeze each skill variant, give each performer its own project and prevent access to peer outputs, author conclusions and assessment notes. Shared host instructions and filesystem access limit isolation.

Use only Python and Node built-ins. No installs, production builds, deployments, external services or changes outside the assigned project. The API below is a synthetic contract, not an application fact. Loopback HTTP tests are allowed; browser/layout verification is outside this task. Report actual skill/reference reads, changed files, commands/results, source comprehension obstacles and unavailable evidence. Do not treat test counts or agent source review as owner readability acceptance.

## A. Small backend correction

Supply this `discount.py`:

```python
def discount(total, percent):
    if percent < 0 or percent >= 100:
        raise ValueError("invalid percent")
    return total * (1 - percent / 100)
```

Allow percentages from 0 through 100 inclusive and reject values outside that range, preserving established numeric semantics. Correct the defect and run meaningful regression checks. No unrelated API, schema, identity or framework work is requested. Verify the relevant regression fails against the original code when feasible.

## B. Frontend asynchronous action

Implement an ES module exporting `createSettingsEditor({endpoint, initialName})`. Return an editor with readable state `{name, status, error, fieldErrors}`, `setName(name)` and async `save()`.

- Initial status is `idle`. Edits clear earlier errors and set idle unless a request is saving.
- Save PUTs JSON `{name}` through actual fetch to the supplied endpoint. Status is `saving` during the request.
- A 200 JSON `{name}` response supplies the canonical saved name; status becomes `saved`.
- A 422 JSON `{errors:{name:message}}` response sets error status and exposes field errors without losing the draft.
- Network or other HTTP failure sets error status with a useful message, preserves the draft and permits an explicit subsequent save retry.
- Overlapping save calls produce one request. Do not add automatic retries, change authentication or invent UI/layout requirements.

Write and execute Node tests with a real loopback HTTP server and a controlled transport failure. Distinguish actual HTTP exchange from any transport doubles, source inspection and browser evidence. Check state during the pending request as well as its eventual outcome. This action module does not establish rendered UI, accessibility or production-host correctness.

## Compare useful outcomes

Inspect the actual code and tests rather than only the performer's summary. Check boundary behavior, contract fidelity, draft preservation, explicit retry, duplicate suppression and source flow. Record whether detailed readability references were actually loaded for both cases, while distinguishing correlation from a causal effect of instruction wording. A comparison where both variants pass supports regression coverage but does not demonstrate superiority.

## C. Behavioral contract, implementation and distinguishing checks

Use independently frozen analysis, backend and QA skill variants with equal isolated copies of this module:

```python
class Reservations:
    def __init__(self, capacity):
        self.available = capacity
        self.orders = {}

    def reserve(self, order_id, quantity):
        self.available -= quantity
        self.orders[order_id] = quantity
        return {"order_id": order_id, "quantity": quantity}
```

User request: make this single-threaded in-memory module meet the contract, retaining its public interface. Capacity is a nonnegative integer and quantity is a positive integer; reject booleans and nonintegers. Order IDs are nonblank strings and remain exact identifiers without normalization. A valid new reservation reduces availability once and records the quantity. An identical repeat returns the same logical record without consuming capacity again. A repeated ID with a different quantity is a conflict. Invalid requests, conflicts and insufficient capacity raise `ValueError` without changing availability or orders. Construction with invalid capacity raises `ValueError`. Zero remaining capacity is valid. There is no concurrency, persistence, authentication, HTTP or release requirement.

Implement locally, execute relevant checks, and demonstrate that consequential assertions detect faults in the supplied original. Keep the result and explanation proportionate. Do not expand scope or claim real application integration or owner comprehension. Record actual skills/references used and verification limits.

An assessor should independently exercise valid allocation, equal/conflicting repeats, exact exhaustion, insufficient capacity, invalid inputs and unchanged state after rejection. Inspect how requirements, code boundaries and tests agree; a test generated from incorrect implementation is not independent acceptance evidence. Preserve original failure observations without presenting them as failures of an unrelated application.

## D. Ambiguous promise and an accepted-but-unacknowledged effect

This case tests judgment missing from the fully specified in-memory case. Freeze variants including analysis, solution-design, backend and QA as relevant. Give performers the following raw task and evidence without the assessment notes or other variant's output. No live services, payments, purchases, deployments or external writes are authorized. Initial task is analysis/design only.

User request: "Add automatic service credits when a scheduled pickup is cancelled. Make it safe to retry. Prepare the next implementable increment."

Supplied evidence:

- The current brief says "cancelled pickup gets a credit" but does not settle whether cancellation after the driver begins loading is eligible. Existing code prevents cancellation after loading, but the owner has not accepted that behavior as the new rule.
- The external credit provider supports issuing a credit and querying by a caller-supplied unique reference. A duplicate reference returns its existing operation. A response can be lost after acceptance; queries may temporarily return not-found during propagation. No bound or final-rejection signal is documented yet.
- The local database owns pickup state and credit-request records. It cannot share a transaction with the credit provider. Local startup performs compatibility checks, not schema changes.

After the initial response, supply this owner clarification: "Keep loading-started pickups ineligible. The same cancellation must never produce another credit on retry. The UI may show credit pending until confirmed; uncertain results must remain reconcilable. Keep provider references stable."

Ask for the smallest sufficient design and a discriminating verification plan under that clarification. Where an isolated executable simulator is available, inject acceptance followed by response loss, delayed lookup visibility and a local restart; label this simulation rather than real provider integration. The performer must not invent a provider guarantee or issue a new credit reference merely because a query initially returns not-found.

Keep evaluation keys separate from the performer prompt. Assess whether the first response identifies the consequential eligibility decision without adopting code behavior as approval, and bounds useful independent work. Assess whether the clarified approach separates local atomicity from external reconciliation, retains operation identity and pending state, defines recovery ownership, and tests the ambiguous outcome. A generic queue recommendation, mock-only success or claim of atomic rollback across systems is insufficient. Missing provider evidence remains explicit; old fixture passes do not establish it.
