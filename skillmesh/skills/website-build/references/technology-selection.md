# Technology selection for marketing websites

Use this when a marketing site's technical foundation is genuinely undecided.

## Terms
- **Island:** an independent interactive component inside otherwise pre-rendered pages.

## Start from the facts
- First identify rendering needs, interactive behavior, who edits content and hosting constraints.
- Purchases: recommend hosting, domains, CMS plans and licensed tools with their costs where known. Never buy them. Ask the user to.
- A framework preference is weaker evidence than an existing suitable stack or the owner's publishing workflow.
- The default below is a starting point, not current compatibility evidence. It was reviewed against official documentation on 2026-09-16. At implementation time verify stable releases, integrations and hosting or runtime support in official documentation. Do not hard-code version numbers.

## Default to consider
For a primarily content-driven company website with no contrary constraints, consider Astro with TypeScript and pre-rendered pages, using Tailwind CSS plus custom CSS and design tokens. Evaluate that choice against the actual editing and deployment needs before recommending it.
- Interactivity: add independent interactive components where they earn their runtime cost. React or another supported UI library can serve a complex island without turning ordinary navigation into a whole client application.
- Basis: choose this stack for its fit with content-driven rendering, not a universal performance claim.
- Styling: Tailwind is optional when existing CSS architecture fits. Neither styling tools nor rendering frameworks establish art direction or visual quality.
- Hosting: trace the conversion path before choosing it: browser, endpoint or managed integration, destination and operating owner.
- Static hosting: a static or CDN deployment serves pre-rendered pages but cannot itself perform private-key delivery. Verify that the provider supports the endpoint's runtime and configuration.
- Content: keep it in structured files for developer- or agent-maintained sites. Introduce an editor-friendly CMS for real ownership, preview, localization or publishing needs.
- Motion: prefer CSS for ordinary transitions. Add a motion library only when choreography warrants it. Maintain reduced-motion behavior and mobile performance.
- Assets: use optimized authentic or generated assets from the established art direction.

## Depart from the default deliberately

| Situation | Decision |
| --- | --- |
| Existing viable site or established team/platform | Preserve it unless a justified migration is in scope |
| Extensive connected React interactions or shared application architecture | Evaluate Next.js with TypeScript. Use server and client boundaries intentionally |
| Owner requires frequent visual editing and publishing | Select the editing, CMS or platform workflow first. Do not impose source-file editing |
| Existing provider or managed website-building environment fixes the stack | Follow its supported environment and apply the same design, content and quality standards |
| Ecommerce checkout or authenticated product dominates scope | Reclassify the scope as product or commerce work |

- A contact form, a small calculator or animation alone does not force a full application architecture.
- Do not force a complex interactive application into a static-only deployment.
- Next.js: decide between runtime hosting and static export from actual feature needs. Features requiring a runtime are not supplied by a static export.

## Record the decision
- Record: the selected rendering, styling, interaction, editing and asset approach, with the form and data flow and hosting evidence.
- Trade-offs: explain consequential ones, including why a migration is worthwhile if one is proposed. A departure from a default needs a reason, not an approval ceremony.
- Dependencies: select supported stable versions at implementation time and pin them with a lockfile.
- Proof: prove compatibility with the actual build, rendered output, important journeys and deployment behavior.
- If delivery or runtime testing is unavailable: keep that part provisional. Do not present a successful scaffold as readiness.

## Official reference points
- [Astro's purpose and design principles](https://docs.astro.build/en/concepts/why-astro/)
- [Astro islands architecture](https://docs.astro.build/en/concepts/islands/)
- [Astro image handling](https://docs.astro.build/en/guides/images/)
- [Tailwind mobile-first responsive styling](https://tailwindcss.com/docs/responsive-design)
- [Next.js server and client components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [Next.js static export and limitations](https://nextjs.org/docs/app/guides/static-exports)
