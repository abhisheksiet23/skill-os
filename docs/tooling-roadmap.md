# Tooling roadmap

2026-11-12. Local tracking pilot implemented; no application integration or tools installed.

**Goal:** reduce repeated effort without losing correctness. Initial stack: Angular, .NET Core/.NET and SQL Server.

| Work | Why | Next step | Done when |
| --- | --- | --- | --- |
| Build per-use tracking | Discover which repeated tasks consume effort. | Local [collection pilot](use-tracking.md) proved; select an authorized application and measure collection overhead/usefulness. | Real uses produce useful records with visible measurement gaps and low collection overhead. |
| Compare Serena | Improve symbol navigation and impact analysis. | Compare its LSP backend with existing search on Angular and .NET tasks. Run alongside tracking. | Correctness, cold/warm overhead and fallback needs support adopting, narrowing or rejecting it. |
| Offload repeated work | Replace mechanical model work with reliable operations. | Use observations to choose one recurring burden; reuse existing runners first. | A deterministic path preserves results and reduces total effort, including setup and corrections. |
| Inspect SQL Server schema | Ground analysis in actual database structure. | Use an authorized development target; start with native catalog queries. | Relevant schema and drift are established. Choose MCP only if repeated access friction warrants it. |

## Tracking minimum

One use is a purposeful operation, not every tool call. Capture project/task, category, mechanism, observed duration where available, outcome/rework and measurement source/gaps. Separate estimates from measurements; missing tokens/cost remain unknown. Do not double-count nested or overlapping work.

Keep records project-local. Collect metadata, excluding secrets and raw prompts, code or query results. Show failures and partial coverage; collection failure must not block application work.

**Stop expanding tracking if annotation or integration becomes substantial before yielding a useful finding.** Simplify collection first. No dashboard or general telemetry platform is needed initially.

## Decisions and limits

- Serena is the preferred candidate, not a proven improvement. Check project compatibility and Angular template relationships; retain text search for unsupported paths.
- Defer semantic editing, wider language coverage and arbitrary data exploration. Add bounded data diagnostics for a concrete recurring question.
- No application target or DB access selected. Savings, costs and dates are unknown. Implementation details belong with the next increment.

**Current evidence:** RTK project telemetry was empty. A metadata-only PowerShell runner now records purposeful local operations, including successful validation and failed migration attempts; tokens, cost and savings remain unknown. [Pilot evidence and limits](use-tracking.md#evidence-as-of-2026-11-12).

**Next:** select one owner-authorized representative application for a few measured uses; overhead and application acceptance remain unproved. Serena, offloading and SQL Server work are unchanged. This roadmap does not authorize installation, DB access, deployment or spending.
