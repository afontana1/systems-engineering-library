# Chapter 02 — Develop the M&S plan and conceptual model before implementation

*Book 11 · EN.645.757 · Foundations of Modeling and Simulation · Week 2 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 2](../labs/lab-02-develop-the-m-s-plan-and-conceptual-model-before-implementation.md) → attempt the [original Week 2 assessment](../../../C/P3/EN645757.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-757-w02.md) remains available for a quick recap.

## The decision behind the theory

Most expensive simulation defects begin as unexamined conceptual assumptions. **Essential question:** What must be represented, at what resolution, and with what traceability before code or tool logic is built?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the foundations of modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

The conceptual model is the human-readable specification of what the executable model means. It should be reviewable by domain experts who do not know the implementation language.

Process flow alone is insufficient. Include state, timing, resource rules, priorities, preemption, failures, dependencies, initialization, boundary conditions, and measures.

Traceability links decisions to measures, measures to model elements and data, and model elements to implementation modules and tests.

Assumptions assert something accepted for analysis; simplifications deliberately remove detail; abstractions represent detail at a chosen level. All three require ownership and consequence analysis.

The M&S plan defines roles, baselines, development increments, data, reviews, V&V, experiment design, uncertainty treatment, acceptance criteria, and transition/retirement.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Frame the M&S decision, intended use, terminology, and model-method trade space**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Characterize data quality, probability, dependence, and stochastic input models**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### A conceptual simulation model is a theory about causal events

Before writing a simulation, the modeler must decide what changes state, what resources can be occupied, and which events can alter the future. Those decisions encode a theory of the process. If vehicle dispatch is modeled as an instantaneous action, the simulation cannot reveal congestion caused by dispatch communications; if cancellations are omitted, it cannot measure wasted capacity after a no-show. Software cannot recover information that the conceptual model intentionally or accidentally excluded.

The conceptual model should state its intended use, boundaries, state variables, event vocabulary, operating assumptions, and outputs. Levels of detail should follow the decision rather than mimic every visible aspect of reality. For a fleet-size comparison, vehicle occupancy and demand timing may be central, while passenger names are irrelevant. A precise event-calendar implementation of an invalid conceptual process can yield convincing but misleading results. Conceptual modeling is thus the most consequential stage of simulation credibility, not a preliminary drawing task.

## Graduate depth: the conceptual model as a falsifiable specification

### From a decision question to an executable abstraction

A conceptual model is not a shortened description of the simulation code. It is a claim about which entities, states, mechanisms, and boundaries explain the quantities relevant to a decision. Begin with a *decision variable* (for example, the number of standby vehicles), an *outcome* (the probability that a traveler waits more than fifteen minutes), and a *domain of intended use* (a defined service area and demand regime). These determine the resolution needed. If the decision depends on rare crowd surges, a model of average hourly demand discards the very behavior that might reverse the ranking of alternatives. Conversely, representing individual vehicle components contributes little when the decision is about route capacity and passenger queues.

The conceptual model can be expressed as a transition system: `x(t+) = F(x(t-), e, u, theta)`, where `x` is the state just before or after an event, `e` is the event, `u` is the operating policy, and `theta` contains uncertain parameters. An event such as a passenger arrival changes queue occupancy; a vehicle-departure event changes both occupancy and vehicle availability. A state description is sufficient only if it contains the information needed to predict the next transition given the new inputs. If the next travel time depends on earlier congestion but congestion history is absent from `x`, the assumed state is incomplete. That is a structural defect, not a calibration error.

### Boundaries, evidence, and model risk

Three boundaries matter independently: the *physical boundary* identifies which actors and resources are represented; the *temporal boundary* identifies warm-up, operating horizon, and repeated days; and the *epistemic boundary* identifies which mechanisms are supported by evidence. An external ambulance dispatch system might remain outside the model yet impose correlated interruptions on vehicle availability. Such an influence requires at least an explicit scenario or interface assumption. Excluding it silently can make capacity look more robust than it is. Every omission should be defended by its likely effect on the decision, not by how inconvenient it is to implement.

