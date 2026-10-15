# Selective microcopy guidance evaluation

Run the same requests against the pre-change and candidate skill folders in fresh, isolated sessions with comparable model and tools. Use app-prototype for drafting and app-qa or website-review for review. Give evaluators only the task and the relevant variant, not the assessment criteria below. Preserve actual responses before judging them. These fixtures do not require a live service or external side effects.

## Requests

1. Rewrite “Payment failed. Try again.” The payment request timed out; the provider may have charged the customer. A “Check payment status” action exists. Keep the message calm and brief.
2. Make this password instruction easier to scan without changing policy: “At least 12 characters, including an uppercase letter, a lowercase letter, a number and a symbol.”
3. Write an empty state for a populated project collection when active filters return zero matches. The user can clear filters but cannot create projects.
4. Draft account-deletion confirmation. Access ends immediately, recovery is possible for 30 days, and invoices are retained under the stated retention policy. Include action labels.
5. Review a service-outage screen saying “Back in 15 minutes. Your data is safe.” The incident record confirms only that the service is unavailable. Report findings and suggest supported wording.
6. Review a narrow localized form: the visible label says “Send request,” its accessible name says “Submit,” the confirmation says “Delivered” although only queue acceptance is known, and a translated button is clipped. Specify what can be concluded from this description and what needs execution.

## Assess observable outcomes

- Preserves uncertainty and avoids duplicate-payment advice; uses the available status action.
- Retains every password constraint.
- Describes filter results and offers clearing filters, without creation or completion claims.
- Preserves immediate access loss, recovery window and retention exception.
- Removes unsupported restoration and safety claims without inventing replacements.
- Identifies name/label mismatch, acceptance/delivery mismatch and clipping; does not claim browser or assistive-technology checks were executed.

Accept equivalent wording; do not grade literal matches, word counts or stylistic scores. Record omissions, unsupported claims, instruction overhead and correction burden. User comprehension and production task success remain unknown without user evidence.
