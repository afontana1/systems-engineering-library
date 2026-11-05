# Chapter 05 — Design efficient experiments with factors, responses, noise, power, randomization, and blocking

*Book 10 · EN.645.756 · Metrics, Modeling and Simulation for Systems Engineering · Week 5 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 5](../labs/lab-05-design-efficient-experiments-with-factors-responses-noise-power-rand.md) → attempt the [original Week 5 assessment](../../../C/P3/EN645756.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-756-w05.md) remains available for a quick recap.

## The decision behind the theory

Observational data can reveal association but often cannot separate configuration, environment, and operational causes. **Essential question:** What experiment will produce enough information to support the engineering decision without wasting runs or creating avoidable bias?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the metrics, modeling and simulation for systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Start with the decision and minimum consequential effect. A design should be able to estimate the effect or interaction that could change the decision, not merely fit within an arbitrary run budget.

The experimental unit is the smallest unit independently assigned to a treatment. Repeated sensor samples within one vehicle-run are not independent replicates of the operating policy.

Randomization protects against unknown time trends and assignment bias. Blocking removes known nuisance variation from the error term. Replication estimates variability and improves precision. These are design protections, not optional statistical decorations.

Interactions are central in systems engineering: temperature may change the benefit of preconditioning; passenger load may change the effect of dispatch policy; charger type may interact with battery age. Design for them explicitly.

Operational constraints may require split-plot, repeated-measures, or blocked designs. Document restrictions and use an analysis consistent with the randomization structure.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Use estimation, confidence intervals, hypothesis, equivalence, and engineering significance**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Analyze factorial experiments, interactions, diagnostics, and confirmation evidence**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Experimental design separates causal effects from coincidence

A factorial experiment changes several factors systematically so the response can reveal both individual effects and interactions. An interaction exists when the effect of one factor depends on the level of another. For example, adding vehicles may reduce waiting time under normal network latency but have little effect when dispatch messages are delayed. A one-factor-at-a-time study can miss that dependency entirely.

Randomization protects against unsuspected time trends or environmental changes becoming confounded with a chosen factor. Blocking removes variation from known nuisance conditions, while replication estimates residual variability. These are not ceremonial statistical steps; each protects a different inference. The design should begin with a mechanism worth investigating and a response meaningful to the engineering decision. Statistical significance is not the same as operational importance: a tiny effect can be detected reliably yet remain irrelevant to capacity planning.

## Deeper theory: experimental design as a strategy for separating causal mechanisms

An experiment is not simply a collection of test cases. It is an intervention designed to distinguish explanations that observational data cannot reliably separate. In complex engineering systems, outputs depend on configuration, environment, demand, human behavior and measurement noise. If these influences change together, a performance difference cannot be attributed confidently to the design change under examination. Experimental design organizes variation so that the effect of interest is **identifiable** under explicitly stated assumptions.

A **factor** is an input intentionally varied across experimental conditions; a **response** is an observed outcome; a **noise variable** influences the response but is not necessarily the target of the decision. In a shuttle simulation, factors might include fleet size and dispatch policy, while background demand and trip lengths vary across scenarios. If the high-capacity fleet is always tested on low-demand days and the low-capacity fleet on high-demand days, fleet size is confounded with demand. A difference in average delay cannot be interpreted as a fleet effect alone.

### Randomization is a defense against systematic bias

Random assignment breaks systematic association, in expectation, between treatment choice and uncontrolled factors. It does not guarantee perfectly balanced groups in one finite experiment, and it does not repair a measurement that excludes failed trips. **Blocking** handles known variation by comparing treatments within more homogeneous groups, such as route category or peak/off-peak condition. This can reduce noise and improve precision when blocks explain substantial variation. Blocking must be represented in the analysis; otherwise the design's intended precision gain may not be realized.

In computational experiments, the random-number streams also require attention. To compare two dispatch policies fairly, running both against the same set of synthetic demand realizations can reduce comparison variance through **common random numbers**. The paired difference for demand realization \(i\) is \(D_i=Y_i(A)-Y_i(B)\). The variance of its sample mean is \(\mathrm{Var}(\bar D)=\mathrm{Var}(D)/n\), and \(\mathrm{Var}(D)=\mathrm{Var}(Y_A)+\mathrm{Var}(Y_B)-2\mathrm{Cov}(Y_A,Y_B)\). Positive covariance can improve precision, but the pairing must represent comparable conditions and preserve valid stochastic behavior.

