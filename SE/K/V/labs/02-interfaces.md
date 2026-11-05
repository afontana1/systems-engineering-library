# Laboratory 02 · Adversarial interface contracts

*Independent practice · Book 7 · System Design & Integration · Week 04*

## Learning purpose

This hypothetical laboratory trains the student to apply a method under incomplete evidence and to defend a claim while preserving its assumptions. It is **not** a substitute for the original course's assessed deliverable. First read [the textbook chapter](../chapters/02-interfaces.html), then attempt the questions before consulting the reference diagnostics.

## Mission brief

An integration bench shows acceptable nominal stage timing, but the review board suspects missing composition evidence.

## Available reference observations

| Evidence | Starting condition | Comparison or observation | Expected reasoning |
|---|---|---|---|
| Deterministic total bound | 600 ms deadline | 620 ms bound | Show a 20 ms shortfall |
| Retry under two replicas | Same idempotency key | Double allocation forbidden | Specify atomic persistence and restart test |


## Required engineering deliverables

1. **Model contract (one page).** State system boundary, intended use, configuration, assumptions, input uncertainty, outcome metrics, and exclusions. Identify who has authority to accept the conclusion.
2. **Independent analysis.** Write assumptions and guarantees, create three forbidden transitions, budget the hard latency bounds, and specify fault-injection tests for duplicates, stale route revisions, partition and recovery. Reproduce relevant calculations using the [source model](../code/graduate_models.py) or the [executable notebook](../notebooks/02-interfaces.ipynb). Do not use the model output as an unexplained oracle.
3. **Counterexample.** Change at least two assumptions in plausible adverse directions. Document whether the recommended action reverses, becomes infeasible, or loses evidentiary support.
4. **Evidence matrix.** Link each decision claim to the calculation, test or observation that supports it; include the source configuration and remaining defeaters.
5. **Review memo (500–800 words).** State a recommendation, two serious counterarguments, an evidence-closure plan, a conditional release boundary, and a trigger to reconsider the decision.

## Structured procedure

**Step 1 — Reconstruct:** calculate the nominal result by hand, documenting units and rounding. **Step 2 — Verify:** reproduce it from code. **Step 3 — Falsify:** try edge cases, missing observations, changed authority, or an adverse distribution. **Step 4 — Validate:** ask if the mathematical quantity corresponds to the actual operational decision. **Step 5 — Defend:** tell a skeptical review board what it may legitimately conclude and what remains unknown.

## Reference diagnostics (open after attempting)

<details><summary>Show expected reasoning and common failure modes</summary>

A sum of p99 component times is not the full-system p99; signature validity is not authorization. The correct answer is a **bounded argument**, not a declaration that the hypothetical transportation system is ready. A defensible memo explicitly identifies the evidence sources, tests that could falsify the claim, the configuration for which it holds, and its remaining uncertainty.

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

**Download:** [Python model](../code/graduate_models.py) · [Tests](../code/test_graduate_models.py) · [Notebook](../notebooks/02-interfaces.ipynb) · [Data folder](../data/).
