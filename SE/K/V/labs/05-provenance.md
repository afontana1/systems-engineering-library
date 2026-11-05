# Laboratory 05 · Digital evidence change-impact audit

*Independent practice · Book 16 · Digital and Mission Engineering · Week 09*

## Learning purpose

This hypothetical laboratory trains the student to apply a method under incomplete evidence and to defend a claim while preserving its assumptions. It is **not** a substitute for the original course's assessed deliverable. First read [the textbook chapter](../chapters/05-provenance.html), then attempt the questions before consulting the reference diagnostics.

## Mission brief

A digital thread dashboard says 100% verification, but the current deployment has a new route authorization revision.

## Available reference observations

| Evidence | Starting condition | Comparison or observation | Expected reasoning |
|---|---|---|---|
| Coverage audit | 10 requirements linked | 3 actionable | Report 100% structural vs 30% actionable |
| Revision change | build-21 → build-22 | New impact obligations | Map affected claims and tests |


## Required engineering deliverables

1. **Model contract (one page).** State system boundary, intended use, configuration, assumptions, input uncertainty, outcome metrics, and exclusions. Identify who has authority to accept the conclusion.
2. **Independent analysis.** Audit ten verification records, distinguish structural from actionable evidence, compute a source digest, and construct a change-impact matrix. Produce a review decision listing claims requiring re-test. Reproduce relevant calculations using the [source model](../code/graduate_models.py) or the [executable notebook](../notebooks/05-provenance.ipynb). Do not use the model output as an unexplained oracle.
3. **Counterexample.** Change at least two assumptions in plausible adverse directions. Document whether the recommended action reverses, becomes infeasible, or loses evidentiary support.
4. **Evidence matrix.** Link each decision claim to the calculation, test or observation that supports it; include the source configuration and remaining defeaters.
5. **Review memo (500–800 words).** State a recommendation, two serious counterarguments, an evidence-closure plan, a conditional release boundary, and a trigger to reconsider the decision.

## Structured procedure

**Step 1 — Reconstruct:** calculate the nominal result by hand, documenting units and rounding. **Step 2 — Verify:** reproduce it from code. **Step 3 — Falsify:** try edge cases, missing observations, changed authority, or an adverse distribution. **Step 4 — Validate:** ask if the mathematical quantity corresponds to the actual operational decision. **Step 5 — Defend:** tell a skeptical review board what it may legitimately conclude and what remains unknown.

## Reference diagnostics (open after attempting)

<details><summary>Show expected reasoning and common failure modes</summary>

A hash is not an authorization or adequacy judgment; a correctly typed trace link is not necessarily credible evidence. The correct answer is a **bounded argument**, not a declaration that the hypothetical transportation system is ready. A defensible memo explicitly identifies the evidence sources, tests that could falsify the claim, the configuration for which it holds, and its remaining uncertainty.

</details>

## Assessment rubric

| Criterion | Points | Evidence of mastery |
|---|---:|---|
| Conceptual model and assumptions | 20 | Relevant abstractions; limits and exclusions explicit |
| Mathematical or formal correctness | 25 | Units, derivations and reproducibility correct |
| Counterexamples and uncertainty | 20 | Two meaningful assumption challenges with consequences |
| Traceability and provenance | 15 | Results tied to evidence and configuration |
| Technical judgment | 20 | Conditional recommendation, counterarguments, closure plan |

**Total: 100 points.** A computationally correct answer with no uncertainty and no evidence limitations cannot receive a high score.

**Download:** [Python model](../code/graduate_models.py) · [Tests](../code/test_graduate_models.py) · [Notebook](../notebooks/05-provenance.ipynb) · [Data folder](../data/).
