# Hypothetical Lab 4 — Relationships need semantics, not merely arrows

*Book III: Introduction to Model-Based Systems Engineering · Week 4 · Synthetic educational case, not a deployment or safety assessment.*

**Preparation:** [Read Book Chapter 4](../chapters/04-requirements-modeling-relationship-semantics-.md) and identify its assumptions. **After this rehearsal:** return to [Week 4 in the course guide](../../../C/P1/EN645631.md) and follow that rubric independently.

## Situation brief

The Northstar engineering review board is preparing an evidence-limited decision on **requirements modeling, relationship semantics, and traceability**. You represent the engineering lead; another participant represents an adversarial reviewer. The board refuses to accept a perfect-looking drawing or a passing unit test without knowing what operational claim it supports. The complication for this week is: A common antipattern is a complete-looking graph with “trace” links everywhere but no semantics, versions or actual evidence.

### Provided evidence and assumptions

- The shuttle, people, numbers and institutional authorities in this exercise are fictional.
- Base your decision on the worked scenario in [Chapter 4](../chapters/04-requirements-modeling-relationship-semantics-.md): R-12 requires assignment acknowledgement within 3 seconds under nominal connectivity. Interface I-ACK constrains the messaging contract, design element SW-DISPATCH claims to satisfy R-12, and test T-12 checks the time across 30 trials. T-12 existing in the model says nothing about whether results pass; add execution E-12 and its observed distribution.
- Anything missing from the packet is **unknown**, not presumed safe or verified. Record any assumptions that you introduce.
- A deliverable should be reproducible from its source, identified scenario and stated decision rule.

## Your assignment

Build a miniature typed graph for R-12 plus accessibility and safety requirements. Deliberately introduce two incorrect relation types and identify them with queries.

1. **Frame the question.** Write one paragraph identifying the stakeholder, decision authority, system boundary and the claim you intend to support.
2. **Construct the artifact.** Draw or tabulate the relevant model, behavior, software contract, calculation or evidence chain. Use stable identifiers and include an exception case.
3. **Attack it.** Present an alternative explanation, fault, policy or architecture that could reverse your first answer. Explain how your artifact would need to change.
4. **Propose evidence.** Name a test or analysis, acceptance rule, versioned configuration and reviewer who can close the uncertainty.
5. **Decide conditionally.** Write an 8–12 sentence decision memo stating what is accepted, rejected or deferred and why.

## Files to create

Save `week-04-model.md`, `week-04-review.md` and `week-04-evidence.csv` in your learning workspace. The evidence CSV uses `claim_id,artifact_id,configuration,method,result,limitation,status`; the initial file is deliberately blank apart from headers. Keep your own work separate from the reference response.

## Self-assessment (10 points)

| Criterion | Points |
|---|---:|
| Operational claim and model boundary defined | 2 |
| Representation or calculation is logically reproducible | 2 |
| Counterexample, failure and assumptions are addressed | 2 |
| Verification method and evidence limits identified | 2 |
| Decision and action owners are defensible | 2 |

## Reference reasoning — reveal after attempting

The answer separates a planned test from executed evidence, checks direction and type of each link, and reports any requirement whose support is merely asserted.

A strong solution is not uniquely determined by the supplied data: evaluate whether your assumptions, alternative and proposed evidence are consistent. Unsupported certainty is a lower-quality result than a transparent conditional conclusion. Do **not** submit this example as your independent course project.


## Extended worked problems and lab

Study the [worked problem workshop on typed model graph queries](../practice/graph.md), then complete the [extended laboratory](../practice/lab-graph.md). The exercises are separate from the original assessed coursework.
