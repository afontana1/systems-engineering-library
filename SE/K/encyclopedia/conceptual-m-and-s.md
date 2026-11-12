# Conceptual modeling and intended use

**Reference entry · Analytics, modeling, simulation and decisions · Expanded reference**

## Definition and diagnostic distinction

A **conceptual model** specifies what a simulation or analytical representation will include, omit, and assume before software implementation begins. It connects an intended decision to state variables, processes, boundaries, inputs, outputs, data sources, and credibility requirements. It is distinct from executable code and from the real system. A detailed implementation can be faithful to its conceptual model while the conceptual model is unsuitable for the question.

## Theory: abstraction is a decision-dependent choice

Let a system state be `x(t)`, inputs `u(t)`, uncertain parameters `θ`, and outputs `y(t) = h(x(t),u(t),θ)`. The conceptual model selects which components of `x`, `u`, and `θ` are represented and how transitions `dx/dt = f(x,u,θ)` or discrete events are approximated. The abstraction must retain the mechanisms that could reverse the comparison among candidate decisions. A model for mean fleet demand might aggregate requests by hour; a model for emergency response latency must retain subsecond events, queue priorities, and tail distributions.

Model scope should be defended with **conceptual validation**: are boundaries, assumptions, and causal mechanisms adequate for intended use? Verification asks whether the implementation follows its equations and logic. Empirical validation asks whether predictions match relevant observations to a tolerable degree. These activities are related but not interchangeable. Inputs and calibration data must be separated from independent evidence when a strong predictive claim is needed.

## Worked example: averages hide the deciding mechanism

A planning model assumes 120 arrivals per hour and a dispatch capacity of 140 per hour. An average-rate calculation suggests spare capacity of 20 per hour. But if arrivals occur in concentrated ten-minute bursts, queueing delays can be severe even with the same hourly mean. An aggregate fluid model may be useful for staffing cost, yet inadequate for the question “Will 99% of riders wait under ten minutes?” A discrete-event model with individual requests, service-time variability, and priority behavior is needed for that decision.

## Engineering use and evidence

Write a conceptual-model specification stating intended use, operational scope, state variables, units, event logic, stochastic dependencies, interface assumptions, data provenance, validation data, and rejection criteria. Draw a boundary diagram and a causal/functional representation. Review the model with domain experts before coding. Perform sensitivity analysis to determine whether simplified mechanisms materially change the decision.

## Limitations and connections

Adding detail can worsen credibility by multiplying unsupported parameters. A model calibrated to one operating regime may fail after policy or architecture changes. Connect conceptual modeling to **simulation V&V**, **probability and dependence**, **discrete-event simulation**, **stocks and flows**, and **design of experiments**.

## Technical analysis: conceptual models before executable code

A conceptual model should identify the question, entity classes, state variables, events, conservation relationships, decision outputs, exclusions, and assumptions *before* choosing software. It is a specification of what the simulation intends to represent; implementation correctness is a different claim from fidelity to reality.

For a waiting-room model without abandonment, the number of requests currently inside the boundary obeys `N(t) = N(0) + A(t) − D(t)`, with cumulative arrivals `A` and completions `D`. If the model starts empty, accepts **180 requests**, and completes **167**, then **13** must remain in service or waiting. A simulator reporting **11** is internally inconsistent unless two requests were intentionally lost, transferred, or otherwise removed under explicitly modeled rules. This invariant is useful before statistical calibration, because a model that creates or destroys entities cannot support its intended throughput explanation.

**Evidence boundary.** Enumerate excluded phenomena and the domain of operation; sample uncertainty, parameter uncertainty, and structural uncertainty must be reported separately. A clean conservation check is **verification of a declared invariant**, not validation that the real waiting room obeys the assumed stochastic arrival or priority process.

## Claim-specific sources

The following **selected methodological claims** are tied to identifiable sections or abstracts, not merely generic reading lists. Source scope is stated for each link. Numerical scenarios and computations in this article are **original illustrative examples**, not data, calculations, or endorsements supplied by the linked publishers. Links require internet access; the explanation remains readable offline.

- **C1:** The acceptability and credibility of modeling and simulation evidence should be evaluated for its intended application and decision. **Evidence:** [NASA — NASA-STD-7009B, Standard for Models and Simulations (2024), Document Scope; credibility in model/simulation life cycle](https://standards.nasa.gov/node/263) · *direct standard scope*.
- **C2:** Models of system functions and their behavior should be explicitly defined and recorded as technical work products. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §4.3 Logical Decomposition](https://www.nasa.gov/reference/4-0-system-design-processes/) · *direct guidance*.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · NASA-STD-7009B, Standard for Models and Simulations (2024)](https://standards.nasa.gov/node/263) — Credibility practices for modeling and simulation used in decisions.
- [NASA · NASA-HDBK-7009B, Models and Simulations Implementation Guide (2026)](https://standards.nasa.gov/standard/nasa/nasa-hdbk-7009) — Companion implementation guidance; not a substitute for project-specific requirements.



## Step 02 review studio — model credibility depends on intended use

A queueing simulation may credibly estimate **relative waiting time** under two schedules without being credible for predicting **safety-critical emergency-response latency**. Credibility is claim-specific: define the intended decision, domain, outputs, input evidence, validation comparators, and consequences of model error before selecting model fidelity.

**Solved exercise:** a simple M/M/1 model uses arrival rate 6 jobs/h and service rate 10 jobs/h. Under Poisson arrival, exponential service, single-server, infinite-buffer and stability assumptions, mean time in system is

\[
W=\frac{1}{\mu-\lambda}=\frac{1}{10-6}\;\mathrm{h}=0.25\;\mathrm{h}=15\;\mathrm{min}.
\]

If arrival rate approaches service capacity, the analytic mean grows without bound. The 15-minute result is therefore **not** a general shuttle waiting-time forecast. Verify the simulation against an analytical benchmark where valid, then validate the arrival/service distributions and operating scenarios with data appropriate to the stated decision.

**Credibility boundary:** a correct implementation can model the wrong system. Record conceptual assumptions and excluded mechanisms; test sensitivity to them rather than equating a narrow code pass with external validity.

## Follow the knowledge

**Related concepts**

- [Discrete-event simulation and queues](discrete-event-simulation.md)
- [Stocks, flows, and feedback loops](stocks-flows-feedback.md)
- [Simulation verification, validation, and credibility](model-vv-and-credibility.md)
- [Design of experiments and sensitivity](design-of-experiments.md)

**Go deeper in the 240-chapter textbooks**

- [Book 11, Chapter 02: Book 11 · Chapter 02 — Develop the M&S plan and conceptual model before implementation](../B11/chapters/02-develop-the-m-s-plan-and-conceptual-model-before-implementation.md)
- [Book 11, Chapter 11: Book 11 · Chapter 11 — Plan and evaluate verification, validation, credibility, and accreditation for intended use](../B11/chapters/11-plan-and-evaluate-verification-validation-credibility-and-accreditat.md)
- [Book 12, Chapter 01: Book 12 · Chapter 01 — Frame the advanced M&S decision, intended use, architecture, and credibility strategy](../B12/chapters/01-frame-the-advanced-m-s-decision-intended-use-architecture-and-credib.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
