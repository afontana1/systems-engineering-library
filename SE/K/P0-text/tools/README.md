# Phase 0 calculation laboratory

Requires only Python 3 (no third-party packages). From this folder run:

```bash
python phase0_calculators.py
python -m unittest discover -s . -v
```

The `phase0_calculators.py` module contains transparent examples for weighted trade scores, a simple cost subtotal/contingency, a resource-unconstrained CPM forward/backward pass, and basic earned-value metrics. The included tests reproduce all numerical examples. Change inputs and inspect assumptions. **These are teaching models:** they omit real-world calendars, stochastic simulation, resource leveling, safety assurance, program-specific accounting rules, and contract requirements. Do not use their raw output as an operational or contractual decision basis.
