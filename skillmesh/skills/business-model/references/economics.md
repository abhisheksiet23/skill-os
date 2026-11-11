# Transparent economics

Use this reference to expose the constraints behind a viability recommendation. Select the calculations the decision needs; a complete finance model is not a prerequisite.

## Unit contribution and break-even

Define units and time periods before calculating. For a service, start with engagements times realized revenue per engagement, delivery hours times loaded hourly cost, other variable costs, acquisition/sales cost and fixed operating expense. Include onboarding, review, support and retesting in delivery effort when they occur. Show founder labor both as a cash outlay where paid and as an economic cost; do not silently subtract it twice.

Define contribution explicitly. Contribution before acquisition and contribution after acquisition answer different questions. Operating surplus also subtracts fixed costs; cash flow additionally depends on collection/payment timing, capital outlay and other cash obligations. Do not label revenue or gross margin as profit.

For stable positive contribution per unit, fixed operating costs divided by contribution after acquisition gives an approximate operating break-even volume. State the assumptions: mix, acquisition allocation and capacity costs must stay valid over that range. A step increase in staffing or equipment changes the calculation.

## Locate the binding constraint with a threshold

Compare demand, profitable delivery capacity and cash-funded throughput in the same period. The smallest feasible bound constrains the plan; an average margin alone does not identify it. Calculate the threshold that changes the recommendation and the intervention that could move it. Acquisition alone cannot achieve break-even if maximum feasible throughput stays below that threshold. It can still improve contribution and reduce losses within unused capacity: assess incremental acquisition/delivery cost, cash and opportunity cost before recommending or rejecting it. Do not present loss reduction as a viable steady-state business.

Illustrative service: realized revenue 1,000 per engagement; variable delivery 400; acquisition 100; monthly fixed cash cost 6,000. Contribution after acquisition is 500, so operating break-even is 12 engagements. If each takes 10 delivery hours and the relevant role has 100 productive hours, capacity is 10 engagements and operating loss at capacity is 1,000. Moving from six to ten engagements reduces loss from 3,000 to 1,000 under those same assumptions, but more leads cannot remove the remaining capacity-bound loss. Holding other inputs fixed, break-even at 10 engagements needs realized price 1,100, or variable cost 300; alternatively 12 engagements need 120 productive hours, whose incremental staffing cost must be included. These are alternative conditional thresholds, not simultaneous improvements.

Independently reconcile the decisive result: at capacity, revenue 10,000 minus delivery 4,000 minus acquisition 1,000 minus fixed 6,000 equals -1,000. A second calculation of `(10 * 500) - 6,000` should agree. A copied formula or repeated rounded subtotal is not an independent check. Use executable arithmetic when available; inspect units and allocations as well as totals.

Profitability and cash can give different answers. For the cash illustration, use the feasible ten-engagement alternative at a realized price of 1,100, assuming buyers accept it; retain 100 productive hours and the same listed costs. Revenue is 11,000 and delivery/acquisition/fixed costs total 11,000, so this alternative breaks even economically. If delivery and payments occur in month one but collection occurs in month two, month-one funding need is 11,000 before deposits or starting cash. No added capacity or unpriced staffing is assumed. Compare the cash trough with committed cash, not expected future sales. Change collection timing, not revenue recognition, to test a deposit policy; the new price remains a scenario, not demonstrated willingness to pay.

## Capacity and cash for the actual mix

For mixed offers, calculate each offer's contribution and delivery hours, then weight by the mix. Required delivery hours divided by productive hours per person gives capacity needed under that utilization assumption. Apply utilization once: productive hours already exclude unavailable time. Check bottlenecks by role where work is not interchangeable. A revenue target may need more people than a naive total-hours division suggests.

Place collections and payments in the periods when they occur. Deposits, payment delays, refunds, inventory and capital purchases can make a profitable offer unfundable. Calculate the cash trough and funding requirement under a coherent ramp scenario; distinguish committed financing from an assumed future raise.

## Recurring revenue and uncertainty

For subscription/usage products, separate acquisition, activation, retention, expansion, infrastructure and support. Keep customer retention and revenue retention distinct, and compare cohorts at comparable ages. Avoid long-run lifetime-value claims from an immature cohort or assumed churn. State payback assumptions and how churn/concentration could invalidate them; prefer observed cumulative contribution over an unsupported lifetime projection.

Check break-even and sensitivity to the most uncertain drivers: realized price, delivery effort, utilization, repeat rate, acquisition cost and payment delay. Negative unit contribution cannot be fixed by volume without a credible change in economics.

Keep a compact input/formula/result table or executable model. Put units, periods, assumptions and evidence status beside the inputs; calculate the decision-sensitive drivers first. Independently check arithmetic without recreating an unchanged model. Avoid arbitrary precision, hidden plug values and invented growth. When data is missing, show the conditional scenario and the observation that would narrow it.
