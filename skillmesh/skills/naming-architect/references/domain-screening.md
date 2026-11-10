# Domain screening
Use for the default shortlist screening of a new standalone public brand, company or product unless the brief establishes an existing-domain home or excludes research. Also use whenever the user requests a domain check. A public feature hosted under an existing product/domain does not automatically need one. Screen the actual shortlist before recommending; do not defer the check to the user when read-only lookup tools are available. Recheck finalists before registration.

The outcome is an evidence-backed registration status for exact domains, not legal clearance or a purchase. Preserve the distinction between a strong creative candidate and one that satisfies a verified domain requirement.

1. **Agree on domain strategy.** Default to `.com` for broadly marketed commercial brands; also consider target-market and category TLDs (`.in`, `.co`, `.io`, `.dev`, etc.) where appropriate. Ask about geographic markets and preferred TLD only if the answer would change the recommendation. Note that some TLDs have eligibility or use restrictions.
2. **Normalize each candidate.** Check the exact spelling without spaces, plus only sensible variants (for example `getNAME.com`, `tryNAME.com`, or `NAMEqa.com`). Avoid silently substituting a hyphenated or misspelled address for an exact match.
3. **Verify registration status.** Prefer a live registrar's availability result or authoritative registry RDAP lookup, with the exact queried domain and timestamp. Registered means unavailable for ordinary new registration, even if there is no live website. A domain lacking RDAP records is **not automatically available**: confirm via registrar/registry because of reserved, premium, blocked, and lookup-error cases. Distinguish **available to register**, **registered**, **listed for resale** (still registered), **reserved/restricted**, and **unknown/unverified**. Classify explicit registered/reserved evidence before interpreting wording such as "available for sale". If one source fails, try another suitable accessible route. Only fall back to lookup links or user-executable instructions after actual access limits prevent checking; record the failure and label affected domains **unknown**. Use **not checked** only when no query was made, explaining why. Never infer availability from search results, DNS failures, HTTP errors, or parked pages.
4. **Check practical usability.** Look for spelling ambiguity, accidental word joins, confusing hyphens/digits, misheard pronunciations, close lookalike domains, and potentially misleading associations. Domain availability is separate from trademark rights and company-name conflicts.
5. **Record evidence.** For each checked domain capture: exact FQDN, TLD, status, evidence source, checked-at date/time (and time zone), potential premium/resale cost if verified, and notes. Pricing changes; do not fabricate fees. Recheck before purchase.
6. **Apply a domain decision gate.** Mark `.com` availability as a **preference by default**, not a universal veto. If the brief explicitly requires an exact `.com`, treat its verified unavailability as a hard gate. Otherwise explain tradeoffs and consider a strong name with an appropriate alternative TLD. Never call a domain secured until the user has registered or acquired it.

**Domain status reporting template:**

| Candidate | Exact `.com` | Best alternative | Evidence / checked at | Domain concern |
|---|---|---|---|---|
| ExampleName | Not checked | Not checked | No live lookup performed | Verification required |

Never present placeholder or simulated statuses as real findings. Keep registration evidence separate from creative judgment; do not let unknown availability masquerade as a failed naming criterion.

## Live lookup without a dedicated domain plugin

Use an existing registrar integration or a registrar's interactive search when available. Otherwise, retrieve the [IANA DNS RDAP bootstrap](https://data.iana.org/rdap/dns.json), find the queried TLD's listed service, and request `<service-base>/domain/<exact-domain>` through an available HTTP tool or browser. Do not send every TLD to one hardcoded registry. For example, a `.com` registry lookup is `https://rdap.verisign.com/com/v1/domain/<exact-domain>`. A web search can find an official service; its snippets do not establish current registration status.

Interpret the response body as well as transport status:

- A successful RDAP domain object matching the requested FQDN establishes **registered**. Do not expose registrant contact details in the naming report.
- An authoritative not-found response means **no registration record found; registrability unconfirmed**. Confirm with a live registrar or registry availability result before reporting **available to register**. If confirmation is inaccessible, keep it **unknown**.
- An unsupported TLD, invalid response, access denial, timeout, rate limit or tool error means **unknown**. It is neither registered nor available evidence. Avoid repeated retries against a blocked source.
- If registrar and registry evidence disagree, report the disagreement and keep availability **unknown** until resolved. A verified resale listing is an acquisition option, not ordinary registration availability.

## Finish or iterate

Show each finalist's exact queried domain, status, linked evidence and checked-at time. If all exact domains fail a hard requirement, say no candidate is verified to meet it, then offer a small new batch or explicitly labeled variants. Screen replacement finalists before treating them as qualifying recommendations. If none is verifiable, provide a provisional creative preference without claiming a qualifying winner. Do not quietly replace the required exact `.com` with another TLD or a modifier. Stop retrying when actual access limits prevent reliable evidence; record the attempted routes and failures rather than filling the gap with a guessed status.

