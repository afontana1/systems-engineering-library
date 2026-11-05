# Hypothetical Lab 9 — A physical architecture is a trade, not a picture

*Book III: Introduction to Model-Based Systems Engineering · Week 9 · Synthetic educational case, not a deployment or safety assessment.*

**Preparation:** [Read Book Chapter 9](../chapters/09-candidate-physical-architectures-model-based-.md) and identify its assumptions. **After this rehearsal:** return to [Week 9 in the course guide](../../../C/P1/EN645631.md) and follow that rubric independently.

## Situation brief

The Northstar engineering review board is preparing an evidence-limited decision on **candidate physical architectures, model-based trades, and alternative evaluation**. You represent the engineering lead; another participant represents an adversarial reviewer. The board refuses to accept a perfect-looking drawing or a passing unit test without knowing what operational claim it supports. The complication for this week is: A single aggregated score hides uncertainty, non-compensable risks and the reason a stakeholder values one criterion.

### Provided evidence and assumptions

- The shuttle, people, numbers and institutional authorities in this exercise are fictional.
- Base your decision on the worked scenario in [Chapter 9](../chapters/09-candidate-physical-architectures-model-based-.md): Architecture A has high capital expense but low dispatch latency; Architecture B is cheaper but needs more network coverage. If B violates a strict offline-operability requirement, no amount of weighted score should make it admissible. After screening, test whether a ±20% change in latency weight reverses the ranking.
- Anything missing from the packet is **unknown**, not presumed safe or verified. Record any assumptions that you introduce.
- A deliverable should be reproducible from its source, identified scenario and stated decision rule.

## Your assignment

Assess three physical candidates using a constraints screen and weighted score, then perform a decision-weight sensitivity check and create a decision log.

1. **Frame the question.** Write one paragraph identifying the stakeholder, decision authority, system boundary and the claim you intend to support.
2. **Construct the artifact.** Draw or tabulate the relevant model, behavior, software contract, calculation or evidence chain. Use stable identifiers and include an exception case.
3. **Attack it.** Present an alternative explanation, fault, policy or architecture that could reverse your first answer. Explain how your artifact would need to change.
4. **Propose evidence.** Name a test or analysis, acceptance rule, versioned configuration and reviewer who can close the uncertainty.
5. **Decide conditionally.** Write an 8–12 sentence decision memo stating what is accepted, rejected or deferred and why.

## Files to create

Save `week-09-model.md`, `week-09-review.md` and `week-09-evidence.csv` in your learning workspace. The evidence CSV uses `claim_id,artifact_id,configuration,method,result,limitation,status`; the initial file is deliberately blank apart from headers. Keep your own work separate from the reference response.

## Self-assessment (10 points)

| Criterion | Points |
|---|---:|
| Operational claim and model boundary defined | 2 |
| Representation or calculation is logically reproducible | 2 |
| Counterexample, failure and assumptions are addressed | 2 |
| Verification method and evidence limits identified | 2 |
| Decision and action owners are defensible | 2 |

## Reference reasoning — reveal after attempting

The outcome must identify exclusions before ranking and state what new evidence could reverse the preferred feasible design.

A strong solution is not uniquely determined by the supplied data: evaluate whether your assumptions, alternative and proposed evidence are consistent. Unsupported certainty is a lower-quality result than a transparent conditional conclusion. Do **not** submit this example as your independent course project.
