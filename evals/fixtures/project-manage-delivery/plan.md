# Purpose and delegation

Deliver a local receipt amount helper ready for owner demonstration. Exact signed
decimal input with at most two fractional digits must convert to integer cents.
Examples: 0.29 -> 29; -0.29 -> -29; 1.20 -> 120; 12 -> 1200.
Reject empty, malformed, non-finite and more-than-two-decimal inputs rather than
silently round them. Existing observed defect: 0.29 returns 28 in current code.

Owner priority: correct monetary conversion before optional help-text polish.
Technical readiness requires meaningful executed checks including the defect.
Owner product acceptance follows demonstration and has not been granted. The
agent may implement, test and sequence reversible local work without approval.
No permission for external actions or new spending is implied.

Near-term effort estimates before investigation were 15–30 minutes implementation
and 10–20 minutes checks; these are provisional planning assumptions, not observed
durations. Estimate/reconcile remaining work from actual findings. No confirmed
owner demonstration window exists. Do not invent product acceptance timing.
