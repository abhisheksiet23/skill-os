---
name: app-frontend
description: Implement or change production application UI against established behavior, design and service contracts. Use for frontend features, fixes and integration; preserve existing systems and use mocks only when a real dependency is unavailable.
---

# App Frontend

Inspect the actual application, repository guidance, requested behavior, existing design and service boundaries. Accept adequate contracts and designs from any source; no previous SkillMesh invocation is required.

For material new UX, establish a concrete reviewed direction before expanding production UI. Existing explicit approval or delegated design authority counts. Contained corrections use the established experience. Resolve consequential behavior or contract ambiguity before coding dependent work; continue independent work.

Implement a coherent user journey with real domain copy and meaningful loading, empty, error, success and recovery states. Preserve the reviewed hierarchy, tokens, responsive intent and interaction behavior. Reuse prototype assets/styles when useful and verify framework adaptations visually. Keep semantic structure, keyboard/focus, accessible errors, security and performance active while building.

Use the project's suitable components and styling conventions. Prefer mature components for genuinely complex grids/interactions; do not introduce a framework merely because the skill was invoked. Avoid speculative abstractions.

Use the real API when available. Otherwise put contract-faithful mocks behind the same service boundary and clearly identify unproved integration. Do not alter API/data/auth rules to make UI coding convenient. Prove real integration when it is part of the requested outcome.

Run relevant builds and meaningful tests for logic, state transitions and consequential behavior. For visual changes, render and inspect the affected routes/states at appropriate widths against the reviewed prototype or existing product. Fix drift and retest affected behavior. No browser access means visual proof remains pending.

Exercise one representative real journey using the production bundle and intended serving/security configuration early when integration is material. Development or mock rendering can miss asset, CSP and authentication failures. Preserve useful assertions as project tests; expand coverage with the implementation rather than waiting for final QA to rediscover the boundary.

Record what changed, integration mode, actual checks and remaining gaps in existing project records. Finish the requested scope; frontend-only work does not imply backend work or release. Recommend `app-backend`, `app-prototype` or `app-qa` only for a specific unresolved need. The agent decides; this skill never invokes another skill.
