# Chapter 09 — Design computational experiments to learn efficiently from the design space

*Book 14 · EN.645.784 · Decision Science and Analytics in Systems Engineering · Week 9 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 9](../labs/lab-09-design-computational-experiments-to-learn-efficiently-from-the-desig.md) → attempt the [original Week 9 assessment](../../../C/P3/EN645784.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-784-w09.md) remains available for a quick recap.

## The decision behind the theory

High-fidelity analyses are often too expensive for exhaustive search. **Essential question:** Which design points should be evaluated so that the team learns about effects, interactions, curvature, and promising regions with defensible effort?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the decision science and analytics in systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Begin with the decision question and analysis budget. Screening designs find influential factors; factorial designs estimate interactions; response-surface designs model curvature; space-filling designs support global surrogates.

Computational experiments do not need physical randomization for the same reason as field trials, but randomized execution can reveal infrastructure/time effects and protect against hidden run-order artifacts.

Replicate stochastic simulations or use controlled common random numbers according to the comparison goal. Record failed, infeasible, and censored runs.

Coverage should be assessed in the transformed input space and within each architecture family, not only globally.

Use sequential design: analyze the first campaign, diagnose gaps, then add points where decision value or predictive uncertainty warrants.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Formulate parametric design and conduct multiobjective search**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Build, validate, and use surrogate models without hiding approximation error**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Computational experiment design chooses evaluations to maximize insight about a design space under limited resources.

### Distinguishing related ideas

Uniformly sampling every parameter may spend effort where responses are smooth and miss nonlinear transitions near failure boundaries.

### Interpretation and boundary conditions

Space-filling designs, adaptive sampling and targeted verification answer different kinds of uncertainty and should be selected deliberately.

## Graduate depth: experimental design for expensive simulation models

### Learning from a design space is a statistical problem

In computational engineering, each run has a cost and a position in the input space. A large number of arbitrary runs does not guarantee broad learning. Let a deterministic or stochastic model be `y = f(x_1,...,x_k, z)`, where `x` are design controls and `z` are uncertain operating conditions. The purpose of an experiment is to estimate behavior relevant to a decision: main effects, interactions, constraint boundaries, sensitivity, or evidence for a candidate design. The experimental plan must reflect that purpose and the feasible region rather than simply filling a parameter table.

One-factor-at-a-time sweeps can estimate local changes while holding other inputs fixed, but they can miss interactions. If battery size affects range differently under cold weather than warm weather, the joint battery-weather effect matters. A two-level factorial design separates main effects and interactions under an explicit effect model; fractional factorial designs economize runs but intentionally alias some effects. An aliased effect cannot be interpreted uniquely without further assumptions or follow-up experiments. This is a trade between learning efficiency and identifiability, not a statistical defect to conceal.

### Space filling, replication, and model uncertainty

Latin hypercube and other space-filling designs seek coverage when little is known about response shape. They can reveal curvature or unexpected failure regions, but they do not automatically achieve accurate estimates of extreme probabilities. When simulation is stochastic, independent replication at the same design point estimates noise; sampling many distinct points once estimates a mixture of response variation and noise. A suitable design often uses both exploration points and replication sites so a surrogate or regression model can distinguish these sources.

The distinction matters for surrogate modeling. A regression fit `y_hat(x)` introduces approximation error in addition to the simulator's uncertainty and the real system's uncertainty. Predictive performance must be assessed with held-out design points, preferably including boundary and high-consequence regions. Training error is optimistically biased for model selection. Adaptive sampling can target points where predicted decision benefit or uncertainty is high, but a search that only visits promising regions risks overlooking disconnected feasible islands or severe constraint failures elsewhere.

### Sensitivity and robust design

A response surface is not automatically a causal model. Varying an input inside a simulator measures the consequences of the simulator's equations under the chosen interventions; causal validity depends on the correctness of those equations and whether the intervention is physically feasible. An apparently dominant input may be a placeholder for omitted mechanisms. Standardized effects can ease comparison across differently scaled factors, but sensitivity also depends on chosen ranges and correlations. If design factors are physically coupled, sampling impossible combinations produces misleading conclusions.

Robust design separates decisions within the engineer's control from environmental variation that the engineer must tolerate. One might seek designs minimizing expected operating cost subject to `P(wait > 15 min) <= alpha` across specified demand scenarios. Estimating a small exceedance probability accurately can require many samples, alternative importance-sampling methods, or conservative bounds. Report uncertainty around the probability and any error introduced by a surrogate. Passing a noisy estimated constraint at 4.9% when the limit is 5% is not proof of compliance.

### Northstar experiment logic

For Northstar, consider dispatch fleet size, charging capacity, and routing rule as controls; event intensity and degraded communications as environmental factors. A screening design can identify major interactions, after which a focused experiment near the capacity boundary can estimate the probability of unacceptable delay. Common random numbers support fair comparisons between candidate policies, but each candidate must also face independent replications for final uncertainty estimates. Reserve out-of-sample scenarios to challenge the selected solution.

