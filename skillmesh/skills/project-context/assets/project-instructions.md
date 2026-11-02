# Automatic project context — adaptable project instruction snippet

Merge the following into the project's existing agent instructions when adopting automatic maintenance. Replace example paths with real project records and verify agent loading. Preserve existing rules; the method also works without an installed skill. These paths are examples, not required directories.

```markdown
## Project context

Maintain project context automatically within authorized local work. At start/resumption, establish the project root and task/branch, read this map and relevant sections only:
- Purpose, scope and current constraints: README.md
- Accepted requirements and decisions: docs/decisions.md
- Current task checkpoints: docs/workstreams/ (use only this task's record)
- Session assessments: docs/session-assessments.md (closeout/resumption only)

Treat explicit owner decisions as accepted, verified facts as source/revision-bound, and assumptions or recommendations as provisional. Preserve replaced decisions as superseded with reasons. Update authoritative records after consequential changes; link evidence instead of copying conversations. Do not replace accepted intent merely because implementation differs.

Before completion, pause or handoff, refresh this workstream's boundary, candidate, actual checks, unknowns and next action. Re-read before editing, preserve other workstreams and concurrent changes, and mark evidence stale when affected code changes. Local updates do not authorize commits, pushes, deployment or external writes. Respect explicit read-only requests.

At every project session closeout, append a concise assessment in the mapped record: date/session/workstream, outcome and evidence, next action; score observed continuity, decision fidelity, evidence freshness, retrieval economy, project/workstream separation and review independence as 0=failed, 1=partial, 2=evidenced success. Use unknown when unobserved and N/A when not exercised, with reasons. Continuity in a maintenance-only closeout stays unknown until a separate resumption/recipient recovers the maintained state. Token/time/cost savings stay unknown unless measured. A normal work-period closeout is a session, not each reply; record missed closeouts on resumption without fabricating scores. Keep detailed evidence in project records. If available, the project-context skill supplies the full rubric.

Fresh reviewers receive only the target and selected evidence/constraints, without authoring history, speculative notes or session assessments. Use a no-history reviewer when available; ordinary rereads are not independent. A fresh conversation still shares filesystem/project instructions unless separately restricted. Skip broad context recovery during an explicitly bounded independent review.
```
