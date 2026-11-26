# Review the candidate, not the intention

Choose the lenses below from the requested scope. A useful review connects an observed page or journey state to a buyer consequence and a correction. It does not infer quality from a technology choice, checklist completion or the author's description.

## Terms
- **Frozen revision:** the exact, unchanging version that was reviewed.
- **Snapshot:** a dated record of a search result or AI-assistant answer. It shows what appeared, not rankings, reach or influence.
- **Benchmark:** an inspected visual reference with the specific qualities the site should meet.
- **Sampling boundary:** the explicit statement of which routes, templates and states were inspected and which were not.
- **Target queries:** the searches and questions each page should answer, listed per page.
- **Crawler policy:** the owner's decision on which crawlers may access the site and for what purpose, such as search results, AI answers or AI training.
- **Blocking:** a false or unsupported central claim, a broken primary journey (including one that keyboard or assistive-technology users cannot complete), exposed secrets or private data, or another defect that defeats safe intended use.
- **Material:** meaningfully damages comprehension, fit assessment, trust, access or responsiveness.
- **Polish:** a localized craft issue without material loss of function or meaning.

## Scope and severity
- Identify: the frozen revision, environment and available acceptance evidence.
- Choose: representative routes, unusual content and interaction patterns, and all business-critical journeys.
- Boundary: record the sampling boundary. A large site can be reviewed systematically without claiming every page was visually inspected.
- Reuse: check whether existing evidence still applies to this candidate.
- Shared changes: a shared typography, template, navigation or integration change can invalidate proof across routes. Use that dependency to choose rechecks. Do not re-review every page, and do not check only the edited route.

Severity rules:
- Explain consequence and scope.
- Readiness is "needs changes" while any Blocking finding is open, and only then. Report other problems as improvements.
- Do not equate personal stylistic preference with a defect.
- Record unresolved material issues and any explicit owner acceptance of a limitation. Acceptance does not turn a failed test into a pass.

## Select entry pages by the task they must support
- Sources: choose routes from known acquisition paths, supplied search and campaign data, and realistic buyer tasks. Without those, label plausible entry scenarios as assumptions.
- Priority: a path where failure would lose a suitable buyer, mislead them or block access, plus any distinctive template or state risk.
- Homepage tour: it alone can miss a visitor who lands directly on a service or case page.

| Plausible entry and task | Follow through | Consequential failure to look for |
| --- | --- | --- |
| Search visitor lands on a service page to assess fit. | Scope and exclusions → relevant proof → suitable action. | The page assumes homepage context, hides limits or offers no credible reason to proceed. |
| Referred buyer opens a case study to reduce risk. | Evidence and context → applicable service → enquiry. | Results lack attribution or qualification, or the path never explains applicability to the buyer. |
| Campaign visitor follows a specific offer. | Campaign promise → landing detail → form → actual next step. | Offer, cost, availability or commitment changes between surfaces. |
| Returning prospect wants contact on a phone. | Navigation and contact route → input → recovery and confirmation. | Sticky UI, inaccessible validation or an unsupported receipt promise prevents a useful action. |

Using the table:
- Use actual source evidence to choose among these examples. Do not manufacture every scenario.
- Note which templates, routes and states the sample covers and what remains uninspected.
- Extend when a shared issue or a different buying task exposes a new risk.
- Prioritize findings by buyer consequence and reach. A misleading offer across a campaign journey can outweigh several isolated spacing defects. An inaccessible primary control can outweigh an otherwise polished mobile layout.
- Keep visual and functional evidence separate even when both affect the same task.

## Review lenses
Use the lenses the scope requires, and skip those it excludes.

| Lens | Investigate | Useful evidence |
| --- | --- | --- |
| Buyer | Offer, fit, buying questions, trust, next step, readiness differences | Actual page content and complete entry-to-action journey |
| Business | Accurate scope, meaningful differentiation, appropriate qualification, operational promises | Brief and claim sources compared with published copy |
| Editorial | Specificity, coherence, scannability, jargon, repetition, qualifications | Exact passages and page-purpose comparison |
| Design | Company-specific expression, hierarchy, type, spacing, composition, imagery, continuity | Inspected renders compared with recorded direction, and with the identity usage rules where defined |
| Responsive | Reflow, reading order, menus, sticky elements, crops, overflow, form usability | Narrow, intermediate and wide screenshots and interactions |
| Accessibility | Semantics, labels, contrast, keyboard and focus, errors, zoom, reduced motion | Manual interactions plus relevant automated findings |
| Functional | Links, routes, forms, validation, success and failure, integrations, redirects, consent and privacy behavior against the privacy notice | Reproducible steps and observed destination behavior |
| Operational | Content editing, receipt and routing, failure awareness, secrets and config, handoff | Configuration without secrets, approved test results, owner workflow |
| Findability | Content present in rendered output, unique titles and descriptions that match each page's intent, canonical, robots and noindex agreeing, structured data matching visible content, redirects, representation in sample searches and AI answers | Raw and rendered output, crawl results, validator output, dated query snapshots |
| Performance | Asset and script behavior, layout shift, loading | Measured conditions on a representative device and network |

