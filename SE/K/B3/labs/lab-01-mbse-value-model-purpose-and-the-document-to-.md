# Hypothetical Lab 1 — A model has to earn its existence

*Book III: Introduction to Model-Based Systems Engineering · Week 1 · Synthetic educational case, not a deployment or safety assessment.*

**Preparation:** [Read Book Chapter 1](../chapters/01-mbse-value-model-purpose-and-the-document-to-.md) and identify its assumptions. **After this rehearsal:** return to [Week 1 in the course guide](../../../C/P1/EN645631.md) and follow that rubric independently.

## Situation brief

The Northstar engineering review board is preparing an evidence-limited decision on **mbse value, model purpose, and the document-to-model transition**. You represent the engineering lead; another participant represents an adversarial reviewer. The board refuses to accept a perfect-looking drawing or a passing unit test without knowing what operational claim it supports. The complication for this week is: Tool purchase is not an outcome; uncontrolled duplication, misleading completeness and unrecorded assumptions are foreseeable failure modes.

### Provided evidence and assumptions

- The shuttle, people, numbers and institutional authorities in this exercise are fictional.
- Base your decision on the worked scenario in [Chapter 1](../chapters/01-mbse-value-model-purpose-and-the-document-to-.md): Two documents use the term “available vehicle.” One means powered on; the other means dispatched and able to accept new passengers. Importing both as the same model property creates a false agreement. Create VEH-STATE and VEH-ELIGIBILITY as distinct properties, define their derivation and record the discrepancy before accepting the imported source.
- Anything missing from the packet is **unknown**, not presumed safe or verified. Record any assumptions that you introduce.
- A deliverable should be reproducible from its source, identified scenario and stated decision rule.

## Your assignment

Audit six supplied claims about shuttle capacity. Identify which belong as authoritative model elements, source references, calculations or unresolved issues. Produce a model-value hypothesis with a measurable test.

1. **Frame the question.** Write one paragraph identifying the stakeholder, decision authority, system boundary and the claim you intend to support.
2. **Construct the artifact.** Draw or tabulate the relevant model, behavior, software contract, calculation or evidence chain. Use stable identifiers and include an exception case.
3. **Attack it.** Present an alternative explanation, fault, policy or architecture that could reverse your first answer. Explain how your artifact would need to change.
4. **Propose evidence.** Name a test or analysis, acceptance rule, versioned configuration and reviewer who can close the uncertainty.
5. **Decide conditionally.** Write an 8–12 sentence decision memo stating what is accepted, rejected or deferred and why.

## Files to create

Save `week-01-model.md`, `week-01-review.md` and `week-01-evidence.csv` in your learning workspace. The evidence CSV uses `claim_id,artifact_id,configuration,method,result,limitation,status`; the initial file is deliberately blank apart from headers. Keep your own work separate from the reference response.

## Self-assessment (10 points)

| Criterion | Points |
|---|---:|
| Operational claim and model boundary defined | 2 |
| Representation or calculation is logically reproducible | 2 |
| Counterexample, failure and assumptions are addressed | 2 |
| Verification method and evidence limits identified | 2 |
| Decision and action owners are defensible | 2 |

## Reference reasoning — reveal after attempting

An acceptable answer distinguishes model content from generated view, gives every imported claim an owner and status, and names one decision whose evidence improves because of the model.

A strong solution is not uniquely determined by the supplied data: evaluate whether your assumptions, alternative and proposed evidence are consistent. Unsupported certainty is a lower-quality result than a transparent conditional conclusion. Do **not** submit this example as your independent course project.
