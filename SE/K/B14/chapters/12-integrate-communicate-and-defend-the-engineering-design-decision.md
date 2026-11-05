# Chapter 12 — Integrate, communicate, and defend the engineering design decision

*Book 14 · EN.645.784 · Decision Science and Analytics in Systems Engineering · Week 12 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 12](../labs/lab-12-integrate-communicate-and-defend-the-engineering-design-decision.md) → attempt the [original Week 12 assessment](../../../C/P3/EN645784.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-784-w12.md) remains available for a quick recap.

## The decision behind the theory

The final task is not to present every computation; it is to make the decision process auditable and actionable. **Essential question:** What can the decision authority responsibly conclude, what remains unresolved, and what would cause the recommendation to change?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the decision science and analytics in systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Use an evidence chain: decision → objectives → measures → alternatives/design space → data/models → analysis → uncertainty/preferences → recommendation → conditions and implementation gates.

Separate the design recommendation from authorization to build or deploy. Additional safety, regulatory, contractual, or validation gates may remain.

Provide an executive view, a technical report, reproducible notebooks, and a controlled decision record. Each serves a different audience but must agree.

Innovation benefits from objectives-driven alternative generation and transparent exploration. Analytics can inhibit innovation when early metrics, incumbent data, or optimization formulations prematurely narrow the space.

The oral defense tests understanding, not presentation polish. The learner must reproduce calculations, explain limits, and revise responsibly when new evidence appears.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Analyze uncertainty, sensitivity, robustness, regret, and value of information**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **the integrated course decision**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

A defended engineering decision identifies feasible choices, preferences, uncertainty, sensitivity and the authority accepting risk.

### Distinguishing related ideas

A mathematical optimum is conditional on its objective model and assumptions; it is not a universal best design.

### Interpretation and boundary conditions

Communicate what evidence would reverse the decision and which stakeholders would bear the costs of an incorrect prediction.

## Worked engineering example from the course

The final recommendation is a hybrid human-operated/supervised-autonomy architecture with 14 vehicles, six chargers, a 15% reserve, and priority-aware dispatch, contingent on winter charging validation and accessibility co-design. The decision record explicitly rejects immediate bounded autonomy deployment, preserves a staged option, and schedules a review after pilot data.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A defensible final recommendation should state constraints, stakeholder weights, uncertainty, sensitivity, evidence shortfalls and who owns approval. A high optimum score is conditional on the scope and preferences in the model, not a universal best design.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A design succeeds with probability 0.8 for benefit $500k, otherwise loses $100k. What is expected value before acquisition cost?

<details><summary>Show a reasoned solution</summary>

EV=0.8×500k+0.2×(−100k)=$380k. A risk-averse or budget-constrained decision maker may still reject it.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Graduate synthesis: defending a design decision as a robust policy

### From preferred design to conditional recommendation

A final design study should explain why an option is admissible, why it is preferred among admissible options, and when the preference would reverse. The answer cannot be compressed into a single rank without losing the mechanisms. Start with feasibility filters: mandatory safety, accessibility, legal, interface, and funding constraints. Then compare surviving alternatives using a transparent value model, scenario analysis, and explicit stakeholder judgments. A design with the best nominal utility may still be dominated in a high-consequence scenario.

A multiattribute model `V(a) = Σ wᵢ vᵢ(a)` is useful if preferential independence and the meaning of scales are defensible. A weight of 0.4 on accessibility does not mean accessibility is worth 40% of cost; weights encode the value of swings between defined endpoints. When interactions matter, an additive model can be misleading. For example, a reduction in response time may be valuable only if accessible vehicles are actually available. Check weighting and scale sensitivity before treating the total as robust.

### Combine Pareto analysis with uncertainty

An alternative is Pareto dominated if another is at least as good on every considered attribute and strictly better on one, under a fixed assessment. Uncertainty changes this comparison: two designs may alternate dominance under weather, maintenance, or demand states. Rather than forcing one global frontier from point estimates, report scenario-specific frontiers and violation probabilities. A cost-effective shuttle fleet under median demand may be infeasible during the peak accessibility scenario. A robust recommendation can include staging and fallback policies rather than a single hardware choice.

Regret provides a useful decision perspective: `regret(a,θ) = max_b V(b,θ) − V(a,θ)`. Choosing the action with the smallest maximum regret differs from maximizing average utility. Neither rule is automatically correct; they represent different attitudes toward missed opportunities and adverse outcomes. State what decision rule is being used and why the organization has authority to accept its consequences.

### Make the defense operational and auditable

Suppose one concept has expected annualized cost $1.8M and another $2.0M, but the cheaper option's 95th-percentile waiting time exceeds a required threshold under peak demand. If the threshold is mandatory, the cheaper concept is infeasible for that operating envelope. If it is a negotiable service objective, quantify the tradeoff and seek stakeholder authorization rather than quietly changing the objective. The final technical memo should distinguish observed data, calibrated predictions, expert judgments, and value choices.

Preserve the input baseline, analysis code or formulas, model limitations, dissent, and a sensitivity table with decision-reversal conditions. Recommend a monitoring plan: what changes in demand, reliability, supplier economics, or regulations should trigger reassessment? A design decision is not finished when a board approves a slide. It becomes a usable **adaptive policy** when later engineers can reconstruct why it was chosen and how to react when its assumptions cease to hold.

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* The recommendation exceeds the validated analysis or decision authority.
* Executive and technical products disagree.
* A surprise fact is dismissed to protect the original answer.
* The repository cannot regenerate key results.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is an evidence chain?
2. Why separate recommendation from authorization?
3. What is a reversal condition?
4. How can analytics inhibit innovation?

<details><summary>Explain the answers</summary>

**1. What is an evidence chain?** Traceable linkage from decision need through objectives, measures, alternatives, data/models, analyses, uncertainty/preferences, and recommendation.

**2. Why separate recommendation from authorization?** Other lifecycle, safety, regulatory, funding, or validation conditions may govern implementation.

**3. What is a reversal condition?** A stated change in evidence, assumptions, constraints, preferences, or context that would reopen or change the decision.

**4. How can analytics inhibit innovation?** By optimizing a prematurely narrowed design space or overvaluing what is easy to measure.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 12](../labs/lab-12-integrate-communicate-and-defend-the-engineering-design-decision.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[11 — Previous chapter](11-analyze-uncertainty-sensitivity-robustness-regret-and-value-of-infor.md) · End of the book · [Book index](../README.md)
