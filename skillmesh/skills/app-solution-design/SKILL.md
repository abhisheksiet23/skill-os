---
name: app-solution-design
description: Design and compare technical solutions for application requirements, defining architecture, component responsibilities, data and integration flows, and consequential engineering decisions before implementation. Use for new systems, material cross-component changes or modernization; skip contained fixes with settled architecture and UX-only design.
---

# App Solution Design

Turn intended behavior and constraints into a coherent, implementable technical approach. Own the consequential choices between requirements analysis and production implementation. Accept adequate requirements and existing designs from any source; no prior skill invocation, prescribed document tree or approval ceremony is required. A small change with settled architecture needs no separate design exercise.

## Establish the decision

Inspect the affected implementation, project instructions, contracts and existing decisions. Identify the outcome, scope, compatibility obligations, external dependencies, team capabilities and operational constraints that could change the solution. Separate facts, assumptions, accepted decisions and unknowns. Do not invent workload, availability, budget or compliance requirements to justify a preferred architecture.

Recover enough current structure and runtime evidence to understand what must change and what can remain. Source code alone does not prove deployment behavior. Resolve consequential contradictions explicitly. Ask only when an unavailable fact or genuine owner choice changes the recommendation; continue independent design while it is pending. Missing product behavior calls for targeted clarification, not an invented requirement or a wholesale restart of analysis.

## Choose a coherent approach

Compare credible alternatives at the actual decision boundary, including extending the existing system when viable. Explain the recommendation through requirement fit, failure behavior, delivery effort, operational burden, cost and reversibility where they matter. Do not manufacture alternatives for settled choices or default to distributed services, queues, caches or new vendors without a concrete need. Respect accepted technology constraints; verify current product capabilities from authoritative evidence when the decision depends on them.

Trace representative use cases through components and external systems. Define responsibilities, authoritative data owners and writers, interfaces and trust boundaries. Show where validation, authorization, state transitions, transactions and external effects occur. Make relevant synchronous/asynchronous flows, consistency, concurrency, retries, idempotency, ordering and partial-failure recovery explicit. State who owns each guarantee rather than assuming a diagram or transport provides it.

For new account-based applications, default to application-owned Users with one Role foreign key, Roles, Modules and ModuleRoleMapping, without a user-role join table. Local credentials use the owner's selected bcrypt implementation through maintained security components. Separate authentication from current local role/module and record/workflow authorization. Plan stable local user IDs and a unique optional external issuer/subject link so central authentication can replace credential verification later while all four tables and business references remain local. External tokens identify users; they do not silently assign local roles. Preserve genuine existing requirements and define an explicit migration before changing deployed identity/authorization structures.

Connect material quality constraints to mechanisms and proof: for example, a latency budget to the critical path, recovery objectives to restore behavior, or tenant isolation to enforcement boundaries. Use calculations or measured evidence when available; label estimates and sensitivity to assumptions. Address deployment topology, configuration/secrets, observability and operating cost to the depth that can affect the decision. Avoid a generic checklist of technologies or ungrounded scale claims.

For substantial integration, distributed work or replacement, use [boundary and failure design](references/boundaries-and-failures.md) to test the consequential seams. Keep the design proportional: a focused component change may need a short decision and sequence; a broad system may need a component view, critical flows and focused supporting contracts. Use diagrams when they clarify ownership or execution, with prose for guarantees and trade-offs.

## Make the design usable

Identify the assumptions most likely to invalidate the approach. Specify the smallest useful spike, measurement or real integration check, its pass/fail signal and what decision would change. Execute bounded checks when authorized and feasible; distinguish executed evidence from a proposed validation plan. Mocks cannot settle an uncertain external contract. Do not grow a design on top of an unproved critical dependency without making the consequence explicit.

Define coherent implementation increments around working paths and stable contracts. Include compatibility, data migration, rollout and recovery implications when existing users or data are affected. Leave routine local code structure to implementation; settle cross-component guarantees and expensive-to-reverse choices before dependent work.

Treat owner-initiated compilation, publishing and deployment as the library default. Prepare settings, profiles and commands; do not assume authorization to produce release binaries/packages or run deployment steps. For new .NET relational applications plan EF Core migrations with reviewed SQL releases, manually generated by the owner and applied through SSMS on SQL Server, and a separate administrator bootstrap. Production startup verifies compatibility rather than mutating schema or seeding data. Preserve adequate existing migration systems and use stack-appropriate clients elsewhere; explicit project direction may override these defaults. Design schema/app compatibility and persistent data/configuration locations so operator-controlled upgrades and recovery are concrete.

Lead with the recommended solution, its rationale and material trade-offs. Reuse the project's authoritative design and contract records rather than copying requirements into a new dossier. Preserve consequential decisions and rejected alternatives with their reasons, evidence, unresolved risks and conditions for revisiting them. Include enough component, interface and flow detail for implementation and verification without guessing the important guarantees. Do not present a recommendation as an accepted user decision.

Finish when the scoped approach is coherent, consequential choices are resolved or precisely bounded, and implementers can identify what to build and how to prove it. A known blocker may prevent readiness; state the affected work and continue independent design. This skill produces technical design and bounded evidence, not production implementation or release authorization.

Optional expertise: `app-analyze` for unresolved behavior or requirements; `app-prototype` for unresolved experience; `app-backend` or `app-frontend` for implementation; `app-qa` for independent verification. Explain the concrete gap and useful evidence. These recommendations never invoke skills or require a fixed sequence; the agent owns orchestration.
