# Delivery efficiency baseline responses

Variant: `.eval-runs/efficiency-before/skills` only. Four independent cases; no project execution, browsing, installation or production edits. Responses below describe proposed work, not executed proof. Token usage: unknown (not measured).

Measured clock interval: 81 seconds, from 2026-09-20 08:00:29 UTC to 08:01:50 UTC, covering skill reads and response drafting/writing; excludes initial instruction/task reads and final bookkeeping. Full end-to-end elapsed time was not measured.

## 1. Modernize an existing portal

**Response**

Keep analysis bounded to Login, Home, Menu and their compatibility boundaries. The 11 widgets, legacy sessions and 100 retained pages are baseline observations; widget retention is an unresolved product decision.

Ask the product owner immediately:

- What should Home help users accomplish, and should its configurable widgets be preserved, simplified or retired? Recommend deciding this before tracing all 11 deeply; retaining everything increases compatibility and UX work.
- Which roles and critical journeys must remain supported through the upgrade, including direct links to retained pages?
- What UX outcomes and supported devices define success? Which existing behaviors are intentional versus candidates for correction?

Meanwhile, identify source revision, local schema/data date and deployment evidence. The local database is a month behind: inspect it read-only for a provisional baseline, then obtain an authorized schema/configuration comparison or current sanitized snapshot for relevant identity, permissions, sessions and widget settings. Do not treat local observations as deployed truth.

Trace login validation and credential verification, session creation/renewal/logout, permission checks and menu routing. Determine how upgraded and retained pages share authenticated state, including direct navigation, session expiry and denied access. Map widget configuration/data dependencies shallowly; deepen only those selected or needed to assess a consequential choice. Sample retained pages by distinct session/routing pattern rather than auditing all 100.

Record current behavior separately from proposed changes. Define preserved credentials and schema, authoritative writers, old/new auth trust and routing contracts, recovery/cutover assumptions, and observable acceptance for each affected journey. Flag any proposed write that old consumers could not safely read.

Analysis is complete when Home scope and consequential UX choices are decided, affected contracts and representative coexistence behavior are evidenced, environment discrepancies are resolved or precisely bounded, and acceptance is sufficient to implement without inventing behavior. A missing consequential owner decision remains an explicit blocker; continue independent analysis around it.

**Skills read:** `app-analyze/SKILL.md`; `app-analyze/references/existing-systems.md`; `app-analyze/references/requirements.md`.

**Limitations:** Supplied shallow findings only; no source/database inspection performed in this exercise.

## 2. Contained correction

**Response**

Locate the recovery dialog's visible text or its translation entry and change only “Contcat your administrator” to “Contact your administrator.” Reuse the existing component, layout and approved design; this does not need new product analysis or design approval.

Inspect the diff to confirm the correction has the intended scope. Run the existing targeted dialog tests covering opening and closing. If a snapshot or existing copy assertion contains the typo, update it to the corrected text and review that specific change. Do not add a new test suite for this spelling correction.

Open the dialog once in the normal application flow to confirm the corrected wording renders and no unexpected wrapping occurs. Report the changed location and actual verification results. If browser access is unavailable, state that visual verification is pending rather than treating source inspection as visual proof.

No code was edited or tests executed in this exercise.

**Skills read:** `app-frontend/SKILL.md`.

**Limitations:** Implementation and verification approach only; repository/component location not supplied.

## 3. Repeat QA after an auth change

**Response**

Record the exact candidate, production-build configuration and test environment. First reproduce the original sequence with two tabs sharing one browser context: tab A retains a stale CSRF token, tab B signs in and changes session state, then tab A performs the protected action. Establish the intended recovery behavior and ensure a failed request cannot silently duplicate the action. Demonstrate the failure on the earlier candidate when available, then repeat on the fix.

Run the 28 backend and 11 frontend tests, inspecting results and coverage relevance. Add targeted regression coverage for token/session rotation, stale-token rejection and the intended client recovery. Verify unauthenticated and unauthorized requests remain rejected; token recovery must not weaken CSRF protection. Test real API behavior using designated local accounts.

Convert the reusable browser journeys into ordinary executable test modules behind a Node command, using the existing browser framework if suitable. Replace dependencies on interactive agent calls with supported browser APIs, deterministic fixtures, stable user-facing selectors, controlled setup/cleanup and assertions. Add the two-tab regression plus affected sign-in, sign-out and menu journeys. Run these in CI for upcoming changes, retaining traces/screenshots and sanitized failure details. Avoid arbitrary waits; synchronize on observable state.

Serve the production build with production-equivalent CSP headers and inspect the actual affected pages. Recheck the previously blocked stylesheet through network/console evidence and screenshots, and verify keyboard/focus behavior. An automation pass against a development server would not resolve the production-CSP finding.

An MCP service is unnecessary for a Node-capable CI runner and local browser tests. Consider one only if a demonstrated integration requirement cannot be met by the direct runner; interactive access alone does not make a reusable regression suite.

Report commands, candidate, environment, pass/fail/blocked outcomes and remaining gaps. Preserve unaffected valid evidence across changes and rerun affected checks. Every check above is proposed: this exercise establishes no executed test or visual pass.

**Skills read:** `app-qa/SKILL.md`; `app-qa/references/verification.md`.

**Limitations:** Existing test counts and CSS finding are supplied evidence; test contents, candidate and results were not inspected.

## 4. First real integration

**Response**

Start with the real identity boundary. Read the relevant legacy schema, identity lookup and designated account's role assignments through the read-only connection, keeping credentials and private values out of reports. Confirm credential-verification behavior and the actual stored role names; do not assume storage uses the transport labels Admin/Executive.

Define an explicit, server-side mapping between verified legacy values and the agreed API roles. Keep storage and transport separate and preserve the legacy identity store and schema. Resolve ambiguous role semantics with the owner before implementing dependent authorization; unknown or unsupported roles must not gain privileges by default.

Implement one coherent API slice covering real authentication, role mapping, authorization and agreed errors. Use the existing contract and independently exercise the endpoint against the local legacy store with the designated account. Verify successful access, denied access, invalid credentials and relevant unknown-role behavior. Read-only access supports inspection and read/auth paths; if the implementation requires persistent session or audit writes, identify the missing authorized test facility rather than claiming those effects were proved.

Keep contract-faithful mocks for isolated tests where useful, but passing mocks do not establish identity-store compatibility. Use meaningful unit tests for mapping and error rules plus real integration checks for actual stored values. Do not manufacture missing real accounts or mutate the identity store to make tests pass; report uncovered roles explicitly.

If frontend integration is included in the requested outcome, connect the approved UI to the real API and exercise the actual sign-in and authorized/denied journeys before expanding implementation. An API-only scope needs no UI rebuild. The existing approved design does not need another prototype cycle.

Completion evidence should identify the candidate and environment, verified legacy-to-transport mapping, unchanged schema/credential compatibility, independently exercised endpoints, actual test results and any real consumer journey results. Separate mocked coverage from real boundary proof and disclose unavailable write-path or role coverage. No implementation or verification was executed in this exercise.

**Skills read:** `app-backend/SKILL.md`; `app-backend/references/data-and-integration.md`.

**Limitations:** Stored roles and real compatibility remain unverified; frontend integration scope is conditional.
