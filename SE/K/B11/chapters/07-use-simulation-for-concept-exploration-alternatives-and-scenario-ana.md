# Chapter 07 — Use simulation for concept exploration, alternatives, and scenario analysis

*Book 11 · EN.645.757 · Foundations of Modeling and Simulation · Week 7 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 7](../labs/lab-07-use-simulation-for-concept-exploration-alternatives-and-scenario-ana.md) → attempt the [original Week 7 assessment](../../../C/P3/EN645757.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-757-w07.md) remains available for a quick recap.

## The decision behind the theory

Simulation can compare alternatives, but only if the alternatives, scenarios, measures, and uncertainty are treated fairly. **Essential question:** What experiment set can distinguish concepts without embedding a preferred answer?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the foundations of modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

An alternative is a controlled configuration with architecture, policy, resources, and assumptions—not an undocumented set of code edits.

Use common scenario definitions and measure calculations. Different alternatives may require different implementation detail, but comparison semantics must remain stable.

Common random numbers can improve paired comparisons when outputs respond similarly to shared stochastic streams; verify that stream alignment is meaningful.

Present distributions and constraint violations, not only weighted scores. Simulation output should feed decision analysis with uncertainty and scenario context.

Robust alternatives perform acceptably across plausible conditions. A nominal winner that fails under small assumption changes may not be decision-preferred.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Model detailed operations and complete computational verification**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Analyze transient and steady-state output with defensible run controls**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Simulation-based concept exploration uses common scenarios to compare how alternatives respond to changing conditions.

### Distinguishing related ideas

A design's rank may depend on demand intensity, dispatch policy or capacity uncertainty, not simply nominal fleet size.

### Interpretation and boundary conditions

Common random inputs can reduce comparison noise, but must not conceal differences in each option's relevant operating envelope.

## Graduate depth: scenario exploration as disciplined counterfactual reasoning

### Exploration is not forecasting

Concept exploration asks how candidate systems behave under plausible combinations of conditions. A scenario is a structured statement about demand, operating policy, environment, disruption, and stakeholder constraints. It is not necessarily a prediction about how likely the future is. Treat the scenario family as a design instrument for exposing weak assumptions, not as an arbitrary collection of dramatic cases or a concealed probability forecast.

Write the feasible outcome of design `d` in scenario `s` as `Y(d,s,omega)`, where `omega` denotes random events within a scenario. The scenario-to-scenario difference measures sensitivity to chosen external conditions, while replicate-to-replicate variation measures stochastic outcome uncertainty. Collapsing both into one pooled standard deviation can obscure the source of risk. For each alternative, estimate a response surface across demand, resource outages, priority rules, and degraded interfaces. Record which dimensions are controlled choices and which are uncontrollable conditions; optimizing a controllable dispatch parameter is categorically different from assuming favorable weather.

### Explore interactions, not isolated perturbations

A one-factor-at-a-time experiment assumes that local changes approximate the behavior of combinations. That can fail when system constraints are nonlinear. For example, extra vehicles may improve wait times when chargers are plentiful but reduce service availability when they saturate a constrained charging facility. A simple two-factor experiment uses low and high fleet counts crossed with low and high charger counts. If the fleet effect differs between charger settings, there is an interaction. In a coded factorial model, `Y = beta_0 + beta_1 x_1 + beta_2 x_2 + beta_12 x_1 x_2 + epsilon`, the interaction coefficient `beta_12` captures that difference under the specified design and model assumptions.

Random events should be controlled through independent replications, and common random numbers can help compare alternatives subjected to matched disturbances. However, fixed seeds do not remove uncertainty about scenario likelihoods, omitted structural mechanisms, or errors in the input distributions. Screening experiments can identify factors worth deeper study, but the validity region of a discovered relationship must be stated. In particular, extrapolating a response surface beyond its sampled capacity range is not a verified engineering prediction.

### Robustness, feasibility, and regret

A design that wins in the nominal scenario may perform badly under a rare but consequential disruption. Define a hard feasibility indicator `F(d,s)` for safety, accessibility, interoperability, and resource limits. Evaluate preferences only among designs satisfying the required constraints in the relevant scenarios. For uncertain consequences, one useful diagnostic is scenario regret: `R(d,s) = U(d_star(s),s) - U(d,s)`, where `d_star(s)` is the best eligible alternative if scenario `s` were known in advance. Minimax regret can expose fragile solutions, but it is not automatically the right decision rule when probabilities or risk preferences are credible.

For Northstar, suppose an optimized dispatch rule yields excellent normal-day response time but fails during correlated service outages. A slightly less efficient rule may preserve accessible emergency trips under both cases. Neither result proves its real-world superiority until model applicability, scenario coverage, and implementing authority are examined. The strongest output of exploration may be a *region* of feasible architecture choices with explicit triggers for revisiting the design. Carry the scenario definitions and sensitivity evidence into subsequent integration tests instead of converting the preferred model output into a guaranteed field-performance number.

## Worked engineering example from the course

A 10-vehicle concept with aggressive dispatch beats a 12-vehicle concept on mean wait time in one seed. Across paired replications and event-demand scenarios, the 12-vehicle concept has lower tail waits but higher cost, while the policy-focused concept is more sensitive to charger outage. The result becomes a tradeoff, not a single winner.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

For alternatives A and B, use the same random arrivals in paired simulation runs to reduce the variance of the difference. But shared random numbers do not justify treating outputs from one run as independent observations.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** For a theoretical M/M/1 queue λ=8/hour and μ=10/hour, calculate utilization and expected time in system.

<details><summary>Show a reasoned solution</summary>

ρ=8/10=0.8; W=1/(10−8)=0.5 hours=30 minutes. M/M/1 assumptions are restrictive.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Alternatives are compared using different demand or measure definitions without disclosure.
* One seed or one run determines the ranking.
* Simulation output is converted directly to a final decision with no value/risk context.
* A favored alternative receives more favorable assumptions.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. Why use common scenarios?
2. What can common random numbers reduce?
3. What is robustness?
4. What is dominance?

<details><summary>Explain the answers</summary>

**1. Why use common scenarios?** To ensure differences arise from alternatives rather than inconsistent environmental conditions.

**2. What can common random numbers reduce?** Variance in estimated differences when paired stochastic inputs are meaningfully aligned.

**3. What is robustness?** Acceptable performance across plausible assumptions, scenarios, and uncertainty.

**4. What is dominance?** One alternative is no worse on all relevant objectives and better on at least one, under the stated conditions.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 7](../labs/lab-07-use-simulation-for-concept-exploration-alternatives-and-scenario-ana.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[06 — Previous chapter](06-model-detailed-operations-and-complete-computational-verification.md) · [08 — Next chapter](08-analyze-transient-and-steady-state-output-with-defensible-run-contro.md) · [Book index](../README.md)
