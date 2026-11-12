# Chapter 09 — Integrate technical performance with lifecycle cost, resources, maintenance, and affordability

*Book 12 · EN.645.758 · Advanced Systems Modeling and Simulation · Week 9 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 9](../labs/lab-09-integrate-technical-performance-with-lifecycle-cost-resources-mainte.md) → attempt the [original Week 9 assessment](../../../C/P3/EN645758.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-758-w09.md) remains available for a quick recap.

## The decision behind the theory

Advanced M&S should connect dynamic technical behavior to resources and affordability. Energy use, thermal stress, component cycling, charger demand, maintenance, spares, downtime, and model-development costs can change the preferred architecture.

**Essential question:** How do dynamic technical outcomes translate into cost and lifecycle consequences without false precision?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the advanced systems modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

* Define estimate scope and WBS before equations. State base year, inflation treatment, schedule, quantity, learning, operations period, ownership, exclusions, and reserves.
* Map dynamic outputs to cost drivers: kWh, peak demand, battery throughput, thermal excursions, charge cycles, pump hours, failures, maintenance labor, fleet downtime, and infrastructure utilization.
* Avoid double counting when one cost relationship already includes subsystem management, integration, or operations content.
* Model correlation: higher mass may increase purchase cost, energy, brake/tire wear, and battery size simultaneously. Independent cost sampling can understate risk.
* Report ranges and confidence honestly. A detailed spreadsheet does not create mature data. Use sensitivity and value-of-information analysis to identify useful next evidence.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Model natural and man-made environments as dynamic, correlated scenario systems**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Extend the model to population or biological dynamics and communicate behavior through visualization**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Lifecycle performance and cost depend on duty cycles, degradation, maintenance and resource availability interacting over time.

### Distinguishing related ideas

A component with a favorable purchase price may increase energy consumption or downtime sufficiently to worsen system value.

### Interpretation and boundary conditions

Coupled technical-economic models must keep physical feasibility and uncertainty visible rather than hiding them in one optimized cost number.

## Graduate depth: lifecycle affordability is a coupled performance constraint

### Engineering capability, availability, and cost share one architecture

A system with excellent peak performance may be a poor lifecycle design if it is unavailable during maintenance or too costly to operate at the required service level. Technical performance, reliability, maintainability, support resources, and affordability are linked through usage and failure mechanisms. Treating them as independent spreadsheet categories creates implausible alternatives: a higher-utilization concept can increase wear and maintenance demand, while a redundancy decision can improve mission availability but add capital cost, weight, and replacement inventory.

For a repairable system in a simple steady-state alternating-up/down model, operational availability is approximated by `A = MTBF / (MTBF + MTTR)`. This relationship assumes appropriately defined uptime and downtime, sufficiently representative failure and repair processes, and no overlooked logistics or common-cause outages. A more detailed operational availability assessment must account for waiting on parts, scheduled maintenance, mission scheduling, and correlated subsystem failures. Availability is a fraction of relevant time or demand opportunities, not identical to reliability over a specified mission interval.

A lifecycle cost model may be expressed as `LCC(d) = C_acquire(d) + sum_{t=1}^T [C_operate(d,t) + C_maintain(d,t) + C_support(d,t)]/(1+r)^t + C_retire(d)/(1+r)^T`, with consistent real or nominal cash flows and an explicit discount-rate assumption. This equation is a decision accounting structure, not a prediction engine. It will be misleading if service demand, energy price, degradation, spares, staffing, and policy changes are represented as certain when they are not.

### Resource constraints change realized performance

The output of a maintenance system depends on queues and shared resources. If repair requests arrive at average rate `lambda` and a resource completes work at average rate `mu`, utilization `rho = lambda/mu` approaches one as demand nears effective capacity. For an ideal M/M/1 queue, expected time in the system is `W = 1/(mu - lambda)`. Real maintenance has priorities, different repair types, shifts, parts shortages, and changing failure rates; the ideal formula is a diagnostic for congestion, not a credible replacement for a maintenance simulation. An architecture that increases parts demand can push the support system into unstable backlogs long before its nominal cost estimate signals trouble.

