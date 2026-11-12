# Simulation verification, validation, and credibility

**Reference entry · Modeling and simulation · Expanded reference**

## Three questions, not one approval stamp

**Model verification** asks whether a model implementation correctly realizes its conceptual specification and governing equations. **Model validation** asks whether the model adequately represents the real system for a specific intended use. **Credibility** is the reasoned confidence that its results are suitable for a particular decision, given the evidence, uncertainties, limitations, and consequences of being wrong.

A simulation can be numerically flawless yet predict badly because demand, human behavior, boundary conditions, or rare failures were modeled incorrectly. A model that performed well for average weekday traffic may be unsuitable for evacuation planning. Credibility is **use-specific and conditional**, not a permanent certification attached to a file.

## Conceptual, implementation, and empirical evidence

A credible modeling argument identifies (1) the decision and required accuracy, (2) relevant physical and organizational mechanisms, (3) conceptual assumptions, (4) software and numerical verification, (5) empirical comparisons, (6) uncertainty, and (7) validation limits. The sequence matters: calibrating parameters cannot repair an omitted feedback loop, and a fine mesh cannot compensate for incorrect boundary conditions.

Verification techniques include unit and dimensional checks, conservation laws, limiting cases, monotonicity, event invariants, code review, and convergence studies. Validation uses comparison with **independent, relevant observations**, expert judgment, cross-model reasoning, and predictive checks on data not consumed by calibration. Agreement with training data is primarily a calibration result, not an independent validation claim.

## Worked example: verification passes, use fails

A campus shuttle discrete-event simulator conserves passenger counts: every generated request is classified as completed, abandoned, or still waiting. Event timestamps are monotone and no vehicle exceeds declared capacity. Those are strong **verification checks**. The model predicts a mean wait of 7 minutes under a Poisson arrival assumption.

An operational holdout dataset from 20 peak days shows a mean wait of 10 minutes, with particularly large spikes after lectures. The difference may result from time-varying burst arrivals, boarding interactions, or dispatch behavior—not a coding mistake. The model should be challenged with arrival-pattern diagnostics and independent holdout scenarios before using it to justify a fleet reduction.

Suppose two alternatives have simulated mean waits of 7.0 and 7.4 minutes. If plausible model discrepancy is ±2 minutes in this regime, declaring the first design decisively better is not justified. The **required credibility is proportional to the decision sensitivity**, not to the visual polish of the simulator.

## Numerical and statistical checks

For continuous models, refine the step size **h** or mesh and compare results; numerical convergence should be consistent with the claimed discretization order in a regime where the method's assumptions hold. Beware stiff dynamics, discontinuities, and unstable coupling between solvers. For discrete-event models, validate event ordering, resource exclusivity, queue discipline, warm-up treatment, and random-stream reproducibility.

Statistical output analysis also needs independent replications or appropriate time-series methods, confidence intervals, and simultaneous comparisons when many designs are screened. Reusing identical random streams across alternatives can improve precision for paired comparisons, but the dependence must be preserved in the analysis.

## Decision-centered credibility review

1. Write the intended-use statement with decision, scenario envelope, performance metric, and tolerable error.
2. Document conceptual mechanisms and exclusions; ask which missing mechanism could reverse the decision.
3. Verify implementation, numerical behavior, and physical or logical invariants.
4. Compare with independent operational evidence representative of the decision scenario.
5. Quantify input, parameter, stochastic, and model-form uncertainty separately where practical.
6. Test ranking stability, boundary scenarios, extrapolation, and alternative assumptions.
7. Preserve versions, input provenance, calibration/validation partition, reviewer dissent, and approved limitations.

## Common failure patterns

*“The simulator matches yesterday's data”* is not enough if yesterday was used to tune it. *“The code passed every unit test”* establishes little about reality. *“We used a high-fidelity physics package”* does not demonstrate that parameters, boundary conditions, or interactions are appropriate. The model is credible only to the degree the evidence warrants for the intended decision.

## Cross-disciplinary connections

This entry connects requirements, statistics, numerical methods, system identification, digital twins, operational test, uncertainty propagation, and model-based assurance. Credibility is a chain from claim through model to independently challengeable evidence.

## Reference shelf retained from the earlier primer

These links are supplied for deeper reading. Confirm current publication versions before relying on them for compliance.

