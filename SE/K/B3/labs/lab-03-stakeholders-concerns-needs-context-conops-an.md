# Hypothetical Lab 3 — Stakeholder concern becomes a model view

*Book III: Introduction to Model-Based Systems Engineering · Week 3 · Synthetic educational case, not a deployment or safety assessment.*

**Preparation:** [Read Book Chapter 3](../chapters/03-stakeholders-concerns-needs-context-conops-an.md) and identify its assumptions. **After this rehearsal:** return to [Week 3 in the course guide](../../../C/P1/EN645631.md) and follow that rubric independently.

## Situation brief

The Northstar engineering review board is preparing an evidence-limited decision on **stakeholders, concerns, needs, context, conops, and operational scenarios**. You represent the engineering lead; another participant represents an adversarial reviewer. The board refuses to accept a perfect-looking drawing or a passing unit test without knowing what operational claim it supports. The complication for this week is: An actor omitted from the context may later appear as an “unexpected” interface; an actor shown inside the system by mistake may hide a dependency the engineering team cannot control.

### Provided evidence and assumptions

- The shuttle, people, numbers and institutional authorities in this exercise are fictional.
- Base your decision on the worked scenario in [Chapter 3](../chapters/03-stakeholders-concerns-needs-context-conops-an.md): In a late-night shuttle scenario, a rider requests pickup, dispatch assigns a vehicle, a location service reports a delayed position and an operator intervenes. Map the external actors, information exchanged, operational states and decision authority. The late report belongs in the scenario and may imply an additional requirement for freshness.
- Anything missing from the packet is **unknown**, not presumed safe or verified. Record any assumptions that you introduce.
- A deliverable should be reproducible from its source, identified scenario and stated decision rule.

## Your assignment

Hold a synthetic stakeholder hearing on late-night service. Produce one context model, three scenarios, and a concern-to-view mapping that records two conflicting concerns.

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

A strong answer shows the boundary explicitly, gives each view a named audience and concern, and explains what the model does not claim about operations.

A strong solution is not uniquely determined by the supplied data: evaluate whether your assumptions, alternative and proposed evidence are consistent. Unsupported certainty is a lower-quality result than a transparent conditional conclusion. Do **not** submit this example as your independent course project.
