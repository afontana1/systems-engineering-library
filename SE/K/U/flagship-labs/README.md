# Flagship laboratory toolkit (v9)

All tools use the Python standard library. They are teaching references, not certification or operational decision software.

Run from this directory:

```bash
python -m pytest -q test_flagships.py
python decision_analysis.py
python reliability_evidence.py
```

Pytest is needed only to run the tests; the modules themselves require no external packages.

The 4 Jupyter notebook files in `../flagship-notebooks/` import these modules; start Jupyter from the notebook directory. Numerical checks do not validate measurement quality, field representativeness, probabilistic assumptions or mission safety.
