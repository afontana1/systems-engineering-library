# Chapter 02 — Analyze stakeholders, mission, scenarios, outcomes, and measures in the authoritative model

*Book 9 · EN.645.632 · Applied Analytics for Model-Based Systems Engineering · Week 2 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 2](../labs/lab-02-analyze-stakeholders-mission-scenarios-outcomes-and-measures-in-the-.md) → attempt the [original Week 2 assessment](../../../C/P3/EN645632.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-632-w02.md) remains available for a quick recap.

## The decision behind the theory

Stakeholder statements arrive with different authority, vocabulary, time horizons, and embedded solutions. **Essential question:** What problem, outcomes, operations, and measures must the system model represent before architecture analysis begins?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the applied analytics for model-based systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Model stakeholders as accountable roles or organizations, not merely names on a diagram. Record concern, authority, source, date, priority, conflict, and decision right.

Needs should state a desired outcome or capability without embedding an unjustified implementation. Preserve the original statement and create an analyzed interpretation rather than silently rewriting source evidence.

Operational scenarios provide the bridge from concerns to behavior. Include nominal, peak, degraded, emergency, maintenance, accessibility, cybersecurity, and transition conditions as appropriate.

Measures need operational definitions. Link each outcome to a measure, unit, population, environment, statistic, threshold or target, data source, uncertainty, and decision use. A measure name alone is not analytic content.

Use queries to find needs without sources, concerns without resolution, scenarios without actors/outcomes, and outcomes without measures. The query result becomes review evidence and a quality trend.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Receive the baseline, define intended use, and tailor the MBSE method and modeling plan**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Develop and analyze the functional architecture from black-box behavior to allocated white-box functions**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### An authoritative model does not manufacture stakeholder agreement

Placing needs, scenarios, objectives, and measures in a common model can reveal inconsistencies, but it does not by itself settle whose goals matter. A model becomes authoritative because its ownership, definitions, reviews, and revision rules are governed—not because every stakeholder uses the same drawing tool. Distinguish stakeholder observations from negotiated requirements, and distinguish operating scenarios from forecasts about how often those scenarios occur.

The advantage of model-based analysis is the ability to propagate a clarified meaning across viewpoints. If “service availability” changes from vehicles powered on to passenger requests successfully served, the revised definition should expose which measures, allocations, and verification plans are affected. That propagation is valuable only when relations express real dependency. A visually dense model with ambiguous links can give a false impression of integration while concealing disagreements that need explicit decisions.

## Deeper theory: mission analysis should expose stakeholder value conflicts

### An operational model is a representation of competing purposes

Stakeholders may legitimately define success in different ways: passengers want dependable and accessible journeys, operators want manageable exceptions, maintainers want safe repair access, and a campus may want affordable capacity. An authoritative model can put these interests into one traceable information structure, but it cannot eliminate disagreements by giving the data a single source identifier. Authority of configuration is different from authority of judgment. The model must preserve whose objectives and assumptions each measure represents.

Separate operational outcomes from architectural means. “Students arrive within the permitted window” describes a mission outcome; “use a centralized dispatch service” describes a potential solution. Prematurely encoding a solution as a need can make alternative concepts appear noncompliant even when they would satisfy stakeholders better. The mission model should expose the environmental triggers, actors, decisions, and observable effects before allocating them to a technology.

### Scenario structure matters more than scenario count

A scenario is an instance of behavior under an initial state and operating assumptions. A useful scenario set covers distinct causal mechanisms, not just many narrative variations. Nominal morning operation, peak demand with vehicle shortages, communications loss, accessibility assistance, and emergency control transfer may probe different architecture obligations. Ten slightly different nominal rides can provide less design information than one well-chosen degraded-mode scenario.

Scenario models should make transitions explicit. The state after a communications failure is not described completely by saying “manual mode begins.” The analysis must establish what prior reservations remain valid, which actor owns authority, how stale information is identified, and what conditions permit restoration. Such transitions often reveal requirements whose absence is invisible in normal-mode diagrams.

### Measures are part of the causal claim

The measure of effectiveness should represent the outcome the enterprise seeks; measures of performance describe system capabilities that contribute to it. For example, on-time arrival rate may be an effectiveness measure, while dispatch decision latency is a performance measure. Improving the latter does not guarantee improvement in the former when vehicle capacity, accessibility, or routing dominate outcomes. Traceability between measures should therefore encode a hypothesized causal pathway that can be tested, not a simple assertion that one metric “supports” another.

The denominator matters. `on_time_trips / accepted_requests` rewards rejecting difficult requests if acceptance is unconstrained; `on_time_trips / eligible_requests` reveals a different service outcome. No metric is neutral. Each creates incentives and potential blind spots, so model queries should show population, timeframe, units, and exclusions along with values.

### The model's semantics must survive reuse

Operational terms such as *mission completed*, *request served*, and *vehicle available* need precise definitions. If two organizations reuse the same label for different events or clocks, an integrated repository can produce an apparently coherent but false comparison. A robust metamodel distinguishes events, states, actors, operational conditions, and measurement definitions. It also records ownership of assumptions and the provenance of observations.