### Factorial designs reveal interactions

A one-factor-at-a-time experiment can miss mechanisms in which the effect of one input depends on another. Suppose fleet size is either small or large and route information is either fresh or delayed. A larger fleet may improve service substantially with fresh information but barely help when dispatch decisions use stale data. That is an **interaction**, not noise. In a \(2^2\) factorial design with coded levels \(-1,+1\), the difference in effects across the second factor provides an interaction contrast. Its magnitude and sign convey how the system responds to combinations rather than isolated changes.

However, factorial coefficients are not universal physical constants. Their interpretation depends on the selected factor levels, response scale, randomization, model form and unmeasured interactions. A two-level design can identify local directional effects but may fail to reveal curvature or thresholds. A strong empirical result near one operating point may not extrapolate to rare weather events or an overloaded region.

### Power is about the decision-relevant difference

An experiment should be designed around the size of an effect that would matter for the engineering decision. With too few independent runs, the estimate may be so uncertain that a practically important difference remains unresolved. With enormous runs, a trivially small difference may become statistically detectable while having no operational importance. The distinction between **statistical significance** and **engineering significance** should be established before interpreting results.

The experiment's unit of independence matters. Ten million events produced inside one simulation replication are not necessarily ten million independent observations. They may share one generated demand history and one initial condition. Treating individual events as independent replications is pseudoreplication and can make confidence intervals absurdly narrow. In a real field experiment, passengers on the same route or vehicles managed by the same dispatcher may have correlated outcomes. Designs should reflect clustering and interference rather than merely count observations.

### A good experiment makes failure interpretable

Acceptance tests often ask whether a threshold was met. Experimental design asks *why* performance changed and *what competing explanations remain*. A robust experiment documents its causal model, factor ranges, nuisance conditions, randomization, blocking, calibration, exclusion rules and planned analysis. It also plans how to interpret unexpected results. If the estimated treatment effect reverses across route categories, averaging it into a single favorable score may erase the very phenomenon the engineering decision needs to address.

The graduate-level skill is not to memorize named design patterns. It is to construct a study in which alternative mechanisms make distinguishable predictions—and to know when the data are too entangled to support the desired causal claim.

## Worked engineering example from the course

The team proposes comparing two dispatch policies on consecutive weeks. That design confounds policy with weather, demand, learning, and fleet condition. The revised experiment uses vehicle-day experimental units, randomizes policy within blocks defined by route and demand period, includes temperature and battery-age factors, repeats each combination, and predeclares wait-tail and energy responses. A simulation-based precision study shows the run count needed to detect a 1.5-minute 90th-percentile improvement.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A two-factor experiment varies vehicles (2,3) and dispatch policy (FIFO,priority). Replicate each of four cells and randomize run order. If storm severity changes through the day, blocking by weather prevents systematic confounding of policy with storm exposure.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A sample of 25 independent results has mean 14 min and sample standard deviation 5 min. Estimate a 95% t interval for the population mean using t(24)≈2.064.

<details><summary>Show a reasoned solution</summary>

Standard error = 5/√25=1; interval ≈ 14±2.064, or [11.936,16.064] minutes, under the sampling assumptions.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Repeated measurements are counted as independent treatment replicates.
* Policy is confounded with time, route, vehicle, or weather without mitigation.
* The design cannot estimate a decision-critical interaction.
* Run count is selected without an engineering effect size or precision target.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is an experimental unit?
2. Why randomize?
3. What does blocking do?
4. What is pseudoreplication?

<details><summary>Explain the answers</summary>

**1. What is an experimental unit?** The smallest unit independently assigned to a treatment or condition under the design.

**2. Why randomize?** To reduce assignment bias and distribute unknown nuisance effects, supporting valid causal comparisons.

**3. What does blocking do?** Groups similar experimental units or runs so known nuisance variability is separated from treatment comparison.

**4. What is pseudoreplication?** Treating nonindependent repeated observations as independent experimental units.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 5](../labs/lab-05-design-efficient-experiments-with-factors-responses-noise-power-rand.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[04 — Previous chapter](04-use-estimation-confidence-intervals-hypothesis-equivalence-and-engin.md) · [06 — Next chapter](06-analyze-factorial-experiments-interactions-diagnostics-and-confirmat.md) · [Book index](../README.md)
