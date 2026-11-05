# Hypothetical Laboratory 12 — Concept baseline and handoff

*Book 6: System Conceptual Design · Fictional Northstar case · Week 12*

## Mission brief

You are the independent review team for a proposed Northstar regional mobility service. Your job is **not** to optimize the supplied favorite; it is to decide which claim can be supported now and what should happen next. The supplied material is synthetic. No result here qualifies a real vehicle, a transportation service or a safety-critical system.

**Case packet:** A mixed-fleet concept can baseline accessible service zones while treating autonomous operations as conditional pending demonstration. These statements must not share an unconditional approval status.

**Technical focus:** The conceptual-design handoff transfers not only drawings and preferred options but decision rationale, alternatives rejected, assumptions, model versions and evidence gaps. A receiving team must be able to reconstruct why the baseline holds and what would invalidate it.

## Your deliverable

Produce a decision-log excerpt and baseline manifest; require the next team to challenge five inherited assumptions.

Create a small but reviewable package with these four files:

1. `W12-decision.md` — claim, decision alternatives, scenario, recommendation and residual uncertainty.
2. `W12-evidence.csv` — `claim_id,source_revision,configuration,assumption,method,observed_or_predicted_result,status,limitation`.
3. `W12-model.md` — your calculation, causal chain, interface contract or structural representation, with units and revisions.
4. `W12-review.md` — a red-team objection and your technical response.

**Task sequence**

- **First pass, without calculation:** Identify the objective, the stakeholder bearing a consequence, and at least two competing explanations or design alternatives.
- **Model:** Construct the minimum useful representation. Keep the difference between a projected result and a measured result visible.
- **Stress:** Vary one critical assumption, introduce a fault or change the mission scenario; determine whether the decision reverses or becomes conditional.
- **Evidence:** Define an observable outcome, acceptance rule and test article or model version. Name what this exercise cannot establish.
- **Review:** Write a recommendation of **accept for next stage**, **accept conditionally**, **defer pending evidence** or **reject**; support it with specific facts.

## The twist

The beautiful final slide cannot replace a configuration-controlled claim-to-evidence trail. A reviewer asks: **Which design decision is unsafe to freeze without a new test?** Your package must answer this in a way that changes either a design decision, a test plan or an explicit uncertainty status. Do not give a generic “more testing needed” response.

## Self-check before opening the reference guidance

| Criterion | Points |
|---|---:|
| Problem and mission scope explicitly bounded | 2 |
| Model is reconstructable, with units and revisions | 2 |
| Critical counterexample is treated seriously | 2 |
| Evidence request has objective acceptance logic | 2 |
| Decision limits and action owners are clear | 2 |

<details><summary>Reference reasoning and review hints</summary>

An appropriate response begins by classifying the packet: the supplied numbers are **teaching assumptions or example observations**, not automatically operational evidence. For this week's situation, the essential conceptual distinction is: The conceptual-design handoff transfers not only drawings and preferred options but decision rationale, alternatives rejected, assumptions, model versions and evidence gaps. A receiving team must be able to reconstruct why the baseline holds and what would invalidate it.

A credible submission explicitly handles the counterargument that the beautiful final slide cannot replace a configuration-controlled claim-to-evidence trail. State whether a different plausible assumption could overturn your recommendation and what experiment would discriminate the possibilities. Strong work can conclude that the information is insufficient; unsupported unconditional approval should score poorly.

The best answer is *not uniquely determined* by this case. Grade the traceability, calculation, falsifiability, and clarity of decision limits rather than whether the learner matches a preferred diagram or recommendation.

</details>

## Return to the curriculum

Read [Chapter 12](../chapters/12-final-concept-baseline-oral-defense-and-handoff.md) as needed, then complete the independent assessment in [Course Week 12](../../../C/P2/EN645767.md). This hypothetical lab prepares technique; it is not the course's submitted solution.