## Interface copy in conversion journeys
Use this when the journey contains forms, validation or confirmations.
- Compare the exact wording with validation rules, actual submission states and supported next actions.
- Preserve qualifications when shortening text.
- Check terminology across the journey.
- Distinguish no matches from no content or restricted access.
- Flag invented delivery promises, failure causes or recovery times.
- Inspect visible labels, accessible names and error context together.
- Localized journeys: check representative expanded text and count and date formats.
- Report consequential confusion with evidence. Do not treat preferred phrasing as a defect.

## Important distinctions
Use these before stating a conclusion about proof.
- A call-to-action click is not a lead. A displayed thank-you is not proof of receipt.
- A prototype's simulated states are not production integration evidence.
- An automated accessibility pass is not a complete accessibility evaluation.
- A synthetic performance result is not field performance.
- Reviewer comprehension is not a completed customer usability study.
- A polished design is not measured conversion improvement.
- An old test pass does not automatically cover a changed candidate.
- A search or AI-assistant result is a dated snapshot, not a measurement of ranking, citation or traffic.
- Valid structured data is not proof of eligibility or ranking.
- A new site's absence from results is not a defect. Absence of indexing after the owner-agreed or provider-documented window is. If neither exists, report indexing as unknown.

## Execute meaningful journeys
Entry and forms:
- Start from plausible search, campaign or referral entry pages as well as the homepage. Follow the buyer's path to fit assessment, supporting proof and action.
- For important forms, inspect exact labels and validation, invalid input, the success state and an appropriate failure and recovery path.
- Verify that the next action promised in each state exists.

Findability:
- Fetch raw and rendered output for the representative pages.
- Check that each page answers its intended query.
- Check that crawler rules match the owner's recorded decision. If none is recorded, report that as a gap.
- Where the brief names target queries or questions, record dated snapshots of search results and AI-assistant answers. Do not infer ranking or influence from them.
- If no AI assistant can be queried, report the result as unknown. Never record an answer you did not observe. Your own reply is not an observation.

Real effects:
- Separate a safe UI exercise from a real downstream transaction.
- Confirm authorization and the test destination before sending a message or causing another external effect.
- If receipt cannot be checked, report that boundary as unverified.
- Never complete a checklist by triggering a purchase or an unauthorized enquiry.

Responsive:
- Review the mobile journey and composition first. Then review intermediate and desktop layouts with equal care.
- Check supported viewport sizes and actual breakpoints.
- Include keyboard operation, clear focus, navigation state, form errors, long content, and images and fonts as relevant.
- Check that mobile crops preserve image meaning, sticky elements do not obstruct actions, and input stays usable with the onscreen keyboard where device tools permit.
- Inspect screenshots directly. Recording them without examination is not visual review.

Visual readiness:
- Evaluate it separately from functional readiness.
- Compare actual pages with the recorded art direction and visual benchmarks. Cover the opening impression, secondary sections, detail pages, image-family consistency and small-screen craft.
- Generic placeholder art or a visually unfinished page remains an open design finding even when its links and forms work.
- Do not certify a site as visually stunning solely from instruction compliance or a numeric score. Demonstrate the result and its limits through inspected evidence.

## Record concise findings
- Reconstructable: candidate, route and state, environment and viewport, expectation, observation, consequence and severity, evidence, correction, and retest result when available.
- Grouping: group systemic issues with affected examples. Do not repeat one defect per page.
- Evidence: link inspected screenshots and logs.
- Preference: distinguish a design preference from an evidenced loss of meaning, usability or fidelity to the agreed direction.
- Repairs: after an in-scope repair, repeat affected checks and the downstream journeys the change could influence.

Report two judgments with their scope:
- Readiness: ready, needs changes, or not yet determinable.
- Verification: complete, or incomplete with named gaps.

These are independent. Explicit acceptance of a limitation does not erase the finding, and technical readiness does not confer publication authority.
