# Microcopy evaluation scenarios

Run each scenario independently against frozen baseline and candidate skill folders, using comparable models and tools. Give the task performer the selected scenario, repository instructions and assigned skill variant; keep the [assessment key](microcopy-assessment.md) separate. For a scenario with product variants, supply its shared handoff and one variant per fresh context. Save actual responses before assessing them. These are synthetic product examples; no live payments, account changes, messages or service access are needed.

Use app-prototype for drafting and app-qa or website-review for review when testing those skills directly. The processing scenario names app-frontend explicitly. Repeat suitable scenarios through website skills when their guidance changes. These are instruction-application checks, not a benchmark of automatic skill selection. Paired product variants test whether a principle transfers while wording and action choices follow each product's evidence.

## A retail checkout that did not finish

We sell household supplies online. We need better copy for the checkout screen after a payment request times out. Please give us the message and action label we should use.

The current screen says “Payment failed. Try again.” and offers a Pay again button. Engineering's note says the browser stopped waiting before the provider returned a result; the provider can still complete the charge. The screen also has a payment-status action that looks up the existing attempt. No final charge result is available yet.

## Password help in a learning platform

Adult learners often register for our evening courses on their phones. This password help is hard to scan. Rewrite it for the existing form:

“At least 12 characters, including an uppercase letter, a lowercase letter, a number and a symbol.”

The validator checks all five requirements. We are changing the help text only, not the password policy or the form layout.

## Two empty lists with different meanings

Write the empty-state message and action for the supplied product. Keep the existing layout.

### Library catalogue

The library has books available, but none match the reader's current language and branch filters. The page says “No books yet. Add your first book.” Readers can change or clear filters; they cannot add books. Clear filters is an existing action. The catalogue gives factual, welcoming guidance to readers of different ages.

### Volunteer shift checklist

The volunteer has completed every task assigned for the current shift; completion is confirmed in the shift record. The page says “Nothing found. Clear filters.” No filters are active. Volunteers cannot create tasks. View upcoming shifts is available. The service acknowledges volunteers' contributions briefly without implying that all future work is finished.

## Before someone deletes a fitness account

Our fitness tracker stores exercise history. Write the confirmation dialog shown when someone selects Delete account, including the action labels. We want people to understand the choice without reading a policy page first.

The account policy says:

- Account access ends when deletion is confirmed.
- The person can request account recovery for 30 days afterward.
- Payment receipts remain under the existing receipt-retention policy; no specific retention duration is supplied here.

The current dialog says “Delete everything permanently?” with Yes and No buttons.

## An industrial monitoring outage

Review this proposed status banner for an equipment-monitoring dashboard and suggest a replacement using the incident information below:

“Monitoring will return in 15 minutes. All equipment is operating safely.”

The incident record says the monitoring service is unavailable. Cause and restoration time are still under investigation. Current equipment status cannot be established from this service. The communications lead would like the banner to sound reassuring. No alternative monitoring procedure is supplied in this handoff.

## A public-service application form

Review this handoff for a municipal permit-application form and tell us what needs changing and what still needs checking. You have the snippets and QA note below, but no running page or screenshot.

```html
<button aria-label="Submit">Send application</button>
```

After the API returns `202 Accepted` with `status: queued`, the form displays “Permit issued.” The product contract says staff must review the application before a permit can be issued. No staff receipt or review result is available.

QA note: “At the narrow mobile width, the German translation of the button label is cut off.” The actual viewport dimensions and translated string were not recorded.

## Museum tickets ready to download

Tidy up this panel in a museum's ticket-booking flow. Return one version with the text and link label; the current layout can stay.

“Your ticket generation request has been successfully processed by our system. To obtain your tickets, please click here.”

The ticket PDF has finished generating and its download URL is available. Opening that link downloads the tickets. It does not email them. No information about refunds or entry procedures is supplied.

## The same draft flow in two product voices

Make the three strings fit the supplied product and explain the writing choices briefly. This is a small correction; retain the existing flow. The main action saves a private draft. Publishing is a separate action. The validation rule allows the same start and end date, but rejects an end date before the start date.

Current strings: main action “Submit”; confirmation “Successfully processed”; validation “Invalid end date.”

### Trail-club route planner

Members draft routes before sharing them with the club. The product calls these Routes. Approved copy elsewhere includes “Where will your next adventure take you?” and “Route added. Time to explore.” Members enjoy the sense of discovery but want to check dates before publishing. No new voice guide is needed.

### Laboratory inspection planner

Staff draft inspection records before publishing them to the facility schedule. The product calls these Inspection records. Approved copy elsewhere includes “Inspection record saved” and “Review required before publication.” Staff use this terminology daily and need to distinguish drafts from published records. No new voice guide is needed.

## A file that is still processing

Use app-frontend to give a targeted change plan for the supplied product, including representative strings and acceptance checks. Keep the current components and layout.

Both products use this processing contract:

```text
POST /processing-jobs -> 202 { jobId }
GET /processing-jobs/{jobId} -> { status: queued | working | ready | failed }
previewUrl is present only when status is ready.
```

An existing job-status component owns polling. The screen already has associated labels and a live status region. Failed-request recovery and retry safety are not specified in the supplied contract. Sending or publishing requires a separate action after processing; neither happens automatically.

Only this handoff is available; there is no runnable application. Distinguish the plan's assertions from executed application checks.

### Language-learning audio practice

The learner uploads a practice recording. The handler posts a processing request and immediately shows “Your teacher has received your recording.” Once processing finishes, the learner can preview it, then use the separate Send to teacher action. Existing terms are Practice recording and Preview. Copy elsewhere is patient and encouraging without promising learning results.

### Photography portfolio upload

The photographer uploads a photo. The handler posts a processing request and immediately shows “Your photo is live.” Once processing finishes, the photographer can preview it, then use the separate Publish photo action. Existing terms are Photo and Preview. The portfolio uses spare, understated copy.

## A music subscription cancellation dialog

Review this proposed music-streaming cancellation dialog before we ship it. Return findings and suggested corrections; do not redesign the cancellation flow.

> **Cancel your plan?**
>
> Don't let your playlists down. This is your last chance to keep Premium.
>
> **Keep my plan** / **Give up my benefits**

The policy says cancellation switches off renewal. Premium access continues through the paid-through date, and renewal can be restored before then. Playlists remain on the free plan. The actual date is supplied by the account record but is not included in this handoff. There is no separate last-chance deadline.

## Copy around an AI travel itinerary

Write the short introduction and action labels around an AI-generated itinerary. A traveller will review it before sharing it with companions.

The itinerary uses six confirmed bookings. It does not include current traffic or venue opening hours. The interface supports editing, regenerating and saving a draft. Sharing is a separate action with its own review step. The handoff does not say whether the current itinerary has been saved, and no measured accuracy rate is available. No new booking or reservation is made by generating the itinerary.