The final result should explain where the design was tested, which interactions were resolved, what model and observation errors remain, and how the decision changes under alternative factor ranges. Computational experiments are an instrument for structured learning, not a device for laundering the uncertainty of simulated worlds into certainties about deployed systems.

## Worked engineering example from the course

A two-stage campaign first screens fleet size, chargers, reserve ratio, zones, demand multiplier, and disruption rate. Fleet-by-charger and demand-by-reserve interactions are large. A second Latin-hypercube campaign concentrates on feasible high-service regions and balances samples across three architecture families.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A Latin hypercube can cover input ranges more evenly than equal-size plain random samples, but not automatically reproduce correlated inputs. Experiment design should match the response surface and target decision region.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** Alternative A scores 0.8 on cost and 0.6 on reliability, while B scores 0.5 and 0.9. At cost weight w, derive the preference switching point.

<details><summary>Show a reasoned solution</summary>

A=0.6+0.2w; B=0.9−0.4w. Equate them: 0.6w=0.3, so w=0.5. Feasibility and scaling of value scores remain separate questions.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* The design cannot estimate a claimed effect.
* Failed runs are silently dropped.
* One architecture family dominates the sample without rationale.
* Stochastic noise is confused with factor effect.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is confounding?
2. What is a screening design?
3. What is a response-surface design?
4. Why use a Latin hypercube?

<details><summary>Explain the answers</summary>

**1. What is confounding?** When effects cannot be separately estimated from the chosen design.

**2. What is a screening design?** A design intended to identify influential factors efficiently, often with limited interaction resolution.

**3. What is a response-surface design?** A design supporting estimation of curvature and local response behavior.

**4. Why use a Latin hypercube?** To obtain stratified space-filling coverage of continuous inputs.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 9](../labs/lab-09-design-computational-experiments-to-learn-efficiently-from-the-desig.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[08 — Previous chapter](08-formulate-parametric-design-and-conduct-multiobjective-search.md) · [10 — Next chapter](10-build-validate-and-use-surrogate-models-without-hiding-approximation.md) · [Book index](../README.md)

## Step 03 integrated NS-DA14.1 decision-analysis laboratory: Chapter 09

### Factorial experiments separate effects and interactions

A design of experiments (DOE) should target a question, not merely populate a CSV. For a transparent initial study fix hybrid architecture, priority dispatch, human operation, four zones and 18 mph, then evaluate a full \(2^3\) factorial over fleet \(n\in\{12,18\}\), chargers \(c\in\{4,8\}\) and reserve \(r\in\{0.10,0.20\}\). The resulting [eight-run matrix](../case/factorial-doe.csv) uses the same deterministic synthetic response function as the design enumeration. It has no Monte Carlo replications or stochastic confidence bounds, because the oracle is deterministic.

### Derive main effects correctly

Code factors \(x_n,x_c,x_r\in\{-1,+1\}\). For observed response \(y\), the two-level *effect* for chargers is \(\bar y_{x_c=+1}-\bar y_{x_c=-1}\); the associated regression coefficient is half of that effect. Interactions are not nuisance noise: \(\hat\beta_{nc}=\frac{1}{8}\sum_j x_{n,j}x_{c,j}y_j\). For example, at fleet 12 and reserve 0.10, going from four to eight chargers reduces modeled wait from **20.3406** to **17.6526** minutes, an effect of **−2.6880 min**. At fleet 18 with 10% reserve it falls from **18.0456** to **14.0136**, an effect of **−4.0320 min**. These differ because the response formula includes \(n_{active}/(c+1)\); report charger-by-fleet interaction instead of claiming a universal benefit of four more chargers.

### Sequential campaign and model diagnostics

The factorial's two reserve levels cannot identify an interior curvature effect. A next round could add reserve 0.15, charger count 6 and fleet 14, or select points near the wait and cost eligibility boundaries. Reserve levels are inputs, not empirical probabilities. Define failure handling: a model error should be recorded as a failed run with the exact config, never imputed as an attractive outcome. Randomize the **execution order** when experiment noise or drift is possible; here deterministic runs still get stable run IDs for traceability. If a real discrete-event simulator replaces the oracle, allocate replication seeds and compute uncertainty in each outcome before constructing effects.

**Exercise and solution.** From the two stated fleet-12 results at reserve 0.10, compute the mean wait reduction per added charger, assuming an average slope across that interval. **Solution:** \((17.6526-20.3406)/(8-4)=\mathbf{-0.6720}\) minute per charger. This is a *secant*, not the derivative or a validated estimate beyond chargers 4–8. Because the formula is nonlinear in chargers, extrapolating it to ten chargers without checking the oracle is unjustified. A recommendation needs cost, reliability, reserve and emissions consequences as well as wait change.
