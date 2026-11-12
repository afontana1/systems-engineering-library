# NS-DME16.1 — Digital Mission Evidence and Resilience Laboratory

**Course:** EN.645.782, Foundations of Digital and Mission Engineering, Book 16. This is a **fictional, synthetic, unclassified** instructional case linked to the pre-existing Northstar Resilient Mobility Mission. It is not a validated real-campus, public-safety, military or vehicle decision model.

[Book 16 chapters](../README.html) · [Embedded textbook](../OPEN-BOOK.html) · [Controlled inputs](controlled-inputs.json) · [Executable model](../tools/step03_book16_mission.py) · CLO crosswalk

## Decision and scope

The joint resilience review board must compare fleet investments with continuity policies and decide what evidence would support an eventual public-safety mobility deployment. The engineering use of the case is **course-screening only**. The source course retains its separate graded assignments, mission-architecture rubric and approved architecture/tool choices. Nothing here asserts that JSON dictionaries conform to SysML, that a Python role check enforces enterprise security, or that the scenario model is calibrated.

Book 16 inherits the *themes* of operational queueing from Book 11, physical energy/thermal modeling from Book 12, feedback policies from Book 13, alternative selection from Book 14, and technical-change governance from Book 15. It deliberately **does not reuse their numeric baselines**: those cases have different boundaries, configurations, and assumptions. Only explicitly reconciled, versioned evidence can be combined in a real mission argument.

## Files, provenance, and reproduction

| File | Purpose | Authority / limitations |
|---|---|---|
| [controlled-inputs.json](controlled-inputs.json) | Graph with typed relations, five requirement claims, four disruptions, four policies, and synthetic SOC observation | Fictional source; no operational authority |
| [step03_book16_mission.py](../tools/step03_book16_mission.py) | Pure Python standard-library validator, trace query, impact query, scenario screen, and scalar twin update | Teaching model, not SysML, UAF, enterprise IAM, or physical twin |
| [trace-quality.csv](trace-quality.csv) | Five requirement path checks with explicit nonqualification fields | Structural/configuration completeness only |
| [supplier-impact.json](supplier-impact.json) | Test/requirement/decision impact from interface 1.0→2.0 | Only explicitly modeled dependencies |
| [mission-scenarios.csv](mission-scenarios.csv) | 4 policies × 4 scenarios, per-group served counts and fractions | Capacities not calibrated; mutually exclusive synthetic scenarios |
| [mission-summary.csv](mission-summary.csv) | Joint scenario coverage, expected service fractions, incremental cost | Weights are hypotheses, not frequencies or reliability estimates |
| [model-results.json](model-results.json) | Structured decision summary and bounded SOC update | No deployment authorization |
| [authority-matrix.csv](authority-matrix.csv) | Case information custody, roles, and allowed intended uses | Illustrative policy; actual security requires external controls |
| [evidence-register.csv](evidence-register.csv) | Claim-to-evidence status, falsifiers, and missing qualification evidence | Administrative teaching record |
| [decision-log.csv](decision-log.csv) | Dissent, unresolved gaps, gate and review disposition | No sign-off from an actual review board |

From the repository root (no network and no third-party Python packages required):

```bash
python3 SE/K/B16/tools/step03_book16_mission.py
python3 scripts/check_step03_book16.py
python3 scripts/sync_step03_book16.py
python3 scripts/check_textbook_readers.py
python3 scripts/check_links.py
```

To experiment without overwriting the published CSV/JSON, import `step03_book16_mission` and modify a deep copy of `inputs()` in memory, or run the CLI with `--out /path/to/scratch` for a separate output location. The supplied script intentionally regenerates the published data deterministically, allowing a byte comparison during release.

## Method one — evidence graphs and change impact

