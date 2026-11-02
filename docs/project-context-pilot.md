# Automatic project context pilot

## Accepted direction

The owner authorized automatic project-context maintenance and a toolkit assessment reviewed and filled after every project session. Accepted on 2026-11-02 in the toolkit authoring chat. Project context must be portable across agents and devices. Use project-owned Markdown, existing authoritative records and selective retrieval, with Git synchronization following existing authorization. Keep observations, accepted decisions, provisional recommendations and superseded decisions distinct. No database, indexing service or agent-private memory becomes the source of truth by default.

## Implementation and adoption

The packaged [project-context skill](../skillmesh/skills/project-context/SKILL.md) owns the self-contained method and [session rubric](../skillmesh/skills/project-context/references/session-assessment.md). Its [instruction snippet](../skillmesh/skills/project-context/assets/project-instructions.md) makes the adopted rule portable even without this plugin. Adapt existing project instructions; verify the intended agent loads them. Installation/discovery alone is not proof that maintenance will happen. Other skills remain independently usable and do not invoke this skill.

Keep each project's context and session assessments inside that project. Reuse adequate records, with separate task/branch continuation state. Fill the assessment before a normal completion, pause or handoff; an abrupt closure is recovered as a missed-closeout gap at the next session. The compact assessment is explicitly requested, not a mandatory workflow ledger for production readiness. Read-only tasks can leave a pending update in the response rather than mutate files. No global hook or automatic cross-project collection is installed.

## Pilot obligations and stopping criteria

- At every adopted project session, record the six factors: continuity, decision fidelity, evidence freshness, retrieval economy, project/workstream separation and review independence. Use observed 0/1/2 scores, unknown, or N/A with reasons. Fill even analysis-only sessions; avoid treating each conversational reply as a new session.
- On the next real project, adopt the map in its own records and confirm loading. Include a later fresh-session resumption, another workstream and an independent artifact review when genuinely useful; do not manufacture project work merely to populate scores.
- Review whether recovery preserved consequential decisions and unknowns, maintenance avoided conflicts, and relevant evidence was found without broad repeated loading. Record corrections and available measurement boundaries. Token, cost and time savings remain unknown without comparable measurements.
- Keep real project results local. When toolkit source is available and edits are authorized, summarize only sanitized, generalizable lessons here and link an authorized assessment location. Do not copy company facts, private records or transcripts into this repository.
- Promote a stronger default or add indexed retrieval only after repeated observed gaps justify it. No fixed number of sessions establishes universal quality; an observed consequential failure remains visible and requires a useful correction.

## Current pilot status

Application-project pilot: **pending adoption in a real application/business project**. Toolkit authoring and isolated synthetic exercises do not count as that pilot. This repository adopts maintenance through its own AGENTS.md; [its session assessments](toolkit-session-assessments.md) track the authoring project only. The [executed implementation evaluation](../evals/project-context-assessment.md) records actual synthetic maintenance, fresh recovery, a bounded no-history probe and a correction to inflated continuity scoring. Shared host instructions limit baseline attribution, and token/cost/time savings remain unknown.

## Skeptical review — 2026-11-02

Review findings, not new owner decisions or changes to the accepted maintenance policy:

- Automatic maintenance is agent-followed guidance. Reliable activation in other projects/clients, abrupt-close recovery and cross-device delivery are unproved; no lifecycle hook guarantees persistence. Adoption and sync must be observed before claiming those outcomes.
- Recurring method/rubric reads, context edits and six-factor assessments add work before any net token/time/rework benefit has been measured. The baseline recovered the same essential state and shared current host guidance. This comparison cannot justify general superiority or the overhead of every component.
- Self-assessment can measure compliance with instructions while missing usefulness. Initial continuity over-scoring was actually observed; the correction passed one repeat. Numerical scores remain fallible author judgments, not objective product-quality measurements.
- Reading a record again before editing is not an atomic concurrency guarantee. The unchanged unrelated fixture checkpoint did not test two agents editing a shared decision concurrently. Branch/workstream isolation and actual conflict handling still need evidence.
- The no-history reviewer probe found an obvious scope contradiction and did not know a parent-only marker. It did not test contamination through project instructions, broad memory access or a biased evidence list, nor compare usefulness with an author-context review.
- Markdown portability does not itself deliver updated context to another device or retire stale conclusions. Uncommitted records, divergent branches and incorrectly summarized decisions can still propagate confusion despite source links.

Recommendation, provisional: keep the file-based foundation and current owner-requested session assessment, but treat the full method as a pilot. In the next real multi-session workstream, assess actual constraint recovery, user corrections, unnecessary reads/maintenance and any conflicts, keeping unknown metrics explicit. Revise or remove optional guidance that repeatedly adds work without changing an outcome. A causal efficiency claim needs a less-contaminated comparison and measured usage, not more synthetic reports. No new tooling, policy rollback or application edits are authorized by this review alone.
