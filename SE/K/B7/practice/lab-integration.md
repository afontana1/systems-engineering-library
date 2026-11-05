# Hypothetical Laboratory · Reliability Allocation, Common Cause, and Integration Evidence

*Book 7 · Week 9 · 90–120 minutes · Independent practice, not the assessed course submission.*

## Engineering brief

Northstar's review board needs a defensible answer about **series reliability · redundancy · common-cause failure · incremental integration**. The program is fictional. Your obligation is to create an auditable model and identify at least one reason the result may not transfer to a real deployed service.

**Assigned reading:** [Advanced workshop](integration.md) (remove spaces in a copied Markdown reference if necessary). Use the original course's Week 9 deliverable as a separate assessment, not as a place to paste these sample answers.

## Reference fixture and code

- [Python program](book7.py) — runnable with Python 3 and no third-party dependencies.
- [CSV input fixture](book7-interfaces.csv) — synthetic and intentionally small.
- [Jupyter notebook](book7.ipynb) — structured worksheet and reproducible calculations.
- [Interactive workbench](WORKBENCH.html) — change values in the offline website, then verify the same result in Python.

## Procedure

1. **Identify the claim.** State the decision to be supported, the owner, the operating boundary, the configuration and the acceptance criterion. Do this before running code.
2. **Reproduce the reference outcome.** Run `python book7.py` or the notebook. Record your Python version, the source revision and the supplied assumptions.
3. **Perturb one assumption.** Use `book7.py` to compare the three-element series path with redundant middle element, both with and without a shared power outage. Write a fault tree with a single-point common-cause cut set. Draft a staged integration sequence with contract tests, simulated dependencies, degradation tests, and end-to-end evidence. Include test IDs and an explicit acceptance limitation.
4. **Inject a counterexample.** Choose an edge case such as a duplicate command, correlated failure, a feasibility breach, stale information, or a requirement change. Predict the outcome before running it.
5. **Write a decision memo.** Separate verified results from model assumptions and unresolved evidence requests. Do not infer real-world readiness from this synthetic case.

## Submission checklist

- One page of clearly defined system boundary, assumptions and requirements.
- One reproduction log with commands or notebook output and environment.
- One model diagram, trade table, state diagram or interface budget as appropriate.
- At least three distinct test cases, including a negative or invalid case.
- One table of results, including at least one sensitivity or uncertainty check.
- One conclusion with limits, technical owner and proposed next evidence.

<details><summary>Reference review guidance — read after attempting</summary>

A strong answer reproduces the supplied calculation and then **names the assumption on which it depends**. The strongest answer also detects that the preferred decision can change under a different scenario or configuration. In the final memo, distinguish what is required, what is predicted, what is observed in the model, and what still needs independent verification.

</details>
