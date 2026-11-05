# Chapter 07 — Integrate the model baseline and design advanced simulation experiments

*Book 12 · EN.645.758 · Advanced Systems Modeling and Simulation · Week 7 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 7](../labs/lab-07-integrate-the-model-baseline-and-design-advanced-simulation-experime.md) → attempt the [original Week 7 assessment](../../../C/P3/EN645758.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-758-w07.md) remains available for a quick recap.

## The decision behind the theory

Midcourse integration converts separate domain demonstrations into one controlled analytic instrument. The challenge is to distinguish physical behavior from parameter, numerical, coupling, and implementation effects before using the model for decisions.

**Essential question:** Is the integrated model ready for runs that will be treated as evidence?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the advanced systems modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

* Freeze a review baseline before experimentation. Record every equation, component, parameter, interface, solver, library, and unresolved issue.
* Use screening to identify important factors before expensive high-resolution experiments. Include interactions that are physically plausible.
* Separate scenario variables, controllable design factors, stochastic noise, epistemic parameter ranges, and numerical settings. Do not mix solver settings into the physical DOE without a clear verification purpose.
* Define response calculations before looking at results. Preserve time histories needed to investigate peaks, modes, failures, and integrals.
* A run for record requires approved configuration, inputs, seed policy, execution log, quality checks, and a controlled analysis script.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Design interoperable HLA/FMI federations, LVC interfaces, and composable co-simulations**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Model natural and man-made environments as dynamic, correlated scenario systems**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

A simulation experiment is an argument about cause and effect under controlled assumptions, not a demonstration of graphical realism.

### Distinguishing related ideas

Numerical convergence, parameter calibration and stochastic replication answer different questions and should not be conflated.

### Interpretation and boundary conditions

A design that appears superior at one solver step size may have benefited from a numerical artifact rather than an actual physical advantage.

## Graduate depth: integrated simulations as statistically designed experiments

### A whole model is more than the sum of verified components

Integrating mechanical, electrical, thermal, software, and operations models creates new paths through which errors propagate. A controller may assume an actuator command takes effect immediately, while the electrical and mechanical components contain delays. The individual models may be verified locally, yet their combined feedback loop oscillates. Integration therefore requires an interface contract specifying direction of data flow, physical units, update frequency, interpolation, extrapolation rules, and who owns each state. The contract is part of the experiment apparatus: changing it changes the modeled system.

Simulation output also contains several uncertainty layers. Aleatory variation represents randomness within the stated model, such as demand-arrival variability. Epistemic uncertainty reflects incomplete knowledge of parameters or model form. Numerical error comes from time steps, coupling approximations, and convergence tolerances. Experimental variation comes from random seeds and finite replications. These cannot be collapsed into one confidence interval without describing the probability framework and dependencies. A narrow Monte Carlo interval only addresses finite-sampling variability conditional on the simulation model and inputs.

### Designing comparisons that answer the decision

For comparing two dispatch policies, define a response such as the 95th-percentile time to accessible pickup, not an unqualified phrase like “better service.” Keep the operational demand scenario and service definition consistent. Using *common random numbers* means evaluating both policies under matched random arrival and travel streams. Let `D_i = Y_A,i - Y_B,i` be the paired response difference in replication `i`. The estimated mean difference is the mean of the `D_i`, with estimated standard error `s_D / sqrt(n)` if the pairs are independent across replications. Positive correlation between paired outputs can reduce variance relative to unpaired comparisons. However, poorly synchronized random streams may destroy that advantage; the coupling must be deliberate.

For nonlinear and threshold behavior, a factorial or space-filling design is often more informative than changing one factor at a time. Vary passenger arrival intensity, charger availability, ambient temperature, and dispatch logic in combinations to expose interactions. A reduced average response can coexist with a dangerous corner case; inspect tails and constraint violations. A surrogate fitted to this experiment should be evaluated on held-out parameter combinations and never assumed reliable outside its sampled design region.

### Transients, steady state, and reproducibility

An initial fleet with every vehicle fully charged represents a transient advantage. If the purpose is long-run utilization, design a defensible warm-up or steady-state assessment and document the decision rule. If the purpose is startup after an emergency, the transient is the actual phenomenon of interest and must not be discarded. For terminating mission scenarios, distinguish variability across missions from variability within one mission and use independent replications of the full episode.

A Northstar comparison might find that policy A reduces mean pickup time by two minutes while increasing missed-accessibility thresholds during peak demand. An overall average is insufficient for a policy that has hard equity or safety obligations. Publish the factor definitions, scenario seeds, initialization, solver and interface versions, output definitions, and analysis code with the result. Reproducibility means another analyst can regenerate the finding; credibility additionally requires that the experiment represents a decision-relevant situation.

## Worked engineering example from the course

A 2^(6−2) fractional factorial screens ambient temperature, payload, route traffic, rolling resistance, cooling-pump efficiency, and controller aggressiveness. Responses are energy reserve, peak battery temperature, trip-time deviation, and real-time computational load. The design reveals a strong temperature × pump-efficiency interaction that would be missed by one-factor-at-a-time analysis. Four center/nominal repeats estimate execution and stochastic variation before a focused response-surface study.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

In a co-simulation, a 0.1 s communication step across coupled fast dynamics may hide high-frequency instability. Halving the step and comparing energy, peak acceleration and event order is a minimum sensitivity check, not proof of convergence.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** For x˙=−2x, x(0)=1 and Euler step h=0.2, calculate the first two numerical states.

<details><summary>Show a reasoned solution</summary>

x1=1+0.2(−2)=0.6 and x2=0.6+0.2(−1.2)=0.36. The exact states are e^(−0.4)≈0.6703 and e^(−0.8)≈0.4493.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Runs for record begin with unresolved critical model defects.
* Factor ranges or distributions have no source or rationale.
* One-factor-at-a-time work is used where interactions are decision-relevant.
* Raw outputs, seed/configuration records, or analysis scripts are not preserved.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is a run for record?
2. Why screen first?
3. Why preserve time histories?
4. What is blocking?

<details><summary>Explain the answers</summary>

**1. What is a run for record?** An execution from an approved configuration whose result may be used as decision evidence.

**2. Why screen first?** To identify influential factors and interactions before spending runs on detailed characterization.

**3. Why preserve time histories?** Aggregates can hide modes, peaks, transients, event order, and failure mechanisms.

**4. What is blocking?** Structuring an experiment to account for known nuisance variation.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 7](../labs/lab-07-integrate-the-model-baseline-and-design-advanced-simulation-experime.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[06 — Previous chapter](06-design-interoperable-hla-fmi-federations-lvc-interfaces-and-composab.md) · [08 — Next chapter](08-model-natural-and-man-made-environments-as-dynamic-correlated-scenar.md) · [Book index](../README.md)
