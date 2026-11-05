# Chapter 05 — Translate feedback hypotheses into stocks, flows, units, and accumulation equations

*Book 13 · EN.645.781 · Systems Thinking and Systems Dynamics · Week 5 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 5](../labs/lab-05-translate-feedback-hypotheses-into-stocks-flows-units-and-accumulati.md) → attempt the [original Week 5 assessment](../../../C/P3/EN645781.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-781-w05.md) remains available for a quick recap.

## The decision behind the theory

The move from CLD to stock-and-flow model is where qualitative stories become mathematically explicit and many hidden inconsistencies emerge. **Essential question:** What accumulates, what changes it, and are the equations capable of producing the reference behavior?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the systems thinking and systems dynamics perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Stocks are state variables. Their current value depends on prior inflows and outflows, not only current inputs. They create memory and often the delays that make policy difficult. Flows have units of stock per time. Auxiliaries calculate rates, perceptions, capacities, or decisions but do not accumulate directly.

Use the bathtub test: if all flows stopped, would the quantity remain? If yes, it may be a stock. The test is helpful but not sufficient—averages and ratios can persist numerically without representing accumulation. Ask what process stores the quantity.

The continuous stock equation is `Stock(t) = Stock(t0) + integral(inflows - outflows)`. Every equation must have units. Unit balance is a structural test, not formatting. A model with inconsistent units may run and still be meaningless.

Translate mechanisms selectively. For example, maintenance backlog is a stock increased by maintenance work generated and decreased by work completed. Active fleet may be a stock changed by failure and repair-completion flows. Trust may be modeled as a smoothed perception stock when it changes gradually through experience and communication. Document why each stock exists.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Use archetypes and mental models to generate competing intervention hypotheses**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Implement and verify the first executable Vensim model**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Stocks preserve the memory that flow diagrams lose

A stock accumulates the difference between inflows and outflows. This simple conservation idea explains why an apparently balanced operating process can still behave badly. If arrivals exceeded service capacity yesterday, the backlog persists today even when current arrival rate returns to normal. A purely instantaneous flow diagram may conceal that inherited burden. The stock is a state variable: it records consequences of the system's past.

The governing relation, in continuous time, is the derivative of the stock equal to total inflow minus total outflow. But a valid mathematical form does not guarantee valid behavior. Completion rates cannot remain positive when there is no work available, and flows may be limited by staffing, supplies, or policy. Units and physical bounds expose such mistakes. Stocks and flows distinguish an accumulated condition from the activity that changes it; confusing the two leads to interventions aimed at visible symptoms rather than the mechanisms that keep regenerating them.


## Deeper theory — why accumulation changes system behavior

### A stock is memory made explicit

A stock is a quantity that persists because past inflows and outflows have accumulated. A flow is the rate at which the stock changes. This distinction seems simple, but it explains why many well-intentioned interventions have delayed or counterintuitive effects. Booking backlog is a stock: requests remain in the system until completed, cancelled or rejected. New requests and completed rides are flows. You cannot determine backlog from today's arrival rate alone; you also need the state inherited from yesterday.

The continuous-time stock–flow equation is

\[
\frac{dB(t)}{dt}=a(t)-c(t)-r(t),
\]

where \(B\) is backlog, \(a\) arrivals, \(c\) completed trips and \(r\) other legitimate removals. The corresponding integral statement is

\[
B(t)=B(0)+\int_0^t[a(s)-c(s)-r(s)]\,ds.
\]

This is a conservation relationship. It is not a claim that the flows are constant, independent or known precisely. It says that every change in the stock must be accounted for by a flow across the chosen boundary. If observed backlog changes without a modeled cause, either the measurement, boundary or flow model is incomplete.

### Units reveal conceptual mistakes

Backlog has units of requests. Arrival and completion rates have units of requests per hour. Integrating a rate over hours produces requests. A common spreadsheet error is to subtract an hourly capacity directly from a count without multiplying by a time interval. Another is to let the completion flow exceed the available backlog. For a discrete daily model, a physically meaningful update is \(B_{k+1}=\max[0,B_k+A_k-C_k]\) when \(C_k\) denotes *actual* completions rather than an unrestricted service-capacity claim. More carefully, actual completions are bounded by available work and realizable capacity within the period, accounting for event order.

