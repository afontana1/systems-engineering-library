# Chapter 07 — Reframe the engineering design problem and generate alternatives through morphology

*Book 14 · EN.645.784 · Decision Science and Analytics in Systems Engineering · Week 7 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 7](../labs/lab-07-reframe-the-engineering-design-problem-and-generate-alternatives-thr.md) → attempt the [original Week 7 assessment](../../../C/P3/EN645784.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-784-w07.md) remains available for a quick recap.

## The decision behind the theory

In a design problem, the candidate solutions do not yet exist. **Essential question:** How can the team create a diverse, feasible design space without letting the current architecture define the answer?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the decision science and analytics in systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Reopen the problem. Project 1 selected a pilot; Project 2 designs a scalable service and may not inherit the pilot architecture.

Architectural variables are discrete structural choices. Parametric variables tune quantities within an architecture. Mixing them can confuse compatibility and optimization.

Morphological dimensions should be decision-relevant, distinct, and expressed at comparable abstraction. Options should be internally clear and collectively varied.

Cross-consistency assessment removes combinations that are physically, logically, policy, or operationally incompatible. “Unfamiliar” is not a valid incompatibility reason.

Prune in stages: hard incompatibility, minimum feasibility, decomposition, lower-bound screening, and analysis budget. Preserve counts and reasons.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Visualize, communicate, and defend the pilot selection decision**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Formulate parametric design and conduct multiobjective search**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Reframing an engineering design problem may reveal alternatives outside the initially chosen hardware or process family.

### Distinguishing related ideas

Optimizing vehicle count is less useful if dispatch policy, service geography or demand management offers better system-level leverage.

### Interpretation and boundary conditions

The design space is partly a product of modeling choices; documenting excluded variables helps readers assess whether optimization answered the right question.

## Graduate depth: morphological design is controlled exploration of possibility

### Why choosing from a fixed list can be premature

Decision analysis assumes a set of alternatives has been defined. Early engineering design has a more fundamental problem: the alternatives themselves must be created. Morphological analysis decomposes a function into subfunctions and proposes multiple solution principles for each. If there are four propulsion concepts, three energy-storage concepts, and five dispatch concepts, the raw combination space contains `4 × 3 × 5 = 60` candidates. The count is not 60 equally viable engineering architectures. Compatibility, safety, interfaces, weight, energy, regulatory obligations, and operational dependencies eliminate many combinations.

The value of morphology is that it makes hidden defaults visible. A team that begins with “build a larger vehicle” may never consider changing dispatch rules, transfer infrastructure, or the demand contract. Describing functions in solution-neutral terms—“store energy,” “allocate pickup requests,” “provide accessible boarding”—creates room for non-obvious concepts. But decomposition is itself a modeling choice: functions that strongly interact may not be independently combinable, and a concept generated by naive Cartesian product can violate physical laws.

### Feasibility graphs and set-based reasoning

Represent incompatible choices as edges in a constraint graph. A battery architecture might be incompatible with a selected charging interface or thermal strategy. A valid candidate must satisfy all selected compatibility rules plus system-level constraints. A constraint such as `mass_total ≤ mass_limit` is evaluated after assembling the relevant subsystem assumptions. Because properties are coupled, pruning a choice on one nominal figure can be dangerous: a heavier battery may reduce charging stops enough to offset mass elsewhere. Maintain intervals or envelopes while the design remains immature.

Set-based design delays irreversible narrowing until enough evidence exists to eliminate regions of the design space. Instead of selecting a single Northstar vehicle-platform concept immediately, the team might retain three families with bounded mass, cost, service, and charging requirements. Experiments can then target the uncertainty most likely to separate them. This is an application of value-of-information reasoning: a prototype with low demonstration appeal may be highly valuable if it falsifies an entire family of infeasible designs.

### Screening without suppressing innovation

The first screen should apply non-compensatory constraints such as legal accessibility, safety limits, or physically possible interface combinations. The second may use Pareto dominance to remove concepts that are no better on any important attribute and worse on at least one. A third screen can compare value or robust performance, but only after assumptions and normalization are explicit. Pareto dominance depends on the selected criteria; omitting maintainability can make a concept look dominated when it is not.

In a fictional Northstar case, replacing vehicle travel with a transfer-hub option appears attractive on energy cost but creates a new requirement for uninterrupted accessible transfers. The concept cannot be assessed only against vehicle-level energy use. It changes the system boundary, service architecture, human interaction, and acceptance evidence. Morphological exploration therefore connects creative design to functional architecture, interface engineering, and lifecycle assurance.

A disciplined design record keeps the rejected combinations and reasons for rejection, not just the surviving shortlist. New materials, regulatory changes, or supplier capabilities may later make a previously infeasible family worth reconsidering. The objective is neither maximal option count nor premature closure; it is a transparent path from a broad solution space to a defensible engineering commitment.

