# Implementation decisions and proof

## Choose the simplest adequate foundation

Inspect existing architecture and deployment constraints first. Marketing content generally needs readable, crawlable output and reliable navigation; choose rendering deliberately. Add a CMS when editing needs justify it, not automatically. Preserve the user's stack/provider when suitable. Verify changing framework or provider specifics using current official documentation when needed.

Define which content the owner can edit, required asset sizes, and how edits reach production. Avoid adding a database or service solely to store static content. If complex application behavior emerges, identify its boundary and use the appropriate application workflow rather than silently expanding scope.

## Content and routes

Implement meaningful titles, descriptions, heading hierarchy, internal links, canonical intent, social previews, sitemap and indexing configuration where applicable. Use structured data only for supported facts and relevant page types. A preview's indexing controls must not accidentally ship as production settings.

For redesigns, inventory existing paths and record preserve/replace/redirect decisions. Test redirects to relevant destinations and avoid redirecting every removed page to the homepage. Do not remove useful pages merely because analytics are unavailable. Check 404 behavior and campaign links when relevant.

Do not create speculative location pages, fake addresses, or repetitive keyword pages. Keep public content and private strategy/research artifacts separate in the build output. Inspect the deployable output when the source repository contains private material.

## Forms and integrations

Specify destination, responsible owner, minimal fields, qualification/routing rules, privacy wording, submission mechanism, and valid success/failure behavior. Confirm any promised response time with the business. Avoid unnecessary personal-data collection.

Validate at the trust boundary, use appropriate abuse protection, and handle invalid input, unavailable service, retries, and repeated submissions. Do not embed private service keys in browser code. Do not log sensitive form values unnecessarily. Use approved test recipients or sandbox destinations for delivery tests; actual messages to people require authorization.

Verify client feedback, provider acceptance, and downstream receipt separately. A mocked integration proves UI behavior only. If live delivery cannot be tested, record the exact gap and avoid calling that journey release-ready unless the owner explicitly accepts the limitation or an honest alternative is implemented and tested.

## Responsive and accessible behavior

Implement mobile-first: establish the small-screen reading order, navigation, type scale, artwork crop, and form flow as the base, then enhance the layout at content-driven breakpoints. Avoid hover-only access, desktop-sized downloads on small screens, and fixed elements that obstruct the mobile keyboard or primary action. Keep desktop deliberately composed rather than merely stretched. Choose exact test viewports from the supported audience and actual layout; common starting samples such as 360, 390, 768, and 1440 CSS pixels are examples, not a complete device coverage claim.

Use semantic landmarks, purposeful heading structure, descriptive link/button text, visible focus, keyboard operation, appropriate contrast, useful alternatives for meaningful images, and decorative-image treatment. Forms need associated labels, understandable errors, and a clear recovery path. Check menus, dialogs, focus movement, zoom/reflow, touch interactions, and reduced motion as relevant.

Inspect narrow, intermediate, and wide layouts at recorded viewport sizes chosen to exercise actual breakpoints. Test long content and image loading where these expose real risks. Do not claim accessibility certification from an automated scan or a few manual checks.

## Performance and measurement

Control image dimensions/formats, fonts, script weight, third-party embeds, and avoidable layout shifts. Measure a representative candidate under recorded conditions; explain the limitations of synthetic results. Do not promise a universal score or field performance without field evidence.

Use responsive image sources and purposeful crops; preserve visual quality while controlling transfer size. Do not lazy-load the main above-the-fold image by default. Check the site with representative mobile network/CPU constraints and reduced motion as tools permit, recording conditions and any simulation limits. Visual ambition must work on mobile hardware and connections, not only a powerful desktop.

Define conversion events around meaningful milestones, distinguishing CTA clicks, attempted submissions, accepted submissions, and qualified outcomes where measurable. Avoid collecting form contents or unnecessary identifiers. Determine tracking/consent requirements from actual project context and current applicable guidance; do not invent jurisdictional compliance claims.

## Acceptance examples

- An intended buyer arriving on a service page can identify scope, fit, evidence, and the appropriate next step.
- The primary enquiry journey validates input, recovers from service failure, and reaches its intended test destination when authorized.
- Important old URLs remain useful through preserved content or tested relevant redirects.
- Representative pages retain reading order, usable navigation, and legible composition on narrow and wide screens.

Adapt these to the project; do not manufacture irrelevant tests or treat this list as the entire acceptance contract.
