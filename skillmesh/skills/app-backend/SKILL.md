---
name: app-backend
description: Implement backend business rules, APIs, persistence, migrations and integration with meaningful behavioral proof. Use for server-side changes or contract integration in existing or new software; no frontend-first sequence is required.
---

# App Backend

Deliver backend behavior that consumers can rely on: enforced business rules, explicit API/data guarantees, compatible persistence and executed evidence. Work in the application's repository from adequate requirements and designs, regardless of who produced them. Backend work does not require a prototype, frontend or prior skill invocation.

## Establish the working boundary

Inspect the affected implementation, project instructions and accepted decisions. Identify the caller, intended outcome, access/data scope, state changes and observable acceptance. Resolve routine code choices locally; surface missing consequential behavior or architecture before building dependent work. Continue independent implementation while a genuine decision is pending.

For uncertain existing-system or external contracts, test the consequential boundary with representative identity/configuration before multiplying dependent code. An adjacent successful operation or passing mock is insufficient. Preserve exact stored-to-domain mappings when they matter, and bound the affected work if the check is unavailable.

Use predictable folders. A single backend project's project file and source normally belong directly in `backend/`; add subprojects for actual component boundaries, not scaffolding defaults. Preserve adequate existing layouts. A justified move includes project/solution references, scripts and documentation.

## Implement a complete path

Trace endpoint or message entry through authorization, validation, business decisions, state mutation, persistence/external effects and response. Place enforcement at authoritative boundaries. Make transaction, concurrency, retry, idempotency and partial-failure behavior deliberate wherever the outcome depends on them; separating transport and storage helps only when it protects a real contract.

Write for a developer returning after six years. Use business names, named consequential request/response contracts and structured values instead of opaque objects or delimiter conventions. Separate logical blocks with blank lines, expand branches/calls/initializers and keep normal, rejection and recovery paths visible. Read the relevant sections of [readable implementation](references/readable-implementation.md) when authoring or reviewing source, including small changes. Apply them to the affected code without expanding into an unrelated refactor. Fewer lines and formatter success do not establish readability.

Load the relevant specialist detail as the change requires it:

- **Accounts or permissions:** use [identity and local authorization](references/identity-and-authorization.md). New local-account applications default to Users with one Role foreign key, Roles, Modules and ModuleRoleMapping, and maintained bcrypt verification. Keep authentication separate from local module and record/workflow authorization. Preserve adequate existing systems and genuine multi-role requirements until an explicit data-preserving migration is defined.
- **Persistence, external effects or coexistence:** use [data and integration](references/data-and-integration.md). Inspect representative existing data and query growth; prove upgrade as well as fresh setup and distinguish local rollback from already accepted external effects.
- **Relational schema or master data:** use [manual database releases](references/manual-database-releases.md). Deliver actual initial SQL, normally `database/initial.sql`, with database creation, required DDL and master data, plus ordered `database/changes/<sequence>-<purpose>.sql` changes. Commands or placeholder SQL are incomplete. New .NET relational applications retain EF migrations as schema authority and SQL Server/SSMS operator application; other stacks and adequate existing systems keep their native mechanism. Production startup checks compatibility without creating, migrating or seeding; administrator bootstrap is separate.
- **HTTP API changes:** use [Postman API checks](references/postman-api-checks.md). Maintain a runnable repository-owned collection from the first increment, normally in `postman/`, with affected contracts, examples and assertions. Extend the existing collection. Internal-only refactors need relevant regression runs, not cosmetic collection edits. Non-HTTP systems and explicit project exceptions use appropriate native checks.

Use supported secret input or references. Raw secrets must not enter recorded arguments, URLs, scripts, logs or evidence; output redaction cannot undo input exposure. Missing secure input blocks the authenticated check, not independent work. Make failures diagnosable without leaking private payloads.

## Prove and hand over the behavior

Test business invariants and API/data boundaries with meaningful unit/integration checks. Run affected Postman folders against the authorized development/test API and the agreed regression set before handoff. A collection does not prove every concurrency, transaction or external-system guarantee. Report the actual target, candidate and results, or the exact unavailable runner/environment.

When a consumer is in scope, exercise the real agreed boundary; separately passing frontend mocks and backend tests do not prove agreement. API-only work does not require frontend changes. For defects, establish the reproduction, isolate the cause, correct it and rerun the original case and affected regressions. Prove coherent increments before expanding unverified work.

Review one material path in execution order for comprehension and report remaining obstacles separately from test results. Owner readability is unverified until the owner reviews it. Keep cleanup within scope and rerun affected checks.

SQL authoring and safe local generation belong to implementation. Release compilation, publishing, package production and database execution remain owner-controlled unless explicitly authorized. If SQL generation needs unavailable tooling or an unauthorized build, supply the authorable portions and exact blocker and mark the script incomplete.

Finish with delivered behavior, consumer implications, actual checks and precise migration/integration limitations. In projects adopting automatic context maintenance, update authoritative API/data decisions, candidate-bound evidence and this workstream's checkpoint; distinguish proposed from applied migrations. Recommend analysis, technical design or independent verification only for a concrete unresolved need. The agent chooses expertise; this skill invokes none.
