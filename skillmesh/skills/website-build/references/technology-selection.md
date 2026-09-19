# Technology selection for marketing websites

Recommendation reviewed against official documentation on 2026-09-16. Recheck current stable releases, integrations, hosting/runtime support, and relevant documentation when implementing; do not freeze version numbers into this skill. This is a reasoned default for greenfield marketing work, not a requirement to replace an existing suitable stack or override a chosen platform's constraints.

## Default to consider

For a primarily content-driven company website, recommend Astro with TypeScript, pre-rendered pages where suitable, and Tailwind CSS plus custom CSS/design tokens for the visual system. Add interactive components only where needed. Astro's architecture supports independently interactive islands; use React or another supported UI library for a complex interactive component when that actually helps. Ordinary navigation and basic interactions need not pull in a whole client application.

This recommendation follows the fit between the project type and Astro's content-driven/server-first design, not a claim that it universally outperforms every alternative. Tailwind is a styling tool, not an art direction or a guarantee of good design. Existing CSS architecture is a valid reason not to add it.

Use a supported static/CDN deployment for pre-rendered content, adding a compatible server endpoint or managed integration for submissions when required. Validate destination/provider/runtime choices together. A static build alone cannot process private-key form delivery. Keep content in structured files for developer/agent-maintained sites; introduce an editor-friendly CMS when actual ownership, preview, localization, or publishing needs justify it.

Prefer CSS for ordinary transitions. Add a motion library only when choreography warrants it; maintain reduced-motion behavior and mobile performance. Use optimized authentic/generated assets from the established art direction. No rendering framework determines whether a website is visually striking.

## Depart from the default deliberately

| Situation | Decision |
| --- | --- |
| Existing viable site or established team/platform | Preserve it unless a justified migration is in scope |
| Content-heavy public site with modest interaction | Astro is a strong default to evaluate |
| Extensive connected React interactions or shared application architecture | Evaluate Next.js with TypeScript; exploit server/client boundaries intentionally |
| Owner requires frequent visual editing and publishing | Select the editing/CMS/platform workflow first; avoid imposing source-file editing |
| Existing provider or managed website-building environment fixes the stack | Follow its supported environment and apply the same design/content/quality standards |
| Ecommerce checkout or authenticated product dominates scope | Reclassify scope and use an appropriate product/commerce workflow |

A contact form, a small calculator, or animation alone does not force a full application architecture. Conversely, do not force a complex interactive application into a static-only deployment. With Next.js, decide between runtime hosting and static export from actual feature needs; features requiring a runtime are not supplied by a static export.

## Record the decision

State rendering approach, styling, interaction strategy, content editing, images, form/data flow, hosting compatibility, and tests. Explain the actual constraint behind each non-default choice. Select supported stable dependency versions at implementation time and pin them with a lockfile. Verify build, rendered output, important journeys, and deployment behavior; neither framework choice nor a successful scaffold proves readiness.

## Official reference points

- [Astro's purpose and design principles](https://docs.astro.build/en/concepts/why-astro/)
- [Astro islands architecture](https://docs.astro.build/en/concepts/islands/)
- [Astro image handling](https://docs.astro.build/en/guides/images/)
- [Tailwind mobile-first responsive styling](https://tailwindcss.com/docs/responsive-design)
- [Next.js server and client components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [Next.js static export and limitations](https://nextjs.org/docs/app/guides/static-exports)
