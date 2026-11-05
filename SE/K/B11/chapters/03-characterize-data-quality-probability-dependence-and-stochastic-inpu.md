# Chapter 03 — Characterize data quality, probability, dependence, and stochastic input models

*Book 11 · EN.645.757 · Foundations of Modeling and Simulation · Week 3 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 3](../labs/lab-03-characterize-data-quality-probability-dependence-and-stochastic-inpu.md) → attempt the [original Week 3 assessment](../../../C/P3/EN645757.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-757-w03.md) remains available for a quick recap.

## The decision behind the theory

A simulation can be perfectly coded and still be misleading because its inputs are wrong. **Essential question:** How should observed variability and data limitations be represented without inventing confidence?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the foundations of modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Data quality is fitness for an intended model use, not an intrinsic label. A dataset may be adequate for average demand but inadequate for tail waits or disruption behavior.

Explore before fitting. Plot time order, histograms, ECDFs, quantiles, groups, censoring, missingness, and relationships. Operational changes may create mixtures or nonstationarity.

Goodness-of-fit combines visual diagnostics, statistical measures, physical support, tail behavior, and consequences. A high p-value does not prove truth; a low p-value may reflect large sample size or minor harmless differences.

Dependence matters. Arrival volume, weather, trip duration, boarding, charging, and disruption may share causes. Model correlation or conditional structure where it changes decisions.

Sparse inputs should be represented with ranges, scenarios, expert elicitation, or parameter uncertainty—not hidden behind a precise point estimate.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Develop the M&S plan and conceptual model before implementation**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Use M&S for needs, opportunity, current-state, and baseline analysis**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Stochastic inputs must represent the arrival, service and failure processes that cause variation in the real setting.

### Distinguishing related ideas

Matching an average and variance does not establish tail behavior or dependence; rare bursts can dominate congestion even when mean demand seems moderate.

### Interpretation and boundary conditions

Parameter uncertainty, intrinsic randomness and scenario uncertainty should be kept separate so additional data is not mistaken for a cure for an incomplete model.

## Deeper theory: stochastic inputs are a claim about the world

A simulation does not become realistic merely because it draws random numbers. Its random inputs constitute a theory about where variability originates, how it is observed, and which outcomes can occur together. This distinction is especially important for the Northstar mobility service. Trip requests may arrive in clusters after a lecture ends; trip durations may lengthen in bad weather; and communication outages may coincide with the very conditions that increase demand. Drawing independent values from convenient distributions can produce a smooth-looking model while eliminating the combinations of events that matter most to service reliability.

### Random variables, observation, and the meaning of a distribution

A random variable maps an uncertain event to a numerical value. Its probability distribution is not the physical mechanism itself but a representation of uncertainty about that mechanism. An empirical histogram describes the collected observations; a fitted probability law asserts that a family of distributions is adequate beyond those observations. For example, an exponential interarrival model implies a memoryless arrival process under its usual Poisson-process interpretation. If a lecture bell synchronizes hundreds of riders, that assumption fails even when the average arrival rate is estimated correctly.

Suppose the mean arrival rate is 12 requests per hour. An exponential interarrival law has mean five minutes and standard deviation five minutes. A deterministic arrival process with one request every five minutes has exactly the same mean but no interarrival variability. The two systems may have radically different waiting-time behavior when service capacity is constrained. The input model must therefore describe at least the aspect of variability to which the decision is sensitive. Matching the mean alone is rarely sufficient.

In data analysis, distinguish **aleatory variability** from **epistemic uncertainty**. Aleatory variability is the variation the model represents among trips or operating days. Epistemic uncertainty concerns the modeler's imperfect knowledge of rates, tails, dependence, or mechanisms. Additional observations may reduce parameter uncertainty without eliminating day-to-day randomness. If an analyst samples one plausible arrival-rate parameter for an entire day and then simulates requests conditional on that rate, the model expresses a different hypothesis from resampling the rate independently for every request. The former creates correlated demand within the day; the latter often destroys that dependence.

