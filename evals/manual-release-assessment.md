# Manual release assessment — 2026-10-17

Updated backend, frontend, solution-design, delivery and QA instructions. The library default is owner-initiated release compilation, SQL generation, publishing, packaging and installation. Instructions/profiles/templates can be prepared without executing them. Ordinary development builds/tests remain implementation verification. EF Core migrations are the default schema authority for new .NET relational projects, with owner-generated SQL manually applied through SSMS on SQL Server. Existing adequate migration systems and other stacks remain supported. Production startup does not create/migrate/seed schema.

Added local backend database-release and delivery backend-release references. They cover migration baselines, SSMS batch/error handling, separate provisioning/bootstrap, data preservation, permissions, recovery, IIS folder publishing, persistent files/keys/configuration, identity-dependent key recovery and manual cutover.

## Executed evaluation

One evaluator produced actual before/after responses for the same two offline requests using HEAD `4bd1301` versus the working tree: new EF/SQL Server/IIS with persistent uploads and DPAPI keys; existing Python/PostgreSQL/Alembic. Responses are saved in ignored `.eval-runs/manual-release/evaluation.md`. The same evaluator saw both versions, so this is a contaminated paired exercise, not a blind or causal benchmark. No release-producing or deployment commands were executed.

Baseline responses already proposed sensible migration review, backups and manual hosting. Candidate responses made the schema authority, fail-stop behavior across GO batches, absence of EF runtime migration locking for manual SQL, separate recoverable identity bootstrap, host identity/key recovery and non-EF preservation more explicit. No blocking instruction defect was observed.

The owner then clarified manual compilation/publishing too. Earlier answers predate that clarification and were not counted as proof of the final instructions. The evaluator reread current skills and produced a new instructions-only response: owner restores/builds the frontend/backend, generates pinned EF SQL, runs folder publishing, inspects outputs, packages and deploys in explicit stages. Actual evaluator actions were source reads and evaluation Markdown writes only; no build, publish, SQL-generation or package command. New QA/frontend guidance prevents generating an absent release artifact simply to complete verification. A minor final-reference phrase saying “prepare the package” was corrected to “prepare the recipe” to remove ambiguity.

## Evidence limits

Library packaging validator: 19 skills, zero errors. Official skill validator passed all five changed entrypoints; whitespace checks passed. This is metadata/reference evidence only.

The evaluation tested instruction application and action boundaries, not actual SQL Server, SSMS SQLCMD error handling, IIS deployment, application compilation/publishing, authentication, DPAPI recovery, backup/restore or upgrade correctness. All those production/package checks remain pending. Tokens, performance, recovery time and owner usability are unknown. No active Medcross code, installed plugin or remote deployment was changed.

Current documentation checked during design: [EF migration deployment](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/applying), [ASP.NET Core on IIS](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/), and [SQLCMD commands](https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-commands). Relevant expectations were written into the references rather than treating a documentation link as executed proof.

## Frontend clarification

The owner also specified manual frontend build/publishing and deployment to IIS. Expanded app-frontend and the delivery reference to cover standalone static IIS versus ASP.NET Core bundled assets, SSR runtime requirements, public API/base-path settings, navigation-only fallback, API/asset exclusions, authentication across origins, backend web.config preservation, cache/lazy-chunk transitions and operator cutover/recovery. No separate-site requirement was imposed on the combined application.

The same evaluator appended four actual baseline/candidate operator-recipe answers for standalone Angular under `/helpdesk` with a separate authenticated API, and Angular bundled with ASP.NET Core. The candidate explicitly addressed these seams and preserved owner execution. No blocking instruction defect was observed; a frontend-only entrypoint still gives concise guidance while detailed operations live in the delivery skill's own reference. Same-context bias remains. No frontend build, SQL generation, publishing, file transfer or IIS/browser test was executed. Additional library and official frontend/delivery validation passed. Current [Angular deployment](https://angular.dev/tools/cli/deployment) and [IIS MIME guidance](https://learn.microsoft.com/en-us/iis/configuration/system.webServer/staticContent/mimeMap) informed the reference.
