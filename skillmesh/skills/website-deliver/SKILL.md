---
name: website-deliver
description: Prepare and execute an authorized marketing website launch, verify the live site and hand over editing, integrations and measurement. Use for website release or launch preparation; a build-only request does not authorize publication.
---

# Website Deliver

Move a reviewed candidate to its authorized destination, prove what is live and leave the owner able to operate it. Keep prepared, deployed and directly verified states separate throughout the handoff.

## Terms
- **Prepared, deployed, verified:** three distinct states. Prepared means ready to ship. Deployed means published. Verified means directly checked on the live destination.
- **Candidate:** the specific version of the site that is being built, reviewed or released.
- **Blocking finding:** a false or unsupported central claim, a broken primary journey (including one that keyboard or assistive-technology users cannot complete), exposed secrets or private data, or another defect that defeats safe intended use. It counts whoever finds it.
- **Shipped record:** the record of what is currently live.
- **Launch baseline:** the dated record, taken at launch or at the first review, used for later comparison: source and date range, indexed pages, impressions and clicks, query list with positions, each AI question with its assistant and date, and technical state.
- **Crawler policy:** the owner's decision on which crawlers may access the site and for what purpose, such as search results, AI answers or AI training.
- **Operating owner:** a person or role who can act on a recurring task and recognize its failure. A named provider or mailbox is not one.

## Prepare the concrete release
Do this before any publication.
- Identify: the exact candidate and shipped record, destination and provider, review evidence, configuration, redirects and limitations.
- Evidence: accept adequate proof from any author.
- Checks: compare candidate, configuration and destination with the evidence. Reuse applicable proof and focus preparation on changed or unverified boundaries.
- Prelaunch evidence: it cannot replace live destination checks.
- Confirm: accepted content decisions, who operates the site and who receives enquiries.
- Guidance: for meaningful launches use [release guidance](references/release.md) for deploy steps, domain implications, recovery and live checks for the chosen provider. Use its section on operating gaps where ongoing actions could be orphaned.

Authority:
- Honor existing publication authority. If it is absent, finish the reviewable candidate and release plan before requesting it.
- Review gate: do not publish with an open Blocking finding unless the owner explicitly accepts the named risk. Acceptance does not turn the finding into a pass, and cannot cover anything under Never ships.
- Never ships, even with owner acceptance: exposed secrets, private data published without authorization, a claim known to be false, or a simulated primary conversion such as a form, booking or payment. Remove or correct it first. Replace a simulated conversion with a tested, honest contact route.
- Essential checks: before publishing, check the main conversion path and central claims, whether or not the site was reviewed. A conversion path is checked when followed as far as the environment and authority safely allow. If either cannot be checked, name the gap and what it could cost, and publish only if the owner explicitly accepts it. Report other missing evidence.
- Open improvements: before publishing, show the material problems still open, what visitors may lose and the smallest fix for each, and encourage the owner to close them. They do not block publication. Do not press again without new evidence.
- Crawler policy: if no decision is recorded, ask the owner before launch. Do not change crawler rules without the owner's decision.
- DNS decisions and messages keep their own authorization boundaries.
- Launch work does not imply new accounts or unrelated infrastructure changes.

## Publish and verify the real destination
- Deploy: the reviewed candidate, through the authorized mechanism.
- Uncertain operations: inspect their result before retrying.
- Check: actual live pages and assets, navigation, indexing intent, redirects, responsive presentation, and the primary conversion. Include production configuration and authorized delivery tests.
- Failures: diagnose them and apply bounded, authorized recovery.
- Preview: it is not proof of production behavior.

## Hand over the observed state
- Lead: the actual launch state and its consequence for visitors and operators.
- Form: concise labels for prepared, deployed and verified facts, with evidence links and actionable gaps. Do not write a deployment diary.
- Record: revision, time, URL, live evidence, residual risks and recovery information. Update the shipped record only with what shipped.
- Owner actions: explain common content and asset edits. Explain who owns domains, hosting and enquiries, without exposing secrets.
- Launch baseline: capture it before launch and record it with the handoff record.
- Review: name who will review search and analytics after launch, and how often. Record whether recurring review is authorized, declined or not yet asked. It is a separate scope.
- Scale: size the handoff to the site.

Measurement:
- Define meaningful measurable outcomes. Separate visits, attempts, accepted submissions, receipt and qualified demand.
- Neither deployment nor a short before-and-after comparison proves conversion improvement.
- Recurring monitoring and campaigns need their own scope.

Finish with verified status or the precise dependency preventing completion. Missing candidate proof may call for an independent candidate review. Explain the gap.
