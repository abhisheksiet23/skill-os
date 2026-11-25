# Implement a visitor journey and prove its boundaries

Read the sections relevant to the change.
- Use the site's actual acceptance criteria to select checks. A navigation correction does not need a fresh stack decision or an unrelated integration audit.
- For new sites, connect the choices below into one entry-to-action journey.

## Terms
- **Invariant:** what the representative journey established, recorded so its pattern can be reused.
- **Unverified:** evidence that is unavailable. It is not failed, and it is not passed by inference.

## Choose the simplest adequate foundation
- Inspect first: existing architecture and deployment constraints.
- Rendering: marketing content generally needs readable, crawlable output and reliable navigation. Choose rendering deliberately.
- CMS: add one when editing needs justify it, not automatically.
- Existing stack: preserve the user's stack and provider when suitable. Verify changing framework or provider specifics in current official documentation when needed.
- Editing: define which content the owner can edit, required asset sizes and how edits reach production.
- Services: do not add a database or service solely to store static content.
- Application behavior: if complex behavior emerges, identify its boundary and treat it as separate application work. Do not silently expand scope.

## Prove the risky seam before repeating pages
Select the risky seam, then implement one representative path across it using the real stack and available integration.
- A static visual sample cannot resolve an uncertain submission contract.
- A working API call cannot establish that the approved composition survives content.

| Risk exposed by the work | Representative proof before repetition | Preserve while implementing |
| --- | --- | --- |
| A polished prototype uses unusually short content. | Render a real long heading, proof qualification, list and image through the shared layout at narrow, intermediate and wide sizes. | Hierarchy, meaningful reading order, text measure and proximity of claim to qualification. |
| Owner edits could break the design. | Preview an ordinary content or asset replacement through the actual editing path. | Supported field lengths, optional content behavior, crops and alt text, and safe layout variation. |
| The enquiry UI depends on a provider. | Exercise available acceptance, failure and unknown states across the real boundary. Test authorized receipt separately. | Accurate state wording, retry behavior and supported operator destination. |
| A redesign changes route structure. | Follow one valuable old deep link through its proposed redirect to relevant content and action. | Search and referral intent, useful detail and destination query parameters where required. |

After the proof:
- Choose the row that addresses the actual uncertainty. Do not perform all of them by default.
- Record the invariant, then reuse its component and content pattern.
- Expand proof only for a genuinely different page purpose or boundary.
- If real content forces an approved design change, explain its buyer consequence and preserve existing design authority. Do not silently replace the visual direction with framework defaults.

## Content and routes
- Rendering: put each page's important text, headings and links in the HTML a crawler receives. Do not leave them only in client-side script. Check the raw and the rendered output.
- Metadata: use the titles and descriptions supplied with the copy. If none exist, write unique ones from each page's target queries.
- Page structure: one heading hierarchy, descriptive internal links and social previews. Place the supplied favicon set and share image.
- URLs: give each page one canonical URL. Handle URL variants such as trailing slash, case and parameters. Use correct status codes: 301 for moved, a real 404 for gone. Add hreflang only for real language or region variants.
- Sitemap and robots: list intended URLs only. robots.txt controls crawling, not indexing, and noindex works only on a crawlable page. A preview's indexing and blocking rules must not ship as production settings.
- Structured data: use it only for facts visible on the page and types the page qualifies for. Validate it with available tools.
- Markup limits: do not mark up reviews, FAQs or prices the page does not show. Valid markup does not guarantee display or ranking.
- Images: use descriptive file names and useful alternative text, and reserve dimensions.
- Local presence: where the business serves a location, keep its name, address and contact details consistent with its public profiles.
- Crawler policy: decide it with the owner and record the decision. Search crawling is normally wanted.
- AI access: access for AI answers and access for AI training are separate business decisions. Check each provider's current official documentation for crawler names and what each control does.
- AI-specific files: do not treat `llms.txt` or similar files as a requirement or a promised benefit.
- Redesigns: inventory existing paths and record preserve, replace or redirect decisions.
- Redirects: test them against relevant destinations. Do not redirect every removed page to the homepage.
- Removed pages: do not remove useful pages merely because analytics are unavailable. Check 404 behavior and campaign links when relevant.
- Do not create speculative location pages, fake addresses or repetitive keyword pages.
- Privacy: keep public content and private strategy or research artifacts separate in the build output. Inspect the deployable output when the source repository contains private material.

