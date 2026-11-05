# Hypothetical Lab 12 — The capstone is a defense of claims

*Book III: Introduction to Model-Based Systems Engineering · Week 12 · Synthetic educational case, not a deployment or safety assessment.*

**Preparation:** [Read Book Chapter 12](../chapters/12-integrated-model-baseline-capstone-review-ora.md) and identify its assumptions. **After this rehearsal:** return to [Week 12 in the course guide](../../../C/P1/EN645631.md) and follow that rubric independently.

## Situation brief

The Northstar engineering review board is preparing an evidence-limited decision on **integrated model baseline, capstone review, oral defense, and lessons learned**. You represent the engineering lead; another participant represents an adversarial reviewer. The board refuses to accept a perfect-looking drawing or a passing unit test without knowing what operational claim it supports. The complication for this week is: Model trace completeness, model correctness and operational fitness are distinct achievements; the first does not guarantee the others.

### Provided evidence and assumptions

- The shuttle, people, numbers and institutional authorities in this exercise are fictional.
- Base your decision on the worked scenario in [Chapter 12](../chapters/12-integrated-model-baseline-capstone-review-ora.md): The shuttle model claims peak service for 8 requests/hour with 2 vehicles at 3 trips/hour each. The capacity constraint contradicts the mission claim. The correct review action is not to hide the constraint but to identify the gap, bound the operating envelope, and propose a new candidate or an experiment that could change the assumptions.
- Anything missing from the packet is **unknown**, not presumed safe or verified. Record any assumptions that you introduce.
- A deliverable should be reproducible from its source, identified scenario and stated decision rule.

## Your assignment

Prepare a ten-minute design defense with a six-claim evidence matrix, one acknowledged contradiction, and a change scenario posed by a red-team reviewer.

1. **Frame the question.** Write one paragraph identifying the stakeholder, decision authority, system boundary and the claim you intend to support.
2. **Construct the artifact.** Draw or tabulate the relevant model, behavior, software contract, calculation or evidence chain. Use stable identifiers and include an exception case.
3. **Attack it.** Present an alternative explanation, fault, policy or architecture that could reverse your first answer. Explain how your artifact would need to change.
4. **Propose evidence.** Name a test or analysis, acceptance rule, versioned configuration and reviewer who can close the uncertainty.
5. **Decide conditionally.** Write an 8–12 sentence decision memo stating what is accepted, rejected or deferred and why.

## Files to create

Save `week-12-model.md`, `week-12-review.md` and `week-12-evidence.csv` in your learning workspace. The evidence CSV uses `claim_id,artifact_id,configuration,method,result,limitation,status`; the initial file is deliberately blank apart from headers. Keep your own work separate from the reference response.

## Self-assessment (10 points)

| Criterion | Points |
|---|---:|
| Operational claim and model boundary defined | 2 |
| Representation or calculation is logically reproducible | 2 |
| Counterexample, failure and assumptions are addressed | 2 |
| Verification method and evidence limits identified | 2 |
| Decision and action owners are defensible | 2 |

## Reference reasoning — reveal after attempting

The submission passes when it is reproducible, versioned and bounded; a well-argued conditional recommendation is preferable to an unsupported approval.

A strong solution is not uniquely determined by the supplied data: evaluate whether your assumptions, alternative and proposed evidence are consistent. Unsupported certainty is a lower-quality result than a transparent conditional conclusion. Do **not** submit this example as your independent course project.
