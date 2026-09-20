# Delivery efficiency — candidate responses

Only the supplied case evidence and repository skills were used. These are independent responses, not executed project work. No browsing, installs, database access, application execution or code edits occurred. Token usage: unknown. Measured evaluation interval: 2026-09-20 08:02:07–08:03:48 UTC (101 seconds), excluding initial instruction/case reads and this final metadata write. Case word counts, including skill/limitation notes: 298, 133, 296 and 301.

## 1. Modernize an existing portal

I recommend bounding the upgrade to Login, Home and Menu, with an explicit compatibility boundary for the 100 retained pages. Decide Home's release scope before recovering all 11 widget implementations.

Immediate product-owner questions:

- Should this release retain all widgets, a selected subset, or a simpler Home? I recommend selecting widgets needed for priority tasks; the trade-off is reduced recovery/build work versus changed user workflows. Which customization settings must survive?
- Must retained pages remain reachable with uninterrupted authentication through the new menu? I recommend preserving this journey; any deliberate restriction needs an agreed alternative.
- Which current UX failures and user/role journeys define success for these three surfaces? Agree observable outcomes before choosing replacement interactions.

While answers are pending, trace credential verification, session creation/renewal/logout, cookie and CSRF boundaries, and menu visibility versus server-side access enforcement. Sample retained-page entry and return paths to establish the shared session contract; inspect additional consumers only where evidence indicates a different contract. Inventory widgets shallowly, then deeply recover only selected widgets and dependencies that constrain compatibility.

Use targeted source/schema reads to record exact identifiers, auth mappings and shared writers. Record source/local database versions separately. The month-newer deployed database means local evidence cannot establish deployment compatibility: obtain an authorized read-only schema/configuration comparison or deployment evidence, without importing sensitive records. Document unresolved differences.

Complete analysis when the release boundary, Home decision, affected journeys, UX direction, auth/session/menu contracts, credential/schema preservation, deployment compatibility and cutover/recovery approach are defined well enough to implement and verify without consequential guesses. Keep one current contract with evidence, decisions and acceptance checks. Unresolved deployed-schema differences remain explicit blockers to compatibility claims. Defer unrelated module behavior; no implementation or whole-app audit.

Skills read: `app-analyze/SKILL.md`; `app-analyze/references/requirements.md`; `app-analyze/references/existing-systems.md`.

Limitations: supplied shallow findings only; no source/database inspection or owner answers.

## 2. Contained correction

Locate the recovery dialog's authoritative copy or localization entry and change only “Contcat your administrator” to “Contact your administrator.” Preserve component structure, styling and behavior; inspect the diff for accidental changes.

Run the existing component checks that open and close the dialog. Render the affected dialog once to confirm the corrected text and unchanged layout. If an existing snapshot or text assertion contains the typo, update that expectation and inspect the resulting diff. No new test harness, design review or broad requirements exercise is warranted.

Report the changed location and actual check results when implementation occurs. For this exercise, this is an approach only: no code was edited and no tests or visual checks were executed.

Skills read: `app-frontend/SKILL.md`.

Limitations: repository location, existing assertions and rendered appearance were not inspected.

## 3. Repeat QA after an auth change

Identify the exact candidate, including uncommitted changes, and establish the expected cross-tab recovery behavior. Reproduce the defect with two pages in the same browser context: tab A obtains a CSRF token; tab B signs in and changes session state; tab A attempts a protected operation. Assert the agreed refresh/recovery behavior, correct user identity and authorization, and no duplicate side effect. Add token rejection and failed-recovery checks at the API level where practical.

Inspect and run the applicable existing backend/frontend tests; their counts (28 and 11) establish inventory, not coverage or passes. Exercise the real account/API boundary with controlled local fixtures. Use the production bundle under intended CSP and serving configuration early: verify stylesheet loading and computed/rendered appearance as well as the auth journey. The previously blocked CSS remains a known concern until retested on this candidate.

For ten upcoming changes, adapt reusable journey functions into project-owned tests runnable without interactive agent calls. Reuse an existing runner; otherwise a compatible Playwright Test setup is reasonable. Provide a documented Node command, readiness assertions, deterministic setup, fresh contexts per test (shared context within the cross-tab case), and cleanup after failures. CI runs that same command using secret-managed credentials.

Run the new harness twice; where feasible show the regression assertion fails against the original defect. Report candidate/environment, commands, executed/passed/failed/blocked counts, duration and retries, with standard structured reports and sanitized failure artifacts. Preserve unaffected evidence, rerun affected checks after changes, and retain focused visual review.

No MCP service is presently justified: Node execution already provides the needed access. Add one only for a demonstrated access/coordination gap, wrapping the same runner.

Skills read: `app-qa/SKILL.md`; `app-qa/references/verification.md`; `app-qa/references/repeatable-verification.md`.

Limitations: all checks above are proposed; none were executed. Initial setup, repeated-run cost, maintenance and escaped defects remain unmeasured.

## 4. First real integration

Begin with the uncertain legacy identity boundary, before expanding API implementation. Inspect the actual verifier and use the read-only local connection to establish the designated account's stored identity/role values and eligibility rules. Do not infer stored names from the transport labels Admin/Executive or alter the identity schema to match them.

Prove a thin path from that account through the real verifier and stored roles to the API response. Record exact stored-to-domain-to-transport mappings using sanitized evidence. Resolve ambiguous or unmapped values explicitly; authorization must not grant access by guessing. Verify that using the verifier is compatible with read-only access: if it requires a write such as last-login tracking, identify that limitation and use an authorized disposable fixture/environment rather than silently changing access.

Then implement the remaining API against the confirmed contract, enforcing authorization server-side and preserving the legacy store. Add meaningful tests for mappings, invalid credentials, unauthorized roles, malformed requests and relevant errors. Independently exercise the delivered endpoint against the real local store; mock passes remain useful unit/contract evidence but do not prove this boundary.

The approved frontend design and faithful mock do not block backend work or require redesign. If frontend integration belongs to the requested delivery, replace the mock at its service boundary and verify one real end-to-end journey with the production bundle and intended serving/security settings. For this API-only request, provide a verified consumer contract and explicitly leave frontend integration unproved.

Completion evidence should identify the candidate/environment, confirmed mapping, unchanged identity-store/schema handling, actual API/integration commands and outcomes, authorization/error results and any blocked coverage. Evidence from one designated role cannot establish all role mappings; missing representative fixtures remain gaps. Keep credentials/private payloads out of artifacts.

Skills read: `app-backend/SKILL.md`; `app-backend/references/data-and-integration.md`.

Limitations: no inspection or execution occurred in this exercise; real mappings and all completion evidence remain pending.