Suppose a service begins with 30 outstanding requests, receives 14 per day and completes 10 per day. Backlog grows by four requests per day under the simplified assumptions. After five days it reaches 50, even though the team has completed 50 rides. A report celebrating higher throughput can coexist with worsening stakeholder experience. This is why flow metrics such as “rides per day” must be interpreted with stock metrics such as pending requests and age distribution.

### Delays and perceived state

Managers rarely observe the true stock continuously. They see reports, delayed dashboards, ticket counts or estimates. A delayed observation creates an additional informational stock or smoothing process. If capacity is increased only when a weekly report shows high backlog, the action addresses a state that may already have changed. If capacity is cut immediately after one low-backlog report, oscillation can follow. Delays are not merely slower arrows; they change the causal timing of decisions and can alter the feedback structure.

A common representation of a smoothed perception is

\[
\frac{dP}{dt}=\frac{B-P}{\tau},
\]

where \(P\) is perceived backlog and \(\tau\) is an information-adjustment time. A larger \(\tau\) produces slower adjustment. This simple equation carries an assumption about first-order exponential smoothing, not necessarily the actual cognitive process of an operations manager. It can nonetheless make a hypothesis about delayed decision-making explicit and testable.

### Nonlinear capacity and saturation

Completion rate is seldom an unrestricted function of backlog. It may be limited by fleet size, driver availability, charging, geography or safety rules. A first approximation is \(c(t)=\min\{\mu(t), B(t)/\Delta t + a(t)\}\) for a discrete interval of length \(\Delta t\), but continuous models need carefully specified service dynamics rather than a formula that can remove more work than exists. Real services also experience diminishing productivity under overload: dispatchers make more corrections, vehicles queue at charging points, and recovery work consumes capacity. A linear model extrapolated into severe overload may therefore predict recovery that the real system cannot achieve.

The difference between a stock and a rate also explains why adding capacity can appear ineffective at first. When backlog is large, extra completions initially reduce accumulated work rather than instantly restoring short waits. Stakeholders may judge the policy ineffective while the stock is still declining. Conversely, a temporary demand collapse can make a policy look successful without any structural improvement. A credible explanation uses reference behavior over time, not just before/after snapshots.

### Boundary choice changes the story

If the boundary counts only accepted requests, the reported backlog may fall when the system rejects more demand. From the dispatcher's perspective, work in process has improved. From the rider's perspective, unmet demand has shifted outside the measured stock. Adding an “unserved eligible demand” stock can expose this displacement. The mathematical identity is not wrong in either model; the boundary determines which social consequences it makes visible.

This is why a system-dynamics model is a theory of accumulation and policy feedback, not merely an animated diagram. Its quality rests on credible stocks, flows, units, delays, decision rules and evidence about behavior. The most useful models often reveal that a celebrated output metric is a flow, while the actual problem resides in the accumulating stock it fails to describe.

## Deeper theory: stock-flow models turn policy stories into conservation laws

### Stocks represent memory that cannot be wished away

A stock is an accumulated quantity: `S(t) = S(0) + ∫(inflow − outflow)dt`. A flow has units of stock per unit time; its value usually depends on stocks, auxiliary variables, decisions, and delays. For an outstanding maintenance backlog `B`, the structure might be `dB/dt = new_defects − repairs_completed`. Increasing repair staffing changes the outflow, but the backlog cannot vanish instantaneously without an explicit removal mechanism. The equation encodes why a policy announcement has delayed effects and why snapshot performance metrics can misrepresent improving or deteriorating conditions.

Stocks are not just boxes drawn around variables. A traveler arrival *rate* is not a stock; the number of travelers waiting is. A desired fleet size is a decision target, whereas available vehicles are a physical stock affected by delivery and retirement. Units help expose such errors. If `B` has units of vehicles, `new_defects` and `repairs_completed` must have vehicles/day; adding a dimensionless priority score directly to either is meaningless. Dimensional consistency is a necessary test but not proof that the process mechanism is right.

### Delays and nonlinear constraints determine the shape of behavior

