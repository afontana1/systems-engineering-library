# Hypothetical Lab 5 — Iteration must still produce system evidence

*Book V: Software Systems Engineering · Week 5 · Synthetic educational case, not a deployment or safety assessment.*

**Preparation:** [Read Book Chapter 5](../chapters/05-integrate-agile-product-engineering-with-syst.md) and identify its assumptions. **After this rehearsal:** return to [Week 5 in the course guide](../../../C/P1/EN645764.md) and follow that rubric independently.

## Situation brief

The Northstar engineering review board is preparing an evidence-limited decision on **integrate agile product engineering with systems evidence**. You represent the engineering lead; another participant represents an adversarial reviewer. The board refuses to accept a perfect-looking drawing or a passing unit test without knowing what operational claim it supports. The complication for this week is: Velocity measures delivery throughput, not mission effectiveness or safety confidence.

### Provided evidence and assumptions

- The shuttle, people, numbers and institutional authorities in this exercise are fictional.
- Base your decision on the worked scenario in [Chapter 5](../chapters/05-integrate-agile-product-engineering-with-syst.md): A sprint finishes a booking API but no one has tested duplicate messages or vehicle-offline behavior. The code may be merged but the system capability is not evidence-complete. Add those cases to the acceptance gate and make release readiness depend on configuration-specific results.
- Anything missing from the packet is **unknown**, not presumed safe or verified. Record any assumptions that you introduce.
- A deliverable should be reproducible from its source, identified scenario and stated decision rule.

## Your assignment

Rework two user stories into evidence-linked capabilities with acceptance tests, architecture implications and a bounded release decision.

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

The answer distinguishes implementation completion from qualification and documents what is deferred and why.

A strong solution is not uniquely determined by the supplied data: evaluate whether your assumptions, alternative and proposed evidence are consistent. Unsupported certainty is a lower-quality result than a transparent conditional conclusion. Do **not** submit this example as your independent course project.
