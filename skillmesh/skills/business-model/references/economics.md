# Transparent economics

Use this reference to expose the constraints behind a viability recommendation. Select the calculations the decision needs. A complete finance model is not a prerequisite.

## Unit contribution and break-even
Before calculating, define units and time periods.

For a service, start with these:
- engagements times realized revenue per engagement
- delivery hours times loaded hourly cost
- other variable costs
- acquisition and sales cost
- fixed operating expense

- Delivery effort: include onboarding, review, support and retesting when they occur.
- Founder labor: show it as a cash outlay where paid, and as an economic cost. Do not silently subtract it twice.

Define contribution explicitly. These measures answer different questions:

| Measure | What it covers |
| --- | --- |
| Contribution before acquisition | Contribution without acquisition cost deducted |
| Contribution after acquisition | Contribution with acquisition cost deducted |
| Operating surplus | Also subtracts fixed costs |
| Cash flow | Also depends on collection and payment timing, capital outlay and other cash obligations |

Do not label revenue or gross margin as profit.

When contribution per unit is stable and positive:
- Break-even volume: fixed operating costs divided by contribution after acquisition. The result is approximate.
- State the assumptions: mix, acquisition allocation and capacity costs must stay valid over that range.
- Step costs: a step increase in staffing or equipment changes the calculation.

## Locate the binding constraint with a threshold
Compare demand, profitable delivery capacity and cash-funded throughput in the same period.
- Bound: the smallest feasible one constrains the plan. An average margin alone does not identify it.
- Threshold: calculate the one that changes the recommendation, and the intervention that could move it.

When maximum feasible throughput is below the break-even volume:
- Acquisition alone cannot reach break-even.
- It can still improve contribution and reduce losses within unused capacity.
- Before recommending or rejecting it, assess incremental acquisition and delivery cost, cash and opportunity cost.
- Do not present loss reduction as a viable steady-state business.

### Illustrative service
Inputs: realized revenue 1,000 per engagement, variable delivery 400, acquisition 100, monthly fixed cash cost 6,000. Each engagement takes 10 delivery hours. The relevant role has 100 productive hours.
- Contribution after acquisition is 500, so operating break-even is 12 engagements.
- Capacity is 10 engagements. Operating loss at capacity is 1,000.
- Moving from six to ten engagements cuts the loss from 3,000 to 1,000 under the same assumptions.
- More leads cannot remove the remaining capacity-bound loss.

Each change below reaches break-even with other inputs fixed. They are alternative conditional thresholds, not simultaneous improvements.
- Realized price 1,100 at 10 engagements.
- Variable cost 300 at 10 engagements.
- 12 engagements with 120 productive hours, including the incremental staffing cost.

## Check the decisive result independently
- Reconcile: reach the result a second way. At capacity, 10,000 revenue - 4,000 delivery - 1,000 acquisition - 6,000 fixed = -1,000. `(10 * 500) - 6,000` should agree.
- Not independent: a copied formula or a repeated rounded subtotal.
- Tool: use executable arithmetic when available.
- Inspect: units and allocations as well as totals.
- Unchanged model: check its arithmetic without recreating it.

## Check cash separately from profit
Profitability and cash can give different answers.

Cash illustration. It uses the ten-engagement alternative at a realized price of 1,100, assuming buyers accept it. Productive hours stay 100 and other listed costs are unchanged. No added capacity or unpriced staffing is assumed.
- Revenue is 11,000. Delivery, acquisition and fixed costs total 11,000. It breaks even economically.
- If delivery and payments occur in month one and collection in month two, month-one funding need is 11,000 before deposits or starting cash.
- The new price remains a scenario, not demonstrated willingness to pay.

When checking cash:
- Timing: place collections and payments in the periods when they occur.
- Compare: set the cash trough against committed cash, not expected future sales.
- Deposit policy: test it by changing collection timing, not revenue recognition.
- Unfundable profit: deposits, payment delays, refunds, inventory and capital purchases can make a profitable offer unfundable.
- Funding: calculate the cash trough and funding requirement under a coherent ramp scenario.
- Financing: distinguish committed financing from an assumed future raise.

## Capacity for the actual mix
When offers are mixed:
- Per offer: calculate contribution and delivery hours, then weight by the mix.
- People needed: required delivery hours divided by productive hours per person, under that utilization assumption.
- Utilization: apply it once. Productive hours already exclude unavailable time.
- Bottlenecks: check by role where work is not interchangeable.
- Targets: a revenue target may need more people than dividing total hours suggests.

## Recurring revenue
For subscription or usage products:
- Separate: acquisition, activation, retention, expansion, infrastructure and support.
- Retention: keep customer retention and revenue retention distinct.
- Cohorts: compare them at comparable ages.
- Lifetime value: make no long-run claim from an immature cohort or assumed churn.
- Payback: state its assumptions, and how churn or concentration could invalidate them.
- Prefer observed cumulative contribution over an unsupported lifetime projection.

## Sensitivity and presentation
- Sensitivity: check break-even against the most uncertain drivers: realized price, delivery effort, utilization, repeat rate, acquisition cost and payment delay.
- Order: calculate the decision-sensitive drivers first.
- Negative unit contribution: volume cannot fix it without a credible change in economics.
- Working form: keep a compact input, formula and result table, or an executable model.
- Beside inputs: units, periods, assumptions and evidence status.
- Avoid arbitrary precision, hidden plug values and invented growth.
- Missing data: show the conditional scenario and the observation that would narrow it.
