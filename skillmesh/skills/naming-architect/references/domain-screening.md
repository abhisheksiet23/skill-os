# Domain screening
Use when a standalone name needs a separate domain or the user requests a check. A public feature hosted under an existing product/domain does not automatically need one. Screen promising candidates, then recheck finalists before a decision.

1. **Agree on domain strategy.** Default to `.com` for broadly marketed commercial brands; also consider target-market and category TLDs (`.in`, `.co`, `.io`, `.dev`, etc.) where appropriate. Ask about geographic markets and preferred TLD only if the answer would change the recommendation. Note that some TLDs have eligibility or use restrictions.
2. **Normalize each candidate.** Check the exact spelling without spaces, plus only sensible variants (for example `getNAME.com`, `tryNAME.com`, or `NAMEqa.com`). Avoid silently substituting a hyphenated or misspelled address for an exact match.
3. **Verify registration status.** Prefer a live registrar's availability result or authoritative registry RDAP lookup, with the exact queried domain and timestamp. Registered means unavailable for ordinary new registration, even if there is no live website. A domain lacking RDAP records is **not automatically available**: confirm via registrar/registry because of reserved, premium, blocked, and lookup-error cases. Distinguish **available to register**, **registered**, **listed for resale**, **reserved/restricted**, and **unknown/unverified**. If no live registration tool is accessible, explicitly label all statuses **not checked** and provide registrar/registry lookup links or user-executable instructions; never infer availability from search results, DNS failures, HTTP errors, or parked pages.
4. **Check practical usability.** Look for spelling ambiguity, accidental word joins, confusing hyphens/digits, misheard pronunciations, close lookalike domains, and potentially misleading associations. Domain availability is separate from trademark rights and company-name conflicts.
5. **Record evidence.** For each checked domain capture: exact FQDN, TLD, status, evidence source, checked-at date/time (and time zone), potential premium/resale cost if verified, and notes. Pricing changes; do not fabricate fees. Recheck before purchase.
6. **Apply a domain decision gate.** Mark `.com` availability as a **preference by default**, not a universal veto. If the brief explicitly requires an exact `.com`, treat its verified unavailability as a hard gate. Otherwise explain tradeoffs and consider a strong name with an appropriate alternative TLD. Never call a domain secured until the user has registered or acquired it.

**Domain status reporting template:**

| Candidate | Exact `.com` | Best alternative | Evidence / checked at | Domain concern |
|---|---|---|---|---|
| ExampleName | Not checked | Not checked | No live lookup performed | Verification required |

Never present placeholder or simulated statuses as real findings. Keep registration evidence separate from creative judgment; do not let unknown availability masquerade as a failed naming criterion.

