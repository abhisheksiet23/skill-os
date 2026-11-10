# Assign and test cross-boundary guarantees

Follow one consequential operation across the proposed boundaries and identify the component responsible for each guarantee. Use the questions below where they could change the approach; they are not mandatory document sections.

## Data and external effects

Locate the authoritative writer and transaction boundary for each consequential state change. When persistence and an external effect cannot commit atomically, explain the durable handoff, retry ownership and reconciliation. A queue alone does not prevent lost work or duplicate effects. Check crashes before and after commits, acknowledgements and remote calls; distinguish delivery guarantees from business-effect guarantees.

### Duplicate and ambiguous outcomes

Define idempotency scope, key lifetime and concurrent duplicate behavior where required. Account for an external system that lacks idempotency or returns an ambiguous timeout. Do not promise exactly-once effects without an enforceable end-to-end mechanism. Identify recovery ownership and any unresolved requirement for manual intervention.

### Concurrent and asynchronous state

For concurrent updates, decide which invariant needs locking, version checks, serialization or compensation. For asynchronous flows, define accepted versus completed, stale reads, event versioning, ordering needs, poison messages and replay behavior where consequential. Tie overload controls and retry limits to dependency capacity; do not make outages worse with unlimited retries.

## Trust and integration

Trace identity and authorization across ingress, services, workers and data access. Identify tenant/record scope, privileged operations and untrusted payloads. State where enforcement occurs; propagating a tenant identifier is not proof of isolation. Separate business audit records from diagnostic logs when auditability is required.

Confirm the consequential parts of an external contract: identifiers and stored values, auth, errors, limits, timeout semantics and compatibility. Separate documented capability, observed behavior and assumptions. Design graceful degradation only where the product permits it; otherwise make failure visible and recoverable.

## Change and operation

For coexistence and replacement, define entry routing, session/auth compatibility, authoritative writers, shared consumers/jobs and old/new data compatibility. Avoid uncoordinated dual writes. Sequence schema and API evolution so rolling versions can coexist, or make the required outage explicit. A routing rollback does not undo migrated data or external effects; specify restore, reconciliation or forward recovery and how it will be demonstrated.

### Capacity and operational recovery

Check the critical path against representative load and data growth. Include expensive queries, fan-out, backlogs, connection limits and dependency latency only where they affect the design. Describe signals that distinguish healthy, degraded and stuck behavior, who can recover it and which state must survive failure. Capacity and cost estimates should expose their workload assumptions rather than suggest measured precision.
