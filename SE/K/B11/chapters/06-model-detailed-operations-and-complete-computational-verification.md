# Chapter 06 — Model detailed operations and complete computational verification

*Book 11 · EN.645.757 · Foundations of Modeling and Simulation · Week 6 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 6](../labs/lab-06-model-detailed-operations-and-complete-computational-verification.md) → attempt the [original Week 6 assessment](../../../C/P3/EN645757.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-757-w06.md) remains available for a quick recap.

## The decision behind the theory

Complex models often fail at interactions, edge cases, and bookkeeping rather than basic flow. **Essential question:** Does the executable model implement the approved rules across nominal, boundary, extreme, and failure conditions?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the foundations of modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Computational verification asks whether the executable model correctly implements its specification and numerical logic. It is different from asking whether the specification adequately represents reality.

Use layered tests: unit/module tests, deterministic integration cases, event-trace review, conservation checks, extreme conditions, statistical checks, regression tests, and independent review.

Extreme and degenerate tests intentionally simplify or stress the model: zero arrivals, infinite resources, no failures, all failures, deterministic inputs, one entity, or overwhelming demand.

Metamorphic testing checks expected relationships when an exact answer is unavailable—for example, adding identical capacity should not worsen throughput absent a modeled interference mechanism.

A defect log records symptom, reproduction, root cause, affected outputs, fix, regression evidence, and credibility impact.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Implement discrete-event processes, resources, queues, priorities, and statistics**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Use simulation for concept exploration, alternatives, and scenario analysis**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Computational verification asks whether the program solves the intended conceptual model; it is distinct from whether the model describes reality.

### Distinguishing related ideas

Testing a fixed-seed example checks reproducibility, but not exhaustive event ordering or logic under boundary conditions.

### Interpretation and boundary conditions

In a resource queue, event ties, preemption and end-of-run behavior can produce incorrect counts while leaving average results superficially plausible.

## Graduate depth: detailed operation models as conserved event systems

### State, events, and invariants

A discrete-event simulator is not primarily an animated timetable. It is a state-transition system. Represent its state at time `t` as `x(t)`, containing the count of waiting requests, available vehicles, vehicles in service, charger occupancy, pending maintenance, and other variables needed to make future transitions well-defined. An event `e` maps the pre-event state to a post-event state, `x(t+) = T_e(x(t-))`. The event calendar chooses the next transition time; between transitions, the state stays constant unless the model includes continuous dynamics. If an apparently random output changes when event-processing order changes, the model may have an unexamined scheduling rule.

Conservation relationships provide verification oracles independent of any plotted result. With no vehicle entering or leaving the modeled fleet, `N_total = N_available + N_busy + N_charging + N_maintenance` at all times. For requests, `N_arrivals = N_waiting + N_served + N_cancelled + N_in_service`, assuming every category is defined to be mutually exclusive and collectively exhaustive. Every transition should preserve these invariants or report a documented source or sink. A model can produce plausible average wait time while silently creating an extra vehicle during reassignment; the invariant catches a defect that statistical agreement may miss.

### Event priority and resource deadlocks

Suppose a vehicle finishes charging at exactly the same simulated instant as a dispatch request arrives. The result may depend on whether charging completion occurs before dispatch selection. Explicit tie-breaking is part of the model semantics, not a harmless software detail. Events should carry stable priority and secondary order rules, and those rules should be tested for their consequences. A simulation implementation that uses processor scheduling or nondeterministic iteration order as an implicit tie-breaker can fail reproducibility even with a fixed random seed.

Detailed resource models also create deadlock and starvation risks. A request might reserve a vehicle while waiting for a driver, while a driver is reserved for another request waiting for a vehicle. Neither can proceed. The underlying structure is a resource-allocation graph with circular wait conditions. A possible remedy is atomic reservation of jointly required resources, but that changes utilization and fairness. Priority rules may prevent a high-consequence request from waiting yet increase lower-priority tail delay. These are policy tradeoffs, not merely software fixes.

### Verification from microbehavior to system behavior

Verification should proceed in layers. First check each transition with small deterministic inputs: one vehicle, one request, no travel variability. Then test invariants across long traces, boundary cases at zero capacity, simultaneous events, zero-duration service, cancellations, and interrupted charging. Next compare against limiting analytical cases. For example, under stable single-server conditions the long-run departure rate cannot exceed service capacity, and Little's law `L = λW` should hold when the same stable population, averaging horizon, and definition of work in system are used. A violation may reveal a measurement or bookkeeping error, although finite-sample deviations alone do not prove a bug.

In Northstar, a 10,000-replication estimate of mean queue length is not credible just because its confidence interval is narrow. The model should first pass state-transition tests and invariant checks. Only then do replications quantify stochastic output uncertainty. Verification establishes consistency with the implemented specification; comparison with observed operational behavior is the separate validation task. Report both, along with the event-order convention and the exact configuration used to generate each result.

## Worked engineering example from the course

