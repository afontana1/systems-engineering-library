# Phase 3 executable learning toolkit

Standard-library Python 3.10+; no installation or network access required for the `.py` tools.

```bash
cd phase-3-textbook
python tools/phase3_lab.py
python -m unittest discover -s tools -p 'test_*.py'
```

**Algorithms and purposes:** `mean_interval_normal` (large-sample normal approximation; not a small-sample t interval), `factorial_2x2` (effect contrasts), `correlated_sum_mc` (joint-normal uncertainty), `mm1_metrics` (ideal stable queue), `deterministic_queue` and `des_queue` (single-server event logic), `stock_flow` (bounded Euler stock), `euler_cooling` (ODE solver accuracy), `pareto_min` (dominance under all-minimization), `expected_value_and_evpi` (risk-neutral information value), `sample_cost_npv` (discounted simple cash flows), `write_demo_csv` (fabricated experiment fixture).

All methods expose assumptions in docstrings. None of the methods or fabricated inputs validate real operational performance. The notebooks in `notebooks/` require a Jupyter-capable program if you wish to execute them as notebooks; the underlying Python functions work without Jupyter.

The 24 `unittest` cases check basic invariants and known-answer examples. They are software-level checks, *not* empirical model validation.
