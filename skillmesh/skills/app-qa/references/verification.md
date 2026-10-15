# Verification that changes confidence

Identify the candidate revision or snapshot and whether uncommitted changes are included. A past pass belongs to the candidate and environment actually tested. Later changes invalidate affected evidence; do not rerun unrelated checks without reason.

Choose checks from the changed behavior and its consumers: builds/static checks; rule/state/calculation tests; API/data integration; access and data-scope boundaries; migrations/backfills; consequential performance; observable failure handling. For coexistence include retained consumers and behavior after new writes.

For browser work, prefer existing automation and user-observable selectors. Test high-value journeys and recovery with deterministic fixtures. Examine actual screenshots at recorded viewports, routes and states, including long/dense content and empty/error cases. No browser means browser evidence is unavailable, not a source-inspection pass.

For changed interface copy, compare messages with actual rules, operation outcomes and available recovery actions. Check that edits preserve requirements and consequences; queued work is not completed work, filtered-out content is not an empty collection, and an unknown payment result is not a failed charge. Flag unsupported causes, reassurance, deadlines or progress claims. Check terminology, visible labels and accessible names in context, field-error association and announcements where relevant. For localized interfaces, exercise representative expanded text and count/date variants. Editorial preference is not a defect or measured usability improvement.

For uncertain defects, establish expected behavior and a repeatable failure, minimize it, test competing explanations, fix the cause and rerun both the reduced and original scenario. Add a meaningful regression test when feasible. Performance comparisons need equivalent workloads; intermittent failures need enough observations to justify the conclusion.

Review requirements and engineering separately in the same concise report if useful. Cite the requirement and affected implementation for gaps. Scope fixes to approved behavior; optional refactors should not become blockers.

Keep proof factual: command or interaction, environment, result and limitations. Test-file existence does not prove execution; coverage percentage does not prove adequacy; a mocked result does not prove external integration. Sanitized outputs are enough; private records and credentials do not belong in evidence.

Before a release recommendation, verify the combined candidate, unresolved defects, migration/configuration implications and affected acceptance. A ready local candidate and an authorized, validated deployment are different outcomes.