A graph node carries an ID, type, revision, owner, sensitivity label, and authority-for-purpose list. Allowed relations include `allocated_to`, `realized_by`, `checked_by`, `produced`, `uses_interface`, `depends_on` and `informs`. Five requirement paths are structurally and configuration current at the **course-screening** baseline: `R-STD`, `R-ACCESS`, `R-CRITICAL`, `R-COMMS`, and `R-ENERGY`. Every row explicitly sets `operationally_qualified = false`.

The controlled Week 8 change to supplier dispatch interface `IF-DISPATCH` revision 2.0 invalidates evidence `E-COMMS` that was witnessed only on 1.0. The executable impact query identifies `T-COMMS`, `E-COMMS`, `R-COMMS`, and `DEC-MISSION-16`. Thus configuration-current screen paths fall **5/5 → 4/5**. This is stale-evidence detection, not evidence of a field failure. Recovery requires a controlled interface comparison, new tests, independently reviewed evidence and a decision update.

A role-check illustration rejects reader access to restricted supplier artifacts. It does not protect these example files from an individual with filesystem access; it is a teaching demonstration of use-specific authority versus access rights.

## Method two — mission policy and common disruptions

There are three service groups: standard (160 daily requests), accessible (28), critical (12). Their productivity assumptions are 14, 10, and 8 trips per assigned vehicle-day, respectively, without resource sharing or queue dynamics. Four scenario categories—normal, grid outage, communications loss, road closure—have synthetic weights 0.62, 0.18, 0.12 and 0.08 (sum one). Each scenario sets group-specific capacity derating. Backup power, offline dispatch and mutual aid add assumed restoration fractions capped at 100% productivity.

For group \(g\), policy \(p\), scenario \(s\), the service fraction is

\[
q_{gps}=\min\left[1,\frac{n_{gp}r_g\min(1,f_{gs}+u_{gps})}{d_g}\right].
\]

A scenario passes only when **all** groups meet the illustrative floors: standard at least 95%, accessible at least 95%, and critical 100%. The joint coverage measure is the weighted sum of passing scenarios, not the product of marginal service rates or the mean of three served fractions.

| Policy | Estimated additional cost | Joint scenario coverage | Screening disposition |
|---|---:|---:|---|
| P0 status quo | $0 | 0.62 | FAIL versus 0.95 |
| P1 vehicles only | $1.50 million | 0.62 | FAIL versus 0.95 |
| P2 continuity | $0.65 million | 0.80 | FAIL versus 0.95 |
| P3 combined | $2.15 million | 0.92 | FAIL versus 0.95 |

**Critical limitation:** This is an enumeration of assumed discrete regimes, not a probability estimate from sampled operations. It has no observations, calibration, parameter uncertainty, route geography, vehicle interactions, differential travel times, shift resources, charging, safety, hazard-model integration, or socio-technical failure interactions. The 0.92 is only an illustrative expected *scenario coverage weight* conditional on the specified hypothetical inputs.

## Method three — bounded state estimate from synthetic telemetry

The SOC demonstration begins with prior 0.68 ± 0.02 (one standard deviation), measurement 0.59 ± 0.03, known illustrative bias −0.04, and age 4 minutes. Bias correction gives observation 0.63; scalar Gaussian gain is 0.307692; posterior SOC is **0.664615** and posterior sigma is approximately **0.016641**. Omitting the assumed known bias gives 0.652308. If the packet is 16 minutes old under a 10-minute age limit, the checker rejects the update and returns no posterior. Real battery twin operation requires a full state-space model, error covariance characterization, validation, handling of sensor fault and missing data, fail-safe controls, cybersecurity and independent review.

## Decision gate and engineering limits

The educational decision is **HOLD FOR OPERATIONAL QUALIFICATION**, even with five original configuration-current paths and the best policy covering 0.92 of the toy scenario weight. The next evidence must include physically witnessed interface and fallback tests; validated demand, service and scenario distributions; hazard analyses; accessible-service trials; telemetry bias assessment; independent security/data-rights review; and configuration approval. The case supports critical study and cross-repository query practice, not procurement or safety certification.