Vehicle utilization exceeds 100%. Trace review shows charging time is counted as both busy service and unavailable charging state. A state-partition invariant detects the overlap; the statistic logic is corrected and all prior experiment results are invalidated and rerun.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A discrete-event simulator should preserve causality: service cannot complete before it begins, queue length cannot be negative, and no vehicle serves two exclusive trips simultaneously. Verify invariants with deterministic fixtures before interpreting stochastic output.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A simulation delivers 12, 14, 16, 18, 20 and 22 completed requests in six independent runs. Calculate sample mean.

<details><summary>Show a reasoned solution</summary>

The mean is (12+14+16+18+20+22)/6=17 completed requests. Six replications are insufficient to claim a rare-event guarantee.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Known computational defects affect critical outputs and are ignored.
* State/resource statistics violate conservation or partition rules.
* Changes invalidate prior results but reruns are not performed.
* Formal experiments begin without a controlled model version.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is computational verification?
2. What is metamorphic testing?
3. Why test zero demand?
4. What is a regression test?

<details><summary>Explain the answers</summary>

**1. What is computational verification?** Evidence that the executable model correctly implements the specified model and computations.

**2. What is metamorphic testing?** Testing expected relationships between transformed inputs and outputs when exact results are unavailable.

**3. Why test zero demand?** It exposes initialization, spontaneous events, resource leaks, and improper statistics.

**4. What is a regression test?** A repeatable test used to detect unintended behavior changes after modifications.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 6](../labs/lab-06-model-detailed-operations-and-complete-computational-verification.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[05 — Previous chapter](05-implement-discrete-event-processes-resources-queues-priorities-and-s.md) · [07 — Next chapter](07-use-simulation-for-concept-exploration-alternatives-and-scenario-ana.md) · [Book index](../README.md)

## Step 03 integrated mobility simulation case: implementation and computational verification

### Distinguish conceptual adequacy from code correctness

Computational verification asks whether the **implemented** model accurately executes its *specified* events, states and mathematics. Validation asks whether those specifications represent relevant aspects of the *real* service. Both are separate from the sponsor's permission to rely on results. A passing Monte Carlo run is not a computational-verification test: many bugs yield plausible histograms.

The [mobility code](../tools/step03_book11_mobility.py) loads a versioned [JSON configuration](../case/model-assumptions.json), validates ranges and segment continuity, creates demand from independent random streams, schedules arrivals/completions in a priority queue, and exports all replication-level output. It uses only Python's standard library. Users may change a declared scenario **without editing event transition logic**; source control should capture each change. The generated [replication CSV](../case/replication-output.csv) contains all seeds, fleet sizes, request counts, standard and accessible p90, charger usage and end-of-day backlog.

### A four-layer test argument

1. **Parameter tests:** reject probabilities outside [0,1], noncontiguous demand windows, negative rates, impossible charging distributions, and invalid fleet sizes. These are preconditions, not empirical validation.
2. **Unit tests:** exercise `nearest_rank([0,4],0.9) == 4` and a two-request deterministic queue. Test accessible vehicle eligibility separately; never infer it from the overall percentile.
3. **Invariant tests:** assert \(I+T+Q+C=F\), \(C\le c\), SOC in [0,1], and request flow conservation; run with unusually stressed inputs and after-close events.
4. **Metamorphic tests:** keep the same request stream while varying a *single* factor. Increasing vehicle count should generally help service on average but is **not guaranteed** to monotonically improve every realized result when route/charging assignments change. The appropriate check is a conditional distribution comparison and explanation of any counterexample, not an invalid blanket assertion of monotonicity.

### Work through an implementation error before it reaches the evidence report

A code reviewer sees a JSON triangular triple `[24,32,50]` intended as minimum, mode and maximum. Python `random.triangular(low, high, mode)` takes a *different* argument order: `triangular(24,32,50)` would place the mode above its apparent maximum and silently distort the generator. The correct call is `triangular(24,50,32)`. The same issue affects standard boarding and travel. The model's configuration contract deliberately uses `(low,mode,high)` and must explicitly map it to the library call, validated by a distribution moment/quantile check.

If charge durations were all exactly 35.33 minutes, one could hand-check total charge resource time; with a triangular generator, a seeded replicate is only **reproducible** under the program/library version and control of random-draw order. Reproducibility establishes repeatable data processing, not valid underlying distributions. Differences between desktop and server runtimes should be investigated rather than treated as benign.

### Change control and test ownership

For this illustrative release, the controlled requirement IDs are `MS11-R01` through `MS11-R06`; the [credibility register](../case/credibility-register.csv) distinguishes *documented*, *tested*, *assumed* and *missing* work. Every claim must link to the source assumption, test case or independent observation. An independent reviewer should challenge event tie behavior, accessible dispatch, charging threshold crossings, randomness, after-close policy and sampling interpretations; the current automated suite does not fully prove correctness for all possible schedules.

**Exercise and solution.** A developer verifies that the same seed produces the same p90 twice. Is computational verification complete? **Solution:** no; a deterministic wrong algorithm is also repeatable. Add a known-trace reference, invariants, invalid input checks, independent analytic bounds, and reviews of units and event priorities. Field validation must additionally use real operating evidence.

[Case dossier](../case/INDEX.html) · [Chapter 7](07-use-simulation-for-concept-exploration-alternatives-and-scenario-ana.md).
