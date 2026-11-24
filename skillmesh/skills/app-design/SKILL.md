---
name: app-design
description: Design, compare and review technical solutions for application requirements, defining architecture, component responsibilities, flows and consequential engineering decisions before implementation. Use for new systems, material cross-component changes, modernization or standalone technical design and plan review; skip contained fixes with settled architecture and UX-only design.
---

# App Design

Turn intended behavior into a technical approach with clear ownership, failure guarantees and proof. Settle consequential choices. Leave routine local code structure to implementation. Produce design and bounded evidence, not production implementation or release authority.

## Terms
- **Consequential:** crosses components, or is expensive to reverse.
- **Guarantee:** a behavior the design promises, such as no duplicate effect or no lost work. A named component enforces it.
- **Done-check:** the acceptance condition for a flow or quality item, taken from the specification. It is required acceptance, not executed proof.
- **ADR:** architecture decision record. One consequential decision with its reasons, rejected alternatives, evidence, open risks and revisit conditions.
- **Executed evidence:** a check that was run on a stated candidate. A validation plan is not executed evidence.
## Always
1. Separate verified facts, assumptions, accepted decisions and unknowns.
2. Invent no workload, availability, budget or compliance need to justify an architecture.
3. Treat source alone as insufficient evidence of deployed behavior.
4. Treat a recommendation as a proposal until the owner accepts it.
5. Build only on explicit request, and never deploy or execute against a database without authority. Writing scripts does not grant it.

## Frame the technical decision
Use existing project records first. Link them instead of copying.

Inputs, in order of use:
- Project instructions, adequate requirements and existing decisions.
- The current use-case specification, or an adequate equivalent. It is the main behavioral input: selected flows, shared rules, done-checks, quality and compatibility constraints, linked gaps.
- Analysis findings, for rationale, source conflicts and unresolved scope. Their jobs and journey show where quality constraints matter most. Consume them; do not produce them.
- The owner brief's decisions (D-n) and facts (F-n), linked and not copied. A default marked "on defaults" makes the dependent design provisional.

Do not rebuild behavior from analysis findings when the specification already states it.

Scope the investigation:
- Start with the component map and the changed or uncertain boundary.
- Follow only evidence that could change the decision. Reuse source-bound findings while still valid.
- Identify outcome, scope, compatibility, external dependencies, team capability and operating constraints that could change the solution.
- Recover enough structure and runtime evidence to know what can stay and what must change.

When facts conflict or are missing:
- Reconcile consequential contradictions.
- Ask only when a missing fact or owner choice changes the recommendation.
- Missing product behavior: ask a targeted question. Do not invent requirements or restart the analysis.
- Keep designing independent parts while a decision is pending.

When the owner is in the conversation, ask before writing the design:
- Send one batch: the decisions needed now and the facts you need.
- Question form: one plain line, your recommended default, what it changes.
- Facts: ask as ordinary questions, not as decisions.
- Use the host's question tool if it has one. Otherwise a numbered list in chat.
- Let the owner accept all defaults at once. Record each answer with date and decider.
- Owner absent: design the independent parts and mark dependent parts "on defaults".

## Choose mechanisms from required guarantees
Compare credible alternatives at the real decision boundary, including extending the existing system.
- Explain the recommendation by requirement fit, failures, delivery effort, operating burden, cost and reversibility, where material.
- Name the few quality characteristics that drive the design (for example availability, scalability, security, cost) and which one wins when they conflict. Justify the architecture style against them.
- Respect accepted technology constraints. Verify current product capabilities from authoritative evidence when they matter.
- Do not manufacture alternatives for settled choices.
- Add no service, queue, cache or vendor without a concrete need.

Produce a technical design artifact:
- Keep it separate from analysis. Link behavioral requirements and do not copy the specification.
- Trace representative use cases through components and external systems. Keep their stable flow and rule references.
- Name responsibilities, authoritative data owners and writers, interfaces and trust boundaries.
- Show where validation, authorization, state transitions, transactions and external effects occur.
- For consequential synchronous or asynchronous flows, specify consistency, concurrency, retry, idempotency, ordering and partial-failure recovery.
- For each guarantee, name who enforces it and the done-check it satisfies. A diagram or transport alone does not provide it.

Quality requirements:
- Connect each material one to a mechanism and an observable check. Examples: latency to a critical path, recovery objectives to restore behavior, tenant isolation to enforcement.
- Use measured evidence or calculations where available. Label estimates and their assumptions.
- Cover topology, configuration and secrets, observability and operating cost to the depth that affects the decision.

