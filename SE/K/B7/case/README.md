# NS-DI7.1 — System Design and Integration

**Fictional engineering case · all figures synthetic.** This controlled *design* baseline matures the NS-CD6.1 preferred hybrid mobility concept. It is not a tested or approved operating system. An analytic requirement pass, structural traceability, and independently executed verification evidence are different claims.

## Inspect and reproduce the artifacts

- [Machine-readable system and decision assumptions](model-baseline.json).
- [Eight requirements and verification methods](requirements.csv), [five functional allocations](allocation.csv), and [five interface contracts](interfaces.csv).
- [Eight baseline-qualified evidence records](evidence-register.csv), including deliberately stale, incomplete, and model-only items.
- [Twelve synthetic measurements from a two-factor experiment](doe-synthetic.csv).
- [Editable architecture diagram](architecture.dot) and [viewable SVG](architecture.svg).
- [Python 3 standard-library reviewer](../tools/step03_book7_design_check.py), which reconstructs the calculations and checks reference consistency.

## Operating envelope and engineering objectives

At an event peak the design must serve **46.2 trips per hour**, a threshold inherited from Book 6's 42 trips/hour plus 10% reserve. The nominal fleet throughput is modeled as **52.8 trips/hour**. The degraded end-to-end command deadline is **500 ms**, with a separate **10% design reserve**, so the model allocation should be **450 ms or less**. The shift energy limit is **30 kWh**. An eight-hour mission is assigned minimum reliability **0.98**, while operational availability must reach **0.99**. The toy safety top-event target is at most **0.005 per demand**. Accessibility offer coverage is at least **95%** across a defined population; evidence on the design baseline must be current.

## Timing and physical architecture

A strictly sequential illustrative chain has nominal stages 65, 85, 110, 100, and 20 ms, totaling **380 ms**. The corresponding degraded estimates are 85, 120, 140, 110, and 35 ms, totaling **490 ms**. A faster gateway is modeled to save 15 ms; parallel dispatch processing, 35 ms. Together, they produce a modeled **440 ms** and **60 ms** reserve. Only the combination meets the 50-ms reserve policy under the declared arithmetic. The summed budgets do **not** establish an end-to-end 99th percentile; correlated waiting and implementation overhead must be investigated.

The synthetic factorial experiment has cell means 488, 472, 451, and 428 ms. The gateway main effect is **-19.5 ms**, dispatcher main effect **-40.5 ms**, and difference-of-differences interaction **-7 ms**. The invented readings are not field measurements. A separate *hypothetical* Gaussian model with mean 428 and standard deviation 20 ms would give approximately **13.57%** probability of exceeding 450 ms, demonstrating why a favorable mean is not a p99 guarantee.

## Reliability, safety and support

With an exponential failure-rate approximation, 0.0015 failures/hour and an eight-hour mission imply \(R(8)=e^{-0.012}\approx0.98807\). An additional shared failure hazard of 0.0012/hour yields \(e^{-0.0216}\approx0.97863\), below the **0.98** target. The constant-rate assumption is illustrative, not a qualified failure model.

A simple 400-hour MTBF and 2.5-hour hands-on MTTR yield inherent availability **0.99379**. Including an assumed three-hour logistics delay drops the operational availability proxy to **0.98644**, below **0.99**. A *separate* toy spare-availability scenario yields expected restoration time \(0.90(2)+0.10(8)=2.6\) hours. Do not add incompatible downtime models together.

With a common-cause brake-safety pathway of probability 0.002 per demand and conditional independent brake/interlock failures of 0.007 and 0.010, the stylized top-event probability is \(0.002+0.998(0.007)(0.010)=0.00206986\). It remains unvalidated because the model's rates and dependence structure have no empirical basis.

For five end-of-year operating periods and 5% discounting, the illustrative lifecycle cost is \(2.8+\sum_{t=1}^5(0.42+0.11)/1.05^t+0.2/1.05^5\approx\$5.2513\) million. The units are USD millions; no inflation, taxes, or salvage value is included.

## Integration and evidence decision

The six-task precedence model has a **nine-week critical path A–C–D–E–F**. The evidence register includes a stale degraded timing record on NS-DI7.0, a planned accessibility test, several model-only calculations and a missing baseline reconciliation. These are deliberately present to teach critical review rather than to represent successful system testing.

**Decision: HOLD operational release.** The combined timing redesign is a reasonable prototype candidate; the assumed mission reliability and logistics-adjusted availability miss requirements, and major evidence remains stale or unexecuted. A conditional continuation of detailed design is not an acceptance or deployment decision.

## Suggested investigations

1. Explain what changes if the five timing stages overlap or share a variable queue; propose an end-to-end percentile study.
2. Quantify the maximum logistics delay compatible with 99% operational availability under the simple renewal model.
3. Use an event tree or fault tree to challenge the assumed common-cause frequency and independence of safety controls.
4. Change a requirement owner or interface timing in a local copy of the CSV, then run the checker to see which structural problems it can and cannot detect.
5. Write a traceable integration review decision distinguishing calculation, observation, requirement status and authority.

## Technical references and limitations

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — design definition, interfaces, verification and validation, and technical reviews.
- [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/) — experimental design, confidence limits and distributional reasoning.
- [NASA Models and Simulations Implementation Guide](https://standards.nasa.gov/standard/nasa/nasa-hdbk-7009) — limitations and credibility of modeled results.

These links are sources for the engineering methods; the numerical scenarios and artifacts are original educational examples. The provided checker validates selected synthetic calculations and referential consistency; it is **not** a SysML parser, a reliability qualification tool, a safety case assessor or an operational deployment authority.