### Illustration: Northstar charging and maintenance

Suppose an alternative adds three vehicles and reduces nominal queue delay, but consumes more charge cycles and expands overnight maintenance. If a single maintenance bay is already close to saturation, fleet availability may fall, reversing the projected response-time improvement. Another alternative may cost more initially but use modular replaceable components that shorten downtime. These effects should be evaluated using the same mission demand scenarios, reliability assumptions, resource calendars, and cash-flow basis. Report the uncertainty around both service availability and cost; do not add optimistic means from different scenarios to manufacture an attractive result.

A defensible decision separates *hard adequacy constraints* (safe operation, accessibility, supportability, mission capacity) from *preferences* among feasible choices. Sensitivity to the discount rate, maintenance learning, uncertain demand, and supply disruption can dominate small differences in acquisition price. The model's final product is a conditional affordability argument, with named assumptions and revision triggers, rather than a single precise total cost disconnected from engineering behavior.

## Worked engineering example from the course

Architecture A uses a smaller battery and aggressive fast charging; B uses a larger battery and lower charge rate. A is cheaper to buy but the simulation predicts 2.1× fast-charge events, higher thermal excursions, and earlier battery replacement. Over an eight-year synthetic lifecycle, A’s median cost is lower by $70k but its 80th-percentile cost is higher by $95k. The decision changes when battery replacement correlation and downtime are included.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Lifecycle model compares acquisition $500k with annual operations $90k for five years at 6%: discounted operations total about $379k, so present cost is about $879k before residual value and risk. A cheaper acquisition can still lose on lifecycle costs.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** For x˙=−2x, x(0)=1 and Euler step h=0.2, calculate the first two numerical states.

<details><summary>Show a reasoned solution</summary>

x1=1+0.2(−2)=0.6 and x2=0.6+0.2(−1.2)=0.36. The exact states are e^(−0.4)≈0.6703 and e^(−0.8)≈0.4493.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Point estimates are presented without uncertainty for a consequential decision.
* Technical and cost outputs are disconnected or double counted.
* Estimate scope or base-year assumptions are undefined.
* Precision exceeds the maturity and evidence of the inputs.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. Why start with a WBS?
2. What is a CER?
3. Why integrate dynamic outputs?
4. Why model correlation?

<details><summary>Explain the answers</summary>

**1. Why start with a WBS?** To define scope, ownership, completeness, and prevent omissions/double counting.

**2. What is a CER?** A relationship that estimates cost from one or more technical/programmatic drivers.

**3. Why integrate dynamic outputs?** Usage, stress, cycles, failures, and downtime create lifecycle costs.

