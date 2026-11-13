# Choose evidence for the guarantee being assessed

Begin by naming the guarantee or user outcome under assessment, its requirement source and the candidate revision/snapshot, including relevant uncommitted changes. A past pass belongs to the candidate and environment actually tested. Later changes invalidate affected evidence; do not rerun unrelated checks without reason.

Keep requirement-source identity distinct from the implementation candidate and tested environment. Reconcile affected assertions when source intent changes; do not silently rewrite historical results. Link existing contracts, tests and reports rather than introduce a new verification template.

## Exercise the affected behavior and consumers

Turn the highest consequential uncertainty into a test that distinguishes correct behavior from a plausible faulty implementation. Choose the cheapest layer that can observe the guarantee; use real integration when the uncertainty is at that boundary. Avoid expanding into unrelated risk categories merely because they appear below.

| Risk | Distinguishing setup and assertion | Insufficient evidence |
| --- | --- | --- |
| Cross-record access leak | A permitted actor requests another scope's known record directly; no protected fields or mutation escape. | Hiding the other scope's navigation link. |
| Lost update | Two readers edit the same version; second write gets the contracted conflict or merge without losing the first. | Two unrelated records save successfully. |
| Duplicate external effect | Accept an operation, lose its response, retry the same operation and inspect the recipient's effect count. | A mocked retry returns 200. |
| Upgrade breaks retained consumer | Upgrade representative existing data, perform a new write, then use the supported old reader. | Fresh schema creation and new-client tests only. |
| Preview is mistaken for a committed operation | Compare, revise and cancel a proposal; inspect business records and effect recipients. Change relevant data or permission before Apply and verify current constraints are enforced. | A preview looks plausible or only client-side Apply is disabled. |
| Incomplete work is lost or finalized incorrectly | Save and reload a permitted incomplete draft with missing and legitimate zero values; exercise changed access/concurrent edits and attempt finalization without required evidence. Verify no final-action effects escape. | A saved label, an in-memory draft, or happy-path approval of a complete record. |

For a defect regression, establish that the assertion detects the reported failure: run it against the original candidate when available and safe, then against the corrected candidate with equivalent fixtures. If the original cannot run, use a narrow controlled reintroduction of the cause in an isolated test workspace only when that meaningfully validates sensitivity; report that limitation. A synthetic mutation is not an original-candidate run. Never mutate shared/live state to prove test sensitivity. A test that passed before the fix may cover a neighboring path rather than the defect; investigate before accepting it as regression proof.

For example, a test for stale search results must delay the earlier response until after the newer response and assert the visible result belongs to the newer query. Checking that both calls complete cannot detect the overwrite. Keep the failure artifact and the corrected result tied to their respective candidates rather than presenting only the final green run.

Choose checks from the changed behavior and its consumers: builds/static checks; rule/state/calculation tests; API/data integration; access and data-scope boundaries; migrations/backfills; consequential performance; observable failure handling. For coexistence include retained consumers and behavior after new writes.

For browser work, prefer existing automation and user-observable selectors. Test high-value journeys and recovery with deterministic fixtures. Examine actual screenshots at recorded viewports, routes and states, including long/dense content and empty/error cases. No browser means browser evidence is unavailable, not a source-inspection pass.

For changed interface copy, compare messages with actual rules, operation outcomes and available recovery actions. Check that edits preserve requirements and consequences; queued work is not completed work, filtered-out content is not an empty collection, and an unknown payment result is not a failed charge. Flag unsupported causes, reassurance, deadlines or progress claims. Check terminology, visible labels and accessible names in context, field-error association and announcements where relevant. For localized interfaces, exercise representative expanded text and count/date variants. Editorial preference is not a defect or measured usability improvement.

## Diagnose before claiming a fix

For uncertain defects, establish expected behavior and a repeatable failure, minimize it, test competing explanations, fix the cause and rerun both the reduced and original scenario. Add a meaningful regression test when feasible. Performance comparisons need equivalent workloads; intermittent failures need enough observations to justify the conclusion.

Review requirements and engineering separately in the same concise report if useful. Cite the requirement and affected implementation for gaps. Scope fixes to approved behavior; optional refactors should not become blockers.

## Verify account and authorization boundaries

When identity/authorization changes, verify the single-role foreign key and local module grants where required; no redundant user-role join table should appear without a real multi-role requirement. Exercise real bcrypt verification, wrong-password and multibyte length boundaries for local login. Module grants must not bypass record/tenant/workflow rules. For central identity, check trusted issuer/subject mapping, wrong audience/signature/expiry, unknown or disabled local accounts, local role changes and rejected external-role escalation. Confirm stable local user IDs/business history survive linking and that invalid external authentication cannot silently fall back to local credentials. Separate stubbed token/schema checks from real library, issuer and database evidence.

## State what the evidence supports

Keep proof factual: command or interaction, environment, result and limitations. Test-file existence does not prove execution; coverage percentage does not prove adequacy; a mocked result does not prove external integration. Sanitized outputs are enough; private records and credentials do not belong in evidence.

Before a release recommendation, verify the combined candidate, unresolved defects, migration/configuration implications and affected acceptance. A ready local candidate and an authorized, validated deployment are different outcomes.
