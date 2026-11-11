# Establish release readiness from the actual candidate

Bind proof to the exact candidate, environment and intended scope. A partial release needs a coherent authorized subset; one passing increment does not prove the combined change. Candidate changes invalidate affected evidence.

## Write steps an operator can execute

Use the actual project's commands, paths and authorized mechanism. For each consequential step give the prerequisite, exact action, expected observation and stop/recovery condition. Share common prerequisites once; trivial steps need no ceremonial row. Unresolved values must be named inputs with a way to obtain them, not plausible invented defaults. Preparation-only scope authors the procedure without executing restricted actions.

| Stage | Prerequisite and action to make concrete | Expected observation | Stop/recovery boundary |
| --- | --- | --- | --- |
| Preflight | Verify destination identity, baseline/schema, artifact checksum and available backup/recovery. | All identities match the supported upgrade path. | Mismatch: stop before mutation and reconcile the actual target. |
| Quiesce and migrate | Name every writer to drain/stop and the exact reviewed script/client settings. | Writers are stopped; target schema and verification queries match. | Error/partial application: preserve output and inspect history/data before any rerun. |
| Cut over | Name staged release path, configuration source and host switch/start action. | Destination reports the intended candidate and starts without compatibility errors. | Startup failure: use prior release only if current schema/data remain compatible. |
| Smoke and close | Name test identity, concrete read/write journey, expected results and cleanup. | User behavior and affected workers succeed under destination configuration. | Failed effect or unknown outcome: reconcile before retry; follow the assessed recovery route. |

“Deploy and check logs; roll back if needed” is not executable. A useful instruction identifies the site's old/new physical paths, exact stop/start method, expected version endpoint value and a smoke action with its expected result. It also says when switching back is unsafe, such as after a schema contraction. Recovery may require forward repair or coordinated data/file restoration; name that dependency rather than implying a folder switch reverses everything. Validate the procedure against available tooling and artifacts within authority, and label unexecuted host/database steps as pending.

## Check compatibility before execution

For migration, establish affected data, supported application/schema versions, expected duration, backup/restore or forward recovery and representative existing-data checks. A destructive migration does not become reversible because application code can be reverted.

For coexistence, verify routing/auth boundaries, retained consumers and authoritative writers. Demonstrate old readers remain compatible after new writes or use compatible expansion and tested reconciliation. Routing rollback cannot undo data or external effects.

## Verify the result and recover deliberately

Define critical smoke checks and observable failure signals against the destination's actual configuration. Build success, command success and verified live behavior are distinct. After interruption or an uncertain remote response, inspect the result before retrying. Bound recovery by observations instead of repeatedly deploying or migrating into unknown state.

Record only verified shipped behavior as current product knowledge. Preserve decisions/evidence in existing change history, link substantial artifacts and leave a precise next action for pending scope. Keep sanitized commands and configuration locations only where they aid continuation; never store secret values.
