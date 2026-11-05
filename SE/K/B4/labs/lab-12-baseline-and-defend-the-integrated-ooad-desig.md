# Hypothetical Lab 12 — A defendable design is a consistent set of claims

*Book IV: Object-Oriented Analysis and Design · Week 12 · Synthetic educational case, not a deployment or safety assessment.*

**Preparation:** [Read Book Chapter 12](../chapters/12-baseline-and-defend-the-integrated-ooad-desig.md) and identify its assumptions. **After this rehearsal:** return to [Week 12 in the course guide](../../../C/P1/EN605704.md) and follow that rubric independently.

## Situation brief

The Northstar engineering review board is preparing an evidence-limited decision on **baseline and defend the integrated ooad design**. You represent the engineering lead; another participant represents an adversarial reviewer. The board refuses to accept a perfect-looking drawing or a passing unit test without knowing what operational claim it supports. The complication for this week is: Diagrams may be internally consistent but still solve the wrong problem; revisit actor goals and original constraints.

### Provided evidence and assumptions

- The shuttle, people, numbers and institutional authorities in this exercise are fictional.
- Base your decision on the worked scenario in [Chapter 12](../chapters/12-baseline-and-defend-the-integrated-ooad-desig.md): A stakeholder adds a last-minute request: riders may transfer an active trip to another passenger. This challenges identity, authorization, state transitions, privacy and storage simultaneously. Trace the change through all affected views instead of editing only the use-case title.
- Anything missing from the packet is **unknown**, not presumed safe or verified. Record any assumptions that you introduce.
- A deliverable should be reproducible from its source, identified scenario and stated decision rule.

## Your assignment

Present a ten-minute design defense and a change-impact matrix for trip transfer. Include two alternative solutions and the test evidence each would require.

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

Approval is justified only when obligations agree across views and unresolved risks are explicitly recorded.

A strong solution is not uniquely determined by the supplied data: evaluate whether your assumptions, alternative and proposed evidence are consistent. Unsupported certainty is a lower-quality result than a transparent conditional conclusion. Do **not** submit this example as your independent course project.
