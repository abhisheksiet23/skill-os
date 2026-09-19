# Release and owner handoff

## Candidate-bound launch plan

Record the reviewed revision/snapshot, production destination, previous live revision, build command, required configuration names, domain/DNS changes if any, and release operator. Keep secret values in their designated secret store.

Identify which checks were performed locally, in preview, and against real integrations. For unresolved items, state impact and an actionable owner/dependency. A primary form that only pretends to submit is not a functioning conversion path. If the owner chooses a simpler contact route, implement and verify that honest alternative before launch.

Record recovery: how to restore the prior version or provider deployment, who can perform it, and what data/configuration changes complicate reversal. Prefer a release that preserves the current working site until the new candidate is ready. Do not delete infrastructure or previous deployments as routine cleanup.

## Live smoke checks

After publication, inspect the actual deployed candidate:

- Correct domain, TLS, intended pages/assets, and important redirects.
- Appropriate canonical, robots/indexing, sitemap, metadata, and social preview behavior where applicable.
- Primary navigation and conversion journey, including destination/receipt checks using authorized recipients.
- Production-specific forms, booking embeds, consent/tracking settings, and configuration.
- Representative responsive layout and any material issue likely to differ from preview.

Record evidence and limitations. Diagnose before retrying. If rollback is needed but its scope is not authorized, state the concrete failure and recovery action requiring approval; complete non-mutating diagnosis meanwhile.

## Handoff that an owner can use

Explain how to edit common content, replace assets without breaking composition, preview and publish changes, access enquiry destinations, and recognize delivery failures. Identify ownership for domain, hosting, editing, integrations, and measurement. Supply relevant project/provider links without credentials.

Keep maintenance proportional to the site. Do not create a large operations manual for a small static website. Document the few actions the owner actually needs and material dependencies that could expire or fail.

## Measurement

Record the business definition of a useful outcome and any valid pre-launch baseline. Separate traffic, CTA engagement, attempted/accepted submissions, received enquiries, and qualified opportunities. Specify which are currently observable and which require business follow-up.

Do not claim causality from a short before/after comparison without considering traffic mix, seasonality, campaigns, and volume. Recommend learning priorities rather than automatically launching experiments. Additional campaigns, monitoring, or recurring optimization require their own scope.
