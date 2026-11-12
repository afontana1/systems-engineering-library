# Chapter 01 — Frame the M&S decision, intended use, terminology, and model-method trade space

*Book 11 · EN.645.757 · Foundations of Modeling and Simulation · Week 1 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 1](../labs/lab-01-frame-the-m-s-decision-intended-use-terminology-and-model-method-tra.md) → attempt the [original Week 1 assessment](../../../C/P3/EN645757.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-757-w01.md) remains available for a quick recap.

## The decision behind the theory

A simulation begins with a decision and an intended use, not a tool. **Essential question:** What evidence is needed, and is a model or simulation the most appropriate way to obtain it?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the foundations of modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Modeling is purposeful abstraction. Every model omits reality; quality depends on whether the omissions are acceptable for a stated use.

A simulation is an execution of a model through time, events, scenarios, or sampled uncertainty. A spreadsheet equation may be a model without being a simulation; an event-driven queue model is both.

Model selection should consider decision timescale, interactions, stochastic behavior, feedback, spatial detail, data burden, explainability, cost, and verification/validation feasibility.

Fidelity is multidimensional. More detail can increase cost, defects, calibration burden, and false confidence while adding little decision value.

The intended-use statement is a configuration-controlled requirement for the M&S activity. Changing the use may require changing data, resolution, validation evidence, and acceptance authority.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **the preparatory technical courses**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Develop the M&S plan and conceptual model before implementation**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

A simulation should begin with a decision question, because the question determines which causal features must be represented and which omissions are harmless.

### Distinguishing related ideas

Simulation is not automatically prediction: it can be used to compare mechanisms, explore possible outcomes or examine sensitivity, each with different credibility requirements.

### Interpretation and boundary conditions

A model adequate for comparing queue disciplines may be insufficient for estimating exact passenger wait distributions at an unobserved station.

## Graduate depth: modeling as a contract between uncertainty and action

### Why intended use changes the model you need

The engineering value of a model is not proportional to its visual realism or its number of state variables. It is proportional to the extent to which it can distinguish decisions with materially different consequences. Let `d` denote a feasible action, `θ` an uncertain state of the world, and `L(d, θ)` the loss associated with taking the action under that state. If credible probabilities are available, a risk-neutral decision maker might select the action minimizing `E[L(d, θ)]`. A model helps when it estimates that loss more accurately, clarifies its uncertainty, or reveals a constraint that eliminates a seemingly attractive action. A model that predicts vehicle trajectories precisely but omits accessible boarding delays may be sophisticated and decision-inadequate at the same time.

This gives the intended-use statement three technical components: the decision and alternatives, the measurable consequence of an error, and the operating conditions over which the evidence is meant to apply. It also defines an *inference boundary*. A discrete-event queue simulation can estimate conditional congestion for the arrival processes it represents. It does not establish that those arrival processes describe every emergency, or that an operator will obey the simulated dispatch rule. Validation evidence must address those separate claims. The chain from input data to simulated behavior to recommended action should have an explicit evidence link at each transition.

### Abstraction, error budgets, and the value of information

Suppose a Northstar decision compares a ten-vehicle fleet against an eleven-vehicle fleet. The additional vehicle costs 80,000 monetary units over the planning horizon, while the expected cost of service failures under the ten-vehicle option is estimated at 115,000, with a very wide uncertainty range. The appropriate question is not whether the simulator can show an impressive animation of the eleventh vehicle. It is whether uncertainty in demand tails, charging access, and recovery time could reverse the decision. A simple threshold analysis asks how much reduction in expected failure cost would justify the extra 80,000. A high-fidelity model of vehicle suspension would contribute little to that comparison unless suspension behavior materially affects availability.

An *error budget* partitions uncertainty into input variability, parameter estimation, model-form error, numerical approximation, and implementation defects. These categories have different remedies. More replications reduce Monte Carlo sampling error, not systematic omission of outages. Better numerical solvers reduce discretization error, not uncertainty about travel demand. Independent operational observations may reduce model-form uncertainty, but only in the regimes represented by those observations. The total uncertainty need not equal the simple sum of component uncertainties when errors are dependent.

The expected value of perfect information is the expected loss under the best decision available with perfect knowledge subtracted from the best expected loss without that knowledge. It is an upper bound on what further investigation could be worth under the assumed probability and loss model. When the ranking of options is robust across plausible assumptions, more modeling may have low value. When a small change reverses the preferred action, focused data collection or a deliberately limited pilot may dominate further general-purpose simulation development.

### What can legitimately be concluded

Simulation comparisons require common definitions of service, failure, cost horizon, and baseline. A decision model also needs a rule for unacceptable outcomes: an accessibility or safety obligation is not necessarily compensable by average cost savings. Treat such obligations as feasibility constraints before optimizing among the remaining options. Carry the resulting uncertainty and limitation statements into the simulation plan, test strategy, and decision record; otherwise later teams may reuse the output outside its defensible intended use.

## Worked engineering example from the course

The sponsor asks whether ten vehicles are enough. A static capacity ratio suggests yes, but it cannot represent request peaks, accessible boarding, charging contention, or disruptions. A discrete-event model is selected for fleet/resource interactions, while a spreadsheet remains the independent sanity-check model.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Before opening simulation software, distinguish question from implementation. “Will two vehicles keep 90th-percentile waits below 15 minutes on event nights?” specifies a decision; “build a queue simulation” describes an activity. A model method is chosen in service of the first.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** For a theoretical M/M/1 queue λ=8/hour and μ=10/hour, calculate utilization and expected time in system.

<details><summary>Show a reasoned solution</summary>

