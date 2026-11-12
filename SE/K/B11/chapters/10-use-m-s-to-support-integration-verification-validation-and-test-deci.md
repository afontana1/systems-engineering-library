# Chapter 10 — Use M&S to support integration, verification, validation, and test decisions

*Book 11 · EN.645.757 · Foundations of Modeling and Simulation · Week 10 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 10](../labs/lab-10-use-m-s-to-support-integration-verification-validation-and-test-deci.md) → attempt the [original Week 10 assessment](../../../C/P3/EN645757.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-757-w10.md) remains available for a quick recap.

## The decision behind the theory

Models can reduce test burden and expose integration risk, but model evidence must not silently substitute for required real-world evidence. **Essential question:** Which T&E claims can the model support, and what physical, operational, or independent evidence remains necessary?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the foundations of modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

M&S can rehearse procedures, design test matrices, predict observability, inject faults, generate synthetic loads, explore unsafe corners, and interpret sparse physical tests.

Model-supported verification requires that the method is authorized for the requirement and that model credibility, configuration, and uncertainty support the acceptance criterion.

Use physical or operational test data to update, challenge, or bound models. Discrepancies are evidence, not nuisances to be tuned away automatically.

Configuration traceability must identify the system article, model version, parameter set, environment, and requirement revision.

A hybrid evidence argument states which claim portion comes from test, analysis, simulation, inspection, demonstration, or expert judgment.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Apply simulation in design and development using selection, ranking, and design of experiments**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Plan and evaluate verification, validation, credibility, and accreditation for intended use**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Simulation can support integration and test planning by exposing high-risk event sequences and observability gaps.

### Distinguishing related ideas

A synthetic result is not evidence that the implemented system passed a physical test; it is evidence about a conditional model of the system.

### Interpretation and boundary conditions

Choose simulated fault scenarios to design better test cases while preserving the boundary between predicted outcomes and measured compliance.

## Worked engineering example from the course

A physical pilot tests eight weather scenarios, while the simulation evaluates thousands of demand/weather combinations. The model is calibrated only on independent parameters, validated on held-out scenarios, and used to estimate coverage gaps. It supports risk characterization but does not replace the required emergency-stop field test.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A simulated “pass” is evidence about model behavior, not validation of its representation of the real system. Test traces and measured event logs must be compared by purpose, time window, and operational context.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A simulation delivers 12, 14, 16, 18, 20 and 22 completed requests in six independent runs. Calculate sample mean.

<details><summary>Show a reasoned solution</summary>

The mean is (12+14+16+18+20+22)/6=17 completed requests. Six replications are insufficient to claim a rare-event guarantee.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Graduate synthesis: using simulation to allocate—not replace—test evidence

### Connect model claims to test decisions

Simulation can inform integration order, test environments, scenario selection, and expected system responses. But a simulated pass and a physical test pass are not interchangeable observations. A model may predict that emergency stopping completes within a specified distance; the real vehicle also depends on tire condition, actuator wear, sensor bias, pavement, and human interaction. The simulation's credibility is conditional on the purpose and domain for which it was validated. Write every model-based decision with four elements: the claim, the operating envelope, supporting evidence, and excluded phenomena.

A useful strategy is to map the evidence ladder from requirements to analytical checks, model-based simulation, software-in-the-loop, hardware-in-the-loop, integrated ground tests, and field trials. Each stage is selected to expose failure mechanisms the previous stage could not adequately represent. For a timing constraint, analytic worst-case budgets may bound nominal delays, co-simulation may expose scheduling interactions, hardware tests may reveal actual jitter, and operational testing may uncover network congestion and operator actions. More stages do not automatically increase confidence if they all rely on the same flawed sensor model.

### Choose tests by discriminating power

A good experiment distinguishes competing explanations. Suppose Northstar's simulation predicts unacceptable wait times. Candidate causes are insufficient fleet size, concentrated arrival bursts, and slow accessible boarding. Running ten replicas with the same assumptions may narrow a confidence interval without identifying the cause. A factorial study varying fleet size, demand concentration, and boarding times can estimate main effects and interactions. If the improvement from one extra vehicle disappears under high boarding time, a fleet-only procurement decision is poorly justified.

Formalize the comparison with a response `Y = μ + α_f + α_d + α_b + α_fd + ... + ε`, where interaction terms show why one-factor-at-a-time testing can miss combined failure conditions. The approximation is useful only over the selected scenario range; it is not a universal physical law. Use independent replication and distinguish stochastic noise from model-form error. If the purpose is finding hazardous behavior rather than estimating average performance, rare-event simulation and targeted adversarial scenarios may be more appropriate than random sampling.

### Manage correlation between model and test evidence

A simulation calibrated using the same experimental dataset later cited as independent validation is not actually independently validated. Separate calibration, model checking, and held-out challenge cases. Where sample size is limited, disclose reuse and use sensitivity analysis to limit overconfidence. Similarly, software-in-the-loop and hardware-in-the-loop setups may share the same algorithm implementation, so agreement can reflect a common software defect rather than corroboration.

