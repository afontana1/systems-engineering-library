# Hypothetical Laboratory 6 — Cross-discipline preliminary design review

*Book 7: System Design and Integration · Fictional Northstar case · Week 6*

## Mission brief

You are the independent review team for a proposed Northstar regional mobility service. Your job is **not** to optimize the supplied favorite; it is to decide which claim can be supported now and what should happen next. The supplied material is synthetic. No result here qualifies a real vehicle, a transportation service or a safety-critical system.

**Case packet:** A power budget requires 4.5 kW peak while the available supply is rated 4.1 kW. The arithmetic shortfall is 0.4 kW before safety margin; it cannot be closed by presentation polish.

**Technical focus:** A preliminary design review tests internal consistency: power, mass, timing, human authority, fault behavior, maintenance and interfaces must agree. Red-team disagreements should become decisions with owners, not optimistic footnotes. An incomplete model can still support a conditional review if the boundary is explicit.

## Your deliverable

Construct a multidisciplinary conflict table and recommend design, requirement or demonstration changes.

Create a small but reviewable package with these four files:

1. `W06-decision.md` — claim, decision alternatives, scenario, recommendation and residual uncertainty.
2. `W06-evidence.csv` — `claim_id,source_revision,configuration,assumption,method,observed_or_predicted_result,status,limitation`.
3. `W06-model.md` — your calculation, causal chain, interface contract or structural representation, with units and revisions.
4. `W06-review.md` — a red-team objection and your technical response.

**Task sequence**

- **First pass, without calculation:** Identify the objective, the stakeholder bearing a consequence, and at least two competing explanations or design alternatives.
- **Model:** Construct the minimum useful representation. Keep the difference between a projected result and a measured result visible.
- **Stress:** Vary one critical assumption, introduce a fault or change the mission scenario; determine whether the decision reverses or becomes conditional.
- **Evidence:** Define an observable outcome, acceptance rule and test article or model version. Name what this exercise cannot establish.
- **Review:** Write a recommendation of **accept for next stage**, **accept conditionally**, **defer pending evidence** or **reject**; support it with specific facts.

## The twist

Review readiness measures closure of contradictions, not the number of slides presented. A reviewer asks: **Which conflict threatens several disciplines simultaneously?** Your package must answer this in a way that changes either a design decision, a test plan or an explicit uncertainty status. Do not give a generic “more testing needed” response.

## Self-check before opening the reference guidance

| Criterion | Points |
|---|---:|
| Problem and mission scope explicitly bounded | 2 |
| Model is reconstructable, with units and revisions | 2 |
| Critical counterexample is treated seriously | 2 |
| Evidence request has objective acceptance logic | 2 |
| Decision limits and action owners are clear | 2 |

<details><summary>Reference reasoning and review hints</summary>

An appropriate response begins by classifying the packet: the supplied numbers are **teaching assumptions or example observations**, not automatically operational evidence. For this week's situation, the essential conceptual distinction is: A preliminary design review tests internal consistency: power, mass, timing, human authority, fault behavior, maintenance and interfaces must agree. Red-team disagreements should become decisions with owners, not optimistic footnotes. An incomplete model can still support a conditional review if the boundary is explicit.

A credible submission explicitly handles the counterargument that review readiness measures closure of contradictions, not the number of slides presented. State whether a different plausible assumption could overturn your recommendation and what experiment would discriminate the possibilities. Strong work can conclude that the information is insufficient; unsupported unconditional approval should score poorly.

The best answer is *not uniquely determined* by this case. Grade the traceability, calculation, falsifiability, and clarity of decision limits rather than whether the learner matches a preferred diagram or recommendation.

</details>

## Return to the curriculum

Read [Chapter 6](../chapters/06-integrate-multidisciplinary-design-and-conduct-the-pdr-.md) as needed, then complete the independent assessment in [Course Week 6](../../../C/P2/EN645768.md). This hypothetical lab prepares technique; it is not the course's submitted solution.