A common policy formulation uses a gap-closing flow `adjustment = (desired_stock − actual_stock)/τ`, where `τ` has units of time. For `dS/dt = (S_target − S)/τ`, the error decreases exponentially when the target is fixed and there are no other flows. That first-order response is a model assumption, not a universal law. Hiring, maintenance, purchasing, and skill learning commonly involve multiple stages and constraints. If a purchase order takes two months to arrive, raising a target today cannot create the requested fleet tomorrow.

Material and information delays are distinct. A pipeline of ordered vehicles in production is a physical accumulation; a dispatcher's moving average of incidents is an information state. A first-order information delay can be represented by `dP/dt = (observed_demand − P)/τ_s`, where `P` is a smoothed perception. The smoothed value has the units of demand, while `τ_s` expresses the adjustment time. Replacing a physical supply pipeline with an information filter can generate superficially similar curves but imply the wrong intervention.

### Nonnegativity and conservation need explicit implementation

A naive model may compute `repairs_completed = repair_capacity` even when the backlog is nearly empty. Under a finite simulation step `h`, this can make `B_(k+1) = B_k + h(inflow−outflow)` negative. A robust formulation constrains completed work by available backlog and incoming work over the step, with attention to whether same-step arrivals can be processed. Similar care is required for occupancy limits and staff allocation. Clamping a negative stock to zero after integration conceals a flow inconsistency and may violate the accounting identity; constraints should enter the flow definition where possible.

Suppose Northstar starts a week with 30 disabled vehicles, suffers 12 new faults, and repairs 20. End-of-week backlog should be 22 if there are no other transitions. If a model reports 15 while showing those same flows, the discrepancy represents unmodeled removal or a bookkeeping error. That is not merely a graphing issue: decision makers may believe repair policy is more effective than it is. Good structural tests include zero inflows, zero capacity, equilibrium, large demand surges, and physically impossible parameter limits.

### Calibration does not make feedback structure unique

A decline in backlog can be explained by higher repair productivity, fewer failures, changed classification rules, or deferred inspection. Several different causal structures can fit the same time series. Parameters calibrated to one shock may not predict a sustained staffing change because personnel fatigue, learning, or induced demand is absent. Test the structure using known physical and organizational mechanisms, historical interventions, extreme-condition behavior, and comparison with alternative explanations. Use observed reference modes to judge trends, oscillations, turning points, and response delays—not just squared error. The policy value of stock-flow modeling lies in making accumulation and feedback assumptions explicit enough to challenge, not in producing a single persuasive forecast curve.

## Worked engineering example from the course

From the CLD, construct a maintenance sector:

* **Maintenance backlog** `[vehicle-days]`
* inflow: **maintenance work generated** `[vehicle-days/day]`
* outflow: **maintenance work completed** `[vehicle-days/day]`
* completion rate = minimum(backlog / minimum processing time, maintenance capacity)
* maintenance capacity depends on technicians, productivity, parts availability, and overtime fatigue.

The example checks units, initial conditions, limiting cases, and shows why “repair delay” is an emergent ratio rather than a stock.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A stock obeys dB/dt = arrivals − completions. If backlog begins at 40, arrivals are 12/day and completions 9/day for 5 days, the backlog becomes 55. No flow can instantaneously change the stock except an explicitly modeled event.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A service backlog begins at 40 requests, with 12 new requests and 9 completions per day for 5 days. Compute the ending stock.

<details><summary>Show a reasoned solution</summary>

Backlog = 40 + 5×(12−9)=55. This is a stock balance, not a claim about service quality.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* a stock changes without a flow;
* flow units do not equal stock units per time;
* a rate exceeds a physical bound without explanation;
* initial conditions are arbitrary and materially affect results;
* translation is a mechanical one-to-one conversion from the CLD;
* conservation is violated without a documented source or sink.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What does this conclusion depend on?

<details><summary>Explain the answers</summary>

**1. What does this conclusion depend on?** The configuration, intended use, input provenance, model assumptions, uncertainty and decision rule.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 5](../labs/lab-05-translate-feedback-hypotheses-into-stocks-flows-units-and-accumulati.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[04 — Previous chapter](04-use-archetypes-and-mental-models-to-generate-competing-intervention-.md) · [06 — Next chapter](06-implement-and-verify-the-first-executable-vensim-model.md) · [Book index](../README.md)
