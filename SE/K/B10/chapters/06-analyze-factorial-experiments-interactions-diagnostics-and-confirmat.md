# Chapter 06 — Analyze factorial experiments, interactions, diagnostics, and confirmation evidence

*Book 10 · EN.645.756 · Metrics, Modeling and Simulation for Systems Engineering · Week 6 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 6](../labs/lab-06-analyze-factorial-experiments-interactions-diagnostics-and-confirmat.md) → attempt the [original Week 6 assessment](../../../C/P3/EN645756.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-756-w06.md) remains available for a quick recap.

## The decision behind the theory

A factorial experiment is valuable because it reveals interactions and supports efficient learning, but only when its analysis respects the design. **Essential question:** Which factor combinations materially change performance, and how strong is the evidence?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the metrics, modeling and simulation for systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Fit the planned model before searching many alternatives. Preserve factor coding, block terms, interaction hierarchy, and the correct experimental error structure.

Main effects average across other factors. When interaction is important, report conditional effects and engineering regions rather than one global main-effect statement.

ANOVA partitions variation under a model; it does not establish practical importance or prove assumptions. Pair it with effect estimates, intervals, plots, residual diagnostics, and decision thresholds.

For fractional designs, list the alias structure and avoid naming an effect as identified when it is confounded with another plausible term. Fold-over or follow-up runs may be necessary.

Confirmation runs should occur at selected and comparison settings, preferably under new time or operational conditions, and should test prediction rather than merely repeat the fitting data.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Design efficient experiments with factors, responses, noise, power, randomization, and blocking**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Build and validate performance response models across use and environment**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Factorial experiments estimate both main effects and interactions by comparing responses across controlled combinations of factors.

### Distinguishing related ideas

Optimizing one factor at a time can miss reversal: changing dispatch priority may help under low demand but harm under high demand.

### Interpretation and boundary conditions

Randomization, blocking and repetition protect causal interpretation when nuisance conditions and stochastic outputs vary.

## Deeper theory: interpreting factorial interactions as engineering mechanisms

A factorial experiment produces estimates of effects, but engineering understanding requires an explanation of why those effects vary across conditions. A main effect summarizes an average contrast across levels of other factors. An interaction describes **nonadditivity**: the effect of one factor changes with another. These statistical terms should be connected to mechanisms in the engineered system rather than interpreted as properties of coefficients alone.

Consider two Northstar factors: \(A\), fleet capacity (low or high), and \(B\), connectivity quality (good or degraded). Let the response be average passenger delay in minutes. Suppose the four illustrative cell means are \(Y_{--}=30\), \(Y_{+-}=18\), \(Y_{-+}=44\), and \(Y_{++}=40\), where the first sign indicates low/high capacity and the second indicates good/degraded connectivity. Under good connectivity, increasing capacity improves delay by 12 minutes; under degraded connectivity, it improves delay by only 4 minutes. The capacity effect depends on the information infrastructure. The interaction contrast is \((-4)-(-12)=8\) minutes when differences are oriented as high-minus-low. The specific sign convention depends on coding, but the operational meaning is clear: extra vehicles do less good when dispatch lacks timely information.

### Why averages can conceal system-level failure

A main-effect estimate for capacity averages the change across connectivity conditions. It could be statistically convincing and still be misleading for a deployment where degraded connectivity is common. The engineer should inspect interaction plots and condition-specific effects before recommending fleet expansion. A larger fleet may shift a bottleneck rather than resolve it. A factorial design is valuable precisely because it exposes **complementarity and substitution** among subsystems that isolated tests can miss.

Mathematically, a two-factor linear model with coded levels \(a,b\in\{-1,+1\}\) can be expressed as \(Y=\beta_0+\beta_A a+\beta_B b+\beta_{AB}ab+\epsilon\). The product term \(ab\) allows the slope associated with \(A\) to depend on \(B\). The coefficient \(\beta_{AB}\) is not the whole scientific claim: it is a compact representation of measured nonadditivity over the chosen levels. Transforming the response, changing the factor range or incorporating nonlinear behavior can change the coefficient's interpretation.

### Residual diagnostics ask whether the model is credible

A fitted factorial model may assume constant residual variance, independent errors and an adequate mean structure. If low-capacity configurations become unstable under peak demand, the output distribution may be strongly skewed and heteroscedastic; a simple additive-error linear model may describe the center poorly. Residual plots, replication-level variability and scenario-specific inspection reveal whether the apparent precision is realistic. In simulation studies, runs may share random seeds or warm-up histories; that dependence must be accounted for rather than ignored.

