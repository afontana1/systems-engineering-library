# Chapter 06 — Implement and verify the first executable Vensim model

*Book 13 · EN.645.781 · Systems Thinking and Systems Dynamics · Week 6 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 6](../labs/lab-06-implement-and-verify-the-first-executable-vensim-model.md) → attempt the [original Week 6 assessment](../../../C/P3/EN645781.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-781-w06.md) remains available for a quick recap.

## The decision behind the theory

An executable model converts assumptions into behavior, but software execution is not evidence of correctness. **Essential question:** Does the implemented model faithfully represent the approved formulation and behave correctly in simple conditions?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the systems thinking and systems dynamics perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Implement from the equation dictionary rather than drawing freely in the tool. Each variable should include units and a comment describing meaning, source, and allowed range. Use model sectors/views for navigation, but remember that equations—not diagram position—define the executable model.

Start with small test models: one reinforcing loop, one balancing loop, one stock with constant flows, and one first-order perception delay. Compare behavior to analytical or graphical expectations. These “unit models” build confidence in interpretation and tool use.

Numerical integration approximates continuous equations. The time step should be small relative to the fastest meaningful time constant. Run time-step sensitivity by halving the step and comparing policy-relevant outputs. A visually similar graph may still hide significant metric differences.

Do not calibrate yet. First verify translation: equation review, unit check, initialization, conservation, bounds, and extreme conditions. Maintain a defect log with detection, consequence, correction, and regression test.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Translate feedback hypotheses into stocks, flows, units, and accumulation equations**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Explain delays, nonlinearities, oscillation, overshoot, and changing loop dominance**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

An executable stock-flow model expresses accumulation, rates and feedback so that quantities cannot appear without a source or sink.

### Distinguishing related ideas

A causal arrow is not a flow: influence changes a rate or decision, while a flow changes a conserved stock.

### Interpretation and boundary conditions

Unit consistency and extreme-condition tests reveal structural errors that attractive simulated curves can conceal.

## Graduate depth: executable stock-flow models are numerical claims

### From a diagram to a dimensionally valid state equation

A stock-flow diagram becomes an executable theory when each flow is expressed as a function of the current state, exogenous drivers, and parameters. If `S` denotes available service capacity, one possible structure is `dS/dt = acquisitions - retirements - losses + recoveries`, with every right-hand term measured in vehicles per unit time. An auxiliary such as utilization might be dimensionless, but the rule converting utilization into wear must include a rate coefficient. A unit checker can detect a term adding vehicles to vehicles/hour; it cannot decide whether the wear relationship is empirically plausible.

The first model should be small enough for a reviewer to predict its behavior before running it. With all flows set to zero, a conserved stock must remain constant. With constant inflow of five units/hour and no outflow, it must increase linearly by ten units over two hours. With proportional outflow `outflow = kS` and no inflow, it should decay exponentially, `S(t) = S(0) exp(-kt)`, under a continuous-time interpretation. These analytic limiting cases are unusually effective tests for a Vensim or other systems dynamics implementation.

### Time step and stability are modeling decisions

An explicit Euler calculation uses `S_(n+1) = S_n + Δt [inflow(S_n) - outflow(S_n)]`. For the simple decay model, this becomes `S_(n+1) = (1 - kΔt)S_n`. If `kΔt` exceeds one, a positive stock can become negative in a single step; if it approaches two, oscillatory numerical behavior can mask the physical decay. This illustrates why a diagram that appears structurally sound may produce invalid behavior under a poor integration time step. A solver's adaptive stepping can help, but discontinuities, event conditions, and feedback delays still require explicit attention.

A practical convergence test compares the decision-relevant output across successively smaller steps, for example `Δt`, `Δt/2`, and `Δt/4`. A small change in a plotted final value is not enough if the decision depends on a peak, a threshold crossing, or timing of a service failure. The time horizon must also include slow feedback effects; a policy can appear successful over a short run and fail after delayed capacity or workload responses arrive.

### Boundary conditions and policy interpretation

Real flows often have hard bounds. The outflow of completed requests cannot exceed the number waiting plus arriving during the interval, nor can capacity utilization exceed what the defined assets can actually deliver. Imposing `max` and `min` functions preserves arithmetic feasibility, but introduces nonlinearities that can change loop dominance and create corners where numerical approximations degrade. Document whether a negative stock is prohibited by physics, policy, or simply a modeling convenience.

For Northstar, suppose a delayed hiring policy is triggered whenever backlog exceeds a threshold. A simulated backlog oscillation could represent genuine delayed balancing feedback, or it could result from a coarse time step that repeatedly overshoots the trigger. Diagnose by examining the causal structure, units, initial state, timestep convergence, and the policy event semantics separately. A successful implementation test verifies equations and bookkeeping; credible policy guidance additionally requires sensitivity to behavioral assumptions, data, and alternative structures. The difference between these two claims is central to responsible dynamic modeling.

## Worked engineering example from the course

Implement the maintenance sector and test four cases:

1. no work generated and zero backlog → backlog remains zero;
2. constant work below capacity → backlog converges to a small processing amount;
3. work above capacity → backlog grows approximately linearly;
4. zero parts availability → completion falls to zero and backlog accumulates.

The example predicts behavior before simulation, checks units, runs with `TIME STEP` 0.25 and 0.125 day, and records the difference.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

In a 1-day Euler step, backlog_next = max(0, backlog + arrivals − completions). A Vensim or Python implementation should be checked for units, nonnegative stocks, and mass balance before calibration.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A maintenance stock has 30 open jobs. The next week brings 12 new jobs and 15 closures. What is the new stock?

<details><summary>Show a reasoned solution</summary>

New stock = 30+12−15=27. If the modeled closure rate exceeds available work, cap it or reformulate the flow.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* model check or unit errors remain unresolved;
* implementation departs from the approved formulation without change control;
* time step is selected only by default;
* no tests have predetermined expected behavior;
* the learner cannot locate or explain an equation during live review;
* run settings or software version are missing.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What does this conclusion depend on?

<details><summary>Explain the answers</summary>

**1. What does this conclusion depend on?** The configuration, intended use, input provenance, model assumptions, uncertainty and decision rule.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 6](../labs/lab-06-implement-and-verify-the-first-executable-vensim-model.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[05 — Previous chapter](05-translate-feedback-hypotheses-into-stocks-flows-units-and-accumulati.md) · [07 — Next chapter](07-explain-delays-nonlinearities-oscillation-overshoot-and-changing-loo.md) · [Book index](../README.md)