- [NASA-STD-7009B: Standard for Models and Simulations](https://standards.nasa.gov/node/263) — Modeling intended use, V&V, qualification, credibility and limitations.
- [NASA-HDBK-7009B: Models and Simulations Implementation Guide](https://standards.nasa.gov/standard/NASA/NASA-HDBK-7009) — Companion explanatory handbook to the NASA modeling standard.


## Technical analysis: separate the numerical error budget from physical adequacy

Suppose a model predicts a motor winding temperature of `90°C`. A mesh-refinement study yields `90.0°C` on a coarse mesh and `89.2°C` on a fine mesh, while calibrated thermocouple tests under the nominal scenario show `94.0°C`. The mesh difference (`0.8°C`) is a **numerical convergence indicator**, not a direct estimate of the model's physical bias. The observed model–test discrepancy on the finer mesh is `94.0 − 89.2 = 4.8°C`. To interpret that discrepancy, separately estimate sensor uncertainty, test-to-test variation, parameter uncertainty, boundary-condition mismatch, discretization uncertainty, and omitted physics.

For illustration only, if two *independent standard uncertainties* are `u_measure = 1.0°C` and `u_numeric = 0.6°C`, their combined standard uncertainty is `sqrt(1² + 0.6²) ≈ 1.17°C`. This arithmetic does **not** account for structural model error or correlated inputs. A `4.8°C` discrepancy cannot be dismissed merely because a numerical solver converged. Nor can a pass under one ambient temperature establish credibility under a severe hot-soak condition.

A credible-use statement therefore specifies: **decision** (thermal shutdown threshold), **domain** (ambient, duty cycle, manufacturing variants), **quantity of interest** (peak winding temperature), **evidence** (code verification, grid studies, independent physical data), **limitations**, and **decision sensitivity**. NASA-STD-7009B addresses the practices and communication supporting M&S-influenced decisions; compliance with any specific standard is a separate, authority-dependent determination.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · NASA-STD-7009B, Standard for Models and Simulations (2024)](https://standards.nasa.gov/node/263) — Credibility practices for modeling and simulation used in decisions.
- [NASA · NASA-HDBK-7009B, Models and Simulations Implementation Guide (2026)](https://standards.nasa.gov/standard/nasa/nasa-hdbk-7009) — Companion implementation guidance; not a substitute for project-specific requirements.
- [NIST · Technical Note 1297, Reporting Measurement Uncertainty (1993)](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-7-reporting-uncertainty) — Standard and expanded uncertainty, coverage factors, and reporting conditions.

## Phase 3 technical reference: Credibility requires more than numerical agreement

With \(\lambda=9\)/hour and \(\mu=12\)/hour, a synthetically generated M/M/1 queue's long-run mean should be near 20 minutes. Agreement with \(1/(\mu-\lambda)\) helps **verify** the queue implementation under its idealized assumptions; it does not **validate** those assumptions against observed operations. A 40-replication exercise obtains approximately \(20.347\pm0.599\) minutes using a 95% t interval; this describes simulation sampling error only. A credible-use statement must separately assess input distributions, actual arrival dependence, event priorities, instrumentation, held-out operational evidence, consequences of a bad decision, and model-version applicability. See [the analysis, independent comparison and credibility matrix](../methods/simulation-output-and-credibility.md), based on the principles of NASA-STD-7009B and NASA-HDBK-7009B.

## Phase 5 technical reading: Parameter evidence cannot be replaced by more simulation runs

Suppose a fictional service model is calibrated to 90 arrivals observed in 10 hours. The likelihood-rate estimate is 9/hour, but the profile-likelihood interval [7.2664, 10.9896]/hour shows meaningful parameter uncertainty. Running more replication seeds reduces Monte Carlo noise conditional on each input rate; it does not shrink the uncertainty from those finite observations or correct a missing burst mechanism. Rare-event estimators can reduce numerical variance but will not reveal an omitted common cause. The [full calibration, withheld validation, and importance-sampling treatment](../methods/simulation-calibration-and-rare-events.md) separates epistemic assumptions, stochastic variability, numerical error and operational acceptance.



## Step 02 review studio — calibrate on one dataset, challenge on another

Suppose a queue model is adjusted so its predicted mean waiting time matches a calibration sample of 10 minutes. On a held-out scenario the observed mean is 14 minutes while the model predicts 11. The absolute prediction error is 3 minutes, or approximately **21.4% relative to the held-out observed mean**. A near-perfect calibration fit has not demonstrated external predictive credibility for the new operating regime.

**Solved exercise:** should the engineering team recalibrate on the held-out sample and then report it as an independent validation success? **No.** Once used for fitting, it is no longer independent validation data. Preserve data partitions, input provenance, operational context, and a predeclared error tolerance. If the model is used only to rank two scheduling policies, assess whether *ranking accuracy* rather than absolute time prediction is the relevant decision criterion.

**V&V distinction:** code verification asks whether the model was implemented as intended; model validation asks whether the model adequately represents reality for a specified use. Both are narrower than operational authorization.

## Follow the knowledge

**Related concepts**

- [Conceptual modeling and intended use](conceptual-m-and-s.md)
- [Design of experiments and sensitivity](design-of-experiments.md)
- [Probability, distributions, and dependence](probability-and-dependence.md)
- [Verification, validation, and acceptance](v-and-v.md)

**Explore in the 240-chapter textbooks**

- [Book 11, Chapter 9: Book 11 · Chapter 09 — Apply simulation in design and development using selection, ranking, and design of experiments](../B11/chapters/09-apply-simulation-in-design-and-development-using-selection-ranking-a.md)
- [Book 12, Chapter 12: Book 12 · Chapter 12 — Reproduce, challenge, present, and defend the final complex-system simulation study](../B12/chapters/12-reproduce-challenge-present-and-defend-the-final-complex-system-simu.md)
- [Book 16, Chapter 3: Week 03 · Foundations of Digital and Mission Engineering · Book chapter: M&S foundations, lifecycle uses, and credibility](../B16/chapters/03.md)

**Use this reference responsibly:** examples use hypothetical engineering data; the mathematical results rely on the assumptions stated in each passage. Recheck those assumptions for any real project.

