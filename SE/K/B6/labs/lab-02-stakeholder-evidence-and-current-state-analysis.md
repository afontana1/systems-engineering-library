# Hypothetical Laboratory 2 — Evidence-based stakeholder needs

*Book 6: System Conceptual Design · Fictional Northstar case · Week 2*

## Mission brief

You are the independent review team for a proposed Northstar regional mobility service. Your job is **not** to optimize the supplied favorite; it is to decide which claim can be supported now and what should happen next. The supplied material is synthetic. No result here qualifies a real vehicle, a transportation service or a safety-critical system.

**Case packet:** One wheelchair user reports a pickup 25 minutes late during a football game. Log event-day conditions and distinguish a single 25-minute lateness observation from the unknown distribution of wait times.

**Technical focus:** A stakeholder statement contains observation, meaning, desired outcome, and proposed solution; these are different data types. Convert verbatim interviews into claims with conditions, frequency, source, and uncertainty before assigning priorities. One dramatic interview must not silently become a fleet-wide probability estimate.

## Your deliverable

Create an evidence ledger for six stakeholder claims; identify which are observations, inferences and unmet needs.

Create a small but reviewable package with these four files:

1. `W02-decision.md` — claim, decision alternatives, scenario, recommendation and residual uncertainty.
2. `W02-evidence.csv` — `claim_id,source_revision,configuration,assumption,method,observed_or_predicted_result,status,limitation`.
3. `W02-model.md` — your calculation, causal chain, interface contract or structural representation, with units and revisions.
4. `W02-review.md` — a red-team objection and your technical response.

**Task sequence**

- **First pass, without calculation:** Identify the objective, the stakeholder bearing a consequence, and at least two competing explanations or design alternatives.
- **Model:** Construct the minimum useful representation. Keep the difference between a projected result and a measured result visible.
- **Stress:** Vary one critical assumption, introduce a fault or change the mission scenario; determine whether the decision reverses or becomes conditional.
- **Evidence:** Define an observable outcome, acceptance rule and test article or model version. Name what this exercise cannot establish.
- **Review:** Write a recommendation of **accept for next stage**, **accept conditionally**, **defer pending evidence** or **reject**; support it with specific facts.

## The twist

A popular preference may conflict with a nonnegotiable accessibility or safety outcome. A reviewer asks: **Which stakeholders can be harmed without being frequent system users?** Your package must answer this in a way that changes either a design decision, a test plan or an explicit uncertainty status. Do not give a generic “more testing needed” response.

## Self-check before opening the reference guidance

| Criterion | Points |
|---|---:|
| Problem and mission scope explicitly bounded | 2 |
| Model is reconstructable, with units and revisions | 2 |
| Critical counterexample is treated seriously | 2 |
| Evidence request has objective acceptance logic | 2 |
| Decision limits and action owners are clear | 2 |

<details><summary>Reference reasoning and review hints</summary>

An appropriate response begins by classifying the packet: the supplied numbers are **teaching assumptions or example observations**, not automatically operational evidence. For this week's situation, the essential conceptual distinction is: A stakeholder statement contains observation, meaning, desired outcome, and proposed solution; these are different data types. Convert verbatim interviews into claims with conditions, frequency, source, and uncertainty before assigning priorities. One dramatic interview must not silently become a fleet-wide probability estimate.

A credible submission explicitly handles the counterargument that a popular preference may conflict with a nonnegotiable accessibility or safety outcome. State whether a different plausible assumption could overturn your recommendation and what experiment would discriminate the possibilities. Strong work can conclude that the information is insufficient; unsupported unconditional approval should score poorly.

The best answer is *not uniquely determined* by this case. Grade the traceability, calculation, falsifiability, and clarity of decision limits rather than whether the learner matches a preferred diagram or recommendation.

</details>

## Return to the curriculum

Read [Chapter 2](../chapters/02-stakeholder-evidence-and-current-state-analysis.md) as needed, then complete the independent assessment in [Course Week 2](../../../C/P2/EN645767.md). This hypothetical lab prepares technique; it is not the course's submitted solution.
