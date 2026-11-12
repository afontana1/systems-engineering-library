# Engineering economics: lifecycle costs, options, and organizational value

*Core Concepts · Enterprise & complexity · T20*

> Turn architecture choices into transparent cost, discounting, and option-value arguments.

**Recommended preparation:** [10 Decisions](10-decisions.md), [12 Enterprises](12-enterprises.md)

**Related companion books:** [Book 2](../B2/OPEN-BOOK.html), [Book 6](../B6/OPEN-BOOK.html), [Book 19](../B19/OPEN-BOOK.html)

## 1. The cheapest proposal is not always the least costly system
Systems engineering choices create costs beyond acquisition: integration, training, operation, maintenance, software updates, disposal, transition, and failure response. A comparison that considers only supplier purchase price may select a system that is expensive to own or cannot be sustained. Define the analysis period and the operating concept before calculating a lifecycle cost.

For Northstar, a low-cost fleet may require expensive charging infrastructure, specialized technicians, and more frequent battery replacement. A software-intensive alternative may reduce hardware cost but create ongoing cloud services and cybersecurity assurance obligations. Costs should be attributed to the *system alternative*, not hidden in another agency's budget.

## 2. Use time value of money with explicit conventions
If a future cost $C_t$ occurs at time $t$ and the real discount rate is $r$, its present value is

\[
PV(C_t)=\frac{C_t}{(1+r)^t}.
\]

For an acquisition cost of $1{,}000$ now and annual operating cost of $200$ at each of the next three year-ends, the present cost at a 5% annual real rate is

\[
LCC=1000+\frac{200}{1.05}+\frac{200}{1.05^2}+\frac{200}{1.05^3}\approx 1544.65.
\]

Real versus nominal discounting must match how the cash flows are expressed. Don't use a real rate with nominal costs that already include inflation. A project justification also needs an agreed perspective: municipal budget cost, social cost, or supplier cost can lead to different rankings.

## 3. Compare alternatives over a common service basis
Option A costs less initially but covers 70% of eligible requests; B costs more but covers 95%. Dividing acquisition price by one vehicle is not an equitable service comparison. Normalize per relevant mission outcome—such as cost per completed eligible trip—while retaining the failure and equity criteria as hard requirements. The ratio can become misleading if it encourages minimizing service to difficult users, so pair it with minimum coverage rules.

Use a common horizon and treatment of residual value. Include uncertainty in energy cost, utilization, staff needs, and obsolescence. If future demand grows, a design's expansion flexibility may be an engineering option worth analyzing rather than an unpriced marketing claim.

## 4. Understand value of information and flexibility
Suppose the authority can commit now to a large fleet or pay for a limited pilot before deciding. The pilot incurs cost and delays scale-up, but it may reveal actual demand and avoid an expensive wrong commitment. This is an option: pay a smaller amount to preserve the ability to choose after learning. The maximum rational price for information is bounded by how much it can improve the decision under the modeled probabilities and utilities.

A pilot has **no decision value** if its possible observations will not change the selected investment. It may still be useful for safety or regulatory evidence, but that is a different justification. If a pilot could cross a decision threshold, compare expected value of acting with and without it, subtracting pilot cost and consequences of delay.

## 5. Worked illustration: operating cost changes the ranking
Assume two candidates for three years at 5% real discount rate:

| Candidate | Acquisition | Annual operating cost |
|---|---:|---:|
| A | 1,000 | 200 |
| B | 1,200 | 110 |

The three-year annuity factor is $[1-(1.05)^{-3}]/0.05\approx2.72325$. Thus A costs about $1,544.65$ present-value units, while B costs about $1,499.56$. B is cheaper on the stated lifecycle measure despite being more expensive to acquire. That ranking may reverse if B requires unexpected equipment renewal or if its annual service performance is worse. This is why every cost result needs sensitivity analysis and a service definition.

## 6. Treat uncertainty and distribution honestly
A public system distributes benefits and burdens across groups. One agency's savings can shift costs to another, and an average net benefit can hide severe consequences for particular communities. Create separate budget, operational, environmental, and distributional ledgers rather than collapsing everything into a single unsupported monetary score.

Estimate ranges and decision thresholds. At what annual operating cost would B cease to have a cost advantage? At 5% for three years, the difference in acquisition is 200 units; B can bear at most about $200/2.72325\approx73.44$ units less per year than A before lifecycle costs tie. Here B saves 90 units/year, so it remains cheaper under the baseline assumptions. If that saving falls below 73.44, the ranking reverses.

## 7. From calculation to accountable enterprise choice
A cost estimate is a model of organizational commitments. An economic review should record sources, quantities, unit costs, rate conventions, forecast dates, discount rate, exclusions, scenario assumptions, and sensitivity boundaries. The board must also decide which nonfinancial criteria are constraints: safety obligations, service accessibility, privacy, and continuity of essential operations.

Avoid treating the number of significant digits as evidence of certainty. A spreadsheet that reports $1,499.56 may be less informative than a defensible interval from $1,350 to $1,900 together with an explicit threshold that would reverse the investment.

## Problems
**A.** Derive the three-year present values for A and B. **B.** Calculate the annual operating-cost saving required for B to break even. **C.** Give an example where the cheapest lifecycle option is still unacceptable.

<details><summary>Answer guidance</summary>

A costs approximately $1,544.65; B approximately $1,499.56 at the declared real rate and year-end timing. The break-even operating saving is about $73.44 per year. A candidate can have the lowest cost and still fail safety, access, service-coverage, or other hard requirements.

</details>

## Further connections
[Decision methods](10-decisions.md), [enterprise governance](12-enterprises.md), and [robust optimization](18-robust-optimization.md) explain why economic ranking must remain linked to mission outcomes and constraints.

## Guided laboratory

[Open the corresponding case-based lab](labs/20-lifecycle-economics-workshop.md)


<!-- STEP04-T1-START -->

## Step 04 T1 — Evidence-driven correction and worked transfer

### T1 audit finding: preserve the financial convention and the hard gates

For three annual **year-end** costs, the real discount factor at 5% is \(F=\sum_{t=1}^3(1.05)^{-t}=2.723248\). The worked options have \(PV_A=1000+200F\approx1544.65\) cost units and \(PV_B=1200+110F\approx1499.56\). The higher initial cost of B is offset by its 90-unit annual operating saving. B breaks even if its saving is at least \((1200-1000)/F\approx73.44\) cost units per year. Calling this a probability of B's affordability would be a category error.

Now connect the cost rank to T1's fleet feasibility. A nominally least-cost architecture remains inadmissible if its stressed service falls below ten requests/hour or its hourly energy budget violates a requirement. Also distinguish the public agency's cash-flow ledger from societal or subgroup costs: a saving created by leaving accessible requests pending is not automatically a net social benefit.

**Practice and explained solution.** If B's annual operating cost increases from 110 to 135, its saving relative to A falls from 90 to 65, below the 73.44-unit break-even threshold. Then \(PV_B=1200+135F\approx1567.64\), greater than \(PV_A\). Show this sensitivity before offering an investment recommendation. [Reproduce the cost calculation](labs/T1-INTEGRATED-CASE.md).

<!-- STEP04-T1-END -->
