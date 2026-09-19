# Release risks worth checking

Bind readiness to the actual candidate and intended release scope. Partial delivery needs a coherent, authorized subset; proof of one increment is not proof of the whole change. Recheck affected evidence after candidate changes.

Before a migration, establish compatibility, data affected, expected duration, backup/restore or forward-recovery approach, and checks of representative existing data. Do not describe a destructive migration as reversible merely because code can be reverted.

For coexistence, verify routing and auth boundaries, retained consumers, authoritative data writers and old readers after new writes. A routing rollback does not undo data. Use compatible expansion or a tested reconciliation plan where necessary.

Define smoke checks for critical behavior and observable failure signals. Local and deployed configuration may differ. Distinguish build success, successful deployment operation and verified live behavior.

For interrupted or uncertain external operations, inspect the remote outcome before repeating. Use bounded recovery based on observations; do not repeatedly deploy or migrate without knowing current state.

Keep current product knowledge accurate for what shipped. Preserve decisions and evidence in existing change history, link substantial artifacts, and leave a concise next action for pending scope. Record sanitized launch/check commands and configuration locations only when needed for continuation.
