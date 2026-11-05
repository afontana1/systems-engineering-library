# Executable learning labs

Requires Python 3.10+; no third-party packages.

```bash
cd tools
python -m unittest -v test_phase1.py
python model_graph.py
python trip_domain.py
python reservation_service.py
python performance_budget.py
```

- `model_graph.py`: typed element/link IDs and a conservative impact review *queue*. Its undirected reachability is deliberately overinclusive and requires expert triage.
- `trip_domain.py`: a single-object trip-state machine with invalid event rejection and invariant checks.
- `reservation_service.py`: demonstrates replay idempotency and capacity in **one process only**. It has no database transactions, distributed synchronization, durable store, or security guarantees; do not deploy it.
- `performance_budget.py`: arithmetic for latency margin, Little's Law and simple availability time budget. Do not interpret nominal results as tail guarantees.

Suggested extensions: introduce persistent storage, stale-version rejection, property-based tests, a directed link-semantics policy, and real measurement inputs. All data are invented teaching assumptions.
