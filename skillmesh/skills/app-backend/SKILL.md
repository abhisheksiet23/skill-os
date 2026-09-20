---
name: app-backend
description: Implement backend business rules, APIs, persistence, migrations and integration with meaningful behavioral proof. Use for server-side changes or contract integration in existing or new software; no frontend-first sequence is required.
---

# App Backend

Work from the actual repository, requested outcome and adequate business/API/data decisions, regardless of who produced them. A frontend, prototype, phase ledger or particular document layout is not a prerequisite for backend work.

Identify authoritative boundaries for validation, access and data scope. Implement the required rules, state transitions, calculations and persistence. Keep transport and storage concerns separate when that protects the contract. Make transaction, concurrency, retry, idempotency and partial-failure behavior deliberate where material.

For uncertain existing-system contracts, prove a thin real integration path before expanding implementation: for example, designated identity through the actual verifier and stored eligibility values to the response. Record exact stored-to-domain mappings. Use read-only access and controlled fixtures where appropriate; passing mocks cannot settle an unverified legacy contract. If the dependency is unavailable, identify the unproved boundary and avoid multiplying work that relies on it.

Inspect consequential queries and data growth. Use versioned, project-appropriate migrations and test existing-data compatibility as well as fresh setup. Keep secrets out of code/logs and make failures diagnosable without leaking private payloads. Use [data and integration](references/data-and-integration.md) for migrations, external effects or coexistence.

Prove rules with meaningful tests and API/data boundaries with appropriate integration checks. Verify delivered endpoints independently, including auth and errors. Reuse the project's request collection or executable API checks; create a Postman collection only when it benefits the actual consumer or project convention.

When a frontend or other consumer is in scope, integrate through the agreed contract and exercise the real boundary. A frontend passing against a mock and a backend passing alone do not establish agreement. No frontend work is required for an API-only task.

For defects, reproduce the behavior, isolate the cause, fix it and rerun the reproduction plus relevant regressions. Resolve material contract changes explicitly rather than silently changing scope. Prove complete increments before multiplying unverified work.

Record implementation, actual checks, migration/integration status and remaining limitations using existing project conventions. Missing product decisions may justify recommending `app-analyze`; independent verification may benefit from `app-qa`. These recommendations do not invoke skills or prescribe the next phase; the agent owns continuation.