A statistically small p-value also does not establish a useful engineering improvement. A reduction of 0.1 minute in average wait may be detectable with enough synthetic replications yet irrelevant to the mission. Conversely, a safety-relevant failure occurring in a rare state can be operationally decisive while too infrequent for a conventional small factorial experiment to estimate precisely. Choice of response and design range should follow the engineering decision, not the convenience of a standard analysis table.

### Blocking and randomization support interpretation

If experiments are run over several hardware configurations or demand periods, blocking can separate known environmental variation from the effects under study. Randomization reduces systematic alignment of unmeasured effects with factor settings. These design choices are not postprocessing conveniences; they determine which causal interpretations are defensible. An analysis cannot recover full identifiability from a dataset in which every high-capacity test occurred after a major software upgrade, with no comparable control conditions.

### Confirmation is different from discovery

Exploratory factorial experiments are excellent for discovering interactions and surprising response patterns, but the strongest discovered effects may be exaggerated by selection from many comparisons. Confirmation should evaluate a pre-specified implication on new scenarios or replications. If the proposed mechanism is that stale data limits the value of additional vehicles, a confirmation experiment could vary data freshness independently of fleet size and examine the predicted recovery of the capacity benefit. The aim is not simply another significant coefficient; it is a successful prediction from a causal explanation.

Finally, an experiment's conclusions are bounded by its design space. A two-factor study cannot establish a full mission-level claim if accessibility, battery depletion, human intervention and weather are omitted. It can provide valuable evidence about the interaction it was designed to investigate, provided those boundaries are stated. Factorial analysis becomes an engineering discipline when coefficients are translated into **mechanisms, decisions, uncertainty and testable predictions**.

## Worked engineering example from the course

Analysis finds little average benefit from battery preconditioning, but a strong temperature-by-preconditioning interaction: negligible above 10°C and substantial below 0°C. Dispatch policy also interacts with passenger load. A main-effects-only recommendation would have rejected preconditioning. Diagnostics reveal increasing variance at high demand, so the analysis uses a transformed or heteroscedasticity-aware model and reports conditional prediction intervals. Confirmation runs in a later cold-weather block support the interaction within stated uncertainty.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Four cell means are A−B−:18, A+B−:13, A−B+:14, A+B+:7 minutes. The effect of factor A averages (13+7)/2 − (18+14)/2 = −6 minutes. The interaction contrast (7−13)−(14−18)=−2 minutes; a main effect alone hides the policy dependence.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** An event occurs 0 times in n=30 independent Bernoulli trials. Compute the exact one-sided 95% upper failure-probability bound.

<details><summary>Show a reasoned solution</summary>

p_upper = 1−0.05^(1/30) ≈ 0.0950. The result does not demonstrate failure probability below 1%.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* A decision-critical interaction is omitted solely because its p-value or main effect is inconvenient.
* An aliased effect is described as uniquely identified.
* ANOVA p-values are reported without effect estimates, intervals, and diagnostics.
* Confirmation uses the same fitting data or conditions and is called independent evidence.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What does a main effect represent?
2. Why preserve model hierarchy?
3. What is aliasing?
4. What is lack of fit?

<details><summary>Explain the answers</summary>

**1. What does a main effect represent?** The average change associated with a factor across the levels of other factors in the fitted design.

**2. Why preserve model hierarchy?** Including an interaction generally requires retaining its component main effects for coherent interpretation.

**3. What is aliasing?** Confounding of model terms such that the design cannot estimate them separately.

**4. What is lack of fit?** Evidence that the chosen model form does not adequately describe the response beyond pure experimental error.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 6](../labs/lab-06-analyze-factorial-experiments-interactions-diagnostics-and-confirmat.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[05 — Previous chapter](05-design-efficient-experiments-with-factors-responses-noise-power-rand.md) · [07 — Next chapter](07-build-and-validate-performance-response-models-across-use-and-enviro.md) · [Book index](../README.md)


## Extended worked problems and lab

Study the [worked problem workshop on factorial effects and interactions](../practice/factorial.md), then complete the [extended laboratory](../practice/lab-factorial.md). The exercises are separate from the original assessed coursework.
