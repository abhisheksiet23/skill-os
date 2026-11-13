# Tooling roadmap

2026-11-13. Tracking pilot committed; SkillMesh 0.2.0 source bundles Serena. Installation is device-specific and may lag authored changes; the [current checkpoint](toolkit-session-assessments.md) separates source state from deployment. No application source changed.

**Goal:** reduce repeated effort without losing correctness. Initial stack: Angular, .NET Core/.NET and SQL Server.

| Work | Why | Next step | Done when |
| --- | --- | --- | --- |
| Build per-use tracking | Discover which repeated tasks consume effort. | Local [collection pilot](use-tracking.md) proved; use on relevant operations in the next active project and measure overhead/usefulness. | Real uses produce useful records with visible measurement gaps and low collection overhead. |
| Enable project-aware MCP tools | Make suitable tools usable in whichever project is active. | First bundled provider implemented: native catalog and TypeScript/C# synthetic paths pass. Use in the next applicable project; verify its specific dependencies and relationships. [Implementation](serena.md). | Tools are exposed, bind the correct project and preserve fallback. First integration proof complete; real-application usefulness and Angular template coverage remain open. |
| Offload repeated work | Replace mechanical model work with reliable operations. | Use observations to choose one recurring burden; reuse existing runners first. | A deterministic path preserves results and reduces total effort, including setup and corrections. |
| Inspect SQL Server schema | Ground analysis in actual database structure. | Use an authorized development target; start with native catalog queries. | Relevant schema and drift are established. Choose MCP only if repeated access friction warrants it. |

## Tracking minimum

One use is a purposeful operation, not every tool call. Capture project/task, category, mechanism, observed duration where available, outcome/rework and measurement source/gaps. Separate estimates from measurements; missing tokens/cost remain unknown. Do not double-count nested or overlapping work.

Keep records project-local. Collect metadata, excluding secrets and raw prompts, code or query results. Show failures and partial coverage; collection failure must not block application work.

**Stop expanding tracking if annotation or integration becomes substantial before yielding a useful finding.** Simplify collection first. No dashboard or general telemetry platform is needed initially.

## Decisions and limits

- Owner clarification, 2026-11-12: implement reusable tooling for whichever project is active; a Serena-versus-search comparison or selected benchmark application is not a prerequisite. This supersedes the earlier comparison-first next step.
- Serena remains the first code-navigation candidate, not a mandatory provider for every project. Select tools by the actual task, stack and available capabilities. Check project compatibility and Angular template relationships; retain text search for unsupported paths.
- Defer semantic editing, wider language coverage and arbitrary data exploration. Add bounded data diagnostics for a concrete recurring question.
- No application target or DB access selected. This does not block reusable integration planning. Savings, costs and dates are unknown.

**Current evidence:** RTK project telemetry was empty. A metadata-only PowerShell runner now records purposeful local operations, including successful validation and failed migration attempts; tokens, cost and savings remain unknown. [Pilot evidence and limits](use-tracking.md#evidence-as-of-2026-11-12).

**Next:** use bundled navigation and purposeful tracking in ordinary authorized project work. Choose a recurring mechanical burden for offloading from actual observations; none is selected yet. SQL Server access is unchanged and requires a concrete authorized target. No comparison application is required.

## Project-aware MCP plan

**Accepted objective:** make appropriate MCP capabilities available across projects, adapting to the project being worked on at that moment. Do not require the owner to nominate a comparison application or run a benchmark campaign first.

**Implemented approach:** one bundled provider plus native project/session binding. The agent selects available tools from their descriptions, verifies the active root and uses them when relevant. Skills retain portable methods and fallback guidance. No custom router, provider registry or shared state engine was added.

### Accepted delivery choice

Owner selected SkillMesh-bundled delivery: installing the plugin should bring its tools and usage guidance together. Separate personal MCP configuration was considered but would split setup and recovery from plugin installation. Preserve the existing plugin identity and installation path.

Native plugin-provided MCP support is used. The host exposes Serena's seven navigation tools; this was verified separately from native plugin registration. [Official MCP documentation](https://developers.openai.com/codex/mcp), [implementation and checks](serena.md).

The source now has portable root `plugin.json` and `mcp.json`, with a synchronized `.codex-plugin/plugin.json` compatibility overlay. Native diagnostics established that this host's legacy MCP arguments did not expand plugin-root placeholders; portable package discovery does. The existing installer and packaging checks were extended rather than replaced.

### Project binding and ordinary use

1. Establish the current project/worktree root from the active task; do not bind a reusable connection permanently to skill-os.
2. Prefer starting the provider unbound and explicitly activating the verified task root. A plugin's installation directory is not the application's root: use plugin-root substitution only for packaged assets, and do not assume server working-directory inheritance or an undocumented project-path variable. If the provider requires startup binding, verify the host's supported path mechanism. Keep configuration, caches and project facts in their owning project or documented local provider locations. Inspect activation commands before first use; activation can execute configured commands.
3. Verify a known symbol/reference lookup before trusting semantic results. Missing dependencies, empty results, unsupported files and timeouts must trigger diagnosis or a working fallback, not a claim that no references exist.
4. Use native per-session processes for stateful providers. Serena documents one active project per server instance; avoid sharing a mutable active-project server between unrelated chats. Verify binding again after a project switch. [Server lifecycle](https://oraios.github.io/serena/02-usage/020_running.html), [project workflow](https://oraios.github.io/serena/02-usage/040_workflow.html).
5. Prefer focused semantic navigation where it helps; retain `rg` and file reads for text, configuration, unsupported languages and incomplete relationships. Start with code understanding; semantic editing remains deferred.

Serena's current documentation lists experimental Angular support, requiring resolvable project dependencies; missing `@angular/core` can yield empty template-aware results. Its default C# backend uses Roslyn with .NET 10+ and PowerShell 7 on Windows; OmniSharp is an alternative. Recheck against the installed version and actual project's runtime before choosing settings. These prerequisites are not a requirement to migrate an application's target framework. [Language support](https://oraios.github.io/serena/01-about/020_programming-languages.html).

### Delivered first increment and remaining proof

- Serena 2.1.0, uv-managed Python 3.12, focused provider settings and the `code-navigation` skill are bundled. The Windows installer bootstraps uv if needed and prewarms available initial-stack backends. Existing Serena global settings are left alone; SkillMesh's managed defaults omit editing-mode prompts and disable anonymous usage reporting.
- TypeScript and C# synthetic live checks passed for definitions/references, two process bindings, project switching and missing-root/native fallback. These are integration checks, not application acceptance or model-behavior scores.
- Native host discovery passed with 23 skills and seven Serena navigation tools. New chats must load the installed plugin; current-chat snapshots and other devices require their own checks. Disable/recovery instructions are in the implementation guide.
- Concurrent cold Roslyn extraction failed during testing. Dependency prewarming plus a known-symbol readiness check addresses the observed setup path. Angular dependencies are prepared, but project-specific Angular template behavior remains unproved.
- Observe overhead and usefulness during real use without a comparison gate. The command tracker does not measure individual MCP calls; missing provider/time/cost measurements stay unknown. No telemetry platform was added.

**Remaining boundary:** normal use in the next applicable project, actual Angular relationships and environment-specific prerequisites. Do not expand providers without a concrete task need. Savings, costs and future delivery dates remain unknown.
