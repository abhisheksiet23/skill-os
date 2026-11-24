# Assign and test cross-boundary guarantees

Follow one consequential operation across the proposed boundaries and name the component responsible for each guarantee. Use the questions below where they could change the approach. They are not mandatory document sections.

## Compare the smallest sufficient mechanisms
- Keep only alternatives that could reasonably win under the actual constraints.
- Start with the existing mechanism or a local extension. Compare another approach only when it changes a required guarantee, operating burden or reversibility.
- State the condition that would overturn the recommendation.
- A technology popularity comparison is not a design decision.

| Required outcome | Smallest credible approach | Reason to choose more machinery |
| --- | --- | --- |
| One database must reject duplicate active reservations | Transaction plus an enforceable uniqueness or locking strategy | Another authoritative writer or remote effect crosses that transaction |
| A committed change must eventually notify a remote service | Durable pending work (outbox) with retry and reconciliation | Demonstrated throughput, isolation or independent consumption requires a broker |
| A new field must coexist with old application versions | Compatible expansion, populate and verify, switch readers, then contract | Compatibility is impossible and an explicit outage and restore path is acceptable |

Stress the recommended path where responsibility changes:
- Crash after commit but before acknowledgement.
- Concurrent attempts against the same invariant.
- An old reader after a new writer.

For each, name the durable state, the next actor and the observable recovery.

Migration: a stop halfway must leave a known supported state or an explicit forward-repair or restore dependency.

Contrast pair:
- Not settled: "use a queue for reliable invoices". It leaves the database-commit and publish gap open.
- Settled: an outbox written in the invoice transaction, a stable invoice operation key, and duplicate handling by the recipient.
- Recipient lacks a key or duplicate handling: disclose possible duplicate invoices and name the reconciliation owner. Do not claim exactly once.
- A direct synchronous call can suffice when failure may safely abort the operation and no accepted remote effect can be lost or repeated. Verify that premise before adding a worker.

## Data and external effects
- Locate the authoritative writer and transaction boundary for each consequential state change.
- Persistence and an external effect cannot commit atomically: explain the durable handoff, retry ownership and reconciliation.
- A queue alone does not prevent lost work or duplicate effects.
- Check crashes before and after commits, acknowledgements and remote calls.
- Distinguish delivery guarantees from business-effect guarantees.

### Duplicate and ambiguous outcomes
- Define idempotency scope, key lifetime and concurrent-duplicate behavior where required.
- Account for an external system that lacks idempotency or returns an ambiguous timeout.
- Promise exactly-once effects only with an enforceable end-to-end mechanism.
- Name recovery ownership and any unresolved need for manual intervention.

### Concurrent and asynchronous state
- Concurrent updates: decide which invariant needs locking, version checks, serialization or compensation.
- Asynchronous flows, where consequential: define accepted versus completed, stale reads, event versioning, ordering needs, poison messages and replay behavior.
- Tie overload controls and retry limits to dependency capacity. Unlimited retries make outages worse.

## Trust and integration
- Trace identity and authorization across ingress, services, workers and data access.
- Identify tenant and record scope, privileged operations and untrusted payloads.
- State where enforcement occurs. Propagating a tenant identifier is not proof of isolation.
- Separate business audit records from diagnostic logs when auditability is required.

External contracts:
- Confirm the consequential parts: identifiers and stored values, auth, errors, limits, timeout semantics, compatibility.
- Separate documented capability, observed behavior and assumptions.
- Degrade gracefully only where the product permits. Otherwise make failure visible and recoverable.

## Change and operation
Coexistence and replacement:
- Define entry routing, session and auth compatibility, authoritative writers, shared consumers and jobs, and old and new data compatibility.
- Avoid uncoordinated dual writes.
- Sequence schema and API evolution so rolling versions can coexist, or make the required outage explicit.
- A routing rollback does not undo migrated data or external effects. Specify restore, reconciliation or forward recovery, and how it will be demonstrated.

### Capacity and operational recovery
- Check the critical path against representative load and data growth.
- Include expensive queries, fan-out, backlogs, connection limits and dependency latency only where they affect the design.
- Describe the signals that distinguish healthy, degraded and stuck behavior, who can recover it, and which state must survive failure.
- Show the workload assumptions behind capacity and cost estimates. Do not imply measured precision.
