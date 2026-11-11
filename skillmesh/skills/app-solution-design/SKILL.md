---
name: app-solution-design
description: Design, compare and review technical solutions for application requirements, defining architecture, component responsibilities, flows and consequential engineering decisions before implementation. Use for new systems, material cross-component changes, modernization or standalone technical design and plan review; skip contained fixes with settled architecture and UX-only design.
---

# App Solution Design

Translate intended behavior into a coherent technical approach with clear ownership, failure guarantees and proof. Settle consequential cross-component and expensive-to-reverse choices; leave routine local code structure to implementation. This skill produces design and bounded evidence, not production implementation or release authority.

## Frame the technical decision

Inspect project instructions, adequate requirements, existing decisions and the affected system. Start with the current contract, component map and changed/uncertain boundary; follow only evidence that could change the decision, reusing still-valid source-bound findings. Identify outcome, scope, compatibility, external dependencies, team capability and operating constraints that can change the solution. Separate verified facts, assumptions, accepted decisions and unknowns. Do not invent workload, availability, budget or compliance needs to justify an architecture.

Recover enough structure and runtime evidence to know what can remain and what must change. Source alone does not establish deployed behavior. Reconcile consequential contradictions and ask only when missing facts or an owner choice changes the recommendation. Missing product behavior needs targeted clarification, not invented requirements or a wholesale analysis restart. Continue independent design while a decision is pending.

## Choose mechanisms from required guarantees

Compare credible alternatives at the real decision boundary, including extending the existing system. Explain the recommendation through requirement fit, failures, delivery effort, operational burden, cost and reversibility where material. Respect accepted technology constraints and verify current product capabilities from authoritative evidence when they matter. Do not manufacture alternatives for settled choices or add services, queues, caches or vendors without a concrete need.

Trace representative use cases through components and external systems. Name responsibilities, authoritative data owners/writers, interfaces and trust boundaries. Show where validation, authorization, state transitions, transactions and external effects occur. For consequential synchronous/asynchronous flows, specify consistency, concurrency, retry, idempotency, ordering and partial-failure recovery. Name who enforces each guarantee; a diagram or transport alone does not provide it.

For new account-based applications, default to local Users with one Role foreign key, Roles, Modules and ModuleRoleMapping without a user-role join table. Local credentials use maintained bcrypt components. Separate authentication from current local role/module and record/workflow authorization. Preserve stable local IDs and a unique optional external issuer/subject link so central identity can replace verification without moving the four authorization tables or business history. External claims must not silently assign local roles. Preserve genuine existing requirements and require an explicit data-preserving migration before changing deployed identity structures.

Connect material quality requirements to mechanisms and observable checks: latency to a critical path, recovery objectives to restore behavior, tenant isolation to enforcement. Use measured evidence or calculations where available and label estimates and their assumptions. Address topology, configuration/secrets, observability and operating cost to the depth that affects the decision.

For consequential mechanism choices, integration or replacement, read [boundary and failure design](references/boundaries-and-failures.md) to compare the smallest sufficient alternatives and stress failure/migration transitions. A focused change may need a short decision/sequence; a broad system may need component views, critical flows and focused contracts. Use diagrams to clarify ownership/execution and prose to state guarantees and trade-offs.

## Reduce uncertainty before dependent investment

Identify assumptions most likely to invalidate the approach. Choose the smallest authorized check that could change the decision before disproportionate dependent work, preserving required safety and recovery. Mocks cannot settle uncertain external contracts. If evidence is unavailable, bound the affected investment and continue independent work within delegation; surface consequential trade-offs outside that authority.

In design-only scope, propose the check and its decision consequence unless execution is already authorized. Separate executed evidence from validation plans. Plan coherent implementation increments around working paths and stable contracts, sized by coupling, new mechanisms, reversibility and verification effort rather than item count. Include compatibility, migration, rollout and recovery where users/data are affected; distinguish enabling work from delivered outcomes without inventing supporting features.

For standalone design/plan review or consequential handoff, read [design review](references/design-review.md). Check comprehension outside the authoring context, verify relied-on existing components/interfaces and connect guarantees to acceptance. After material fixes reassess fit, simplicity and contradictions. These checks do not require a review pipeline or approval ceremony.

## Make the approach operable and recoverable

Plan owner-initiated release compilation, publishing and deployment by default. Prepare settings, profiles and commands; execute artifact production only within explicit authority. An explicit build request is sufficient for that build, not for deployment.

Relational backend deliverables include actual repository-owned idempotent initial SQL for database creation, required DDL/master data and ordered subsequent changes. Script authoring and safe local generation do not authorize database execution or release compilation. New .NET relational projects retain EF migrations as schema authority, SQL Server/SSMS manual application and separate administrator bootstrap. Production startup verifies compatibility without schema mutation or seeding. Preserve adequate existing migration systems, stack-appropriate clients and explicit project overrides. Design app/schema compatibility and persistent data/configuration locations so upgrades and recovery are concrete.

Lead with the recommended solution, rationale and material trade-offs. Use labeled facts for decision, guarantee/enforcing boundary, evidence and open risk; compare genuine alternatives in a short table when useful and show critical flow/ownership in a diagram when clearer. Add enough prose to explain failure behavior and why the recommendation fits. Reuse authoritative project records, linking requirements rather than copying them into a new dossier. Preserve important decisions, rejected alternatives/reasons, evidence, unresolved risks and revisit conditions. Recommendations remain proposals until accepted. In projects adopting automatic context maintenance, update accepted technical decisions and provisional risks before handoff and keep each workstream's next action distinct from shipped behavior.

Finish when the scoped approach is coherent, consequential choices are resolved or precisely bounded, and implementers know what to build and how to prove it. State any blocker and its affected work. Requirements, prototype, implementation or independent-verification expertise may help a concrete remaining gap; explain that gap and leave orchestration to the agent.
