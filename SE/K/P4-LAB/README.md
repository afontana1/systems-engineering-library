# Phase 4 — reproducible teaching laboratory

This common resource accompanies Books 15–17. It contains three tiny **synthetic** datasets, numeric validation functions, an executable `unittest` suite, and three notebooks. Outputs are illustrative, not operational safety claims.

Run locally with Python 3.10+:

```bash
python tools/test_phase4.py
```

The notebooks are self-contained so they also run from the extracted ZIP. The functions model narrowly specified assumptions: stationary Little’s Law, independent-event mission multiplication, and a normal-approximate confidence interval. Read the documented limitations before extrapolating.

- `data/agile-flow.csv`: work-in-process and throughput thought experiment.
- `data/digital-trace.csv`: deliberately stale and failing evidence links.
- `data/process-events.csv`: deliberately questionable approval sequence for process-log audits.
