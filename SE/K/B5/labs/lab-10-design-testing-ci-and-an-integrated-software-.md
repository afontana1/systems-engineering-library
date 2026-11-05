# Hypothetical Lab 10 — The verification chain includes build identity

*Book V: Software Systems Engineering · Week 10 · Synthetic educational case, not a deployment or safety assessment.*

**Preparation:** [Read Book Chapter 10](../chapters/10-design-testing-ci-and-an-integrated-software-.md) and identify its assumptions. **After this rehearsal:** return to [Week 10 in the course guide](../../../C/P1/EN645764.md) and follow that rubric independently.

## Situation brief

The Northstar engineering review board is preparing an evidence-limited decision on **design testing, ci, and an integrated software v&v evidence chain**. You represent the engineering lead; another participant represents an adversarial reviewer. The board refuses to accept a perfect-looking drawing or a passing unit test without knowing what operational claim it supports. The complication for this week is: A thousand passing tests can leave a critical hazard uncovered if coverage is counted without requirement and scenario semantics.

### Provided evidence and assumptions

- The shuttle, people, numbers and institutional authorities in this exercise are fictional.
- Base your decision on the worked scenario in [Chapter 10](../chapters/10-design-testing-ci-and-an-integrated-software-.md): Run T-ACK for build 1.2 on a simulated network and observe 29 of 30 acknowledgements under three seconds. Whether this passes depends on the approved acceptance rule. The result does not automatically qualify build 1.3 or a deployed network with different latency.
- Anything missing from the packet is **unknown**, not presumed safe or verified. Record any assumptions that you introduce.
- A deliverable should be reproducible from its source, identified scenario and stated decision rule.

## Your assignment

Create a coverage report with five requirements, test cases, results, versions and an explicit rejected “green” release.

1. **Frame the question.** Write one paragraph identifying the stakeholder, decision authority, system boundary and the claim you intend to support.
2. **Construct the artifact.** Draw or tabulate the relevant model, behavior, software contract, calculation or evidence chain. Use stable identifiers and include an exception case.
3. **Attack it.** Present an alternative explanation, fault, policy or architecture that could reverse your first answer. Explain how your artifact would need to change.
4. **Propose evidence.** Name a test or analysis, acceptance rule, versioned configuration and reviewer who can close the uncertainty.
5. **Decide conditionally.** Write an 8–12 sentence decision memo stating what is accepted, rejected or deferred and why.

## Files to create

Save `week-10-model.md`, `week-10-review.md` and `week-10-evidence.csv` in your learning workspace. The evidence CSV uses `claim_id,artifact_id,configuration,method,result,limitation,status`; the initial file is deliberately blank apart from headers. Keep your own work separate from the reference response.

## Self-assessment (10 points)

| Criterion | Points |
|---|---:|
| Operational claim and model boundary defined | 2 |
| Representation or calculation is logically reproducible | 2 |
| Counterexample, failure and assumptions are addressed | 2 |
| Verification method and evidence limits identified | 2 |
| Decision and action owners are defensible | 2 |

## Reference reasoning — reveal after attempting

The outcome differentiates test existence, execution, passing status, applicability and requirement verification.

A strong solution is not uniquely determined by the supplied data: evaluate whether your assumptions, alternative and proposed evidence are consistent. Unsupported certainty is a lower-quality result than a transparent conditional conclusion. Do **not** submit this example as your independent course project.