**4. Why model correlation?** Common drivers move multiple cost elements and can dominate tail risk.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 9](../labs/lab-09-integrate-technical-performance-with-lifecycle-cost-resources-mainte.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[08 — Previous chapter](08-model-natural-and-man-made-environments-as-dynamic-correlated-scenar.md) · [10 — Next chapter](10-extend-the-model-to-population-or-biological-dynamics-and-communicat.md) · [Book index](../README.md)

## Step 03 integrated NS-CPS12.1 case: performance, charging, resources and cost

### Design decisions need constraints as well as favorable metrics

A physical model says how much energy an illustrative vehicle uses under an assumed route; a fleet design must ask whether depots, chargers, maintenance, drivers, accessibility service, tariffs and capital spending support the mission. If an energy-saving configuration misses passenger schedules or thermal margins, it is not a valid “optimum.” Constrain feasibility before ranking alternatives. Book 11's queue simulation models a distinct operational problem; a future coupling should use verified charging arrivals and charger occupancy, not transplant this plant's convenient average trip time directly into a demand model.

The shuttle course source suggests 100 kW nominal charging, with delivered range 85–105 kW. The teaching JSON holds `charger_kw=100` and charger efficiency 0.93, but **does not** simulate charging events or charger contention. A separate engineering arithmetic estimate for replacing consumed energy \(E\) is

\[
t_\mathrm{grid}=\frac{E}{\eta_\mathrm{charger}P_\mathrm{charger}},\quad
E_\mathrm{grid}=\frac{E}{\eta_\mathrm{charger}},
\]

assuming constant power, no taper, no pack temperature restrictions, and a charger that can deliver the stated power continuously. At 32.38 kWh of modeled battery energy use in the hot low-flow duty cycle, replacing that energy at 100 kW and 93% efficiency takes \(32.38/(0.93\times100)=0.348\) hours or **20.9 minutes**. If delivered power is 85 kW, the estimate becomes about **24.6 minutes**. Neither value proves a station can achieve that turnaround: plug-in dwell, overlapping arrivals, load sharing and SOC taper are excluded.

### Tie technical states to cost consequences

For an energy-only illustration, let tariff \(p_e\) be currency per kWh, and annual cycles \(N\). The annual electrical purchase cost is

\[
C_e=N\,E_\mathrm{battery}/\eta_c\,p_e.
\]

Suppose, solely for a worked example, \(N=250\) duty cycles/year, \(p_e=\$0.20/\mathrm{kWh}\), and \(E_\mathrm{battery}=32.38\) kWh. Annual grid energy is approximately \(250(32.38)/0.93=8704\) kWh and the illustrative bill is **$1,741/year**. This excludes demand charges, peak tariffs, charging infrastructure, insurance, labor, maintenance, cell aging, uptime and embodied capital costs. None of these unit prices or annual repetitions are field-sourced; use a real cost basis before a procurement decision.

A levelized cost model should separate purchase/installation, fixed operating expense, variable energy, battery replacement, maintenance, downtime and retirement. For discount rate \(r\), years \(t=1\ldots T\) and annual net cost \(C_t\), present value is \(PV=C_0+\sum_t C_t/(1+r)^t\). Economic comparison should incorporate the probability and consequence of failing service requirements, not just the mean dollar figure.

### Coupled reliability and maintainability

Charging availability and vehicle serviceability introduce discrete transitions. For an idealized repairable component with exponential failure rate \(\lambda\) and repair rate \(\mu\), steady availability is \(A=\mu/(\lambda+\mu)=MTBF/(MTBF+MTTR)\). At an assumed 200-hour MTBF and 5-hour MTTR, \(A=200/205\approx97.56\%\). If a critical station is unavailable 2.44% of the time, a single-charger schedule can fail even when energy calculations look adequate. These are hypothetical reliability parameters; exponential models are frequently inappropriate for wear, repair queues and correlated common causes.

### Explain the energy-temperature-economic frontier

The current paired hot comparison shows high coolant flow lowers modeled peak pack temperature from about **41.88°C to 40.98°C** but increases battery energy use from about **32.38 to 33.36 kWh**. A simple operating cost preference for low flow would ignore degradation, cell hotspot uncertainty, thermal fault risk and future ambient exposure. Conversely a preference for high flow based only on the 0.90°C reduction ignores pump wear and energy. State a constrained objective, for example minimize \(C_e\) subject to validated thermal, reserve and passenger-service requirements, and explicitly mark which of those constraints are not yet represented.

### Exercises with solutions

**A.** For 35 kWh delivered to the pack, 93% charger efficiency and 85 kW constant delivered grid-side power, calculate ideal charging time. **Solution.** \(35/(0.93\times85)=0.443\) h, or **26.6 min**. Confirm whether “85 kW” denotes grid input or DC output; the formula above assumes AC/grid input and therefore applies efficiency once. If it denotes net DC delivered, use \(35/85\) h instead.

**B.** A proposal has $0.30 lower daily electricity expense but requires $10,000 more cooling hardware. Can it be selected on energy cost alone? **Solution.** No; compare capital present value, maintenance, degradation, reliability and validated constraint margins over the lifecycle. Without decision horizon and uncertainty the economics are indeterminate.

**C.** Why is simulated average energy per route not a fleet charger-capacity claim? **Solution.** Fleet demand has arrival-time clustering, service downtime, shared power and charge-session duration distributions; a single-vehicle plant estimate does not resolve those queue mechanics.

**Deliverable:** a feasible-design constraint table, example energy/charge calculation with power convention, cost ledger separating synthetic prices, and an interface request for Book 11 fleet integration.
