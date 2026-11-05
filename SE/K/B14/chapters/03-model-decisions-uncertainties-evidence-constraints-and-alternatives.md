# Chapter 03 — Model decisions, uncertainties, evidence, constraints, and alternatives

*Book 14 · EN.645.784 · Decision Science and Analytics in Systems Engineering · Week 3 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 3](../labs/lab-03-model-decisions-uncertainties-evidence-constraints-and-alternatives.md) → attempt the [original Week 3 assessment](../../../C/P3/EN645784.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-784-w03.md) remains available for a quick recap.

## The decision behind the theory

A score table can hide causal assumptions and missing information. **Essential question:** What decisions, uncertainties, evidence, and consequences must be represented before alternatives are compared?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the decision science and analytics in systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Influence diagrams communicate structure, not merely chronology. Arcs represent informational or causal relevance and should have a stated interpretation.

Separate aleatory variability, epistemic uncertainty, stakeholder disagreement, and decision-control variables. They require different treatment.

An evidence plan maps each measure to source, collection method, timing, sample, uncertainty, transformation, and verification.

Alternative generation should start from objectives and constraints. Include incumbent, minimal-change, staged, hybrid, and deliberately different options.

Precommit rejection rules and preserve rejected alternatives with evidence. A screening rule is itself a decision assumption.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Translate stakeholder values into objectives, measures, and value structure**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Apply constraints, dominance, and Pareto analysis to the selection problem**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

A decision model combines alternatives, states of the world, information and consequences under stated preference assumptions.

### Distinguishing related ideas

A probability model describes uncertainty, while a utility function expresses choice preferences; multiplying them does not turn preference into fact.

### Interpretation and boundary conditions

The model's usefulness depends on whether it includes the feasible actions and consequences that could realistically change the choice.

## Deeper theory: influence diagrams and the architecture of a decision

### Decisions, uncertain events, and consequences belong in different nodes

A decision model should separate *controllable choices* from *states of the world* and from *valued consequences*. An influence diagram uses decision nodes for actions, chance nodes for uncertain conditions, and value nodes for outcomes. Arcs may represent probabilistic dependence or information available before an action. Their direction matters: a decision made today cannot depend on the result of a test that will occur next month unless a contingent strategy is explicitly modeled. Many apparently sophisticated trade studies accidentally assume perfect foresight by selecting different alternatives in every simulated future and then comparing that impossible policy with a fixed design.

For a single-stage decision, a standard expected-utility rule is `a* = argmax_a Σ_s P(s|I) U(a,s)`, where `I` is the evidence currently available, `s` indexes relevant states, and `U` is the consequence's utility. This expression does not require all values to be monetary; it does require an internally coherent account of preference and probability. A legal or safety requirement may instead be a hard constraint that removes infeasible actions before utility comparison. Distinguish *risk preference* from uncertainty about the likelihood of events: a risk-averse utility curve does not make an estimated failure probability more accurate.

### Evidence changes beliefs, not the world retrospectively

Suppose a communications architecture will meet its latency target with prior probability 0.7, and a test is more likely to pass when the target is met than when it is not. After a positive result, Bayes' rule gives `P(target | positive) = P(positive | target) P(target) / P(positive)`. A test with many false positives can produce only a small shift in the posterior even if it looks impressive. The likelihood must describe the actual test protocol and operating conditions; a demonstration under light traffic is not automatically informative about outage conditions.

A decision tree makes timing clear. Choose whether to test; if testing, observe a result; update beliefs; then select the best available action. If testing takes three months, its expected benefit must account for delay, contract commitments, and any options foreclosed. The same evidence can be valuable for one decision and irrelevant for another. A variable is not worth measuring merely because it has high variance: it matters when it is causally or predictively connected to outcomes on which feasible actions differ.

### Dependence structure prevents double counting and false certainty

A regional incident may simultaneously reduce road capacity, raise demand, and degrade radio networks. Multiplying independent probability distributions for these factors may assign implausibly low probability to precisely the joint state that threatens the mission. Represent common causes, conditional dependencies, or coherent scenarios. Correlation alone does not establish causation: traffic congestion and dispatch delay may share a weather driver, so changing dispatch software may not produce the improvement suggested by their raw correlation.

Avoid counting the same consequence under several criteria. For example, missed emergency transfers, patient delay, and failure to reach care may be linked in one causal chain. Stakeholders may legitimately value each separate effect, but an additive score must articulate what additional value each criterion represents. If they are simply alternate measurements of the same harm, simultaneous inclusion can make one concern effectively carry multiple weights. Trace raw measures through effects to ultimate objectives before assigning preference functions.

### The model boundary is an ethical and technical choice

A dispatch choice may change the total number of successful journeys while shifting wait times toward remote communities. Averaging consequences over the entire region can erase that transfer. Define whose outcomes count, over what horizon, and with what distributional constraints. Also preserve decisions that are unavailable to the program: Northstar may influence mutual-aid agreements but cannot command every independent constituent. A decision model is defensible when its alternatives, evidence, consequences, authority, and time sequence match the real decision—not when its spreadsheet has more columns.

## Worked engineering example from the course

For the pilot selection, deployment time depends on vendor lead time and regulatory approval; availability depends on technical reliability and maintenance support; accessible coverage depends on vehicle configuration and scheduling policy. The influence diagram shows that “autonomy level” affects several outcomes through distinct uncertain mechanisms rather than receiving an unexplained risk score.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A decision tree separates choice nodes, chance nodes, probabilities, and outcomes. If success probability is 0.8 with benefit $500k and failure costs $100k, expected net value is 0.8×500−0.2×100=$380k, before investment costs.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** Alternative A scores 0.8 on cost and 0.6 on reliability, while B scores 0.5 and 0.9. At cost weight w, derive the preference switching point.

<details><summary>Show a reasoned solution</summary>

A=0.6+0.2w; B=0.9−0.4w. Equate them: 0.6w=0.3, so w=0.5. Feasibility and scaling of value scores remain separate questions.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* A consequential uncertainty is hidden inside a composite score.
* Alternatives are generated only from currently favored technology.
* Rejection rules are invented after observing scores.
* Evidence sources have no provenance or comparability assessment.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is a decision node?
2. What is a chance node?
3. Why predeclare constraints?
4. What is epistemic uncertainty?

<details><summary>Explain the answers</summary>

**1. What is a decision node?** A controllable choice owned by the decision authority.

**2. What is a chance node?** An uncertain quantity or event relevant to outcomes or information.

**3. Why predeclare constraints?** To reduce result-driven screening and make exclusion rules reviewable.

**4. What is epistemic uncertainty?** Uncertainty from incomplete knowledge that may be reduced with information.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 3](../labs/lab-03-model-decisions-uncertainties-evidence-constraints-and-alternatives.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[02 — Previous chapter](02-translate-stakeholder-values-into-objectives-measures-and-value-stru.md) · [04 — Next chapter](04-apply-constraints-dominance-and-pareto-analysis-to-the-selection-pro.md) · [Book index](../README.md)
