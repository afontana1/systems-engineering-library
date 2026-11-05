# Hypothetical Lab 3 — Use cases describe externally valuable behavior

*Book IV: Object-Oriented Analysis and Design · Week 3 · Synthetic educational case, not a deployment or safety assessment.*

**Preparation:** [Read Book Chapter 3](../chapters/03-capture-functional-requirements-with-use-case.md) and identify its assumptions. **After this rehearsal:** return to [Week 3 in the course guide](../../../C/P1/EN605704.md) and follow that rubric independently.

## Situation brief

The Northstar engineering review board is preparing an evidence-limited decision on **capture functional requirements with use cases and scenarios**. You represent the engineering lead; another participant represents an adversarial reviewer. The board refuses to accept a perfect-looking drawing or a passing unit test without knowing what operational claim it supports. The complication for this week is: A use-case model without alternate flows gives designers no contract for recoverable failure.

### Provided evidence and assumptions

- The shuttle, people, numbers and institutional authorities in this exercise are fictional.
- Base your decision on the worked scenario in [Chapter 3](../chapters/03-capture-functional-requirements-with-use-case.md): BookTrip begins with an authenticated rider and an available service window; success creates exactly one confirmed reservation. If no capacity exists, the system returns an explicit refusal and leaves no partial allocation. If an answer is lost, retry must not create a second reservation.
- Anything missing from the packet is **unknown**, not presumed safe or verified. Record any assumptions that you introduce.
- A deliverable should be reproducible from its source, identified scenario and stated decision rule.

## Your assignment

Write a fully dressed BookTrip use case with three alternate paths and one idempotency invariant. Trace steps to domain objects and obligations.

1. **Frame the question.** Write one paragraph identifying the stakeholder, decision authority, system boundary and the claim you intend to support.
2. **Construct the artifact.** Draw or tabulate the relevant model, behavior, software contract, calculation or evidence chain. Use stable identifiers and include an exception case.
3. **Attack it.** Present an alternative explanation, fault, policy or architecture that could reverse your first answer. Explain how your artifact would need to change.
4. **Propose evidence.** Name a test or analysis, acceptance rule, versioned configuration and reviewer who can close the uncertainty.
5. **Decide conditionally.** Write an 8–12 sentence decision memo stating what is accepted, rejected or deferred and why.

## Files to create

Save `week-03-model.md`, `week-03-review.md` and `week-03-evidence.csv` in your learning workspace. The evidence CSV uses `claim_id,artifact_id,configuration,method,result,limitation,status`; the initial file is deliberately blank apart from headers. Keep your own work separate from the reference response.

## Self-assessment (10 points)

| Criterion | Points |
|---|---:|
| Operational claim and model boundary defined | 2 |
| Representation or calculation is logically reproducible | 2 |
| Counterexample, failure and assumptions are addressed | 2 |
| Verification method and evidence limits identified | 2 |
| Decision and action owners are defensible | 2 |

## Reference reasoning — reveal after attempting

The complete use case explains who starts the interaction, the success guarantee, and what remains true when every alternative fails.

A strong solution is not uniquely determined by the supplied data: evaluate whether your assumptions, alternative and proposed evidence are consistent. Unsupported certainty is a lower-quality result than a transparent conditional conclusion. Do **not** submit this example as your independent course project.