## Forms and integrations
Before wiring a form:
- Identify the destination and responsible operator.
- Determine the smallest useful field set, qualification and routing rules, privacy wording and submission mechanism.
- Define what each visible state means: invalid input, sending, provider accepted, confirmed receipt, or failed or unknown outcome. Show only states the integration can establish.
- Confirm any response-time promise with the business. Avoid unnecessary personal-data collection.

Copy:
- Follow project terminology and approved copy.
- Include consequential strings and state conditions in acceptance checks. Labels match actual actions. Shortening preserves validation rules, costs, commitment and supported recovery.

Security and abuse:
- Validate at the trust boundary and use appropriate abuse protection.
- Handle invalid input, unavailable service, retries and repeated submissions.
- Do not embed private service keys in browser code. Do not log sensitive form values unnecessarily.
- Use approved test recipients or sandbox destinations for delivery tests. Actual messages to people require authorization.
- Email: if the form sends mail from the business domain, check SPF, DKIM and DMARC for the sending service. Test with authorized recipients that messages reach the inbox, not spam.

Testing:
- Test UI behavior, provider acceptance and downstream receipt as separate boundaries.
- Include invalid input, a service failure and the supported retry path. Check repeated submissions where they could duplicate enquiries.
- A mock can demonstrate UI states but cannot establish live delivery. Use an authorized destination for real receipt checks.

Untestable boundary:
- Name the exact missing proof and its visitor consequence.
- Explicit owner acceptance may permit launch of a real integration that could not be tested. It does not turn the gap into verified delivery.
- A simulated primary form never ships. Implement and test an honest contact route instead.

## Responsive and accessible behavior
Mobile first:
- Establish the small-screen reading order, navigation, type scale, artwork crop and form flow as the base. Enhance the layout at content-driven breakpoints.
- Avoid hover-only access, desktop-sized downloads on small screens, and fixed elements that obstruct the mobile keyboard or primary action.
- Keep desktop deliberately composed, not merely stretched.
- Viewports: choose test sizes from the supported audience and the actual layout. 360, 390, 768 and 1440 CSS pixels are example starting samples, not a complete device coverage claim.

Accessibility:
- Use semantic landmarks, purposeful heading structure, descriptive link and button text, visible focus, keyboard operation, appropriate contrast, useful alternatives for meaningful images, and decorative-image treatment.
- Forms need associated labels, understandable errors and a clear recovery path.
- Check menus, dialogs, focus movement, zoom and reflow, touch interactions and reduced motion as relevant.

Inspection:
- Inspect narrow, intermediate and wide layouts at recorded viewport sizes chosen to exercise actual breakpoints.
- Test long content and image loading where they expose real risks.
- Do not claim accessibility certification from an automated scan or a few manual checks.

## Performance and measurement
- Control: image dimensions and formats, fonts, script weight, third-party embeds and avoidable layout shifts.
- Measurement: measure a representative candidate under recorded conditions. Explain the limits of synthetic results. Do not promise a universal score or field performance without field evidence.
- Images: use responsive sources and purposeful crops. Preserve visual quality while controlling transfer size. Do not lazy-load the main above-the-fold image by default.
- Constraints: check the site with representative mobile network and CPU constraints and reduced motion as tools permit. Record conditions and simulation limits. Visual ambition must work on mobile hardware and connections, not only a powerful desktop.
- Conversion events: define them around meaningful milestones. Distinguish call-to-action clicks, attempted submissions, accepted submissions and qualified outcomes where measurable. Avoid collecting form contents or unnecessary identifiers.
- Tracking and consent: determine requirements from the actual project context and current applicable guidance.
- Consent: where consent is required, do not load non-essential tracking before it. Verify the real requests and cookies on first load.
- Privacy notice: it must name the tools actually used.
- Obligations: identify the accessibility and privacy rules that apply to the audience's region. State what needs specialist or legal review. Do not invent jurisdictional compliance claims or claim compliance.

## Choose acceptance evidence
- Binding: tie results to the candidate and the conditions that matter: routes and states, viewport sizes, integration environment and measurement conditions.
- Reuse: keep valid existing proof. After a change, repeat affected checks and the downstream behavior it could influence.
- Gaps: report unavailable evidence as unverified.

Examples of observable outcomes, not a mandatory complete test plan:
- An intended buyer arriving on a service page can identify scope, fit, evidence and the appropriate next step.
- The primary enquiry journey validates input, recovers from service failure and reaches its intended test destination when authorized.
- Important old URLs remain useful through preserved content or tested relevant redirects.
- Representative pages retain reading order, usable navigation and legible composition on narrow and wide screens.

Adapt these to the project. Do not manufacture irrelevant tests or treat this list as the entire acceptance contract.
