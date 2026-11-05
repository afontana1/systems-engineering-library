# Laboratory 03 · Evidence-quality acceptance review

*Independent practice · Book 8 · System Test and Evaluation · Week 04*

## Learning purpose

This hypothetical laboratory trains the student to apply a method under incomplete evidence and to defend a claim while preserving its assumptions. It is **not** a substitute for the original course's assessed deliverable. First read [the textbook chapter](../chapters/03-testing.html), then attempt the questions before consulting the reference diagnostics.

## Mission brief

A test manager claims that a 60-run demonstration proves failure probability below 1%, and that four paired simulations establish an eight-minute improvement without uncertainty.

## Available reference observations

| Evidence | Starting condition | Comparison or observation | Expected reasoning |
|---|---|---|---|
| Zero failures | 60 successful missions | 95% p upper ≈0.0487 | Recommend further trials or conditional approval |
| Paired test differences | 5, 9, 7, 11 minutes | 95% t interval ≈[3.89,12.11] | Explain effective sample size |


## Required engineering deliverables

1. **Model contract (one page).** State system boundary, intended use, configuration, assumptions, input uncertainty, outcome metrics, and exclusions. Identify who has authority to accept the conclusion.
2. **Independent analysis.** Derive both statistical statements, specify the missing sampling assumptions, identify the correct population and denominators, and write a bounded technical review recommendation. Reproduce relevant calculations using the [source model](../code/graduate_models.py) or the [executable notebook](../notebooks/03-testing.ipynb). Do not use the model output as an unexplained oracle.
3. **Counterexample.** Change at least two assumptions in plausible adverse directions. Document whether the recommended action reverses, becomes infeasible, or loses evidentiary support.
4. **Evidence matrix.** Link each decision claim to the calculation, test or observation that supports it; include the source configuration and remaining defeaters.
5. **Review memo (500–800 words).** State a recommendation, two serious counterarguments, an evidence-closure plan, a conditional release boundary, and a trigger to reconsider the decision.

## Structured procedure

**Step 1 — Reconstruct:** calculate the nominal result by hand, documenting units and rounding. **Step 2 — Verify:** reproduce it from code. **Step 3 — Falsify:** try edge cases, missing observations, changed authority, or an adverse distribution. **Step 4 — Validate:** ask if the mathematical quantity corresponds to the actual operational decision. **Step 5 — Defend:** tell a skeptical review board what it may legitimately conclude and what remains unknown.

## Reference diagnostics (open after attempting)

<details><summary>Show expected reasoning and common failure modes</summary>

Zero failure is not proof of impossibility; four independent replications do not become thousands of independent samples because each contains many requests. The correct answer is a **bounded argument**, not a declaration that the hypothetical transportation system is ready. A defensible memo explicitly identifies the evidence sources, tests that could falsify the claim, the configuration for which it holds, and its remaining uncertainty.

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

**Download:** [Python model](../code/graduate_models.py) · [Tests](../code/test_graduate_models.py) · [Notebook](../notebooks/03-testing.ipynb) · [Data folder](../data/).
