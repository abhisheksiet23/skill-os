# Review findability

Use this for the findability part of a review. Compare like with like, label what is observed, and report limits.

## Terms
- **Like with like:** the same source, date-range length, query set and assistants as the baseline.
- **Confidence label:** observed, likely or unknown.

## Prepare
- Baseline: retrieve it. If absent, capture one now and report that earlier change cannot be attributed.
- Known changes: list site releases, content changes, campaigns and migrations since the baseline.
- Method: use the same sources, date-range length and query set as the baseline.

## Search evidence
- Indexing: compare indexed pages with intended pages. Review errors and excluded pages with their reasons, sitemap status, and whether new important pages are indexed.
- Performance: review impressions, clicks, average position and queries from search console where available. Average position is volatile. Separate branded from non-branded queries. Search console does not report every query.
- Landing pages: check which pages receive search entries and whether they match the intended query.
- Regressions: look for blocking rules, noindex, canonical errors, redirect faults, rendering faults or crawler rules that differ from the owner's recorded decision, shipped by a release.

## AI-answer evidence
- Snapshots: repeat the baseline's questions with the same assistants. Record the date, the exact question, whether the company is named, how it is described, whether the description is accurate and which sources are cited.
- Unavailable: If no AI assistant can be queried, report the result as unknown. Never record an answer you did not observe. Your own reply is not an observation.
- Variation: results vary between runs, users and regions. Run each question more than once where the assistant allows, and report the variation.
- Referrals: identify visits referred by AI assistants where analytics shows a referrer. Some are unlabeled, so the count is a floor.
- Accuracy: where an assistant states something wrong or outdated, trace the source, whether the company's own site, a directory or a third party. Recommend the correction at that source.
- Presence: check that directories, profiles and reviews agree with the site.

## Interpret change
- Attribution: needs a baseline. Consider season, campaigns, site changes and volume. A short window is noise.
- Wording: "no change detected" is not "no effect".
- Confidence: label each finding observed, likely or unknown.
- Promises: report no rankings, citations or traffic as achieved or expected.

## Recommend
Order recommendations by consequence.
1. Technical regressions that block or misdirect crawlers.
2. A page that does not match its intended query.
3. Inaccurate third-party descriptions, corrected at their source.
4. Content gaps. Record them as later content work.

Separate reversible changes from consequential ones, and say which need owner authority.

## Limits
- Tools unavailable: the check is unverified, not failed.
- Search console omits some queries. Analytics undercounts visitors who decline tracking.
- Search features and crawler behavior change. Check current official documentation before relying on remembered rules.
- AI-answer snapshots show how a question was answered at one time, not what any user will see.
