# Executable knowledge labs

These labs illustrate the arithmetic and computational assumptions in the 14 new cross-course concept dossiers. They are not validated engineering tools or safety assurance software.

**Requirements:** Python 3.10+ and standard library only for `engineering_labs.py` and tests. Jupyter is required to open the companion `.ipynb` files.

```bash
cd K/U/labs
python -m unittest discover -v
```

Included examples: requirement-to-evidence graph coverage; feasible Pareto screening; two-factor contrast; one-sided zero-failure binomial bound; expected value of perfect information; deterministic longest precedence path; Little's law and M/M/1; forward Euler convergence; independent series and parallel reliability; difference-in-differences arithmetic; seeded M/M/1 simulation.

**Critical limitations:** the numerical examples use synthetic data and simplified assumptions. The binomial bound requires iid common-probability trials; M/M/1 assumes Poisson arrivals, exponential service and a stable single-server queue; reliability calculations assume independence; difference-in-differences arithmetic alone cannot validate parallel trends; coverage links do not establish quality or correctness of evidence. Review these assumptions before interpreting results.
