# Hypothetical Lab 8 — Parametrics prevent attractive but impossible models

*Book III: Introduction to Model-Based Systems Engineering · Week 8 · Synthetic educational case, not a deployment or safety assessment.*

**Preparation:** [Read Book Chapter 8](../chapters/08-values-units-measures-constraints-parametrics.md) and identify its assumptions. **After this rehearsal:** return to [Week 8 in the course guide](../../../C/P1/EN645631.md) and follow that rubric independently.

## Situation brief

The Northstar engineering review board is preparing an evidence-limited decision on **values, units, measures, constraints, parametrics, and analysis integration**. You represent the engineering lead; another participant represents an adversarial reviewer. The board refuses to accept a perfect-looking drawing or a passing unit test without knowing what operational claim it supports. The complication for this week is: A calculation with precise decimals can still be wrong if demand is peak demand and supply is average capacity, or if trips include multiple passengers.

### Provided evidence and assumptions

- The shuttle, people, numbers and institutional authorities in this exercise are fictional.
- Base your decision on the worked scenario in [Chapter 8](../chapters/08-values-units-measures-constraints-parametrics.md): For 2 vehicles each completing 3 trips/hour, nominal capacity is 6 trips/hour. Demand of 8 trips/hour exceeds that simple capacity, even though neither a requirements nor a structure diagram necessarily shows the contradiction. Represent trips_per_hour with units, compute utilization 8/6 > 1 and mark the configuration infeasible under steady-state assumptions.
- Anything missing from the packet is **unknown**, not presumed safe or verified. Record any assumptions that you introduce.
- A deliverable should be reproducible from its source, identified scenario and stated decision rule.

## Your assignment

Create a constraints table for fleet size, trip rate, request rate and maximum utilization. Inject a unit mismatch and a capacity violation; record whether each is model error or design shortfall.

1. **Frame the question.** Write one paragraph identifying the stakeholder, decision authority, system boundary and the claim you intend to support.
2. **Construct the artifact.** Draw or tabulate the relevant model, behavior, software contract, calculation or evidence chain. Use stable identifiers and include an exception case.
3. **Attack it.** Present an alternative explanation, fault, policy or architecture that could reverse your first answer. Explain how your artifact would need to change.
4. **Propose evidence.** Name a test or analysis, acceptance rule, versioned configuration and reviewer who can close the uncertainty.
5. **Decide conditionally.** Write an 8–12 sentence decision memo stating what is accepted, rejected or deferred and why.

## Files to create

Save `week-08-model.md`, `week-08-review.md` and `week-08-evidence.csv` in your learning workspace. The evidence CSV uses `claim_id,artifact_id,configuration,method,result,limitation,status`; the initial file is deliberately blank apart from headers. Keep your own work separate from the reference response.

## Self-assessment (10 points)

| Criterion | Points |
|---|---:|
| Operational claim and model boundary defined | 2 |
| Representation or calculation is logically reproducible | 2 |
| Counterexample, failure and assumptions are addressed | 2 |
| Verification method and evidence limits identified | 2 |
| Decision and action owners are defensible | 2 |

## Reference reasoning — reveal after attempting

A good result shows dimensions, computations, assumptions and the exact architecture version tested, and it refuses to claim stable service when modeled load exceeds capacity.

A strong solution is not uniquely determined by the supplied data: evaluate whether your assumptions, alternative and proposed evidence are consistent. Unsupported certainty is a lower-quality result than a transparent conditional conclusion. Do **not** submit this example as your independent course project.


## Extended worked problems and lab

Study the [worked problem workshop on energy budget parametrics](../practice/energy.md), then complete the [extended laboratory](../practice/lab-energy.md). The exercises are separate from the original assessed coursework.
