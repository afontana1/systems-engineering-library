# Chapter 06 — Visualize, communicate, and defend the pilot selection decision

*Book 14 · EN.645.784 · Decision Science and Analytics in Systems Engineering · Week 6 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 6](../labs/lab-06-visualize-communicate-and-defend-the-pilot-selection-decision.md) → attempt the [original Week 6 assessment](../../../C/P3/EN645784.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-784-w06.md) remains available for a quick recap.

## The decision behind the theory

Decision products often fail because they show rankings without causes, uncertainty, or alternatives. **Essential question:** How can visual and narrative evidence help the decision authority understand tradeoffs without manipulating attention?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the decision science and analytics in systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Start each visualization with a decision question. Do not choose a chart because it is visually impressive.

Use small multiples, value profiles, Pareto plots, tornado/break-even plots, uncertainty intervals, and evidence-quality annotations to expose causes of preference.

Avoid truncated axes, area encodings for precise comparisons, undisclosed normalization, hidden filters, default sort orders that imply rank, and color-only distinctions.

A dashboard needs a frozen export, data/version identifier, filter defaults, and interpretation notes. Interactive exploration cannot replace a controlled record.

The report should state the decision, efficient set, preference assumptions, robustness, dissent, recommendation, and trigger for reopening.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Converge on a preferred selection using transparent value and decision methods**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Reframe the engineering design problem and generate alternatives through morphology**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Communicating a decision requires making sensitivity and excluded alternatives intelligible to stakeholders with different values.

### Distinguishing related ideas

A compelling single score can conceal close tradeoffs, correlation between measures or the dominance of one stakeholder's weight.

### Interpretation and boundary conditions

Show how plausible weight changes, new evidence or changed constraints would alter the recommendation.

## Graduate depth: a decision presentation should expose the choice mechanism

### From ranked alternatives to an auditable decision model

A bar chart ranking alternatives can conceal the assumptions that matter most. An engineering decision model should make four layers visible: the feasible set defined by non-negotiable constraints, the performance of each feasible option, the value judgments used to compare unlike outcomes, and uncertainty about both performance and judgments. Mixing these layers creates false precision. An alternative that fails a minimum accessibility threshold should not become preferred merely because it has a very low cost and a high weighted aggregate score.

For a simple additive value model, `V(a) = Σ w_j v_j(x_aj)`, where `x_aj` is alternative `a`'s performance on attribute `j`, `v_j` transforms that performance into a common value scale, and `w_j` expresses a stakeholder's tradeoff weight. This structure requires more than weights adding to one. Preference independence and consistent interpretation of attribute ranges are needed if the weighted sum is to represent meaningful tradeoffs. A weight of 0.5 on safety is not proof that the stakeholder would accept double the safety harm for a cost saving; many safety obligations are constraints rather than compensatory objectives.

### Sensitivity, thresholds, and rank reversal

Consider two feasible Northstar pilots with normalized value scores: A has service value 0.9 and affordability value 0.4; B has service value 0.6 and affordability value 0.8. Let `w` be the weight on service, with affordability weight `1-w`. Then `V_A = 0.4 + 0.5w` and `V_B = 0.8 - 0.2w`. The alternatives tie when `w = 4/7`, approximately 0.571. Below that threshold B is preferred; above it A is preferred. Rather than merely announcing A as the winner under one arbitrary weight, show the threshold and ask whether the relevant stakeholders' tradeoffs plausibly lie on either side.

This sensitivity exercise must not be mistaken for uncertainty about physical performance. Weights reflect preferences; predicted response times and costs reflect uncertain consequences. Explore those uncertainties separately. For correlated cost and reliability uncertainty, use joint scenarios or joint distributions rather than independently perturbing each value. Under severe uncertainty it may be more honest to display regret or the fraction of plausible scenarios in which each alternative satisfies hard requirements than to report a single precise score.

### Communication as part of engineering quality

A defensible decision record separates facts, model inferences, normative judgments, and authorized commitments. Show decision boundaries: the option's applicable operating context, constraints, assumption ranges, known counterexamples, and the evidence that would trigger reconsideration. Explain who owns the decision and which stakeholders' values were represented. A Pareto chart is useful when objectives conflict, but it does not identify the ethically or institutionally legitimate chooser.

Visualization should reveal tradeoffs without manipulating them. Truncated axes can exaggerate differences, uncertain bands can be confused with guarantees, and excessive detail can hide a hard constraint failure. Use consistent units and timescales; label whether an interval reflects sampling uncertainty, parameter uncertainty, or alternative scenarios. In the Northstar case, a good briefing makes clear not just which pilot appears best today, but how that recommendation would change if demand, service obligations, evidence, or decision authority changed.

## Worked engineering example from the course