An integration team should maintain an explicit evidence table: what each test can reveal, what it cannot reveal, which configuration it covers, and how failure changes the next step. A test campaign is complete when the necessary claims have adequate, appropriately independent support—not when a target number of test hours is reached. Simulation reduces avoidable physical testing and guides where to look, while field evidence anchors the model to the world the system must actually operate in.

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Simulation silently replaces mandatory physical/operational evidence.
* Model and tested-system configurations cannot be matched.
* Validation data are reused as calibration data without disclosure.
* Discrepancies are removed by tuning with no independent confirmation.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is model-supported T&E?
2. What is held-out validation?
3. Why track configuration?
4. What is a hybrid evidence argument?

<details><summary>Explain the answers</summary>

**1. What is model-supported T&E?** Use of models to design, augment, interpret, or—in authorized cases—provide evidence for test and evaluation decisions.

**2. What is held-out validation?** Evaluation against data not used to calibrate or select the model.

**3. Why track configuration?** Evidence is valid only for the system, model, parameters, environment, and requirement versions represented.

**4. What is a hybrid evidence argument?** A claim supported by a transparent combination of test, analysis, simulation, inspection, and judgment.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 10](../labs/lab-10-use-m-s-to-support-integration-verification-validation-and-test-deci.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[09 — Previous chapter](09-apply-simulation-in-design-and-development-using-selection-ranking-a.md) · [11 — Next chapter](11-plan-and-evaluate-verification-validation-credibility-and-accreditat.md) · [Book index](../README.md)

## Step 03 integrated mobility simulation case: integration and test decisions

### Translate simulation outputs into a verification matrix

A simulation's own reported service outcomes are **model outputs**. They are not independent evidence of system requirement compliance. The [requirements file](../case/requirements.csv) assigns `MS11-R01` to standard p90, `MS11-R02` to accessible p90, `MS11-R03` to the end-of-day nonpickup measure, and `MS11-R04–R06` to staffing, referent demand and charging validation gaps. The calculation status of R01–R03 is **modeled only**. R04–R06 have not been demonstrated by this code. An integration engineer should distinguish the claim's *entity* (software model versus real operation), *test level*, *acceptance criteria*, *configuration* and *authority*.

A credible test/evaluation plan might use three columns of evidence: (1) analytic or simulation evidence for early sizing, (2) test-rig evidence for physical vehicle and charging constraints, and (3) pilot operations for actual demand, human boarding/dispatch, accessible service and degraded events. The pilot cannot be replaced by more seeds from an unvalidated model. Evidence must match the configuration that will operate; previous Book 7–10 conceptual assumptions and unresolved evidence may be inherited, not silently declared closed.

### Quantify the model-versus-system gap

Let \(\hat y_M\) be the simulation's mean daily p90 and \(y_R\) an independently measured operational response. A conceptual discrepancy decomposition is

\[\hat y_M-y_R=\underbrace{\varepsilon_{MC}}_{\text{Monte Carlo}}+\underbrace{\varepsilon_{input}}_{\text{input estimate}}+\underbrace{\delta_{model}}_{\text{structural discrepancy}}+\underbrace{\varepsilon_{measure}}_{\text{referent measurement}}.\]

These terms are **not automatically independent**, so their uncertainties cannot be indiscriminately combined by root-sum-squares. A narrow simulation CI only bounds the first term under the specified stochastic generator. If the route-time and demand referent are missing, the other terms may dominate. A field test must be designed with timestamp definitions, stratification by accessible need, time of day, weather and a transparent sample/quantile estimator.

### Design an informative field comparison

For a pilot, freeze the configuration and ask whether observed request arrivals and service-time distributions agree with the hypothesized inputs. Compare peak-hour counts; check whether the empirical variance exceeds the Poisson prediction; measure accessible boarding p90 and route occupancy; record charger access, delays and failures. Use a held-out day set to evaluate predicted p90 coverage and bias. A model can agree on an overall mean while failing on the accessible tail or high-demand event days. Any test supporting a safety- or equity-critical claim requires qualified oversight and domain-appropriate standards.

For each simulated integration question, define a physical confirmation: *vehicle states* can be checked against telemetry; *charger concurrency* against station logs; *boarding duration* against observed timestamps; *accessible capacity* against seating/equipment configuration and rider experience. If a value has no plausible referent, it should appear in the unresolved limitation register rather than a successful V&V count.

**Exercise and answer.** A team obtains a modeled mean daily accessible p90 of 45 minutes in the 14-vehicle baseline, compared with the 15-minute requirement. May the team write “Requirement failed in the field”? **Answer:** no. It may write “the **specified synthetic model** fails the design screen,” with units, assumptions and version. A field compliance determination requires an independent test using an actual acceptance plan. The adverse model result is still useful: it justifies withholding a pilot readiness claim and investigating alternative dispatch and fleet concepts.

[Credibility and requirements](../case/INDEX.html) · [Chapter 11](11-plan-and-evaluate-verification-validation-credibility-and-accreditat.md).
