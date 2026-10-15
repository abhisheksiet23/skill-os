# Deliverable-quality matched tasks

Run each numbered case in a fresh context against the baseline snapshot and candidate snapshot. Give the evaluator only this file, the named fixture, repository-level instructions and the assigned skill variant. Keep model, tools and output request matched. Do not browse, contact people, deploy or infer authorization. Save verbatim outputs separately; these prompts do not contain scoring answers.

## 1. Opportunity and Strategy Canvas

Assess whether to pursue a release-testing service for small regulated-software teams. Produce the decision-useful result, including a Strategy Canvas only if useful.

Evidence: four target-team leads reported late regression surprises; two shared invoices showing 15–25% release rework. Three competitors advertise fixed-scope release checks, but no sales or profitability data is available. The founder believes “AI-first reporting” will differentiate the offer; no buyer mentioned AI. Competitor A advertises speed and a narrow checklist; B advertises regulated-domain expertise; C advertises low price. Comparable support depth is unknown. No buyer has committed or paid.

## 2. One product, two projects

Create a concise product decision and project plan from the facts below. Keep estimates honest and make the trade-off actionable.

The approved product decision is to promise a predictable, bounded release-readiness assessment without a defect-free guarantee. The app project adds evidence upload and a readiness summary: estimated 8–12 person-days, one engineer at 60% allocation, dependent on an unsettled retention rule. The website project updates the proposition and enquiry path: estimated 3–5 person-days, one designer/developer at 50%, dependent on approved proof and legal review. Work may overlap. Budgets and delivery dates have not been committed.

Follow-up: the owner now approves saying “fixed-scope assessment” but still does not approve public pricing. Update the result without losing the original guarantee decision or merging the projects' estimates.

## 3. Backend implementation and review

In a disposable copy of `fixtures/deliverable-quality/backend`, change `remaining_quota` so overuse returns zero rather than a negative number. The reporting consumer must still receive an integer. Implement, test and report the result. Then review the candidate: an unavailable external billing integration also consumes the value. Distinguish an observed regression from that unverified integration boundary.

## 4. Website experience and review

Review `fixtures/deliverable-quality/website/index.html` as a local candidate for the release-testing service described under “Opportunity and Strategy Canvas.” Inspect the actual page with browser tooling if available and report a prioritized, actionable outcome. Do not claim browser or delivery evidence you did not obtain. Do not modify the fixture.

## 5. Different product

After “One product, two projects,” assess this unrelated request: a neighborhood bakery wants a pre-order page for weekend bread. Known facts: pickup only, six products, quantities close Thursday, no customer interviews, budget and launch date unknown. Recommend the smallest useful next step. Do not import facts or decisions from earlier cases.

## 6. Restraint

Chat only: correct this sentence and return only the corrected sentence: “The checks was completed yesterday.”
