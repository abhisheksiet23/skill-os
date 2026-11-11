# Review the candidate, not the intention

Use the requested scope to choose the relevant lenses below. A useful review connects an observed page or journey state to a buyer consequence and a correction; it does not infer quality from a technology choice, checklist completion or the author's description.

## Scope and severity

Identify the revision or immutable snapshot, environment and available acceptance evidence. Choose representative routes, unusual content/interaction patterns and all business-critical journeys. Record the sampling boundary: a large site can be reviewed systematically without claiming every page was visually inspected. Check whether existing evidence still applies to this candidate before reusing it. A shared typography, template, navigation or integration change can invalidate proof across routes; use that dependency to choose rechecks rather than either reviewing every page again or checking only the edited route.

- Blocking: materially false central claims, a broken primary journey, exposed secrets/private data, or another defect that defeats safe intended use.
- Material: meaningfully damages comprehension, fit assessment, trust, access, or responsiveness.
- Polish: localized craft issue without material loss of function or meaning.

Explain consequence and scope. Do not equate personal stylistic preference with a defect. Record unresolved material issues and any explicit owner's acceptance of a limitation; acceptance does not turn a failed test into a pass.

## Select entry pages by the task they must support

Choose routes from known acquisition paths, supplied search/campaign data and realistic buyer tasks. Without those sources, label plausible entry scenarios as assumptions. Prioritize a path where failure would lose a suitable buyer, mislead them or block access, alongside any distinctive template/state risk. A homepage tour alone can miss a visitor who lands directly on a service or case page.

| Plausible entry and task | Follow through | Consequential failure to look for |
| --- | --- | --- |
| Search visitor lands on a service page to assess fit. | Scope/exclusions → relevant proof → suitable action. | The page assumes homepage context, hides limits or offers no credible reason to proceed. |
| Referred buyer opens a case study to reduce risk. | Evidence/context → applicable service → enquiry. | Results lack attribution/qualification, or the path never explains applicability to the buyer. |
| Campaign visitor follows a specific offer. | Campaign promise → landing detail → form → actual next step. | Offer, cost, availability or commitment changes between surfaces. |
| Returning prospect wants contact on a phone. | Navigation/contact route → input → recovery/confirmation. | Sticky UI, inaccessible validation or an unsupported receipt promise prevents a useful action. |

Use actual source evidence to choose among these examples, not to manufacture every scenario. Note which templates, routes and states the sample covers and what remains uninspected. Extend when a shared issue or a different buying task exposes a new risk. Prioritize findings by buyer consequence and reach: a misleading offer across a campaign journey can outweigh several isolated spacing defects; an inaccessible primary control can outweigh an otherwise polished mobile layout. Keep visual and functional evidence separate even when both affect the same task.

## Review lenses

| Lens | Investigate | Useful evidence |
| --- | --- | --- |
| Buyer | Offer, fit, buying questions, trust, next step, readiness differences | Actual page content and complete entry-to-action journey |
| Business | Accurate scope, meaningful differentiation, appropriate qualification, operational promises | Brief/claim sources compared with published copy |
| Editorial | Specificity, coherence, scannability, jargon, repetition, qualifications | Exact passages and page-purpose comparison |
| Design | Company-specific expression, hierarchy, type, spacing, composition, imagery, continuity | Inspected renders compared with recorded direction |
| Responsive | Reflow, reading order, menus, sticky elements, crops, overflow, form usability | Narrow/intermediate/wide screenshots and interactions |
| Accessibility | Semantics, labels, contrast, keyboard/focus, errors, zoom, reduced motion | Manual interactions plus relevant automated findings |
| Functional | Links, routes, forms, validation, success/failure, integrations, redirects | Reproducible steps and observed destination behavior |
| Operational | Content editing, receipt/routing, failure awareness, secrets/config, handoff | Configuration without secrets, approved test results, owner workflow |
| Discoverability/performance | Indexing intent, metadata, supported structured data, asset/script behavior | Rendered output, crawl/build checks, measured conditions |

## Important distinctions

For interface copy in conversion journeys, compare the exact wording with validation rules, actual submission states and supported next actions. Preserve qualifications when shortening text. Check terminology across the journey, distinguish no matches from no content or restricted access, and flag invented delivery promises, failure causes or recovery times. Inspect visible labels, accessible names and error context together; localized journeys need representative expanded text and count/date formats. Report consequential confusion with evidence rather than treating preferred phrasing as a defect.

- A CTA click is not a lead. A displayed thank-you is not proof of receipt.
- A prototype's simulated states are not production integration evidence.
- An automated accessibility pass is not a complete accessibility evaluation.
- A synthetic performance result is not field performance.
- Reviewer comprehension is not a completed customer usability study.
- A polished design is not measured conversion improvement.
- An old test pass does not automatically cover a changed candidate.

## Execute meaningful journeys

Start from plausible search, campaign or referral entry pages as well as the homepage. Follow the buyer's path to fit assessment, supporting proof and action. For important forms, inspect exact labels and validation, invalid input, the success state and an appropriate failure/recovery path. Verify that the next action promised in each state exists.

Separate a safe UI exercise from a real downstream transaction. Confirm authorization and the test destination before sending a message or causing another external effect. If receipt cannot be checked, report that boundary as unverified; never complete a checklist by triggering an unauthorized purchase or enquiry.

Review the mobile journey and composition first, then intermediate and desktop layouts with equal care. Check supported viewport sizes and actual breakpoints. Include keyboard operation, clear focus, navigation state, form errors, long content, and images/fonts as relevant. Check that mobile crops preserve image meaning, sticky elements do not obstruct actions, and input remains usable with the onscreen keyboard where device tools permit. Inspect screenshots directly; recording them without examination is not visual review.

Evaluate visual readiness separately from functional readiness. Compare actual pages with the recorded art direction and visual benchmarks, including the opening impression, secondary sections, detail pages, image-family consistency, and small-screen craft. Generic placeholder art or a visually unfinished page remains an open design finding even when its links and forms work. Do not certify a site as visually stunning solely from instruction compliance or a numeric score; demonstrate the result and any limits through inspected evidence.

## Record concise findings

Make each finding reconstructable: candidate, route/state, environment/viewport, expectation, observation, consequence/severity, evidence, correction and retest result when available. Group systemic issues with affected examples rather than repeating one defect per page. Link inspected screenshots/logs. Distinguish a design preference from an evidenced loss of meaning, usability or fidelity to the agreed direction.

After an in-scope repair, repeat affected checks and downstream journeys the change could influence. Report two judgments with their scope: readiness (ready, needs changes or not yet determinable) and verification (complete or incomplete with named gaps). These are independent: a candidate can have observed defects and untested areas at the same time. Explicit acceptance of a limitation does not erase the finding, and technical readiness does not confer publication authority.
