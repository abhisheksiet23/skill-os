# Review a real candidate

## Scope and severity

Tie review to a revision or immutable snapshot where possible. Choose representative routes and unusual content/interaction patterns, plus all business-critical journeys. A large site needs systematic sampling and critical-route coverage, not a claim that every page was visually inspected when it was not.

- Blocking: materially false central claims, a broken primary journey, exposed secrets/private data, or another defect that defeats safe intended use.
- Material: meaningfully damages comprehension, fit assessment, trust, access, or responsiveness.
- Polish: localized craft issue without material loss of function or meaning.

Explain consequence and scope. Do not equate personal stylistic preference with a defect. Record unresolved material issues and any explicit owner's acceptance of a limitation; acceptance does not turn a failed test into a pass.

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

Start at plausible entry pages, not just the homepage. Check how visitors assess fit, find supporting detail, and progress. Include invalid input and an appropriate failure/recovery path for important forms. Confirm test-message authorization and destination before sending. Do not trigger purchases, messages, or other external effects merely to complete a checklist.

Review the mobile journey and composition first, then intermediate and desktop layouts with equal care. Check supported viewport sizes and actual breakpoints. Include keyboard operation, clear focus, navigation state, form errors, long content, and images/fonts as relevant. Check that mobile crops preserve image meaning, sticky elements do not obstruct actions, and input remains usable with the onscreen keyboard where device tools permit. Inspect screenshots directly; recording them without examination is not visual review.

Evaluate visual readiness separately from functional readiness. Compare actual pages with the recorded art direction and visual benchmarks, including the opening impression, secondary sections, detail pages, image-family consistency, and small-screen craft. Generic placeholder art or a visually unfinished page remains an open design finding even when its links and forms work. Do not certify a site as visually stunning solely from instruction compliance or a numeric score; demonstrate the result and any limits through inspected evidence.

## Record concise findings

Use: candidate; route/state; environment/viewport; expected; observed; consequence/severity; evidence; fix; retest. Group identical systemic issues under one finding with affected examples. Link screenshots/logs rather than dumping them into the report.

After repair, repeat affected checks and any downstream journey the change could influence. Report readiness and verification separately: readiness is ready within stated scope, needs changes, or not yet determinable; verification is complete within stated scope or incomplete with named gaps. A candidate can both need changes and have incomplete verification. State exactly what each judgment covers. Remaining external authorization is separate from technical readiness.
