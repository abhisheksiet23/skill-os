# Protect data across integration boundaries

## Define what a successful write means

Locate the authoritative server-side checks for permissions, record scope and exceptional actions. Preserve a business audit trail when required, separate from diagnostic logs, using existing project conventions before inventing an audit subsystem.

For external operations, define the observable result and reconcile an uncertain outcome before retrying. Use idempotency or unique business keys when duplication could cause harm. Local transaction rollback cannot undo an effect another system has already accepted.

## Evolve stored data and consumer contracts together

Inspect representative existing records, defaults, nullability, identifiers, constraints and affected queries. Verify fresh-create and upgrade paths, including invalid/boundary data; retain an executable sanitized reproduction when useful.

For independently deployed consumers, prefer compatible expansion before removing old shapes. Record actual models, validation, errors, authentication, paging/filter/sort and relevant retry semantics. Follow project error conventions rather than imposing a vendor format.

For old/new coexistence, identify routing/auth trust, authoritative writers, shared schema and retained jobs, reports and integrations. Demonstrate old readers can handle new writes, or define and test reconciliation/forward recovery. Reverting routing does not reverse data.

## Diagnose the boundary that failed

Separate setup/environment failure from the reported behavior. Use a bounded reproduction and observations that distinguish competing explanations; one lucky pass cannot establish an intermittent defect is fixed. Remove temporary instrumentation after verification, and retain the candidate/environment identity and unresolved limits with the result.