A useful discipline is to maintain a trace from each decision claim to the modeled mechanism and the evidence that supports that mechanism. For example: the claim that priority dispatch lowers severe waits relies on a queue-selection rule, measured call characteristics, and a policy implementation that can actually access the priority attribute. The trace exposes an otherwise hidden failure: a perfectly coded priority rule is irrelevant when priority is not observed consistently in the field. Verification checks the rule's implementation; validation examines whether the rule and input process correspond to the operational referent. The two activities are complementary, not interchangeable.

The strongest conceptual-model review includes countermodels. One candidate treats arrivals as independent; another includes correlated event surges. A third represents passenger abandonment when waits become long. If all three favor the same number of vehicles with acceptable margin, the decision is less sensitive to structural uncertainty. If they disagree, adding finer graphical detail to one model does not resolve the disagreement. The next useful work is to collect discriminating evidence or frame a robust decision that performs acceptably across models.

### A Northstar example and the limits of apparent precision

Suppose the fictional Northstar service averages six requests per hour, with individual capacity of eight requests per hour. A stationary `M/M/1` approximation gives utilization `rho = 6/8 = 0.75` and mean time in system `W = 1/(8-6) = 0.5 hour`. Those values depend on one server, Poisson arrivals, exponential service times, stability, and steady-state operation. They do not predict the tail of event-night waits if arrivals arrive in synchronized batches or if vehicle travel time depends on location. A discrete-event model may represent these mechanisms, but greater detail does not automatically make the result true.

The credibility argument must therefore say which of the queue approximation's assumptions fail, which new mechanisms the event model captures, and what data can test them. One can compare simulated empty-system behavior to an analytic limiting case, verify conservation of passengers and vehicles, examine state traces around simultaneous events, and compare held-out day-level wait distributions to observed distributions. Agreement on the mean alone is weak evidence when the decision concerns the 90th percentile. The conceptual model is complete when reviewers can explain why each retained mechanism changes a decision-relevant prediction and what observation would disconfirm it.

## Worked engineering example from the course

A process diagram shows requests entering a dispatch queue and vehicles serving them. Review reveals missing mobility-device capacity, charging priority, shift-change behavior, abandoned requests, and disruption recovery. These omissions would bias fleet sizing even if the code exactly implemented the diagram.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

The conceptual model identifies entities (requests), resources (vehicles), events (arrival, service start, departure), and state (queue, vehicle status). Time advances to the next event. Define the boundary and omitted mechanisms before writing code.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A simulation delivers 12, 14, 16, 18, 20 and 22 completed requests in six independent runs. Calculate sample mean.

<details><summary>Show a reasoned solution</summary>

The mean is (12+14+16+18+20+22)/6=17 completed requests. Six replications are insufficient to claim a rare-event guarantee.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Implementation begins with no approved conceptual model.
* A critical behavior exists only in prose or code.
* Outputs lack operational definitions.
* Assumptions with decision impact have no owner or validation plan.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is a conceptual model?
2. Why trace a measure to model elements?
3. What is termination logic?
4. Who should validate the conceptual model?

<details><summary>Explain the answers</summary>

**1. What is a conceptual model?** A reviewable specification of the relevant real-world concepts, relationships, rules, assumptions, and measures represented by the executable model.

**2. Why trace a measure to model elements?** To show how the model produces evidence and to support change-impact and verification.

**3. What is termination logic?** The rule defining when a run or entity process ends and how final state is treated.

**4. Who should validate the conceptual model?** Users, domain experts, decision owners, and independent reviewers appropriate to the intended use.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 2](../labs/lab-02-develop-the-m-s-plan-and-conceptual-model-before-implementation.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[01 — Previous chapter](01-frame-the-m-s-decision-intended-use-terminology-and-model-method-tra.md) · [03 — Next chapter](03-characterize-data-quality-probability-dependence-and-stochastic-inpu.md) · [Book index](../README.md)
