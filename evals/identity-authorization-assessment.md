# Identity and local authorization assessment — 2026-10-17

Scope: SkillMesh guidance only, explicitly confirmed by the owner. No Medcross implementation or schema migration. Added an owning backend reference and focused guidance in backend, solution design, requirements, frontend and QA. No new skill, authentication service or routing mechanism was introduced.

The chosen default is one Users.Role foreign key to local Roles, local Modules and ModuleRoleMapping, no redundant user-role join table, and maintained bcrypt for local credentials. Stable local user IDs and optional unique external issuer/subject fields let future central authentication replace credential verification while keeping all four local tables, business references and application permissions. Module access does not replace record/team/clinic/workflow rules. Existing systems need deliberate data-preserving adoption; no automatic framework-schema replacement is authorized.

## Executed before/after exercise

Two separate performers received the same offline request in `identity-authorization-tasks.md`, with no peer outputs or assessment criteria. Baseline read HEAD `4dafbde`; candidate read revised backend/design instructions and references. Actual outputs are locally retained under ignored `.eval-runs/identity/baseline.md` and `candidate.md`. Both inherited parent model/settings. The author assessed both; assessment was not blind.

Both produced credible four-table proposals, preserved local IDs/permissions, rejected automatic trust in external role claims, separated issuer/subject pairs, and proposed safe legacy PBKDF2 and multi-role migration. Baseline was already capable; general superiority is not demonstrated. Candidate made byte limits, exact external identity comparison/index constraints, current local authorization, provider-token profile checks and owner-run release boundaries explicit. Neither produced or executed a real application.

The candidate also identified concrete adoption issues: existing long-password users cannot be silently truncated or locked out during bcrypt transition, zero/multi-role accounts need an approved mapping, and multiple providers linked simultaneously to one user would require a separately assessed identity-link representation. The final reference was tightened after the exercise to explicitly cover normalized-login uniqueness and zero/multi-role reconciliation; these final editorial additions were statically validated, not rerun as another blind trial.

## Verification and limits

Library validator passed: 19 skills, zero packaging errors. Official skill validator passed all five affected skill folders; whitespace checks passed. Primary guidance checked during authoring: [OWASP password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html), [OIDC stable identity](https://openid.net/specs/openid-connect-core-1_0-18.html) and [OWASP REST security](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html).

No actual bcrypt library, token middleware/provider, SQL Server constraints/collation, password migration, account linking or role-scope enforcement was executed. Acceptance cases are proposed, not passed. Runtime security, migration safety, latency and owner usability remain unknown. No release build, publishing, SQL generation, installed-plugin update or production operation occurred. Prior readability status stays open and is unrelated to this design exercise.
