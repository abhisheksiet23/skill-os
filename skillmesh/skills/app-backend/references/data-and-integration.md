# Data and integration risks

For external operations, define the observable outcome and reconcile an uncertain result before retrying. Use idempotency or unique business keys when duplicate submission could cause harm. Distinguish local transaction rollback from effects already accepted by another system.

For data changes, inspect existing records, defaults, nullability, identifiers and constraints. Verify both upgrade and fresh-create paths. Test representative old data and affected queries, including invalid and boundary cases. Keep an executable, sanitized reproduction where useful.

For independently deployed consumers, prefer compatible expansion before removing old shapes. Record the actual API contract: models, validation, errors, auth, paging/filter/sort and relevant retry semantics. Use the project's error conventions rather than forcing a vendor-specific format.

When old and new systems coexist, identify routing/auth trust boundaries, authoritative writers, shared schema and retained jobs/reports/integrations. Prove old readers can handle new writes, or define tested reconciliation/forward recovery. Reverting application routing alone does not reverse data.

Evaluate authorization at server-side boundaries, including record scope and exceptional actions. Keep an audit trail for consequential business changes when required, separate from diagnostic logs. Use existing project conventions before designing a new audit subsystem.

When a check fails, distinguish environment/setup failure from the reported behavior. Investigate with a bounded reproduction and distinguishing observations. One lucky passing run does not prove an intermittent defect fixed. Remove temporary instrumentation after verification.
