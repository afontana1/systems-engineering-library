# Chapter 12 — Defend the Baseline; Learn from the Project

*EN.645.667 · Week 12 · Final proposal, evidence defense and professional reflection · Preceded by [Chapter 11](11-proposal-red-team.md); continue with the final course portfolio.*

> **Study contract.** This chapter teaches the concepts behind Week 12; practice them in [Hypothetical Lab 12](../labs/lab-12-baseline-defense-and-retrospective.md), then complete the [original Week 12 coursework](../../../C/P0/EN645667.md). These fictional examples are not contractual or safety approvals.

## The management problem

The course ends where real project management becomes difficult: a manager must defend a proposal and baseline under scrutiny without claiming certainty the evidence cannot support. A successful defense is not an unbroken series of confident answers. It shows where commitments come from, how numbers were produced, what could invalidate them, and who is authorized to decide when circumstances change.

Your artifacts should tell one traceable story. Customer need creates scope; scope becomes authorized work; work is scheduled and costed; progress rules define what counts as accomplishment; risks identify possible departures; configuration records retain valid versions; and test results substantiate acceptance. If any connection is missing, the manager should describe the limitation and a plan to close it.

Project closure and transition require more than a final briefing. The receiving organization needs controlled configuration, operating and maintenance responsibilities, unresolved limitations, training, acceptance evidence, warranties or support arrangements as applicable, and an ownership map for residual risk. The educational shuttle case stops at a proposal and planning defense; it does not establish real deployment approval.

## Develop the method

Prepare a concise executive narrative and a separate evidence trail. In the opening five minutes state the customer objective, technical concept, price envelope, forecast, critical constraints, three largest risks, and exact approval being requested. Then defend the details with live links to authoritative calculations. Keep a decision log of questions you could not answer; inventing numbers under pressure is more damaging than marking an item open.

For the retrospective, distinguish process quality from project outcome. A favorable outcome may occur despite an unreliable estimate; an unfavorable outcome may follow a good decision under uncertainty. Identify one technique to retain, one assumption to challenge in future projects, and one control that became paperwork rather than useful feedback.

## The mechanism beneath the method

A project defense has two audiences: the sponsor deciding whether the commitment is credible and the engineering team learning why outcomes differed from forecasts.

### Distinguishing related ideas

A retrospective that only explains variance after the fact lacks causal force unless it identifies signals that could have changed earlier decisions.

### Interpretation and boundary conditions

The useful product is a revised decision model—what to measure, which assumptions to retire, and what authority must act when evidence changes.

## Worked Northstar project example

A reviewer notes that the $8.4M proposal lies below the $8.8M ceiling but the simple EVM extrapolation at Month 5 gives $9.0M. The correct answer is not to conceal one figure. They represent different moments and purposes: proposed price versus forecast cost under a continuing CPI assumption. Reconcile them in an affordability and margin-risk discussion; if the project is already executing, identify contract structure and financial exposure before making claims about profit or customer liability.

## Evidence stewardship after the presentation

The final review may be a simulated board, but its most important habit transfers to real engineering: a person should be able to reconstruct how a decision was made after its authors have left the room. Store the authoritative versions of requirements, work packages, cost estimates, schedule network, EVM status, changes, risks and test evidence. The links between artifacts should survive renaming and revision. A polished slide is not a substitute for its underlying calculation.

A final defense should anticipate three adversarial questions: “Which assumption drives the answer?”, “What evidence would make you reverse this decision?”, and “Who has the authority to accept the consequence?” A manager who can answer those questions has a more credible plan than one who memorizes a fixed date and price. In the shuttle case, answer the distinction between **proposal price** and **cost forecast** clearly. An $8.4M offer and an EAC of $9.0M are not numerically contradictory in themselves; they are different analytical objects with serious possible affordability implications that depend on contract and execution context.

**Transfer and handoff.** A receiving operations team should know which product configuration exists, how problems are reported, which procedures are validated, what limitations remain and who owns residual actions. Because this project is an educational planning exercise, the final deliverable is a defensible proposal and evidence roadmap, not an operational approval. Label any unsupported future claim as such.

