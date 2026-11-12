# Chapter 04 — Use M&S for needs, opportunity, current-state, and baseline analysis

*Book 11 · EN.645.757 · Foundations of Modeling and Simulation · Week 4 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 4](../labs/lab-04-use-m-s-for-needs-opportunity-current-state-and-baseline-analysis.md) → attempt the [original Week 4 assessment](../../../C/P3/EN645757.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-757-w04.md) remains available for a quick recap.

## The decision behind the theory

Early models should illuminate the problem before they justify a favored solution. **Essential question:** What does a current-state model reveal about demand, constraints, bottlenecks, and opportunity?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the foundations of modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

A baseline model represents the current or counterfactual condition against which alternatives will be judged. It should not quietly include benefits of the preferred concept.

Calibration changes parameters to align selected outputs with referents; validation evaluates whether behavior is acceptable for intended use. Calibration is not proof of validity.

Use multiple measures: averages, tails, service failures, subgroup outcomes, resource utilization, time-of-day behavior, and degraded conditions.

Bottlenecks can shift with demand and policy. High utilization is not always the root cause; variability, batching, priorities, synchronization, and blocking may dominate.

Early simulation supports problem understanding, hypothesis generation, and data priorities. Avoid causal claims unless the design and evidence justify them.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Characterize data quality, probability, dependence, and stochastic input models**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Implement discrete-event processes, resources, queues, priorities, and statistics**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

A baseline simulation is a controlled representation of the existing operational process, useful for establishing a comparative reference.

### Distinguishing related ideas

A baseline calibrated to observed averages can hide compensating errors, such as excessive service time offset by unrealistically low arrival variability.

### Interpretation and boundary conditions

Use event traces and distributions of intermediate states to assess mechanisms, not just one aggregate output metric.

## Graduate depth: baseline simulation as an identifiable counterfactual

### A baseline is a claim about a process, not a convenient starting number

The practical purpose of a current-state simulation is to estimate what would happen *without* the proposed intervention under explicitly described circumstances. This makes the baseline a counterfactual reference for the future design comparison. It is not simply the first executable model. A defensible baseline identifies the operational population, calendar and time horizon, admission and service rules, physical constraints, data-generating process, and disturbances. In a mobility service, passenger arrivals, vehicle availability, dispatch policy, road closures, accessibility requirements, and recovery after breakdowns may all affect the result. A single mean trip time is insufficient to characterize such a process.

Let `Y_0(s, u, theta)` denote an outcome under the current policy, where `s` is the external scenario, `u` is operational randomness, and `theta` contains uncertain physical and behavioral parameters. An alternative produces `Y_1(s, u, theta)`. The relevant effect is usually `Delta = E[Y_1 - Y_0]` over a *defined* scenario distribution. Changing both the design and the demand distribution and then attributing the entire difference to the design confounds improvement with external change. Conversely, applying a historic baseline to a forecasted operating environment may create false reassurance. The comparison must distinguish a like-for-like engineering effect from the separate forecast of future conditions.

### Calibration, identifiability, and internal evidence

A model can match a published average for the wrong reasons. Suppose the observed average wait is 12 minutes. One model reproduces that number by assuming long service times and unusually regular arrivals; another uses shorter service times and clustered arrivals. They may predict different extreme waits and respond very differently to a fleet increase. This is an identifiability problem: multiple parameter combinations produce similar observable summaries. Matching `E[W]` does not imply that the implied variance, autocorrelation, or cause of waits is correct.

Use multiple independent observables: arrival counts by period, service-time distributions, queue lengths, vehicle utilization, trip cancellation rates, and recovery duration after incidents. A useful calibration criterion can be written `J(theta) = sum_j w_j [g_j(theta) - z_j]^2`, with clearly defined scales and weights. A small `J` establishes agreement only on the selected measures. Hold out time periods and stress conditions for validation; otherwise a flexible simulation may overfit the operating record. Whenever feasible, inspect event traces and conservation identities, such as passengers entering a queue minus passengers served minus passengers abandoning equaling the change in queue population.

### The bottleneck moves when the system changes

A baseline bottleneck is not an immutable property of the architecture. Increasing boarding capacity can move congestion to curb space or downstream road intersections. Little's law, `L = lambda W`, relates average population `L`, throughput `lambda`, and average time `W` for a stable system with consistently defined boundaries. It is a useful cross-check, not a substitute for a distributional model, and cannot justify calculations when a queue is rapidly accumulating or the measurement populations differ.

In the fictional Northstar case, imagine a baseline of 100 trips per hour with a growing accessibility-service queue. Adding vehicles may improve mean waiting time but leave the accessibility bottleneck untouched. A second design that improves boarding operations could reduce the tail of the wait distribution even with fewer added vehicles. Report both outcomes, the operational constraints, and uncertainty around the difference. The lesson is that a current-state model supports *conditional* comparison: it does not certify the historical data, the future scenario distribution, or the social legitimacy of the chosen performance measure.

## Worked engineering example from the course

The current shuttle service appears underutilized on average, but the baseline model shows peak directional imbalance, long accessible boarding, and deadhead travel causing 90th-percentile waits. The opportunity is not simply “more vehicles”; dispatch and staging policies may provide comparable benefit.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

