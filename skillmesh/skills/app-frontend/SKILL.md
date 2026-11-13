---
name: app-frontend
description: Implement or change production application UI against established behavior, design and service contracts. Use for frontend features, fixes and integration; preserve existing systems and use mocks only when a real dependency is unavailable.
---

# App Frontend

Implement a usable application journey against established behavior, visual direction and service contracts. Inspect the real application and repository guidance first. Accept adequate designs from any source; no earlier skill invocation is required.

Use the current use-case specification or adequate equivalent as the primary behavioral input for the selected journey, rules, alternatives and done-checks; combine it with the prototype/visual direction and real API contracts. Consult analysis findings for rationale or unresolved choices, rather than deriving behavior again. Retain useful flow references in checks, and surface consequential gaps instead of treating proposed behavior as accepted.

## Settle the consequential interaction

For material new UX, establish a concrete reviewed direction before expanding production UI. Existing approval or delegated design authority counts. Inspect a representative populated layout at relevant widths in development before repeating the pattern: density, primary actions and long content should expose assumptions early. Contained corrections use the established experience. Resolve behavior or contract ambiguity before dependent implementation and continue independent work.

Reuse the project's suitable components, styling, tokens and interaction conventions. Locate the affected route, representative component, service contract and existing tests before deeper retrieval; reuse settled interaction decisions and valid evidence rather than re-surveying the application. Probe uncertain real API/auth/serving boundaries early before repeating dependent UI. Prefer mature controls for genuinely complex grids/interactions, without introducing a framework or speculative abstractions for ordinary UI. Reuse prototype assets/styles where useful and visually verify framework adaptations.

## Build the journey and its states

Use real domain copy and meaningful loading, empty, error, success and recovery states. Preserve hierarchy, responsive intent, semantic structure, keyboard/focus, accessible errors, security and performance. Consequential strings belong in acceptance checks with their state conditions: action labels must match behavior, pending is not complete, and shortening must preserve validation rules and consequences.

For asynchronous or stateful interactions, use the transition diagnostics in [readable implementation](references/readable-implementation.md): decide stale-response ownership, repeated-action identity, navigation and recovery where they can change the outcome. Keep the state representation as simple as the journey permits.

Write for a developer returning after six years. Separate logical handler blocks and UI sections with blank lines; expand branches, error handling, calls, object literals and template nesting. Keep state, payload, API call and recovery easy to trace. Read the relevant sections of [readable implementation](references/readable-implementation.md) when authoring or reviewing source, including small changes. Apply them to the affected code without expanding into an unrelated refactor. A formatter or passing build is not comprehension evidence.

Use the real API when available. If a dependency is unavailable, put contract-faithful mocks behind the same service boundary, label them and identify the unproved integration. Do not alter API/data/auth rules for UI convenience. Frontend-only scope does not authorize backend changes.

Consume the backend's current-user and allowed-capability contract. Keep credential storage/provider details out of UI logic; unvalidated token contents and external role claims do not establish application permissions. Hidden buttons are not authorization. Preserve denied-access and expired-session recovery when authentication changes, without exposing hashes or server secrets.

## Inspect actual behavior

Run relevant development builds and meaningful tests for state transitions and consequential behavior. Render affected routes and states at appropriate widths and compare them with the reviewed direction or established product. Inspect actual screenshots, keyboard/focus and recovery; correct drift and rerun affected checks. Retain unaffected evidence only while its candidate, environment and assumptions remain valid; shared component, auth or serving changes may require broader coverage. Browser evidence remains pending when no browser is available.

Trace one representative action from template and handler through payload construction, API invocation and success/failure recovery. Make retained or replaced request IDs and version tokens understandable when retries matter. Report source comprehension separately from behavioral results and owner feedback.

When production serving or release preparation matters, read [serving and release](references/serving-and-release.md). Exercise a representative real journey against the production bundle and intended security/serving configuration early when an artifact is available or its generation is explicitly authorized. Development rendering may miss asset, CSP and authentication failures. Release builds, bundling, publishing and deployment are owner-initiated by default; prepare settings and commands, and honor an explicit build request within its scope. Missing production artifacts leave that proof pending while independent checks continue.

Keep useful assertions in the project's existing tests as implementation grows. Present the working journey and code first, then compact labeled facts for changed behavior, checks, real/mocked integration and gaps. Use route/state/viewport/result rows when they make coverage easier to compare; link detailed evidence rather than narrating every screenshot or repeating the service contract. In projects adopting automatic context maintenance, preserve accepted interaction/API decisions, candidate-bound browser evidence and this workstream's next action in existing records. Recommend prototype, backend or QA expertise only for a concrete gap; the agent decides whether to use it.