Consequential mechanism choice, integration or replacement: read [boundary and failure design](references/boundaries-and-failures.md).
- Use it to compare the smallest sufficient alternatives and stress failure and migration transitions.
- Focused change: a short decision and sequence is enough.
- Broad system: component views, critical flows and focused contracts.
- Diagrams show ownership and execution. Prose states guarantees and trade-offs.

### Permission structure
Settle this before dependent account or access implementation.
- Entities: Users, Roles, Permissions with stable resource and action codes, UserRoles assignments, RolePermissions grants.
- One role per user is enough when it fits. Multiple roles use the same assignment relation and combine the explicit grants that apply to the target scope.
- Access also requires an active trusted user, resource scope and workflow eligibility. Recheck them at the guarded write where state is mutable.
- Roles and module visibility never grant every action or record.
- Use equivalent framework entities instead of duplicate stores.
- Use one authorization boundary for APIs, services and UI capability projection.
- Add external identity links, typed memberships, scoped assignments or session state only for an actual requirement. Set no table-count limit and build no speculative policy engine.
- Local passwords use maintained bcrypt. SSO needs no local fallback.
- Preserve stable business IDs, adequate existing systems and accepted central policy.
- Migration needs an explicit data-preserving scope and an effective-access comparison.

## Reduce uncertainty before dependent investment
- Identify the assumptions most likely to invalidate the approach.
- Choose the smallest authorized check that could change the decision before dependent work grows. Keep required safety and recovery.
- Mocks cannot settle an uncertain external contract.
- No evidence available: bound the affected investment and continue independent work within your delegation. Surface consequential trade-offs outside it.
- Design-only scope: propose the check and what its result would change, unless execution is already authorized.
- Keep executed evidence apart from validation plans.

Plan implementation increments:
- Build them around working paths and stable contracts.
- Size them by coupling, new mechanisms, reversibility and verification effort, not item count.
- Include compatibility, migration, rollout and recovery where users or data are affected.
- Separate enabling work from delivered outcomes. Invent no supporting features.

Standalone design or plan review, or a consequential handoff: read [design review](references/design-review.md).
- Check comprehension outside the authoring context.
- Verify the existing components and interfaces the plan relies on.
- Connect guarantees to acceptance.
- After material fixes, reassess fit, simplicity and contradictions.
- No review pipeline or approval ceremony is required.

## Make the approach operable and recoverable
Release, build and deploy:
- Plan owner-initiated release compilation, publishing and deployment by default.
- Prepare settings, profiles and commands.
- Produce artifacts only within explicit authority. An explicit build request covers that build, not deployment.

Relational backends:
- Existing adequate native migration workflow: keep it, with versioned artifacts, repeatable install and upgrade steps and recovery. Add SQL files only when the owner or project requires them.
- Otherwise: plan repository-owned initial DDL and master-data SQL, plus ordered later changes.
- Require safe rerun and partial-failure handling through the chosen mechanism.
- Include guarded database creation where the operator owns provisioning. Managed or provider creation is a separate prerequisite. Do not require privileges that are unavailable.
- Script authoring and safe local generation do not authorize database execution or release compilation.
- New .NET relational projects keep EF migrations as schema authority, with SQL Server and SSMS manual application. Other stacks keep their own native mechanisms.
- Administrator bootstrap is separate. Production startup verifies compatibility and never mutates schema or seeds data.
- Design app and schema compatibility, and persistent data and configuration locations, so upgrades and recovery are concrete.

## Present and hand over
Presentation:
- Lead with the recommended solution, rationale and material trade-offs.
- Use labeled facts: decision, guarantee and enforcing boundary, evidence, open risk.
- Genuine alternatives go in a short table. A critical flow or ownership goes in a diagram when clearer.
- Add prose for failure behavior and why the recommendation fits.
- Reuse authoritative project records. Link requirements instead of copying them into a new dossier.

Record:
- Record each consequential decision as an ADR and link it from the design.
- Keep unresolved risks with their revisit conditions.
- Projects with automatic context maintenance: update accepted technical decisions and provisional risks before handoff. Keep each workstream's next action distinct from shipped behavior.

Finish when:
- The scoped approach is coherent.
- Consequential choices are resolved or precisely bounded.
- Implementers know what to build and how to prove it.

State any blocker and the work it affects. When a concrete gap needs requirements, prototype, implementation or independent-verification expertise, name the gap and why. The agent decides whether to bring it in.
