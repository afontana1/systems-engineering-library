# Hypothetical Laboratory 9 — Supportability and life-cycle costs

*Book 7: System Design and Integration · Fictional Northstar case · Week 9*

## Mission brief

You are the independent review team for a proposed Northstar regional mobility service. Your job is **not** to optimize the supplied favorite; it is to decide which claim can be supported now and what should happen next. The supplied material is synthetic. No result here qualifies a real vehicle, a transportation service or a safety-critical system.

**Case packet:** A component costing $12,000 with a $2,500 annual support obligation over five years totals $24,500 before discounting, failures or disposal. Another option at $16,000 and $1,000/year totals $21,000 under the same simplifications.

**Technical focus:** Support architecture includes spares, repair knowledge, update channels, suppliers, staffing, consumables and end-of-life handling. Compare alternatives using consistent boundaries across acquisition and operations. A cheap vehicle platform may impose expensive recurring uptime and supply risks.

## Your deliverable

Build an undiscounted life-cycle comparison, then list the omitted sources of uncertainty.

Create a small but reviewable package with these four files:

1. `W09-decision.md` — claim, decision alternatives, scenario, recommendation and residual uncertainty.
2. `W09-evidence.csv` — `claim_id,source_revision,configuration,assumption,method,observed_or_predicted_result,status,limitation`.
3. `W09-model.md` — your calculation, causal chain, interface contract or structural representation, with units and revisions.
4. `W09-review.md` — a red-team objection and your technical response.

**Task sequence**

- **First pass, without calculation:** Identify the objective, the stakeholder bearing a consequence, and at least two competing explanations or design alternatives.
- **Model:** Construct the minimum useful representation. Keep the difference between a projected result and a measured result visible.
- **Stress:** Vary one critical assumption, introduce a fault or change the mission scenario; determine whether the decision reverses or becomes conditional.
- **Evidence:** Define an observable outcome, acceptance rule and test article or model version. Name what this exercise cannot establish.
- **Review:** Write a recommendation of **accept for next stage**, **accept conditionally**, **defer pending evidence** or **reject**; support it with specific facts.

## The twist

Lowest acquisition cost and lowest lifecycle cost are not synonyms. A reviewer asks: **What supplier discontinuation would invalidate the support strategy?** Your package must answer this in a way that changes either a design decision, a test plan or an explicit uncertainty status. Do not give a generic “more testing needed” response.

## Self-check before opening the reference guidance

| Criterion | Points |
|---|---:|
| Problem and mission scope explicitly bounded | 2 |
| Model is reconstructable, with units and revisions | 2 |
| Critical counterexample is treated seriously | 2 |
| Evidence request has objective acceptance logic | 2 |
| Decision limits and action owners are clear | 2 |

<details><summary>Reference reasoning and review hints</summary>

An appropriate response begins by classifying the packet: the supplied numbers are **teaching assumptions or example observations**, not automatically operational evidence. For this week's situation, the essential conceptual distinction is: Support architecture includes spares, repair knowledge, update channels, suppliers, staffing, consumables and end-of-life handling. Compare alternatives using consistent boundaries across acquisition and operations. A cheap vehicle platform may impose expensive recurring uptime and supply risks.

A credible submission explicitly handles the counterargument that lowest acquisition cost and lowest lifecycle cost are not synonyms. State whether a different plausible assumption could overturn your recommendation and what experiment would discriminate the possibilities. Strong work can conclude that the information is insufficient; unsupported unconditional approval should score poorly.

The best answer is *not uniquely determined* by this case. Grade the traceability, calculation, falsifiability, and clarity of decision limits rather than whether the learner matches a preferred diagram or recommendation.

</details>

## Return to the curriculum

Read [Chapter 9](../chapters/09-design-for-supportability-producibility-supply-sustaina.md) as needed, then complete the independent assessment in [Course Week 9](../../../C/P2/EN645768.md). This hypothetical lab prepares technique; it is not the course's submitted solution.
