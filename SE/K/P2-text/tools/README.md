# Phase 2 reproducible calculation labs

Use Python 3.10+; all labs use only the standard library. Run `python -m unittest -v test_phase2.py` from this folder. Use `python mission_capacity.py`, `python concept_trade.py`, etc., to inspect sample results. Copy the scripts and edit inputs in a scratch directory; never use them to operate a real system.

| Script | Teaching purpose | Limitation |
|---|---|---|
| `mission_capacity.py` | Simple cycles and capacity | Average-rate scenario, no queues or peak demand |
| `timing_budget.py` | Serial stage sum and margin | No probabilistic tail or concurrency model |
| `concept_trade.py` | Additive weighted value and hard gates | Presumes valid 0–1 preferences and weights |
| `reliability.py` | Series, redundant and shared-cause illustrations | Simplified independence and common-cause assumptions |
| `test_statistics.py` | Zero-failure bound; empirical quantile | Sampling model and representativeness unverified |
| `factorial_experiment.py` | 2×2 effects and interaction | No variance estimation without replicated measurements |

## Suggested experiments

1. Halve the operating window in the capacity model and find which assumptions must change to preserve mission throughput.
2. Add 180 ms security inspection to the nominal timing budget; then argue why the remaining margin is not proof of 99th-percentile compliance.
3. Reweight the trade decision and find the threshold at which the winner flips. Enforce one mandatory eligibility gate.
4. Give the redundant components a shared 0.98 upstream success probability; compare idealized and common-cause estimates.
5. Compute the zero-failure upper 95% bound for `n=100`, `n=1000`, and `n=3000`; explain why correlated tests violate the inference.
6. Compare interaction contrasts for the two factorial datasets given in `deep-dives/experimental-design.md`.

All results are purely educational synthetic examples. To form defensible engineering evidence, specify versioned inputs, sampling plan, instrumentation, configuration, applicable operating domain and independent review.
