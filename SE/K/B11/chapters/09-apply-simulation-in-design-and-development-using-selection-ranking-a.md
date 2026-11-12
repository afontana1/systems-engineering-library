# Chapter 09 — Apply simulation in design and development using selection, ranking, and design of experiments

*Book 11 · EN.645.757 · Foundations of Modeling and Simulation · Week 9 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 9](../labs/lab-09-apply-simulation-in-design-and-development-using-selection-ranking-a.md) → attempt the [original Week 9 assessment](../../../C/P3/EN645757.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-757-w09.md) remains available for a quick recap.

## The decision behind the theory

One-factor-at-a-time tuning misses interactions and wastes runs. **Essential question:** Which structured experiment reveals the design factors and interactions that matter to performance, risk, and robustness?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the foundations of modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

DOE organizes simulation runs so factor effects and interactions can be estimated efficiently. Simulation experiments still require randomization/seed control, replication, and residual diagnostics.

Screening designs identify influential factors; factorial designs estimate interactions; response-surface methods explore curvature near a promising region; sequential designs allocate runs based on learning.

Nuisance factors and scenarios should be blocked, stratified, or included rather than silently averaged away.

Optimization searches model space. It can exploit model defects and uncertain assumptions, so verify candidate optima with independent runs and robustness checks.

A design region or policy rule is often more defensible than a point optimum when parameters, demand, and costs are uncertain.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Analyze transient and steady-state output with defensible run controls**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Use M&S to support integration, verification, validation, and test decisions**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Ranking and selecting designs from stochastic simulation requires accounting for output variance and multiple comparisons.

### Distinguishing related ideas

The design with the lowest observed mean from a handful of runs may only be the luckiest sample.

### Interpretation and boundary conditions

A sequential experiment should spend more computational effort on close alternatives and report uncertainty in the difference, not just separate point estimates.

## Graduate depth: comparing designs under simulation uncertainty

### Selection, ranking, and optimization are different claims

A simulation can estimate performance for alternatives, but turning those estimates into a design decision introduces statistical and value judgments. *Selection* asks which candidates satisfy a criterion; *ranking* orders candidates with evidence about error; *optimization* searches a potentially large design space. These claims require different experiment designs. If a candidate must satisfy a reliability threshold, a small difference in mean throughput between candidates may be irrelevant; the probability of a constraint violation is central. If stakeholder utility combines response time and operating cost, a single simulated metric cannot identify the preferred alternative without the value model.

Write the simulation output for design `d` and random replicate `r` as `Y(d,r) = mu(d) + epsilon(d,r)`. The goal is to estimate `mu(d)` or a distributional property, not to maximize one realized `Y`. Stochastic noise can make an inferior design appear superior, especially when many designs are screened and only the observed winner is reported. This is a winner's-curse effect: selection conditions on an unusually favorable random error. Large automated searches amplify this bias even when every simulation run is internally correct.

### Paired experiments, uncertainty, and stopping rules

Common random numbers can reduce the variance of an estimated difference. Evaluate designs A and B using matched demand and weather seeds; define replicate differences `D_r = Y(A,r) - Y(B,r)`. Then `Var(mean D) = Var(D_r)/n`, where `Var(D_r) = Var(Y_A) + Var(Y_B) - 2 Cov(Y_A,Y_B)`. Positive covariance from matched disturbances can improve precision. It does not guarantee improvement: if a policy transforms events differently, the pairing may induce negative covariance or destroy interpretability. Report the replication design and inspect the differences rather than assuming that a shared seed makes all comparisons fair.

For a mean difference, an approximate confidence interval is `mean(D) +/- t * s_D/sqrt(n)`, provided the independent replicate differences justify the approximation. A confidence interval describes uncertainty of the estimator under the sampling design; it is not a probability that the alternative will work in one future event. For tail outcomes, quantiles or exceedance probabilities may require many more runs and appropriate resampling. Sequentially stopping when a preferred answer appears can invalidate ordinary fixed-sample intervals unless the stopping procedure is incorporated in the analysis.

Ranking-and-selection methods use a *practical indifference zone*: differences smaller than `delta` do not warrant claiming a winner. This improves engineering relevance because capacity, cost, and operating policies rarely justify decisions on negligible simulated differences. Yet `delta` is a stakeholder and consequence-based quantity, not a convenient statistical tolerance. Safety and regulatory constraints should be screened separately before an economic comparison. A design that is marginally faster but lacks required fault-tolerant behavior is not a viable winner.

### Example: selecting Northstar fleet capacity

Consider three fictional dispatch concepts whose estimated average wait times are 13.2, 12.7, and 12.5 minutes. Calling the third design 'best' from those point estimates alone is unwarranted. If the paired 95% interval for the third-versus-second difference in average wait is from -0.9 to +0.5 minutes, the experiment has not distinguished them meaningfully. If the third requires an additional standby vehicle, its incremental cost might dominate the uncertain average-time benefit. Conversely, if its probability of waits longer than thirty minutes drops decisively under high-demand scenarios, it may be preferred for mission reasons invisible in the mean.

The robust comparison considers at least normal demand, correlated surges, maintenance outages, and dispatch-rule errors. Compare the *same* scenario distributions across designs, preserve uncertainty about the distributions themselves, and show performance as a trade space rather than one artificially precise score. A useful result can be 'the second design is sufficient under current evidence, provided surge frequency stays below a stated bound.' That conditional conclusion is stronger than a ranking whose premises are hidden. Simulation supports the decision by exposing sensitivity and uncertainty; the program still owns value judgments, model applicability, and implementation feasibility.