The dashboard places cost versus accessible wait on a Pareto plot, uses marker size for availability and shape for threshold status, provides value profiles for D and C, and includes a sensitivity panel showing the deployment-weight break-even. A banner states that B fails the accessibility threshold in the current configuration.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A presentation should show decision table, constraint violations, sensitivity to weights and uncertainty, and the exact reason for the recommendation. A single radar plot can obscure incomparable units and missing feasibility checks.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A design succeeds with probability 0.8 for benefit $500k, otherwise loses $100k. What is expected value before acquisition cost?

<details><summary>Show a reasoned solution</summary>

EV=0.8×500k+0.2×(−100k)=$380k. A risk-averse or budget-constrained decision maker may still reject it.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* The recommendation is communicated only as a total score.
* Interactive filters can change conclusions without recording state.
* Uncertainty or threshold failures are visually hidden.
* The learner cannot reproduce a critical calculation.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. Why show value profiles?
2. What is a decision record?
3. Why freeze dashboard exports?
4. What should a sensitivity visual show?

<details><summary>Explain the answers</summary>

**1. Why show value profiles?** To reveal where alternatives gain and lose value across objectives rather than only showing totals.

**2. What is a decision record?** A controlled account of authority, alternatives, evidence, assumptions, rationale, dissent, decision, and revisit triggers.

**3. Why freeze dashboard exports?** To preserve exactly what the decision authority saw.

**4. What should a sensitivity visual show?** The parameter/preference change and whether/where the decision changes.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 6](../labs/lab-06-visualize-communicate-and-defend-the-pilot-selection-decision.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[05 — Previous chapter](05-converge-on-a-preferred-selection-using-transparent-value-and-decisi.md) · [07 — Next chapter](07-reframe-the-engineering-design-problem-and-generate-alternatives-thr.md) · [Book index](../README.md)

## Step 03 integrated NS-DA14.1 decision-analysis laboratory: Chapter 06

### Communicate tradeoffs without laundering assumptions into certainty

The Selection Decision Review should show an **alternative register first**, followed by hard gates, the feasible Pareto set, preference decompositions, sensitivity boundaries, source data and disputed assumptions. A chart of all six weighted scores alone is misleading: it makes ineligible alternatives appear as competing procurement choices. A better display separates A–F screening, C/D objective tradeoffs, weight-reversal analysis and residual unknowns. Link each plotted point to a source row and identify axes with units; show estimated coverage as a fraction with a stated denominator, not as an unqualified “accessibility score.”

### Reconstruct a decision summary from controlled data

[The screening file](../case/pilot-screening.csv) preserves the original numeric measures and adds flags. On the course table, D has a modeled 90th-percentile wait **2.3 minutes less** than C, with **$0.7M greater** five-year cost, **0.01 lower** accessible coverage, **4 months later** deployment, **0.008 higher** availability and **38 tCO2e/year lower** emissions. All numbers are comparisons between synthetic baseline entries, not observed confidence bounds. The difference is calculable independently from the CSV. The assumed value model gives D a 0.01595 advantage, reversible by shifting about 0.07251 weight toward accessible coverage.

A decision slide should ask “Does 2.3 minutes of wait improvement justify the cost, time and coverage trade?” rather than “Why is D the winner?” A defensible table records whether evidence is course-provided, derived by an arithmetic rule, an analyst assumption, or independently measured; that distinction may be represented with annotation or separate columns. Avoid truncated scales that magnify 0.01 of coverage as an enormous absolute change. Show absolute percentages and the population of eligible trips before asserting equity consequences.

### Controlled recommendation and dissent

The model's **conditional screening preference** is D *only* if the decision authority approves the illustrated weights and gates. A stakeholder may reasonably favor C because of its accessible-trip measure and quicker deployment; record that dissent and the precise conditions under which the ranking changes. A credible authorization record includes the decision owner, baseline version, approved preferences, exclusions, uncertainty, risk and legal gates, re-open triggers, and the next evidence acquisition. It also explicitly says that five-year cost is not the pilot budget and that Book 11's noncompliant modeled service targets remain unresolved.

**Worked exercise.** A director asks for a single graphic showing that D is “18% superior.” **Solution:** Refuse the unsupported percentage. The value scores differ by about 0.016 on an arbitrary 0–1 anchored preference scale, and their ratio has no invariant meaning. Report the actual attribute differences, preference conditions and a weight-switch interval. A graphic cannot turn synthetic scenario numbers into verified performance. If stakeholders insist on a scalar, report it as *conditional value score, not percent better*.

**Practice and solution check.** Recreate the C/D comparison using the raw table; then hide the cost and coverage columns. You will make D appear uniformly attractive, demonstrating selection bias by omission. Restore the measures, include the named negative review, and place a distinct **HOLD for operational adoption** label in the decision memorandum until qualification evidence exists.
