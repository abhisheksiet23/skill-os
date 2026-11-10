# Technology selection for marketing websites

Use this reference when a marketing site's technical foundation is genuinely undecided. First identify rendering needs, interactive behavior, who edits content and the hosting constraints. A preference for a framework is weaker evidence than an existing suitable stack or an owner's publishing workflow.

The recommendation below was reviewed against official documentation on 2026-09-16. It is a starting hypothesis, not current compatibility evidence. At implementation time verify stable releases, integrations and hosting/runtime support in official documentation; do not freeze version numbers into the skill.

## Default to consider

For a primarily content-driven company website with no contrary constraints, consider Astro with TypeScript and pre-rendered pages, using Tailwind CSS plus custom CSS/design tokens. Evaluate that choice against the actual editing and deployment needs before recommending it. Add independent interactive components where they earn their runtime cost; React or another supported UI library can help with a complex island without turning ordinary navigation into a whole client application.

Choose this stack for its fit with content-driven rendering, not a universal performance claim. Tailwind is optional when existing CSS architecture fits; neither styling tools nor rendering frameworks establish art direction or visual quality.

Trace the conversion path before choosing hosting: browser, endpoint or managed integration, destination and operating owner. A static/CDN deployment can serve pre-rendered pages but cannot itself perform private-key delivery. Verify that the chosen provider supports the endpoint's runtime and configuration. Keep content in structured files for developer/agent-maintained sites; introduce an editor-friendly CMS for real ownership, preview, localization or publishing needs.

Prefer CSS for ordinary transitions. Add a motion library only when choreography warrants it; maintain reduced-motion behavior and mobile performance. Use optimized authentic/generated assets from the established art direction.

## Depart from the default deliberately

| Situation | Decision |
| --- | --- |
| Existing viable site or established team/platform | Preserve it unless a justified migration is in scope |
| Extensive connected React interactions or shared application architecture | Evaluate Next.js with TypeScript; exploit server/client boundaries intentionally |
| Owner requires frequent visual editing and publishing | Select the editing/CMS/platform workflow first; avoid imposing source-file editing |
| Existing provider or managed website-building environment fixes the stack | Follow its supported environment and apply the same design/content/quality standards |
| Ecommerce checkout or authenticated product dominates scope | Reclassify scope and use an appropriate product/commerce workflow |

A contact form, a small calculator, or animation alone does not force a full application architecture. Conversely, do not force a complex interactive application into a static-only deployment. With Next.js, decide between runtime hosting and static export from actual feature needs; features requiring a runtime are not supplied by a static export.

## Record the decision

Record the selected rendering, styling, interaction, editing and asset approach with the form/data flow and hosting evidence. Explain consequential trade-offs, including why a migration is worthwhile if one is proposed; a departure from a default needs a reason, not an approval ceremony. Select supported stable dependencies at implementation time and pin them with a lockfile.

Prove compatibility with the actual build, rendered output, important journeys and deployment behavior. If delivery or runtime testing is unavailable, keep that part provisional instead of presenting a successful scaffold as readiness.

## Official reference points

- [Astro's purpose and design principles](https://docs.astro.build/en/concepts/why-astro/)
- [Astro islands architecture](https://docs.astro.build/en/concepts/islands/)
- [Astro image handling](https://docs.astro.build/en/guides/images/)
- [Tailwind mobile-first responsive styling](https://tailwindcss.com/docs/responsive-design)
- [Next.js server and client components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [Next.js static export and limitations](https://nextjs.org/docs/app/guides/static-exports)
