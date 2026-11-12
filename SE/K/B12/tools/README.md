# Calculation toolkit

`phase3_calculations.py` contains deterministic teaching calculations and self-tests. Run `python phase3_calculations.py` with Python 3.10+. No external packages are needed.

## NS-CPS12.1 integrated vehicle simulator

[Reproducible coupled-model source](step03_book12_coupled_vehicle.py) implements the Book 12 synthetic longitudinal-force, battery-energy, and lumped thermal teaching case. It uses the [controlled versioned inputs](../case/model-inputs.json) to regenerate [five-scenario paired experiment data](../case/experiment-results.csv) and a [summary](../case/summary.json):

```bash
python SE/K/B12/tools/step03_book12_coupled_vehicle.py --write
python scripts/check_step03_book12.py
```

Run from the repository root. Inputs and outputs are fictional; the code is **not** an FMI FMU, HLA federation, calibrated battery or pack thermal model, 10 ms controller, or HIL simulator. Read the [case credibility record](../case/INDEX.html) before using the results.
