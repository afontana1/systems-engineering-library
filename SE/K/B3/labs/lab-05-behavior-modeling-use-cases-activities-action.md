# Hypothetical Lab 5 — Behavior is a family of complementary projections

*Book III: Introduction to Model-Based Systems Engineering · Week 5 · Synthetic educational case, not a deployment or safety assessment.*

**Preparation:** [Read Book Chapter 5](../chapters/05-behavior-modeling-use-cases-activities-action.md) and identify its assumptions. **After this rehearsal:** return to [Week 5 in the course guide](../../../C/P1/EN645631.md) and follow that rubric independently.

## Situation brief

The Northstar engineering review board is preparing an evidence-limited decision on **behavior modeling: use cases, activities/actions, interactions, states, and modes**. You represent the engineering lead; another participant represents an adversarial reviewer. The board refuses to accept a perfect-looking drawing or a passing unit test without knowing what operational claim it supports. The complication for this week is: An activity diagram can describe processing order while accidentally allowing impossible state transitions; cross-view consistency must be checked.

### Provided evidence and assumptions

- The shuttle, people, numbers and institutional authorities in this exercise are fictional.
- Base your decision on the worked scenario in [Chapter 5](../chapters/05-behavior-modeling-use-cases-activities-action.md): For a trip request, states are CREATED, ACCEPTED, ASSIGNED, CANCELLED and COMPLETED. ASSIGNED→COMPLETED requires pickup and drop-off evidence; CANCELLED→ASSIGNED is illegal without a new request identity. A sequence diagram of duplicate API messages demonstrates that a repeated ACCEPT event must not create another assignment.
- Anything missing from the packet is **unknown**, not presumed safe or verified. Record any assumptions that you introduce.
- A deliverable should be reproducible from its source, identified scenario and stated decision rule.

## Your assignment

Draft a use case, a five-state transition table and two interaction traces for trip cancellation. Include a guard for “vehicle no longer eligible.”

1. **Frame the question.** Write one paragraph identifying the stakeholder, decision authority, system boundary and the claim you intend to support.
2. **Construct the artifact.** Draw or tabulate the relevant model, behavior, software contract, calculation or evidence chain. Use stable identifiers and include an exception case.
3. **Attack it.** Present an alternative explanation, fault, policy or architecture that could reverse your first answer. Explain how your artifact would need to change.
4. **Propose evidence.** Name a test or analysis, acceptance rule, versioned configuration and reviewer who can close the uncertainty.
5. **Decide conditionally.** Write an 8–12 sentence decision memo stating what is accepted, rejected or deferred and why.

## Files to create

Save `week-05-model.md`, `week-05-review.md` and `week-05-evidence.csv` in your learning workspace. The evidence CSV uses `claim_id,artifact_id,configuration,method,result,limitation,status`; the initial file is deliberately blank apart from headers. Keep your own work separate from the reference response.

## Self-assessment (10 points)

| Criterion | Points |
|---|---:|
| Operational claim and model boundary defined | 2 |
| Representation or calculation is logically reproducible | 2 |
| Counterexample, failure and assumptions are addressed | 2 |
| Verification method and evidence limits identified | 2 |
| Decision and action owners are defensible | 2 |

## Reference reasoning — reveal after attempting

A valid solution identifies invariants and illegal transitions and demonstrates that the interaction trace respects the state machine, including its failure branch.

A strong solution is not uniquely determined by the supplied data: evaluate whether your assumptions, alternative and proposed evidence are consistent. Unsupported certainty is a lower-quality result than a transparent conditional conclusion. Do **not** submit this example as your independent course project.
