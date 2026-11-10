# Release the reviewed candidate and hand over operation

Use this guidance for a meaningful launch or migration. Reuse adequate project release records and provider workflows; the purpose is a recoverable, verified publication, not a new fixed document set.

## Candidate-bound launch plan

Bind the release to the reviewed revision/snapshot and intended production destination. Record the previous live revision, build command, configuration names, domain/DNS changes and operator as applicable. Keep secret values in their designated store. If the candidate changes after review, determine which evidence is invalidated before relying on it for launch.

Identify which checks were performed locally, in preview, and against real integrations. For unresolved items, state impact and an actionable owner/dependency. A primary form that only pretends to submit is not a functioning conversion path. If the owner chooses a simpler contact route, implement and verify that honest alternative before launch.

Record recovery: how to restore the prior version or provider deployment, who can perform it, and what data/configuration changes complicate reversal. Prefer a release that preserves the current working site until the new candidate is ready. Do not delete infrastructure or previous deployments as routine cleanup.

## Live smoke checks

After publication, inspect the actual deployed candidate:

- Correct domain, TLS, intended pages/assets, and important redirects.
- Appropriate canonical, robots/indexing, sitemap, metadata, and social preview behavior where applicable.
- Primary navigation and conversion journey, including destination/receipt checks using authorized recipients.
- Production-specific forms, booking embeds, consent/tracking settings, and configuration.
- Representative responsive layout and any material issue likely to differ from preview.

Record what the deployed destination actually demonstrated and which checks remain unavailable. When an operation has an uncertain result, inspect provider/deployment state before retrying so a timeout does not cause duplicate mutations. Diagnose the failure and choose a bounded recovery action. If a needed rollback exceeds current authorization, specify the concrete failure and recovery scope while completing non-mutating diagnosis.

## Handoff that an owner can use

Start the handoff with actual status: prepared, deployed and directly verified are distinct facts. Supply the revision, time, live URL, relevant evidence, residual limitations and recovery path. Update the live baseline only for what shipped.

Then explain the owner's recurring actions: edit common content, replace assets without breaking composition, preview/publish changes, access enquiry destinations and recognize delivery failures. Identify who owns domain, hosting, editing, integrations and measurement. Link the relevant project/provider surfaces without credentials.

Keep maintenance proportional to the site. Do not create a large operations manual for a small static website. Document the few actions the owner actually needs and material dependencies that could expire or fail.

## Measurement

Agree what a useful business outcome means and preserve any valid pre-launch baseline. Map each observable event to what it actually establishes: traffic, CTA engagement, attempted submission, accepted submission, received enquiry or qualified opportunity. Identify the outcomes needing business follow-up; do not call a CTA click a lead or treat a thank-you view as receipt.

Do not claim causality from a short before/after comparison without considering traffic mix, seasonality, campaigns, and volume. Recommend learning priorities rather than automatically launching experiments. Additional campaigns, monitoring, or recurring optimization require their own scope.
