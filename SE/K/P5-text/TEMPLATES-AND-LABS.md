# Phase 5 practical learning kit

The `templates/` directory contains **15 editable CSV forms** covering constituent registries, interoperability contracts, evidence lineage, risk cut sets, enterprise outcomes and portfolios, critical-method selection and ethical interventions. `datasets/` contains two invented learning datasets. Columns are starting points: adapt them to the original week's deliverables and maintain version and ownership controls.

## Run the lab

Requires Python 3.10+ and only the standard library.

```bash
python tools/phase5_lab.py
python -m unittest discover -s tools -p 'test_*.py' -v
```

The functions illustrate (1) Bayesian posterior updating; (2) independent series reliability; (3) minimal cut sets of Boolean mission paths; (4) timed data freshness; (5) stock-flow workforce accounting; (6) dependency-constrained portfolio enumeration; (7) disaggregated enterprise metrics; (8) ideal M/M/1 queue time; (9) area under lost-service recovery; and (10) difference-in-differences arithmetic.

**Warnings:** Multiplying probabilities assumes independence. A boolean cut-set model ignores time/capacity. A scalar portfolio 'value' does not establish ethical legitimacy. Difference-in-differences arithmetic does not by itself prove causality. These are small transparent teaching tools, not accredited operational models.
