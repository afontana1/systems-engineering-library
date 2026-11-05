# Hypothetical Laboratory · State Machines, Invariants, and Idempotent Commands

*Book 4 · Week 6 · 90–120 minutes · Independent practice, not the assessed course submission.*

## Engineering brief

Northstar's review board needs a defensible answer about **state transitions · transaction boundaries · exactly-once effects · invariants**. The program is fictional. Your obligation is to create an auditable model and identify at least one reason the result may not transfer to a real deployed service.

**Assigned reading:** [Advanced workshop](state.md) (remove spaces in a copied Markdown reference if necessary). Use the original course's Week 6 deliverable as a separate assessment, not as a place to paste these sample answers.

## Reference fixture and code

- [Python program](book4.py) — runnable with Python 3 and no third-party dependencies.
- [CSV input fixture](book4-requests.csv) — synthetic and intentionally small.
- [Jupyter notebook](book4.ipynb) — structured worksheet and reproducible calculations.
- [Interactive workbench](WORKBENCH.html) — change values in the offline website, then verify the same result in Python.

## Procedure

1. **Identify the claim.** State the decision to be supported, the owner, the operating boundary, the configuration and the acceptance criterion. Do this before running code.
2. **Reproduce the reference outcome.** Run `python book4.py` or the notebook. Record your Python version, the source revision and the supplied assumptions.
3. **Perturb one assumption.** Start with capacity two and a request fixture containing retries and cancellations. Write a transition table, identify all forbidden arcs, then run duplicate keys against `book4.py`. Introduce two conceptual writers reading the same stale version and show why a version check prevents lost updates. Change the key-retention assumption and document which new failure becomes possible. Submit a UML statechart, an invariant table, five negative tests, and a short review disposition.
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
