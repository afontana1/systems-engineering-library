# Chapter 9 — Value functions and double counting

*Book 6: System Conceptual Design · Week 9 — Objectives, value functions, and multiattribute evaluation*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 9](../labs/lab-09-objectives-value-functions-and-multiattribute-evaluatio.md) without looking at the solution → return to [Week 9 of the course guide](../../../C/P2/EN645767.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-767-w09.md) is optional review, not the primary reading.

## The engineering problem

At this point the Northstar team is still free to select among competing mobility-service concepts. A proposed autonomous shuttle is one hypothesis, not the definition of the problem. The governing question this week is **value functions and double counting**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Multiattribute decisions separate measurable performance from stakeholder preference. Transform raw metrics onto transparent value scales, verify monotonicity, and justify weights. Highly correlated criteria can double-count one underlying outcome and dominate the decision by accident.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Value models translate stakeholder priorities into decision comparisons, but weights and scales embody judgments rather than laws of nature.

### Distinguishing related ideas

A weighted sum can double-count a concern if 'travel time' and 'convenience' describe the same underlying value, or hide unacceptable safety tradeoffs.

### Interpretation and boundary conditions

Apply mandatory constraints before preference scoring and test whether plausible changes in weights reverse the ranking.

## Deeper theory: value is a structured expression of stakeholder tradeoffs

### Measures of performance are not measures of preference

Passenger wait time is an observable performance measure; how much a stakeholder values reducing it from twelve minutes to eight is a value judgment. A value function maps raw outcomes to a consistent preference scale, often normalized between undesirable and desirable reference levels. The mapping may be nonlinear: reducing a wait from twenty to fifteen minutes can matter much more than reducing it from five to zero, depending on rider needs and service commitments. Assuming a linear value function because a spreadsheet makes it convenient silently asserts constant marginal value.

A common additive model is `V(x) = Σ_i w_i v_i(x_i)`, with `Σ_i w_i = 1` and `w_i ≥ 0`. The weights represent tradeoffs over defined attribute swings, not independent measurements of moral importance. Their meaning depends on scale anchors. A weight of 0.4 on accessibility has no stable meaning if the definition of “worst” and “best” accessibility changes. In addition, some obligations are categorical: safe boarding and nondiscriminatory access may be mandatory constraints rather than benefits exchangeable for shorter average waits.

### Double counting and dependence need separate diagnoses

Consider two attributes: average travel time and customer satisfaction. Satisfaction may already incorporate travel time, so adding both without clarifying what satisfaction measures may count the same consequence twice. By contrast, travel time and operating cost may be statistically correlated while representing legitimately distinct consequences. The question is not merely whether two datasets correlate; it is whether the value model contains overlapping constructs or whether preference for one attribute depends on the level of another. Preferential dependence can require multiplicative models, interaction terms, or explicit scenario-based judgments rather than a simple additive score.

Risk attitude also matters. Suppose option A always delivers normalized value 0.65, while option B gives 0.90 half the time and 0.35 half the time. Their expected values are 0.65 and 0.625 respectively, but different decision makers may care strongly about the low outcome's mission consequences. Expected *value* is not automatically expected *utility* when preferences over uncertain lotteries are nonlinear. If the adverse outcome violates a critical service obligation, a chance constraint or worst-case guardrail may be more appropriate than averaging over it.

### Robustness asks whether the chosen alternative survives honest disagreement

Stakeholders may agree on measured effects but differ on preference weights. Rather than demanding false consensus, report the weight regions that favor each feasible concept. The Pareto frontier identifies alternatives that cannot be improved on one attribute without worsening another, but it does not itself choose the winner. Sensitivity analysis can expose a decision that changes because of one weakly estimated attribute; this suggests targeted evidence collection, not necessarily a new debate about every weight.

Northstar's value evaluation should therefore distinguish three layers: measured or predicted outcomes, uncertainty in those outcomes, and stakeholder preferences over them. State who authorized the value anchors and feasibility constraints, what decision horizon is assumed, and whether the result is stable under plausible alternative assumptions. A defensible value model is not an algorithm that makes conflict vanish. It makes the source of conflict visible and prevents quantitative formatting from disguising it.

## Worked engineering case

Average wait, p95 wait, on-time arrival and satisfaction may measure overlapping service quality. Four weights of 0.15 each can covertly assign 0.60 to one phenomenon.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

A 0.73 weighted sum is not a physical measurement or proof of superiority. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Resource, affordability, schedule, feasibility, and optimization models](08-resource-affordability-schedule-feasibility-and-optimiz.md); the next connection is [DOE, parametric analysis, uncertainty, sensitivity, and Down-select Review](10-doe-parametric-analysis-uncertainty-sensitivity-and-dow.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Rebuild a scorecard grouping overlapping service measures, then test two plausible stakeholder weight sets.

**Problem B — Adversarial review.** What evidence would make stakeholders reconsider the weight assigned to accessibility?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 9: Value functions and double counting](../labs/lab-09-objectives-value-functions-and-multiattribute-evaluatio.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 9 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.


## Advanced worked practice

- [Deep workshop — Robust Concepts, Regret, and Value of Information](../practice/robust.md)
- [Corresponding independent laboratory](../practice/lab-robust.md)
- [Interactive workbench](../practice/WORKBENCH.html)