An authoritative model earns trust by making conflicts, omissions, and change effects visible. It does not earn trust merely by centralizing records. The strongest mission analysis makes it possible to ask which conclusions depend on disputed assumptions and what operational evidence could resolve those disputes before the architecture is committed.

## Worked engineering example from the course

A stakeholder statement says, ‘Use larger autonomous vehicles so wheelchair users never wait longer.’ The learner preserves the source, extracts the outcome ‘provide equitable accessible wait performance,’ models wheelchair users, dispatch operations, stop infrastructure, and weather as contextual factors, defines 95th-percentile accessible wait time by zone and operating mode as the MOE, and records larger vehicles as only one candidate solution. A query reveals that the winter-emergency scenario has no accessibility outcome or measure, forcing a correction before functional analysis.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

An operational goal of 90% completed accessible trips is not interchangeable with average wait under 12 minutes. If 42 of 50 accessible requests complete, the observed 84% is below the goal, irrespective of fleet-wide wait performance. Model separate denominators, operational conditions, and a decision owner.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** If demand rises 30% from 20 to 26 requests/hour while modeled capacity is 24/hour, calculate the nominal capacity gap.

<details><summary>Show a reasoned solution</summary>

The gap is 26−24=2 requests/hour. This is an arithmetic screening calculation; burstiness and queue buildup require a dynamic model.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Source statements are overwritten with analyst interpretations.
* A proposed solution is modeled as a stakeholder need without rationale.
* Critical off-nominal or accessibility scenarios are omitted.
* Outcomes have no measurable definition or data source.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is source provenance?
2. Why preserve a source statement?
3. What makes an MOE operational?
4. What is a scenario coverage gap?

<details><summary>Explain the answers</summary>

**1. What is source provenance?** The identity, authority, date, version, and context of the evidence from which model content is derived.

**2. Why preserve a source statement?** It allows review of interpretation and prevents the model from silently changing stakeholder intent.

**3. What makes an MOE operational?** Defined unit, population, environment, statistic, time basis, threshold/target, data source, and decision use.

**4. What is a scenario coverage gap?** A required mission, stakeholder, mode, or condition has no represented operational sequence and outcome.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 2](../labs/lab-02-analyze-stakeholders-mission-scenarios-outcomes-and-measures-in-the-.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[01 — Previous chapter](01-receive-the-baseline-define-intended-use-and-tailor-the-mbse-method-.md) · [03 — Next chapter](03-develop-and-analyze-the-functional-architecture-from-black-box-behav.md) · [Book index](../README.md)

## Step 03 integrated technical reference: NS-MBA9.1 — stakeholder outcomes are not diagram labels

### Translate an outcome into a defensible measure

The winter expansion has conflicting stakeholder perspectives: passengers need reasonable trip access, accessible users need reliable accommodation, operators need dispatch and energy margins, and the safety authority needs nonconflicting allocations. The [requirement register](../case/requirements.csv) derives `R01` and `R02` from service need `N01`, `R03` from accessibility need `N02`, `R04` and `R05` from energy need `N03`, and `R06` from safety need `N04`. Every derivation should identify the stakeholder, source, scenario and logical reason—not only the endpoints of an arrow.

A useful measure includes **quantity, unit, population, operating state, baseline, statistic, and decision threshold**. For `R03`, *at least 95% of eligible accessible pickups within 12 minutes* is not equivalent to mean pickup time ≤12 minutes. Nor is the observed fraction from a convenient sample a guarantee about all winter operation. Consider 18 timely requests out of 20 observed: the raw sample fraction is `0.90`, which fails the stated point estimate. Even 20/20 would not independently establish the population guarantee at 95% confidence; the exact lower one-sided binomial bound would be approximately \(0.05^{1/20}\approx0.861\) under idealized independent sampling.

### Build scenarios that try to invalidate the model

A nominal ride workflow may omit a wheelchair boarding interval, a failed connection, charger unavailability, or two passengers requesting the same vehicle. In the model each scenario should specify its actors, preconditions, trigger, abnormal branches and observable outcome. An accessible boarding path is not satisfied merely because the logical function `F02` has a name. Its state transitions and physical capacities must be represented and eventually compared against actual operations.

Traceability should run from need to requirement and then through assigned function, relevant interface/analysis and verification design. An **orphan-need** query can reveal an ignored stakeholder; it cannot determine whether that stakeholder's testimony was representative. A *stakeholder-validation* review and an *internal-model-completeness* review are related but separate activities.

**Exercise.** A pilot reports a mean pickup delay of 8 minutes for 20 riders, but 4 riders waited 16 minutes. Does this meet a 95% within-12-minute requirement?

<details><summary>Worked answer</summary>

No, under this sample's eligibility and timing definitions: at most 16 of 20 were within 12 minutes, yielding 80%. The mean does not reveal tail-service compliance. The evidence still lacks a defined population and representative design; it is an observed sample result, not an accepted population demonstration.

</details>
