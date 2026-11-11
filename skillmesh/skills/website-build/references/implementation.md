# Implement a visitor journey and prove its boundaries

Read the sections relevant to the change. Use the site's actual acceptance criteria to select checks; a navigation correction does not require a fresh stack decision or an unrelated integration audit. For new sites, connect the choices below into one entry-to-action journey.

## Choose the simplest adequate foundation

Inspect existing architecture and deployment constraints first. Marketing content generally needs readable, crawlable output and reliable navigation; choose rendering deliberately. Add a CMS when editing needs justify it, not automatically. Preserve the user's stack/provider when suitable. Verify changing framework or provider specifics using current official documentation when needed.

Define which content the owner can edit, required asset sizes, and how edits reach production. Avoid adding a database or service solely to store static content. If complex application behavior emerges, identify its boundary and use the appropriate application workflow rather than silently expanding scope.

## Prove the risky seam before repeating pages

Select the join most likely to invalidate the implementation: designed content into a CMS schema, mobile composition into actual content, a form into its receiving service, or old URLs into the new routing model. Implement one representative path across that join using the real stack and available integration. A static visual sample cannot resolve an uncertain submission contract; a working API call cannot establish that the approved composition survives content.

| Risk exposed by the work | Representative proof before repetition | Preserve while implementing |
| --- | --- | --- |
| A polished prototype uses unusually short content. | Render a real long heading, proof qualification, list and image through the shared layout at narrow/intermediate/wide sizes. | Hierarchy, meaningful reading order, text measure and proximity of claim to qualification. |
| Owner edits could break the design. | Preview an ordinary content/asset replacement through the actual editing path. | Supported field lengths, optional content behavior, crops/alt text and safe layout variation. |
| The enquiry UI depends on a provider. | Exercise available acceptance/failure/unknown states across the real boundary, with authorized receipt testing separately. | Accurate state wording, retry behavior and supported operator destination. |
| A redesign changes route structure. | Follow one valuable old deep link through its proposed redirect to relevant content and action. | Search/referral intent, useful detail and destination query parameters where required. |

Choose the row that addresses the actual uncertainty rather than performing all of them by default. Record the invariant that the representative path established, then reuse its component/content pattern. Expand proof only for a genuinely different page purpose or boundary. If real content forces an approved design change, explain its buyer consequence and preserve existing design authority; do not silently replace the visual direction with framework defaults.

## Content and routes

Implement meaningful titles, descriptions, heading hierarchy, internal links, canonical intent, social previews, sitemap and indexing configuration where applicable. Use structured data only for supported facts and relevant page types. A preview's indexing controls must not accidentally ship as production settings.

For redesigns, inventory existing paths and record preserve/replace/redirect decisions. Test redirects to relevant destinations and avoid redirecting every removed page to the homepage. Do not remove useful pages merely because analytics are unavailable. Check 404 behavior and campaign links when relevant.

Do not create speculative location pages, fake addresses, or repetitive keyword pages. Keep public content and private strategy/research artifacts separate in the build output. Inspect the deployable output when the source repository contains private material.

## Forms and integrations

Before wiring a form, identify the destination and responsible operator. Determine the smallest useful field set, qualification/routing rules, privacy wording and submission mechanism. Define what each visible state actually means: invalid input, sending, provider accepted, confirmed receipt, or failed/unknown outcome. Show only states the integration can establish. Confirm any response-time promise with the business and avoid unnecessary personal-data collection.

Follow project terminology and approved copy. Include consequential strings and state conditions in acceptance checks: labels match actual actions, and shortening preserves validation rules, costs, commitment and supported recovery.

Validate at the trust boundary, use appropriate abuse protection, and handle invalid input, unavailable service, retries, and repeated submissions. Do not embed private service keys in browser code. Do not log sensitive form values unnecessarily. Use approved test recipients or sandbox destinations for delivery tests; actual messages to people require authorization.

Test UI behavior, provider acceptance and downstream receipt as separate boundaries. Include invalid input, a service failure and the supported retry path; check repeated submissions where they could duplicate enquiries. A mock can demonstrate those UI states but cannot establish live delivery. Use an authorized destination for real receipt checks.

If a boundary cannot be tested, name the exact missing proof and its visitor consequence. Explicit owner acceptance may permit launch with a known gap, but does not turn the gap into verified delivery. Alternatively implement and test an honest contact route rather than leaving a simulated primary form in place.

## Responsive and accessible behavior

Implement mobile-first: establish the small-screen reading order, navigation, type scale, artwork crop, and form flow as the base, then enhance the layout at content-driven breakpoints. Avoid hover-only access, desktop-sized downloads on small screens, and fixed elements that obstruct the mobile keyboard or primary action. Keep desktop deliberately composed rather than merely stretched. Choose exact test viewports from the supported audience and actual layout; common starting samples such as 360, 390, 768, and 1440 CSS pixels are examples, not a complete device coverage claim.

Use semantic landmarks, purposeful heading structure, descriptive link/button text, visible focus, keyboard operation, appropriate contrast, useful alternatives for meaningful images, and decorative-image treatment. Forms need associated labels, understandable errors, and a clear recovery path. Check menus, dialogs, focus movement, zoom/reflow, touch interactions, and reduced motion as relevant.

Inspect narrow, intermediate, and wide layouts at recorded viewport sizes chosen to exercise actual breakpoints. Test long content and image loading where these expose real risks. Do not claim accessibility certification from an automated scan or a few manual checks.

## Performance and measurement

Control image dimensions/formats, fonts, script weight, third-party embeds, and avoidable layout shifts. Measure a representative candidate under recorded conditions; explain the limitations of synthetic results. Do not promise a universal score or field performance without field evidence.

Use responsive image sources and purposeful crops; preserve visual quality while controlling transfer size. Do not lazy-load the main above-the-fold image by default. Check the site with representative mobile network/CPU constraints and reduced motion as tools permit, recording conditions and any simulation limits. Visual ambition must work on mobile hardware and connections, not only a powerful desktop.

Define conversion events around meaningful milestones, distinguishing CTA clicks, attempted submissions, accepted submissions, and qualified outcomes where measurable. Avoid collecting form contents or unnecessary identifiers. Determine tracking/consent requirements from actual project context and current applicable guidance; do not invent jurisdictional compliance claims.

## Choose acceptance evidence

Bind results to the candidate and the conditions that matter: routes/states, viewport sizes, integration environment and measurement conditions. Reuse valid existing proof; after a change repeat affected checks and downstream behavior it could influence. Report unavailable evidence as unverified, not failed or passed by inference.

The following are examples of observable outcomes, not a mandatory complete test plan:

- An intended buyer arriving on a service page can identify scope, fit, evidence, and the appropriate next step.
- The primary enquiry journey validates input, recovers from service failure, and reaches its intended test destination when authorized.
- Important old URLs remain useful through preserved content or tested relevant redirects.
- Representative pages retain reading order, usable navigation, and legible composition on narrow and wide screens.

Adapt these to the project; do not manufacture irrelevant tests or treat this list as the entire acceptance contract.
