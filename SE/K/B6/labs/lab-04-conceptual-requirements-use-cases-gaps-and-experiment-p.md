# Hypothetical Laboratory 4 — Concept-neutral requirements and gap experiments

*Book 6: System Conceptual Design · Fictional Northstar case · Week 4*

## Mission brief

You are the independent review team for a proposed Northstar regional mobility service. Your job is **not** to optimize the supplied favorite; it is to decide which claim can be supported now and what should happen next. The supplied material is synthetic. No result here qualifies a real vehicle, a transportation service or a safety-critical system.

**Case packet:** “Two wheelchair-capable autonomous shuttles” dictates a solution. “At least 95% of eligible accessible requests are offered an appropriate pickup within 15 minutes during the defined event-day profile” states a measurable service claim, though it still needs definitions for eligible, offered, and event-day.

**Technical focus:** A conceptual requirement should constrain an observable outcome, not preselect its realization. Record a verification idea early, but keep alternatives open until evidence supports selection. A capability gap is a difference between needed and demonstrated behavior, not merely a feature missing from the incumbent concept.

## Your deliverable

Convert four solution-loaded features into measurable, concept-neutral outcomes and plan one discrimination experiment per outcome.

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

An impressive precision target is not useful if eligibility or the population denominator is undefined. A reviewer asks: **Which requirements belong at the service level rather than the vehicle level?** Your package must answer this in a way that changes either a design decision, a test plan or an explicit uncertainty status. Do not give a generic “more testing needed” response.

## Self-check before opening the reference guidance

| Criterion | Points |
|---|---:|
| Problem and mission scope explicitly bounded | 2 |
| Model is reconstructable, with units and revisions | 2 |
| Critical counterexample is treated seriously | 2 |
| Evidence request has objective acceptance logic | 2 |
| Decision limits and action owners are clear | 2 |

<details><summary>Reference reasoning and review hints</summary>

An appropriate response begins by classifying the packet: the supplied numbers are **teaching assumptions or example observations**, not automatically operational evidence. For this week's situation, the essential conceptual distinction is: A conceptual requirement should constrain an observable outcome, not preselect its realization. Record a verification idea early, but keep alternatives open until evidence supports selection. A capability gap is a difference between needed and demonstrated behavior, not merely a feature missing from the incumbent concept.

A credible submission explicitly handles the counterargument that an impressive precision target is not useful if eligibility or the population denominator is undefined. State whether a different plausible assumption could overturn your recommendation and what experiment would discriminate the possibilities. Strong work can conclude that the information is insufficient; unsupported unconditional approval should score poorly.

The best answer is *not uniquely determined* by this case. Grade the traceability, calculation, falsifiability, and clarity of decision limits rather than whether the learner matches a preferred diagram or recommendation.

</details>

## Return to the curriculum

Read [Chapter 4](../chapters/04-conceptual-requirements-use-cases-gaps-and-experiment-p.md) as needed, then complete the independent assessment in [Course Week 4](../../../C/P2/EN645767.md). This hypothetical lab prepares technique; it is not the course's submitted solution.
