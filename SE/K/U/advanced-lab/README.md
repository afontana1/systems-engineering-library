# Northstar Advanced Engineering Laboratory — v12

This is the **second**, more demanding laboratory in the Systems Engineering Knowledge Library. It extends the v11 Northstar prototype with a **tool-neutral model-based architecture**, six scenario variants, fault injection, traceability, a reproducible evidence manifest and a paired Monte Carlo comparison. It does **not** implement SysML syntax or certify a real-world engineering system. All demand and failures are synthetic.

## Starting sequence

- [01 — 01 Model Based Architecture](chapters/01-model-based-architecture.md)
- [02 — 02 State And Interface Contracts](chapters/02-state-and-interface-contracts.md)
- [03 — 03 Discrete Event Experiments](chapters/03-discrete-event-experiments.md)
- [04 — 04 Fault Injection And Resilience](chapters/04-fault-injection-and-resilience.md)
- [05 — 05 Statistical Experiment Design](chapters/05-statistical-experiment-design.md)
- [06 — 06 Verification Traceability](chapters/06-verification-traceability.md)
- [07 — 07 Independent Review](chapters/07-independent-review.md)
- [08 — 08 Capstone Change Challenge](chapters/08-capstone-change-challenge.md)

## Edit, run, study

- The [offline reading website](OPEN-ADVANCED-LAB.html) is a self-contained local copy of the lessons.
- The [architecture model](models/architecture.json) is editable JSON; [Graphviz source](diagrams/architecture.dot) and [SVG](diagrams/architecture.svg) supply visual views.
- [Scenario definitions](data/scenarios.json) and [synthetic request fixture](data/requests.csv) are editable.
- [Requirements](data/requirements-v12.csv), [verification plan](data/verification-plan.csv), [fault register](data/fault-register.csv) and [evidence gates](review/evidence-gates.csv) are the working engineering records.
- Four Jupyter notebooks demonstrate model checking, fault injection, paired simulation and evidence review.

From the **advanced-lab** directory, with Python 3.10+ (standard library only for runner):

```bash
python -m unittest discover -s tests -v
python -m src.run_advanced
```

The runner writes `outputs/scenario-results.json`, `outputs/scenario-summary.csv` and `outputs/provenance.json`. Tests should be rerun after changes. The notebooks can be opened in Jupyter; each sets the lab directory as its working directory. The diagrams can be regenerated with Graphviz `dot -Tsvg diagrams/architecture.dot -o diagrams/architecture.svg`.

## Learning boundary

This code is deliberately small enough to inspect. It has no real vehicles, dispatch APIs, medical or emergency-response functions, security hardening, concurrency control, route model, field calibration, or human safety assurance. Its confidence interval describes **Monte Carlo sampling precision inside the synthetic model**, not an estimate of real-world safety or validity. A local review decision may approve only learning and further model development.

Continue from the [v11 Northstar lab](../integrated-lab/README.md), or return to the [unified encyclopedia](../OPEN-ENCYCLOPEDIA.html).

## Release U2 cross-laboratory evidence exercise

The [U2 cross-lab credibility lab](../lab-credibility-u2/README.md) replays this source without rewriting its baseline data or tests. The U2 sections now teach fault, provenance and authorization checks.