ρ=8/10=0.8; W=1/(10−8)=0.5 hours=30 minutes. M/M/1 assumptions are restrictive.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* No named decision owner or intended use.
* Tool is selected before comparing model families or non-model alternatives.
* The model is expected to answer claims outside its boundary.
* Credibility work is deferred without rationale.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is intended use?
2. How does a model differ from a simulation?
3. Why can more fidelity reduce usefulness?
4. What is a referent?

<details><summary>Explain the answers</summary>

**1. What is intended use?** The bounded decision purpose, user, claim, conditions, and consequence for which the model is evaluated.

**2. How does a model differ from a simulation?** A model is a representation; a simulation executes a model to produce behavior or sampled outcomes.

**3. Why can more fidelity reduce usefulness?** It can increase data, cost, defects, opacity, and validation burden without improving the decision.

**4. What is a referent?** Independent information or evidence used to evaluate whether model behavior represents the relevant real-world phenomenon.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 1](../labs/lab-01-frame-the-m-s-decision-intended-use-terminology-and-model-method-tra.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

Start of the book · [02 — Next chapter](02-develop-the-m-s-plan-and-conceptual-model-before-implementation.md) · [Book index](../README.md)

## Step 03 integrated mobility simulation case: decision and intended use

### A decision claim is narrower than a model's capabilities

The original course's campus-mobility problem asks whether a **Phase 2 mobility service** can meet peak, accessible-trip and degraded-service expectations with a defensible fleet and staff plan. We adopt the fictional **NS-MS11.1** baseline, [case assumptions](../case/model-assumptions.json), and [requirements](../case/requirements.csv). The decision owner is the campus mobility sponsor; the analyst is not the deployment approver. The specific **intended use** of this first-pass model is **screening candidate vehicle counts 8, 10, 12 and 14** under explicitly synthetic demand and service assumptions. It is *not* a field-calibrated pilot-qualification model.

Separate the *referent* (an actual campus service, which has not been measured here), the *conceptual model* (requests, vehicles, eligibility, charging and events), the *computational model* (the [executable event scheduler](../tools/step03_book11_mobility.py)), and the *experiment* (paired replications across candidate fleets). These levels can disagree. Successful execution establishes neither fidelity to the conceptual model nor validation against the referent.

### Derive the decision-level capacity sanity check

From the course guide, the hourly expected request totals are 18, 32, 48, then six hours at 22, followed by 42, 50 and 30. Under a nonhomogeneous Poisson arrival approximation, the *expected* daily count is

\[E[N]=18+32+48+6(22)+42+50+30=352\ \text{requests/day}.\]

For any interval of length \(\Delta t\) minutes and rate \(\lambda_h\) per hour, \(E[N_{\Delta t}]=\lambda_h\Delta t/60\), and \(\operatorname{Var}(N_{\Delta t})=E[N_{\Delta t}]\) under the Poisson assumption. This is a *model choice*, not measured dispersion; campus event arrivals may be clustered. The implied accessible-trip expectation is \(0.14(352)=49.28\) requests/day, but a fractional expected count is **not** a passenger or a promise of observed frequency.

The simplest upper-level feasibility screen compares \(352\) jobs/day with \(F(720)/s\), where \(s\) is average minutes of one-vehicle service occupancy and \(F\) is fleet size. If \(s=20\) minutes and charging, staffing and traffic are ignored, fourteen vehicles offer at most \(14(720)/20=504\) single-request service slots/day. This does **not** guarantee that a 50/hour peak, accessible compatibility, or charge queue can be handled. In fact, the average-capacity calculation intentionally hides the bottleneck the event model must expose.

### Model-method trade, cost of error, and necessary evidence

A spreadsheet with time buckets is valuable for independent balance and staffing sensitivity; an M/M/1 queue is useful only as a limiting analytic benchmark, not as a capacity-eight, multi-vehicle, charging-enabled representation. A discrete-event simulation (DES) is the appropriate *next* model for asynchronous arrivals, vehicle occupations, resource contention and charge completion. Agent-based pedestrian interactions, network routing and full physical battery dynamics would add cost and unverified parameters without improving this first screening decision. Escalate model fidelity only when the result is sensitive to a missing mechanism.

The [case credibility register](../case/credibility-register.csv) names unresolved input/validation claims. Hard constraints—accessible service and service reliability—must be screened before optimizing capital cost. Even if an alternative is cheapest, no analyst may infer regulatory accessibility compliance from this toy model.

**Worked screening result.** Execute `python SE/K/B11/tools/step03_book11_mobility.py` at repository root. In the controlled first release, the 14-vehicle baseline averages approximately **36.4 min** for the *daily standard-trip p90* across 30 seeds and **45.4 min** for the *daily accessible p90*; its mean fraction not picked up at the 18:00 close is about **6.0%**. The fictional limits are 12, 15 minutes and strictly below 1%, respectively. These numbers support **HOLD / no qualifying candidate in the screened set**, not a declaration that the actual campus system would fail. See the [full replication outputs](../case/replication-output.csv); results depend on the declared one-request-per-vehicle abstraction.

### Exercise with explained solution

**Question.** A manager claims the 504 theoretical service slots prove 14 vehicles suffice because there are only 352 expected requests. Identify three independent invalid steps. **Solution.** (1) An expectation is not a maximum; Poisson arrivals vary. (2) Average daily capacity is not peak/hourly capacity; requests queue when arrival bursts exceed instant service. (3) Charging, accessible vehicle compatibility and the distribution of service times remove resources from the simple capacity pool. A responsible recommendation must report failure modes, uncertainty and further observations rather than certify feasibility.

**Boundary:** retain this model's [configuration](../case/model-assumptions.json), governing course targets, and review authority whenever the simulation is reused. [Case dossier](../case/INDEX.html) · [Chapter 2](02-develop-the-m-s-plan-and-conceptual-model-before-implementation.md).
