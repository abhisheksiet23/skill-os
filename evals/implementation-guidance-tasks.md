# Implementation-guidance regression cases

These cases exercise actual artifacts after the 2026-11-10 rewrite and 2026-11-11 readability-loading correction. Once used, they are regression inputs, not held-out evidence. For a new comparison use fresh cases that vary behavior and failure paths. Freeze each skill variant, give each performer its own project and prevent access to peer outputs, author conclusions and assessment notes. Shared host instructions and filesystem access limit isolation.

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