## Worked engineering example from the course

The field combines service architecture, vehicle mix, automation, dispatch, accessibility, charging, and supervision. “Bounded autonomy + regional transit partnership + vendor-managed supervision” is not automatically inconsistent; the team must identify the actual operational/control interface. “Opportunity charging + no charging access” is physically inconsistent.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A morphological table combines choices for energy source, dispatch mode and fleet size. Three sources × two modes × three sizes yield 18 nominal combinations, but incompatibilities and constraints may reduce feasible designs.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** Alternative A scores 0.8 on cost and 0.6 on reliability, while B scores 0.5 and 0.9. At cost weight w, derive the preference switching point.

<details><summary>Show a reasoned solution</summary>

A=0.6+0.2w; B=0.9−0.4w. Equate them: 0.6w=0.3, so w=0.5. Feasibility and scaling of value scores remain separate questions.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* The pilot solution is treated as the required architecture.
* Incompatibility means “we do not like it.”
* Pruning rules or rejected combinations are not retained.
* Architectural and parametric choices are conflated without rationale.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is morphology?
2. What is cross-consistency assessment?
3. Why count the design space?
4. What is premature convergence?

<details><summary>Explain the answers</summary>

**1. What is morphology?** Systematic exploration of combinations across multiple design dimensions.

**2. What is cross-consistency assessment?** Evaluation of whether option pairs or combinations can coexist under stated rules.

**3. Why count the design space?** To understand combinatorial growth, coverage, and what has been excluded or sampled.

**4. What is premature convergence?** Narrowing the space before adequate exploration or evidence.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 7](../labs/lab-07-reframe-the-engineering-design-problem-and-generate-alternatives-thr.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[06 — Previous chapter](06-visualize-communicate-and-defend-the-pilot-selection-decision.md) · [08 — Next chapter](08-formulate-parametric-design-and-conduct-multiobjective-search.md) · [Book index](../README.md)

## Step 03 integrated NS-DA14.1 decision-analysis laboratory: Chapter 07

### Project 2 restarts with solution freedom, not an inherited favorite

The pilot-selection problem does not determine the optimal long-term architecture. A morphology considers service architecture (fixed route, demand-responsive, hybrid, regional integration), vehicle mix (shuttle, van, mixed, staged), automation (human, supervised or bounded), dispatch (schedule, nearest vehicle, zone-based or priority-aware), accessibility configuration, energy infrastructure, and supervision. The course's full nominal categorical cross-product has \(4\cdot4\cdot3\cdot4\cdot3\cdot3\cdot4=\mathbf{6912}\) combinations before fleet, charger, reserve, zone and speed parameter choices. This number is a teaching count for those seven specified option-set cardinalities; it neither proves each combination is meaningful nor includes the continuous variables.

A **compatibility matrix** is a first-principles engineering artifact. For example, “regional integration plus entirely vendor-managed control” may demand an unprovided service agreement; “bounded autonomy plus unsupervised operation” may violate a governance rule; a dedicated accessible reserve may require different vehicle capacity than a fixed-capacity shuttle. Mark such pairs `excluded`, `requires analysis` or `supported`; provide evidence rather than coding personal preferences as incompatibility. Never delete a class because it performs poorly in an initial score. The editable [morphology register](../case/morphology.csv) preserves options and constraints.

### Declared computational subset versus full design space

The executable NS-DA14.1 experiment does **not** claim to search all 6912 morphology combinations. It deliberately restricts architecture to hybrid/demand-responsive, dispatch to schedule/priority, automation to human/supervised, zones to four/six, speed to 18/24 mph, and five fleet, three charger, three reserve levels. The finite grid therefore has \(2\cdot5\cdot3\cdot3\cdot2\cdot2\cdot2\cdot2=\mathbf{1440}\) combinations, all enumerated reproducibly. It omits fully autonomous designs, the fixed-route-only family, other energy and supervision variants, and continuous values between sampled grid points. Neither a good frontier nor an empty feasible set in this subset settles those omitted regions.

**Worked exercise.** A review committee proposes adding three more reserve-ratio levels without changing any other choices. How large is the expanded controlled grid? **Solution:** Reserve has six rather than three levels, so it doubles to \(1440\cdot(6/3)=2880\) configurations. An algorithm cannot repair an incomplete architecture set by sampling an existing numeric factor more densely. For every omitted morphology branch, carry a reason (`not yet modeled`, `incompatible with documented rule`, or `intentionally deferred`) and a follow-up owner.

**Engineering limitations.** The parametric response equations are fictional and operate on averaged measures. They cannot evaluate real fleet deadheading, legal speed limits, safety qualification, or negotiated service agreements. Project 2 should reuse Book 11 simulated queues only after translating scenarios and validation boundaries, and Book 12 charging physics only after reconciling its route assumptions.