For an existing service, observed 120 daily requests do not imply 5 requests each hour. A model that spreads arrivals uniformly could miss the ten-minute peak governing service acceptability. Reconstruct a nonstationary baseline using time-stamped requests.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A simulation delivers 12, 14, 16, 18, 20 and 22 completed requests in six independent runs. Calculate sample mean.

<details><summary>Show a reasoned solution</summary>

The mean is (12+14+16+18+20+22)/6=17 completed requests. Six replications are insufficient to claim a rare-event guarantee.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Preferred-solution benefits are embedded in the baseline.
* Calibration uses only one aggregate mean.
* A correlation or model response is described as proven real-world causation.
* Subgroup or degraded outcomes relevant to accessibility/safety are omitted.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is calibration?
2. Why use tail measures?
3. What is a counterfactual baseline?
4. Why can bottlenecks move?

<details><summary>Explain the answers</summary>

**1. What is calibration?** Adjustment of model parameters or structure to improve agreement with selected referent data.

**2. Why use tail measures?** Stakeholder harm and capacity failures often occur in distribution tails, not at the mean.

**3. What is a counterfactual baseline?** An explicitly defined no-change or alternative reference condition used for comparison.

**4. Why can bottlenecks move?** Different demand, policies, priorities, and failures change which resource or rule constrains flow.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 4](../labs/lab-04-use-m-s-for-needs-opportunity-current-state-and-baseline-analysis.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[03 — Previous chapter](03-characterize-data-quality-probability-dependence-and-stochastic-inpu.md) · [05 — Next chapter](05-implement-discrete-event-processes-resources-queues-priorities-and-s.md) · [Book index](../README.md)

## Step 03 integrated mobility simulation case: baseline and opportunity assessment

### Turn needs into observable service measures

The sponsor's problem is not to minimize mean trip time at any cost, but to meet service thresholds during operating conditions. Define standard pickup wait \(W_s=t_{\mathrm{pickup}}-t_{\mathrm{arrival}}\) for each **standard** request and accessible pickup wait \(W_a\) analogously. Compute p90 by the stated *nearest-rank* method \(Q_{0.9}=x_{(\lceil0.9n\rceil)}\); the sample and quantile convention belong in the evidence record. The guide sets maximum 12 minutes for standard p90 and 15 for accessible p90, with **strictly less than 1%** not served in the declared day. Our proxy counts requests still awaiting pickup at 18:00; the study does not simulate denied requests or cancellations. Long waits for trips picked up after close are still reported in p90, and must not be hidden.

An expected arrival-rate calculation provides an independent bound on proposed capacity, not a feasibility proof. Peak demand is 50 requests/hour (16:00–17:00). If fourteen independently available vehicles spend 20 minutes per request, the maximum notional completion rate is \(14(60/20)=42\)/hour, below that local peak even before charging. A fluid queue lower bound accumulates backlog at least \((50-42)(1)=8\) requests over that peak hour, provided no spare capacity carried as idleness and no pooling; on shorter time scales stochastic bursts are worse. But service rates and other hourly patterns need separate assessment, so this bound is explanatory, not a simulation validation result.

### Baseline against a proposed improvement

Our model produces *replication-level estimates*, not measured fleet performance. Run `python SE/K/B11/tools/step03_book11_mobility.py` to regenerate the [paired output](../case/replication-output.csv). Across 30 baseline seeds, the 12-vehicle option has mean daily standard p90 about **69.1 minutes**, compared with about **36.4 minutes** for 14; both miss the 12-minute standard target. The 14-vehicle option likewise misses the accessible p90 and <1% end-of-day nonpickup target (approximately 45.4 minutes and 6.0%, respectively). These results can identify a **model bottleneck and decision to examine**, not prove real fleet inadequacy.

A useful baseline report separates (i) nominal input demand and its provenance, (ii) predicted service per user group, (iii) charging and resource usage, and (iv) *unmodeled* causes: pedestrian routing, ride pooling, traffic networks, special-needs equipment, duty breaks, and maintenance. Do not collapse lack of representation into “zero risk.” The requirements register flags staffing and physical charger validation as missing evidence.

### Counterfactuals and identification

If a model comparison shows less waiting under 14 vehicles, that is a *conditional causal comparison within the fixed model*: only fleet count is manipulated while the same exogenous streams are replayed. It does not establish a causal field estimate unless the operational intervention would preserve dispatch, service times, staffing and other mechanisms. An alternative intervention may be to alter vehicle pooling, driver dispatch, charger placement or work shifts; none has been evaluated in this first release.

**Exercise and solution.** A manager changes the decision criterion from daily mean wait to daily p90 wait. Why might a fleet ranking change? **Solution:** means average all experiences, whereas p90 is sensitive to peak backlog and extended tails. An alternative with more frequent short waits but a few severe queues may have a good mean and unacceptable p90. Report both, and make sure the quantile is computed **within each replication** before forming uncertainty intervals over independent days.

**Next evidence:** measure real demand counts by hour, occupancy/pooling, accessible service and peak-day queue trajectories; compare multiple observed shifts to the model before claiming decision validity. [Case dossier](../case/INDEX.html) · [Chapter 5](05-implement-discrete-event-processes-resources-queues-priorities-and-s.md).
