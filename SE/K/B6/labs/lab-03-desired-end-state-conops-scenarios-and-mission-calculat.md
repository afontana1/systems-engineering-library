# Hypothetical Laboratory 3 — ConOps and mission measures

*Book 6: System Conceptual Design · Fictional Northstar case · Week 3*

## Mission brief

You are the independent review team for a proposed Northstar regional mobility service. Your job is **not** to optimize the supplied favorite; it is to decide which claim can be supported now and what should happen next. The supplied material is synthetic. No result here qualifies a real vehicle, a transportation service or a safety-critical system.

**Case packet:** If requests arrive at 8/hour and an initial concept can serve only 6/hour, backlog grows at approximately 2 requests/hour under sustained demand. Averages hide event surges and inaccessible trips.

**Technical focus:** A Concept of Operations describes actors, triggers, system states, normal and abnormal sequences, and the mission outcomes to be delivered. It is not a marketing narrative. Scenarios reveal hidden boundary conditions and supply the operating envelope used by early mission models.

## Your deliverable

Write a five-step event-day scenario with one road closure and a wheelchair-accessible request, then identify the model inputs required.

Create a small but reviewable package with these four files:

1. `W03-decision.md` — claim, decision alternatives, scenario, recommendation and residual uncertainty.
2. `W03-evidence.csv` — `claim_id,source_revision,configuration,assumption,method,observed_or_predicted_result,status,limitation`.
3. `W03-model.md` — your calculation, causal chain, interface contract or structural representation, with units and revisions.
4. `W03-review.md` — a red-team objection and your technical response.

**Task sequence**

- **First pass, without calculation:** Identify the objective, the stakeholder bearing a consequence, and at least two competing explanations or design alternatives.
- **Model:** Construct the minimum useful representation. Keep the difference between a projected result and a measured result visible.
- **Stress:** Vary one critical assumption, introduce a fault or change the mission scenario; determine whether the decision reverses or becomes conditional.
- **Evidence:** Define an observable outcome, acceptance rule and test article or model version. Name what this exercise cannot establish.
- **Review:** Write a recommendation of **accept for next stage**, **accept conditionally**, **defer pending evidence** or **reject**; support it with specific facts.

## The twist

A calculator that reports an average wait without measuring unserved requests can reward exclusion. A reviewer asks: **How would an event-day mission scenario alter your service-capacity assumption?** Your package must answer this in a way that changes either a design decision, a test plan or an explicit uncertainty status. Do not give a generic “more testing needed” response.

## Self-check before opening the reference guidance

| Criterion | Points |
|---|---:|
| Problem and mission scope explicitly bounded | 2 |
| Model is reconstructable, with units and revisions | 2 |
| Critical counterexample is treated seriously | 2 |
| Evidence request has objective acceptance logic | 2 |
| Decision limits and action owners are clear | 2 |

<details><summary>Reference reasoning and review hints</summary>

An appropriate response begins by classifying the packet: the supplied numbers are **teaching assumptions or example observations**, not automatically operational evidence. For this week's situation, the essential conceptual distinction is: A Concept of Operations describes actors, triggers, system states, normal and abnormal sequences, and the mission outcomes to be delivered. It is not a marketing narrative. Scenarios reveal hidden boundary conditions and supply the operating envelope used by early mission models.

A credible submission explicitly handles the counterargument that a calculator that reports an average wait without measuring unserved requests can reward exclusion. State whether a different plausible assumption could overturn your recommendation and what experiment would discriminate the possibilities. Strong work can conclude that the information is insufficient; unsupported unconditional approval should score poorly.

The best answer is *not uniquely determined* by this case. Grade the traceability, calculation, falsifiability, and clarity of decision limits rather than whether the learner matches a preferred diagram or recommendation.

</details>

## Return to the curriculum

Read [Chapter 3](../chapters/03-desired-end-state-conops-scenarios-and-mission-calculat.md) as needed, then complete the independent assessment in [Course Week 3](../../../C/P2/EN645767.md). This hypothetical lab prepares technique; it is not the course's submitted solution.
