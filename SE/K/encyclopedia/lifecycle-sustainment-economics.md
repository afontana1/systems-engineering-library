# Life-cycle sustainment economics: cost after delivery is a design variable

**Canonical reference · Expanded reference · Internal editorial and worked-example checks; independent external peer review not performed**

## What the decision actually covers

**Life-cycle sustainment economics** compares alternatives by the resources needed to deliver useful service over a defined planning horizon—not by acquisition price alone. The decision boundary may include concept and design, acquisition, verification, deployment, preventive maintenance, corrective maintenance, spare parts, energy, technical-data rights, personnel training, periodic upgrades, operational downtime, and retirement. Cost categories and the economic boundary should be stated before any ranking. NASA's systems-engineering handbook uses life-cycle cost to include development through operations and disposal for the applicable program definition; other organizations may define the accountable horizon differently.

Imagine two autonomous shuttle charging systems. Design A costs less to buy but has frequent repair visits and low peak demand capacity. Design B has higher initial cost, but simpler modular replacement and fewer service interruptions. A procurement-only comparison can choose A even when B is less costly for a ten-year service commitment. That conclusion also depends on labor rates, utilization, replacement cycles, service availability targets, and whether unavailable trips incur material organizational cost.

## Discounting and decision consistency

A basic present-value model for an alternative `j` is `PV_j = C0_j + sum(C_j,t / (1+r)^t) - S_j,T/(1+r)^T`. Here `C0` is initial spending, `C_t` is end-of-year spending, `r` is the discount rate consistent with the cash-flow convention, and `S_T` is terminal salvage or other credited value at horizon `T`. Discount **nominal** cash flows with a nominal rate or **real** inflation-adjusted flows with a real rate; mixing them creates a silent error. Taxes and public-sector social discounting may require other conventions, so the model is not a universally prescribed formula.

**Worked example (illustrative, thousands of dollars).** For a three-year horizon and 5% annual discount rate, A costs 800 initially and 150 at each year end. B costs 970 initially and 100 annually. With no salvage, the annuity factor is `1/1.05 + 1/1.05² + 1/1.05³ = 2.723248`. Thus `PV_A = 800 + 150×2.723248 = 1208.49`; `PV_B = 970 + 100×2.723248 = 1242.32`. A is cheaper by approximately 33.84 under these assumptions. However, if A imposes a justified 20-thousand-dollar additional annual service-loss cost, `PV_A` rises by about 54.46, reversing the ranking. The lost-service valuation is a **decision assumption**, not necessarily a direct cash payment.

## Availability, spares, and cost are coupled

Do not add downtime penalties without defining their measurement basis. For example, lost trips during scheduled maintenance may be absorbed by spare capacity while peak-hour failures cause expensive service interruption. Express a mission-based loss as `sum over demand periods (unserved trips × consequence per unserved trip)` only if the consequence is well defined and double-counting with other cost categories is avoided. Reliability and maintenance inputs should distinguish active repair, administrative delays, logistics delays, and the inventory replenishment policy. A low-cost system can still be unacceptable when service-availability constraints are binding; the trade is then constrained optimization, not an unconstrained monetary minimum.

Spares choices require a stock model and lead-time assumptions. A larger stock lowers some shortage exposure but ties up capital, risks obsolescence, and requires inspection and controlled storage. Similar reasoning applies to contractor support: apparent savings on labor may create slower diagnosis or inaccessible configuration evidence. Build scenarios around expected demand, parts scarcity, labor access, inflation and disruptive events; test whether the preferred design changes.

## Why expected value is not enough

The model should report uncertainty in cost and *service outcomes* separately. Expected life-cycle cost can mask tail risk; a design with lower mean may have unacceptable outage probability. Avoid false precision if supplier lead times and failure dependence are weakly known. Consider sensitivity analysis, regret, and decision rules for scenarios that matter to stakeholders. Record whose costs are included: procurement office, operations provider, affected travelers, taxpayers, and the environment may bear different consequences. A total-cost claim without an organizational boundary can conceal transferred costs rather than savings.

## Evidence and failure modes

For review, require a versioned bill of materials, operating profile, maintenance concept, spares strategy, rate assumptions, discount convention, traceable cost sources, and a change log. Key failure modes include treating constant failure rates as universal, using one nominal scenario to justify a long-term decision, counting lost service twice, omitting retirement hazards, and assuming suppliers remain available without evidence. A decision can be defensible without a unique dollar estimate when uncertain outcomes, limits, and responsible authority are explicit.

## Selected source-to-claim references

- **L1 · Definitions and scope of life-cycle planning:** [NASA Systems Engineering Handbook, life-cycle cost and product support/operations](https://www.nasa.gov/reference/systems-engineering-handbook/). Definitions and scope of life-cycle planning; not the example cash flows.
- **L2 · Life-cycle transitions and operations consideration:** [NASA Systems Engineering Handbook, 3.0 Program/Project Life Cycle](https://www.nasa.gov/reference/systems-engineering-handbook/). Life-cycle transitions and operations consideration; project applicability varies.

## Follow the knowledge

- **Prerequisites:** [Work breakdown structures and technical baselines](wbs-and-baselines.md), [Reliability, availability, and maintainability: three different promises](reliability-availability-maintainability.md).
- **Related concepts:** [The enterprise as a system](enterprise-as-system.md), [Risk, issue, uncertainty, and opportunity](risk-vs-issue.md), [Robust optimization and technical margins: good decisions across plausible futures](robust-optimization-and-margins.md).
- **Go deeper:** [Book 7 · Chapter 9: Supportability and life-cycle costs](../B7/chapters/09-design-for-supportability-producibility-supply-sustaina.md), [Book 12 · Chapter 09 — Integrate technical performance with lifecycle cost, resources, maintenance, and affordability](../B12/chapters/09-integrate-technical-performance-with-lifecycle-cost-resources-mainte.md), [Book 11 · Chapter 12 — Apply M&S to production and sustainment, survey advanced methods, and defend the final baseline](../B11/chapters/12-apply-m-s-to-production-and-sustainment-survey-advanced-methods-and-.md).
