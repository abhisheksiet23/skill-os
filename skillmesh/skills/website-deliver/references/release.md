# Release the reviewed candidate and hand over operation

Use this for a meaningful launch or migration. Reuse adequate project release records and provider workflows. The purpose is a recoverable, verified publication, not a new fixed document set.

## Terms
- **Frozen revision:** the exact, unchanging version that was reviewed.
- **Candidate-bound:** tied to one specific candidate. If the candidate changes, the evidence may no longer apply.
- **Documented versus demonstrated:** a step written down versus a step actually exercised.

## Candidate-bound launch plan
- Bind: the release to the reviewed frozen revision and the intended production destination.
- Record, as applicable: the previous live revision, build command, configuration names, domain and DNS changes, and operator. Keep secret values in their designated store.
- Candidate changed after review: determine which evidence is invalidated before relying on it for launch.
- Checks: identify which were performed locally, in preview and against real integrations.
- Unresolved items: state the impact and an actionable owner or dependency.
- Conversion: a primary form, booking or payment step that only pretends to work is not a functioning conversion path. If the owner chooses a simpler contact route, implement and verify that honest alternative before launch. A simulated primary conversion never ships.

Recovery:
- Record how to restore the prior version or provider deployment, who can perform it, and what data or configuration changes complicate reversal.
- Prefer a release that preserves the current working site until the new candidate is ready.
- Do not delete infrastructure or previous deployments as routine cleanup.

## Live smoke checks
After publication, inspect the actual deployed candidate.
- Domain: correct domain, TLS, intended pages and assets, important redirects.
- Search: production robots.txt does not block intended pages, preview noindex rules are gone, canonical and hreflang point to production, the sitemap lists intended URLs, and structured data renders. Metadata and social previews work where applicable.
- Crawler policy: the live policy matches the owner's recorded decision. If none is recorded, report the gap and leave crawler rules unchanged.
- Identity: the favicon, logo and share image render as supplied.
- Search ownership: verify search-console ownership with an authorized account. Sitemap submission and any DNS verification need their own authorization.
- Journey: primary navigation and conversion, including destination and receipt checks using authorized recipients.
- Production specifics: forms, form-mail email authentication, booking embeds, consent and tracking settings, configuration.
- Layout: representative responsive layout and any material issue likely to differ from preview.

Then:
- Record what the deployed destination actually demonstrated and which checks remain unavailable.
- Uncertain operation: inspect provider and deployment state before retrying, so a timeout does not cause duplicate mutations.
- Failure: diagnose it and choose a bounded recovery action.
- Rollback beyond current authorization: specify the concrete failure and recovery scope while completing non-mutating diagnosis.

## Hand off in a form an owner can use
- Owner actions: explain how to edit common content, replace assets without breaking composition, preview and publish changes, access enquiry destinations and recognize delivery failures.
- Ownership: identify who owns domain, hosting, editing, integrations and measurement. Link the relevant project and provider surfaces without credentials.
- Size: keep maintenance proportional to the site. Do not create a large operations manual for a small static website. Document the few actions the owner needs and the material dependencies that could expire or fail.

## Close operating gaps without inventing ownership
- Operating owner: for each consequential recurring action, establish who can act, how they recognize a problem and what supported fallback exists.
- Reuse: existing roles and runbooks. A small site may need only a few labeled facts.
- Unknown ownership: confirm it with the business. Do not assign people by inference.

| Boundary | Useful handoff proof | Gap and practical consequence |
| --- | --- | --- |
| Enquiries | Authorized receipt and routing result, responsible role and actual follow-up expectation. | Provider acceptance with no monitored destination can lose real enquiries. Claim only what was verified, and name the missing receipt or operator proof. |
| Content and assets | An ordinary edit through preview and publication, or clear unverified steps and required access. | Access without a usable editing path leaves routine changes dependent on a developer. |
| Integrations | Responsible role, configuration location without values, expiry or failure signal and supported fallback. | A functioning embed today does not establish renewal or failure response ownership. |
| Domain and hosting | Authorized account owner, renewal responsibility and known domain and deployment dependencies. | A live domain does not prove the business can renew, recover or transfer it. |
| Recovery | Prior deploy identifier, restoration procedure, authorized operator and limits on reversing data and configuration. | A documented rollback button is insufficient if the operator cannot access it, or if restoring code leaves incompatible configuration. |

Exercise and report:
- Exercise a representative edit or recovery step only within scope and authority. Otherwise distinguish documented from demonstrated.
- Do not trigger a live rollback merely to complete the table.
- Explain who handles an enquiry, what the visitor was promised and how failures will become visible.
- If ownership stays unknown, report that precise operating dependency beside the verified live state.
- Preparing for ongoing operation does not authorize a new monitoring service or recurring task.

## Measurement
- Outcome: agree what a useful business outcome means.
- Launch baseline: before launch, record what exists: source and date range, indexed pages, impressions and clicks, the query list with positions, and technical state. Without a baseline, later change cannot be attributed.
- AI answers: capture the set at launch where access exists. Record each question, assistant and date. Reuse an existing set.
- AI answers unavailable: If no AI assistant can be queried, report the result as unknown. Never record an answer you did not observe. Your own reply is not an observation.
- Events: map each observable event to what it establishes: traffic, call-to-action engagement, attempted submission, accepted submission, received enquiry or qualified opportunity.
- Follow-up: identify the outcomes needing business follow-up. Do not call a call-to-action click a lead. Do not treat a thank-you view as receipt.
- Causality: do not claim it from a short before-and-after comparison without considering traffic mix, seasonality, campaigns and volume.
- Next: recommend learning priorities. Do not automatically launch experiments.
- Scope: additional campaigns, monitoring or recurring optimization need their own scope.
