# Hypothetical Lab 2 — Traceability connects implementation to justified choices

*Book V: Software Systems Engineering · Week 2 · Synthetic educational case, not a deployment or safety assessment.*

**Preparation:** [Read Book Chapter 2](../chapters/02-model-software-allocations-interfaces-and-the.md) and identify its assumptions. **After this rehearsal:** return to [Week 2 in the course guide](../../../C/P1/EN645764.md) and follow that rubric independently.

## Situation brief

The Northstar engineering review board is preparing an evidence-limited decision on **model software allocations, interfaces, and the digital thread**. You represent the engineering lead; another participant represents an adversarial reviewer. The board refuses to accept a perfect-looking drawing or a passing unit test without knowing what operational claim it supports. The complication for this week is: Code commit hashes without semantic links to requirements are provenance, not complete traceability.

### Provided evidence and assumptions

- The shuttle, people, numbers and institutional authorities in this exercise are fictional.
- Base your decision on the worked scenario in [Chapter 2](../chapters/02-model-software-allocations-interfaces-and-the.md): Requirement R-12 constrains acknowledgement to three seconds, service API ACK implements the interface, telemetry measurement M-12 logs timings, and verification run E-12 checks the threshold. If the service timeout changes from two to five seconds, an automated impact report should flag both R-12 and E-12 for review.
- Anything missing from the packet is **unknown**, not presumed safe or verified. Record any assumptions that you introduce.
- A deliverable should be reproducible from its source, identified scenario and stated decision rule.

## Your assignment

Build a five-layer digital-thread table and run a change-impact analysis for an interface-timeout change.

1. **Frame the question.** Write one paragraph identifying the stakeholder, decision authority, system boundary and the claim you intend to support.
2. **Construct the artifact.** Draw or tabulate the relevant model, behavior, software contract, calculation or evidence chain. Use stable identifiers and include an exception case.
3. **Attack it.** Present an alternative explanation, fault, policy or architecture that could reverse your first answer. Explain how your artifact would need to change.
4. **Propose evidence.** Name a test or analysis, acceptance rule, versioned configuration and reviewer who can close the uncertainty.
5. **Decide conditionally.** Write an 8–12 sentence decision memo stating what is accepted, rejected or deferred and why.

## Files to create

Save `week-02-model.md`, `week-02-review.md` and `week-02-evidence.csv` in your learning workspace. The evidence CSV uses `claim_id,artifact_id,configuration,method,result,limitation,status`; the initial file is deliberately blank apart from headers. Keep your own work separate from the reference response.

## Self-assessment (10 points)

| Criterion | Points |
|---|---:|
| Operational claim and model boundary defined | 2 |
| Representation or calculation is logically reproducible | 2 |
| Counterexample, failure and assumptions are addressed | 2 |
| Verification method and evidence limits identified | 2 |
| Decision and action owners are defensible | 2 |

## Reference reasoning — reveal after attempting

An acceptable thread carries stable IDs, configuration and evidence date and reports unknown relationships rather than silently treating them as verified.

A strong solution is not uniquely determined by the supplied data: evaluate whether your assumptions, alternative and proposed evidence are consistent. Unsupported certainty is a lower-quality result than a transparent conditional conclusion. Do **not** submit this example as your independent course project.
