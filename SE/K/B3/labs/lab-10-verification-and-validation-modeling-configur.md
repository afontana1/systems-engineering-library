# Hypothetical Lab 10 — Verification planning and evidence are different objects

*Book III: Introduction to Model-Based Systems Engineering · Week 10 · Synthetic educational case, not a deployment or safety assessment.*

**Preparation:** [Read Book Chapter 10](../chapters/10-verification-and-validation-modeling-configur.md) and identify its assumptions. **After this rehearsal:** return to [Week 10 in the course guide](../../../C/P1/EN645631.md) and follow that rubric independently.

## Situation brief

The Northstar engineering review board is preparing an evidence-limited decision on **verification and validation modeling, configurations, events, and coverage**. You represent the engineering lead; another participant represents an adversarial reviewer. The board refuses to accept a perfect-looking drawing or a passing unit test without knowing what operational claim it supports. The complication for this week is: Counting test cases is not verification coverage; tests may be obsolete, unexecuted or inapplicable to the released configuration.

### Provided evidence and assumptions

- The shuttle, people, numbers and institutional authorities in this exercise are fictional.
- Base your decision on the worked scenario in [Chapter 10](../chapters/10-verification-and-validation-modeling-configur.md): R-12 requires 3-second acknowledgement. An automated test on simulator build 0.9 has 28 successful trials of 30. Mark the requirement NOT VERIFIED under a strict all-trials acceptance rule; a test result from build 0.9 cannot verify build 1.0 without justified applicability.
- Anything missing from the packet is **unknown**, not presumed safe or verified. Record any assumptions that you introduce.
- A deliverable should be reproducible from its source, identified scenario and stated decision rule.

## Your assignment

Audit five requirements against test definitions, execution logs, configurations and validity windows. Classify each as verified, unresolved, failed or evidence-inapplicable.

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

Strong evidence coverage preserves requirement→method→test→execution→configuration relationships and flags claims that lack acceptable results.

A strong solution is not uniquely determined by the supplied data: evaluate whether your assumptions, alternative and proposed evidence are consistent. Unsupported certainty is a lower-quality result than a transparent conditional conclusion. Do **not** submit this example as your independent course project.
