# Readable implementation

## Make consequential transitions explicit

For the affected interaction, identify the current state, triggering event, permitted action, visible result and recovery. Use the project's ordinary state representation; add no state-machine library merely to describe a few transitions. Inspect the cases that can change this journey, rather than adding every state to every component.

| Trigger | Decision to make explicit | Useful proof |
| --- | --- | --- |
| An older search returns after a newer search | Which response still owns the visible results? | Delay the older response; the newer query's results remain visible. |
| Submit is repeated or retried | Is this the same business action, and when may another action start? | Double activation and ambiguous timeout do not create a second accepted operation. |
| Navigate away/back during a write | Does work continue, cancel or need reconciliation? Which draft survives? | A late response cannot overwrite another record or falsely report cancellation. |
| Save conflicts, validation fails or the session expires | Which values are retained, what may be retried and where does focus move? | Recovery preserves permitted work and does not silently overwrite newer data. |

For example, disabling Save while a request is in flight improves feedback but does not establish server-side duplicate safety. Keep the operation identifier for a retry of an unknown result; replace it only for a genuinely new action under the contract. For a read-only search, ignoring an obsolete response may suffice; for a payment or reservation, ignoring its response does not cancel the accepted effect. Trace both visible state and the service outcome before choosing cancellation or retry behavior.

## Keep the implementation readable

Write for the next person reading the code. Prefer the simplest correct implementation that meets the actual requirements; fewer lines are not an optimization. Apply these choices while implementing and reviewing the changed code:

Use an explicit returning-reader standard: a developer returning to code after six years should be able to follow the business workflow without first decoding clever syntax, hidden conventions or framework machinery. Use modern features when they make the flow clearer; briefly explain necessary unfamiliar mechanisms where used. Avoid both line-by-line tutorial comments and unexplained tricks.

- Make logical blocks visually distinct with blank lines between reading form/state, guards, payload construction, retry decisions, API calls, success updates and failure/recovery handling when present. Keep cohesive assignments together rather than separating every statement. Expand branches, callbacks, calls and object literals into indented lines; do not compress guards, catch or finally bodies onto one line. In templates/JSX, expose element nesting, significant attributes, conditions and events on readable lines, with gaps between meaningful UI sections. Use descriptive names and intermediate values instead of packed expressions or nested ternaries. Follow the formatter but inspect the final source for breathing room; formatter success is not a spacing/readability pass.
- Keep rendering and event flow easy to trace. Use explicit branches for materially different UI states and named handlers for multi-step actions. Prefer straightforward derived values over synchronized duplicate state, unnecessary effects or custom hooks that hide simple local behavior.
- Keep components and functions focused on a coherent responsibility. Extract a component or helper when it gives a meaningful name to complexity, isolates behavior or serves actual reuse. Avoid both sprawling components and fragmentation into trivial wrappers, generic render engines or speculative configuration layers. Reuse established project abstractions when they fit.
- Start with straightforward algorithms and appropriate data structures. Add memoization, caching or other complexity only for a measured bottleneck or concrete performance constraint. Explain the reason locally when the extra machinery would otherwise be surprising; preserve accessibility, state correctness and required performance.
- Before finishing, read the changed code in execution order. Simplify code that requires mentally unpacking several operations, tracing unnecessary indirection or deciphering names. Comments explain intent or a non-obvious constraint; rewrite confusing code rather than narrating it. Keep this cleanup within the requested change.

Keep login, ticket/work-item flows, uploads and administration in coherent components or modules when combining them forces a reader to understand unrelated state. Choose boundaries by responsibility rather than line-count quotas. Prefer typed form/action state and named request/response contracts over generic bags, unexplained assertions or delimiter-encoded selections. Expand templates as well as application code: element nesting, conditions, event handlers and error states should be visible without mentally unpacking a long line. Move consequential template decisions into clearly named logic when it improves tracing, not into generic render/configuration engines.

For material work, trace one representative user action from template and handler through payload construction, API call and success/failure recovery. Show why request identifiers and version tokens are retained or replaced where retries matter. The reader should find the relevant state and steps without navigating a multipurpose component or a chain of trivial wrappers. Report the path reviewed and remaining comprehension obstacles separately from build/test results; owner readability remains unverified until they review it.