## Worked engineering example from the course

A factorial experiment varies fleet size, charger count, dispatch threshold, and accessible boarding support. Fleet and dispatch have a strong interaction: the aggressive policy helps small fleets but adds little once capacity increases. A robust region of 11–12 vehicles and 4–5 chargers is recommended instead of the model’s nominal optimum of 11.3 vehicles.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Selection among three dispatch policies using the smallest sample average can be optimistic because the winner was selected on noise. Reserve confirmation replications independent of the screening experiment.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** For a theoretical M/M/1 queue λ=8/hour and μ=10/hour, calculate utilization and expected time in system.

<details><summary>Show a reasoned solution</summary>

ρ=8/10=0.8; W=1/(10−8)=0.5 hours=30 minutes. M/M/1 assumptions are restrictive.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Factor ranges include infeasible designs without controlled handling.
* A point optimum is accepted without independent confirmation.
* Interactions are ignored while making combined-factor recommendations.
* Optimization changes calibration parameters to improve performance.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is an interaction?
2. Why randomize or control run order/seeds?
3. What is a response surface?
4. Why confirm an optimum?

<details><summary>Explain the answers</summary>

**1. What is an interaction?** The effect of one factor changes depending on the level of another factor.

**2. Why randomize or control run order/seeds?** To avoid confounding factor effects with temporal or stochastic artifacts.

**3. What is a response surface?** An empirical approximation of the relationship between factors and response near a region of interest.

**4. Why confirm an optimum?** Search and noise can exploit estimation error or model defects; independent runs test reproducibility.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 9](../labs/lab-09-apply-simulation-in-design-and-development-using-selection-ranking-a.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[08 — Previous chapter](08-analyze-transient-and-steady-state-output-with-defensible-run-contro.md) · [10 — Next chapter](10-use-m-s-to-support-integration-verification-validation-and-test-deci.md) · [Book index](../README.md)

## Step 03 integrated mobility simulation case: design of experiments and selection

### Formulate factors, responses and a decision constraint

A simulation experiment tests the response surface of **a specified executable representation**. For the campus case, candidate factors include fleet size, charger count, accessible-capable fleet fraction, request intensity and travel-time stress. The current controlled experiment changes fleet size and environment only; it keeps four chargers and a one-request dispatch policy. The [configuration file](../case/model-assumptions.json) makes these omitted factors visible so no one mistakes a narrow search for a global optimum.

For each \((F,E)\), the primary response \(Y_{F,E,r}\) is the day-specific standard p90 in replication \(r\). Secondary responses include accessible p90 and fraction not picked up by close. The requirement set imposes **simultaneous** feasibility: \(Q_s\le12\), \(Q_a\le15\) and \(U<0.01\). A cheap fleet failing accessible service cannot be accepted simply because it has a favorable scalar objective. If a trade function is nevertheless proposed, hard safety and accessibility constraints need explicit sponsor and legal authority rather than a covert numerical penalty.

### A small factorial calculation

For a two-level model with \(F\in\{12,14\}\) and \(E\in\{0,1\}\), a main-effect estimate for fleet can be \(\widehat\beta_F=\tfrac12[(\bar Y_{14,0}-\bar Y_{12,0})+(\bar Y_{14,1}-\bar Y_{12,1})]\) under effects coding. The environment-by-fleet interaction is the difference of conditional fleet effects,

\[\widehat I=(\bar Y_{14,1}-\bar Y_{12,1})-(\bar Y_{14,0}-\bar Y_{12,0}).\]

This tells the reviewer whether fleet increments respond differently under stress. **Caution:** the quantity uses four *scenario means*. It is neither an event count nor a field parameter; the stress case itself is an imposed 20%/30% input change. Code reviewers should compute each mean from the [CSV](../case/replication-output.csv) rather than copying an unreferenced chart.

### Ranking and selection without self-deception

If multiple candidates meet all constraints, a ranking-and-selection experiment can seek a candidate with the smallest expected cost or delay to within an *indifference zone*. Predefine the practical improvement \(\delta\), family-wise error risk, and how many candidate comparisons will be made. Repeatedly selecting the lowest observed sample mean without addressing selection bias is a winner's-curse problem. A replication count adequate for rough baseline screening may not separate two near-ties. The current data do not demonstrate feasibility for any candidate; therefore computing a precise optimum among 8, 10, 12 and 14 would be decision theater.

When no candidate passes a requirement, use *diagnostic experiments*: compare all-accessible versus mixed fleet allocations, test charger locations with a spatial model, add driver-shift resources, or introduce pooled request routing. These are future controlled hypotheses requiring conceptual model changes and verification—not features already proved by the current demonstration. Carry forward all original failed tests rather than overwriting them with more attractive alternative results.

**Worked exercise.** Suppose four synthetic factor-cell mean p90 results are \(70,37\) minutes for fleets 12/14 at baseline and \(345,220\) for 12/14 under stress. The baseline fleet effect is \(37-70=-33\), the stress effect \(220-345=-125\), and the interaction \(-125-(-33)=-92\) minutes. **Interpretation:** the fleet addition has a greater absolute modeled benefit when the system is more congested; nevertheless 37 and 220 both miss the 12-minute target. Different inference and field validation are still needed before acting on the difference.

[Case data](../case/INDEX.html) · [Chapter 10](10-use-m-s-to-support-integration-verification-validation-and-test-deci.md).
