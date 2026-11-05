# Hypothetical Laboratory 4 — Measurement and statistical confidence

*Book 8: System Test and Evaluation · Fictional Northstar case · Week 4*

## Mission brief

You are the independent review team for a proposed Northstar regional mobility service. Your job is **not** to optimize the supplied favorite; it is to decide which claim can be supported now and what should happen next. The supplied material is synthetic. No result here qualifies a real vehicle, a transportation service or a safety-critical system.

**Case packet:** With zero failures in 30 independent Bernoulli trials, the exact one-sided 95% upper bound on failure probability is 1−0.05^(1/30)≈9.50%. It does not demonstrate failure probability below 1%.

**Technical focus:** First identify the estimand and sampling regime. Measurement uncertainty, natural variation, model uncertainty and sampling uncertainty are not interchangeable. Design experiments to control nuisance variables and reveal interactions; a single favorable mean hides tails and rare failure risk.

## Your deliverable

Specify a sampling plan for one high-percentile wait metric and one failure-rate claim; defend independence and measurement error assumptions.

Create a small but reviewable package with these four files:

1. `W04-decision.md` — claim, decision alternatives, scenario, recommendation and residual uncertainty.
2. `W04-evidence.csv` — `claim_id,source_revision,configuration,assumption,method,observed_or_predicted_result,status,limitation`.
3. `W04-model.md` — your calculation, causal chain, interface contract or structural representation, with units and revisions.
4. `W04-review.md` — a red-team objection and your technical response.

**Task sequence**

- **First pass, without calculation:** Identify the objective, the stakeholder bearing a consequence, and at least two competing explanations or design alternatives.
- **Model:** Construct the minimum useful representation. Keep the difference between a projected result and a measured result visible.
- **Stress:** Vary one critical assumption, introduce a fault or change the mission scenario; determine whether the decision reverses or becomes conditional.
- **Evidence:** Define an observable outcome, acceptance rule and test article or model version. Name what this exercise cannot establish.
- **Review:** Write a recommendation of **accept for next stage**, **accept conditionally**, **defer pending evidence** or **reject**; support it with specific facts.

## The twist

Zero observed failures is evidence, not proof of zero risk. A reviewer asks: **How does common-cause dependence change your confidence statement?** Your package must answer this in a way that changes either a design decision, a test plan or an explicit uncertainty status. Do not give a generic “more testing needed” response.

## Self-check before opening the reference guidance

| Criterion | Points |
|---|---:|
| Problem and mission scope explicitly bounded | 2 |
| Model is reconstructable, with units and revisions | 2 |
| Critical counterexample is treated seriously | 2 |
| Evidence request has objective acceptance logic | 2 |
| Decision limits and action owners are clear | 2 |

<details><summary>Reference reasoning and review hints</summary>

An appropriate response begins by classifying the packet: the supplied numbers are **teaching assumptions or example observations**, not automatically operational evidence. For this week's situation, the essential conceptual distinction is: First identify the estimand and sampling regime. Measurement uncertainty, natural variation, model uncertainty and sampling uncertainty are not interchangeable. Design experiments to control nuisance variables and reveal interactions; a single favorable mean hides tails and rare failure risk.

A credible submission explicitly handles the counterargument that zero observed failures is evidence, not proof of zero risk. State whether a different plausible assumption could overturn your recommendation and what experiment would discriminate the possibilities. Strong work can conclude that the information is insufficient; unsupported unconditional approval should score poorly.

The best answer is *not uniquely determined* by this case. Grade the traceability, calculation, falsifiability, and clarity of decision limits rather than whether the learner matches a preferred diagram or recommendation.

</details>

## Return to the curriculum

Read [Chapter 4](../chapters/04-apply-measurement-science-statistics-doe-and-sample-rat.md) as needed, then complete the independent assessment in [Course Week 4](../../../C/P2/EN645769.md). This hypothetical lab prepares technique; it is not the course's submitted solution.


## Extended worked problems and lab

Study the [worked problem workshop on zero-failure confidence and test design](../practice/confidence.md), then complete the [extended laboratory](../practice/lab-confidence.md). The exercises are separate from the original assessed coursework.