For the personal retrospective, avoid broad statements like “communication is important.” Name a concrete control that changed your judgment, such as reconciling the proposal's 18-month commitment with resource-loaded network logic before submission. State the trigger that will cause you to apply that control in the next technical project.

## Graduate synthesis: baselines as testable promises across time

### A baseline is a configuration-bound hypothesis

An integrated baseline records a proposed relation between scope, resources, time, technical performance, and contractual conditions. It is not a prophecy. Its forecast can be tested against actual execution, but only when the identity of the underlying configuration remains controlled. If a project reports cost improvement after quietly deleting an acceptance test, it has changed the estimand, not necessarily improved performance. Denote the baseline as `B₀ = (S₀, C₀, T₀, Q₀, A₀)`, where the entries are scope, cost, schedule, quality/technical objectives, and governing assumptions. Later results must either be compared against that same tuple or accompanied by an explicit authorized change record.

A defense is therefore an *argument from evidence*, not a recital of attractive values. The claim “Northstar will be accepted in month 18” should trace backward to remaining work, resource availability, dependent deliveries, rework risk, verification completion, and the definition of acceptance. Because these are coupled, a schedule delay can produce cost growth, and a test failure can invalidate both. Forecasts should be conditional: month 18 *if* the identified dependencies and assumptions hold.

### Combine controls without double-counting certainty

Earned-value measures answer narrower questions than program assurance. At a status date, `CPI = EV / AC` and `SPI = EV / PV` summarize cost and schedule efficiency against a defined baseline. If `BAC = $8.0M`, `EV = $4.0M`, and `AC = $5.0M`, then `CPI = 0.8`; a simple cost-based forecast is `EAC = BAC / CPI = $10.0M`. This is a conditional extrapolation, not a guarantee. It assumes future work will resemble measured work and that earned value reflects genuine physical progress. If the remaining work is primarily high-risk integration rather than repeated production, the ratio may be misleading.

Reconcile the numerical forecast with a bottom-up estimate: `EAC = AC + ETC`, where *estimate to complete* includes remaining labor, materials, rework, test resources, and reserves consistent with the approved scope. The two EAC approaches need not agree; disagreement is a diagnostic opportunity. A convincing baseline defense explains why a favored forecast is applicable, what alternative it would displace, and how decisions change under adverse scenarios.

### Institutionalize learning without retroactive storytelling

Project retrospectives have a causal-identification problem. Teams observe what happened, but cannot directly observe what would have happened under a different management choice. A schedule recovery followed by earlier delivery does not prove the recovery action caused it; suppliers may have caught up independently. Preserve the decision date, information available then, options considered, rationale, predicted observable effect, and later evidence. This prevents hindsight from converting every successful outcome into evidence of an optimal decision.

For Northstar, a good closing recommendation might be: retain the revised service concept subject to a witnessed accessibility test and one additional seasonal demand study. It names the condition, the evidence needed, the responsible authority, and a reopening trigger. **Readiness is bounded permission to proceed**, not a declaration that residual uncertainty has vanished. The professional standard is to make those bounds clear enough for a successor to use the baseline safely.

## Boundary of the method

The phrase “baseline approved” does not establish technical or operational suitability. Define the scope of authorization and the evidence still needed for later gates.

## Retrieval questions and explained answers

1. **Question:** What should a manager do when a reviewer challenges an unknown number?
   **Explanation:** State the unknown, cite the controlled source if available, assign an action and avoid invented precision.
2. **Question:** Why compare proposed price and EAC carefully?
   **Explanation:** They refer to different purposes and potentially different contract, accounting and time assumptions.
3. **Question:** What distinguishes a useful retrospective?
   **Explanation:** It changes future decision practices and controls, not merely recording congratulations or blame.

## Put this into practice

Work through [Lab 12: The Final Management Review Board](../labs/lab-12-baseline-defense-and-retrospective.md), then write a short paragraph on how the laboratory simplifies the real-world management problem. Use the [existing short Week 12 primer](../../P0-text/lessons/645-667-w12.md) for a second explanation. The assessed deliverable is defined in the original course guide, not by the hypothetical lab.
