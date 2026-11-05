# Chapter 10 — DOE and uncertainty-driven down-select

*Book 6: System Conceptual Design · Week 10 — DOE, parametric analysis, uncertainty, sensitivity, and Down-select Review*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 10](../labs/lab-10-doe-parametric-analysis-uncertainty-sensitivity-and-dow.md) without looking at the solution → return to [Week 10 of the course guide](../../../C/P2/EN645767.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-767-w10.md) is optional review, not the primary reading.

## The engineering problem

At this point the Northstar team is still free to select among competing mobility-service concepts. A proposed autonomous shuttle is one hypothesis, not the definition of the problem. The governing question this week is **doe and uncertainty-driven down-select**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

A design of experiments identifies influential factors and interactions using a deliberate trial matrix. Sensitivity checks a decision, not just a model coefficient. If plausible parameter ranges reverse rankings, the proper next action may be a discriminating experiment rather than a premature down-select.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Experiments have information value when results might alter the choice between still-available alternatives.

### Distinguishing related ideas

A sensitivity plot reveals influential assumptions; a designed experiment deliberately varies factors to identify response mechanisms and interactions.

### Interpretation and boundary conditions

An elaborate simulation may add little if the decision is already dominated, whereas a modest charging-window measurement can resolve feasibility.

## Deeper theory: experimental design turns concept selection into controlled learning

### A simulation result is conditional on design choices and uncertainty

A concept study often produces a response such as average wait time, energy use, reliability, or lifecycle cost from inputs such as fleet size, charging strategy, dispatch policy, and passenger demand. The functional relationship can be written as `Y = f(x, z, theta)`, where `x` contains controllable design decisions, `z` represents operating conditions, and `theta` represents uncertain model parameters. Confusing these categories leads to false recommendations. An attractive result at the nominal demand level may not survive adverse demand, and a sensitivity to uncertain battery degradation cannot be eliminated by choosing a different dispatch algorithm alone.

Designed experiments explore the response systematically. Randomly varying all inputs can estimate broad sensitivities, but may waste expensive simulation runs and obscure interactions. A factorial design explores combinations of factor levels so an effect can be interpreted relative to others. However, reduced or fractional designs can **alias** interactions with main effects. This matters when a policy works only for one fleet size: a model that assumes additive effects may recommend a combination never actually tested.

### Interactions are engineering mechanisms

Suppose policy A reduces waiting by 20 seconds with four vehicles and by 80 seconds with eight vehicles. The policy effect depends on fleet size. An interaction contrast, formed from differences of response differences, reveals that dependence. It does not by itself explain the mechanism; examining queue saturation, dispatch balancing, and communication overhead can. Experiments are strongest when empirical contrasts are paired with physical or operational reasoning.

Replicating a stochastic simulation at the same design point estimates run-to-run variability, whereas changing inputs explores systematic differences. Using common random numbers for two competing concepts can improve precision of the *difference* when paired outputs are positively correlated, provided streams are controlled correctly. Increasing the number of runs cannot fix a misspecified demand model or an unmodeled failure mode. Statistical precision and model credibility must be tracked separately.

### Robustness is distinct from average optimization

An alternative with a mean journey time of 12 minutes may be inferior to one with 13 minutes if the first frequently exceeds a 20-minute mission limit. The design decision may therefore use a chance constraint such as `P(T <= 20 min) >= 0.95` under a specified demand distribution, or a worst-case criterion over a justified uncertainty set. These criteria answer different questions. Chance constraints depend on assumed probability distributions; worst-case design depends on the credibility of extreme scenarios; minimizing variance can sometimes sacrifice the primary mission objective.

Constraints should be applied before comparing desirability. A concept that violates a safety requirement should not recover first place merely by earning high scores on cost or comfort. Among feasible concepts, a Pareto frontier identifies alternatives for which improving one objective requires worsening another. That frontier does not choose a winner automatically; stakeholder value judgments are still required.

### A down-select includes the value of additional evidence

When two concepts have similar expected value, a highly uncertain model prediction may make a prototype or field trial more valuable than an immediate irreversible commitment. The relevant question is whether new data could change the selected architecture, not whether researchers would find the data interesting. A targeted experiment may resolve uncertainty in peak-demand behavior that dominates the choice, while more runs at nominal conditions add little decision value.

Results should state the sampled design space, statistical variability, model assumptions, extrapolation limits, and conditions under which rankings reverse. A down-select is justified by how reliably it explains the trade between alternatives, not by the visual precision of a fitted response surface.

## Worked engineering case

Scores A=0.73, B=0.70, C=0.64, D=0.72 imply only a 0.01 margin between A and D. A potential 0.04 score shift from availability uncertainty overwhelms that nominal margin.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

A deterministic top score hides epistemic uncertainty and model-form bias. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Objectives, value functions, and multiattribute evaluation](09-objectives-value-functions-and-multiattribute-evaluatio.md); the next connection is [Risk, opportunity, affordability, schedule, and Concept Validation Review](11-risk-opportunity-affordability-schedule-and-concept-val.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Run a two-factor experiment with peak demand and vehicle availability; show at least one ranking reversal.

**Problem B — Adversarial review.** What single field experiment could separate A and D?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 10: DOE and uncertainty-driven down-select](../labs/lab-10-doe-parametric-analysis-uncertainty-sensitivity-and-dow.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 10 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.