### Dependence is an architectural property of uncertainty

For two random delays \(X\) and \(Y\),

\[\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y).\]

This identity explains why latency budgets assembled from individually measured components can be misleading. If a weather event slows the network and lengthens vehicle approach times, the covariance may be positive. An independence assumption sets the covariance to zero by fiat. The result can be an understatement of total-delay variability and of the probability of exceeding a mission deadline. Correlation is not itself causation, but it is evidence that a joint model may be needed. A causal input model explains which shared conditions generate the dependence.

Dependence also appears in **sampling design**. Ten thousand events observed during one uninterrupted weekday are not ten thousand independent observations of seasonal service. Those observations may be highly informative about that weekday's within-day pattern yet weak evidence about holidays, equipment failures, and unusual demand. The sample frame—when, where, and under what operating configuration measurements were taken—determines the claim the data can support.

### Tail behavior and plausible but dangerous models

Engineering risk is often concentrated in low-frequency combinations. A lognormal trip-duration model and a truncated normal model can fit the central 90% of a dataset similarly while assigning very different probabilities to unusually long trips. When the quantity of interest is the 99th-percentile response time or the chance that all vehicles are occupied, tail assumptions may dominate the decision. There is no universally best distribution; the family must be defended in relation to physical bounds, generation mechanisms, and the amount of tail evidence available.

A useful conceptual separation is between **input calibration** and **output validation**. Matching a fitted arrival histogram establishes little about whether the simulated system reproduces actual waiting-time behavior. The latter also depends on dispatch policy, capacity, priority logic, and how resources are released. A perfectly calibrated input can still be coupled to an invalid process model. Conversely, apparent output agreement can result from compensating errors: an underestimated demand rate masked by an underestimated service time. The best model is not simply the one whose outputs resemble a few observations; it is one whose assumptions and mechanisms are credible for the decision's intended use.

The deeper lesson is that an input dataset is a collection of conditional statements about a world, not a neutral set of numbers. A defensible simulation identifies those conditions, carries uncertainty through the calculation without erasing shared causes, and reports which conclusions survive alternative input hypotheses.

## Worked engineering example from the course

Accessible boarding times are pooled across vehicle designs. A lognormal fit looks acceptable, but the newer ramp design has a different median and variability. The model stratifies by vehicle type and carries parameter uncertainty for the smaller sample instead of using one pooled distribution.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

If arrivals are Poisson with rate 6/hour, exponential interarrivals have mean 10 minutes. But a class-change burst breaks stationary Poisson assumptions; fitted input distributions must preserve time-of-day structure and common environmental causes.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** For a theoretical M/M/1 queue λ=8/hour and μ=10/hour, calculate utilization and expected time in system.

<details><summary>Show a reasoned solution</summary>

ρ=8/10=0.8; W=1/(10−8)=0.5 hours=30 minutes. M/M/1 assumptions are restrictive.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Pooled or transformed data are used without documenting the operation.
* A fitted distribution has impossible support or hidden truncation.
* Critical dependence is assumed away without sensitivity analysis.
* Sparse data are presented as precise knowledge.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is aleatory variability?
2. What is epistemic uncertainty?
3. Why use an empirical distribution?
4. What is nonstationarity?

<details><summary>Explain the answers</summary>

**1. What is aleatory variability?** Inherent or treated-as-random variation in the modeled process.

**2. What is epistemic uncertainty?** Lack of knowledge about model form, parameters, data, or conditions that could be reduced or bounded.

**3. Why use an empirical distribution?** When data support is adequate and imposing a parametric family adds unjustified structure.

**4. What is nonstationarity?** A process whose distribution or parameters change over time or condition.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 3](../labs/lab-03-characterize-data-quality-probability-dependence-and-stochastic-inpu.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[02 — Previous chapter](02-develop-the-m-s-plan-and-conceptual-model-before-implementation.md) · [04 — Next chapter](04-use-m-s-for-needs-opportunity-current-state-and-baseline-analysis.md) · [Book index](../README.md)
