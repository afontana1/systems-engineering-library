# Integrated fictional campus shuttle case: from model to decision

**All figures are illustrative and synthetic, not evidence of a real shuttle service.** The integrated case carries a consistent analysis question through six courses: which dispatch strategy and fleet configuration can meet accessible-service expectations at acceptable lifecycle cost under credible uncertainty?

| Evidence element | ID | Responsibility |
|---|---|---|
| Stakeholder service need | NEED-SVC-01 | Accessible and timely trips across approved scenarios |
| Measurable service requirement | REQ-WAIT-01 | Illustrative p95 pickup wait ≤12 minutes in specified conditions |
| Operational scenario | SCN-PEAK-RAIN | Joint peak demand + wet-weather boarding delays |
| Dispatch event model | MOD-DES-02 | Queues, resource assignments, abandonment and service |
| Physical thermal model | MOD-THERM-01 | Charging constraints and temperature-dependent availability |
| Dynamic fleet-capacity model | MOD-SD-01 | Feedback among demand, perceived service and maintenance |
| Statistical measurement | MEAS-P95-WAIT | Clock-defined pickup wait distribution with uncertainty |
| Decision record | DEC-FLEET-03 | Conditional choice with scenario coverage and reversal thresholds |

## What each course adds

1. **Applied MBSE analytics:** controlled semantics, functions, interfaces, traceability and a parametric capacity estimate.
2. **Metrics and statistics:** distributions, sample validity, dependence, experiments, requirement margins and evidence limits.
3. **M&S foundations:** a reproducible discrete-event simulator and independent known-answer checks.
4. **Advanced M&S:** dynamic power/thermal coupling, time synchronization and numerical convergence.
5. **Systems dynamics:** demand and fleet investment feedback over months rather than minutes.
6. **Decision science:** feasible alternatives, Pareto frontier, stakeholder values, robustness and whether another pilot has decision value.

## Deliberate stress case

A baseline simulator predicts 11.4 min p95 pickup wait against a 12 min illustrative limit. Later you discover the training dataset omitted peak rain; charging parameters came from an earlier battery configuration; and the measure excluded accessibility trips. **Do not mark the requirement verified.** Update data and model baselines, rerun scenario and sensitivity analyses, and require appropriately independent test evidence before a qualification claim.

## Suggested capstone dossier

Use the supplied CSV templates for a controlled scenario manifest, parameter register, measurement contracts, model credibility claims, verification fixtures, experiment design, selected alternatives, uncertainties and decision conditions. At every stage preserve the difference between modeled predictions and observed evidence.
