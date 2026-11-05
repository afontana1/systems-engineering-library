# A08 — Capstone change challenge: re-engineer a stressed service

**Competency:** propose, implement and defend a coherent change across architecture, requirements, model assumptions, experiments, tests and review documentation.

## The engineering change request

A hypothetical stakeholder asks Northstar to maintain more service under temporary vehicle outages while avoiding unsafe commitment when telemetry is stale. The temptation is to “add more vehicles” or “shorten trips.” Those may improve simulated metrics but do not solve the information-trust problem or establish an implementable policy. Begin with the mission and operational constraint; specify who may authorize a degraded-mode decision and what is displayed to users.

Your proposed revision must identify a bounded concept change and its side effects. Possible *learning-only* options include queue admission thresholds, warning/escalation messages, an explicit stale-status hold, adjustable scheduling deadlines, or reserve capacity. Do not implement a real dispatch interface or claim a safe fallback without a hazard argument.

## A disciplined change sequence

1. **Define the need:** Which user-facing failure is the change intended to reduce? Specify a measurable outcome and a no-harm condition.
2. **Update the architecture:** Add or change components/interfaces in `models/architecture.json`, including failure semantics and responsible authority.
3. **Update requirements:** Revise the CSV register and verification plan together. Changes that preserve references but change meanings still require independent review.
4. **Implement a minimal model extension:** Add one scenario parameter or one safe-state transition; document why it represents the proposed concept.
5. **Run controlled comparisons:** Use the same synthetic arrivals across alternatives, multiple seeds and at least one adverse scenario. Report completion, loss and wait together.
6. **Challenge the outcome:** Which omitted mechanism could reverse the decision? Check data provenance and the exercise's false-positive risks.
7. **Prepare a review disposition:** Demonstrate exactly what changed and what evidence remains unsupported.

## Example analytical trade

If adding a reserve vehicle improves completion under OUTAGE, estimate incremental capacity and the administrative costs implied by standby resources. In the existing model, vehicle count is a configurable integer; it has no operating cost, staffing requirements, maintenance or accessibility attributes. A design trade study that assumes “one more vehicle is free” will make a biased recommendation. Either augment the cost model and justify inputs or state clearly that the experiment isolates a narrow service-capacity effect.

## Final challenge questions

**Exercise 1.** A change improves mean completion but makes some subgroups worse. Is the design ready for approval?

<details><summary>Worked answer</summary>No automatic conclusion. The model needs subgroup attributes and governance criteria; currently those aren't represented. Investigate who bears the burden and whether the new policy is acceptable under agreed stakeholder requirements.</details>

**Exercise 2.** Your changed model passes all unit tests. What else is needed?

<details><summary>Worked answer</summary>Revised requirements, architecture and hazards; updated traces, experiment configuration hashes, sensitivity analysis, validation plan and independent review. The approval claim must remain bounded to the synthetic model.</details>

**Submit:** a versioned engineering change package with model diff, code diff, updated tests, before/after results, evidence manifest and independent review memo. Related: [v11 change and digital thread](../../integrated-lab/chapters/09-change-and-digital-thread.md).
