# Establish release readiness from the actual candidate

Bind proof to the exact candidate, environment and intended scope. A partial release needs a coherent authorized subset; one passing increment does not prove the combined change. Candidate changes invalidate affected evidence.

## Check compatibility before execution

For migration, establish affected data, supported application/schema versions, expected duration, backup/restore or forward recovery and representative existing-data checks. A destructive migration does not become reversible because application code can be reverted.

For coexistence, verify routing/auth boundaries, retained consumers and authoritative writers. Demonstrate old readers remain compatible after new writes or use compatible expansion and tested reconciliation. Routing rollback cannot undo data or external effects.

## Verify the result and recover deliberately

Define critical smoke checks and observable failure signals against the destination's actual configuration. Build success, command success and verified live behavior are distinct. After interruption or an uncertain remote response, inspect the result before retrying. Bound recovery by observations instead of repeatedly deploying or migrating into unknown state.

Record only verified shipped behavior as current product knowledge. Preserve decisions/evidence in existing change history, link substantial artifacts and leave a precise next action for pending scope. Keep sanitized commands and configuration locations only where they aid continuation; never store secret values.
