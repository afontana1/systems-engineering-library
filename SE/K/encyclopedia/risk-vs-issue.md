# Risk, issue, uncertainty, and opportunity

**Reference entry · Foundations and management · Expanded reference**

## Definition and diagnostic distinction

A **risk** concerns an uncertain future event or condition that could affect objectives; an **issue** is a present, observed condition requiring action. **Uncertainty** is broader than risk: it includes measurement error, unknown model structure, ambiguity about objectives, and favorable outcomes. An **opportunity** is an uncertain possibility of improving results. Mixing these categories obscures whether to investigate, mitigate, recover, exploit, or make a decision now.

## Theory: probability, consequence, exposure, and information

A basic risk representation is `R = (event, probability, conditional consequence, exposure window, owner, response)`. Expected loss `E[L] = sum_j P(event_j) L_j` can compare options when consequences are commensurable and probabilities credible; it is not a universal safety decision rule. Tail severity, irreversibility, interdependence, and ethical constraints can make a low expected loss unacceptable. Multiplying ordinal 1–5 likelihood and impact scores produces a ranking convention, not a physically calibrated expected loss.

Separate **aleatory** variability (demand, component lifetime) from **epistemic** uncertainty (unknown failure mechanism, poorly supported parameter). More testing may reduce epistemic uncertainty while leaving intrinsic randomness. Dependencies matter: a common power supply can correlate otherwise independent subsystem outages. Responses include avoiding exposure, reducing probability, reducing consequence, transferring financial burden, or explicitly accepting residual risk by an accountable authority.

## Worked example: risk becomes issue

A dispatch server has an estimated 8% probability of a one-hour outage during the trial month, with an illustrative `$50,000` mission-equivalent disruption cost. Expected loss is `$4,000`, but a single outage during an emergency drill may carry a nonfinancial safety consequence that cannot be justified by the average alone. A backup channel might lower modeled probability to 2% at a cost of `$1,500`, yielding an expected financial benefit of `$3,000` under the stated assumptions. If a real outage occurs on Tuesday, it is now an issue requiring restoration and incident analysis; the remaining outage probability is a separate forward risk.

## Engineering use and evidence

Maintain a risk register with cause–event–effect wording, triggers, quantitative assumptions, consequence dimensions, mitigation tests, residual exposure, and named decision authority. Maintain issues with observed symptoms, impact, containment, root-cause hypotheses, and restoration criteria. Track opportunities with the same analytical discipline. Reassess assumptions after design changes, supplier updates, incidents, and new evidence; the best risk response may be to buy information before locking in architecture.

## Limitations and connections

Risk rankings are sensitive to scoring scales, omitted dependencies, and whose losses count. Never use a heat map as proof that a hazardous condition is safe. Connect risk to **probability and dependence**, **model credibility**, **technical baselines**, **resilience**, and **value of information**.

## Technical analysis: residual exposure is conditional, not erased

A risk register should describe a **possible future event** and its consequences; an issue tracks an event already occurring. Expected loss `E[L] = Σ_i p_i L_i` is useful for quantifiable, comparable outcomes, but it is not a license to trade away mandatory safety, legality, or human rights constraints. Explicitly distinguish aleatory variation from lack of knowledge and model shared causes when assigning event probabilities.

A proposed mitigation costs **$4,000**. Without it, an outage has assumed probability **0.10** and produces a **$100,000** cost: expected loss **$10,000**. With the mitigation, probability falls to **0.03**, leaving expected loss **$3,000**. Under a purely financial risk-neutral model the expected avoided loss is **$7,000** and the net expected gain is **$3,000**. This is only as reliable as the estimated probabilities, effectiveness, time horizon, and consequence model; unmodeled common outages may erase the apparent benefit.

**Evidence boundary.** Test mitigation mechanisms, track triggering signals and residual risks, and assign acceptance authority. After the outage occurs, log an issue and restoration actions; it remains necessary to model future recurrence risk separately.

## Claim-specific sources

The following **selected methodological claims** are tied to identifiable sections or abstracts, not merely generic reading lists. Source scope is stated for each link. Numerical scenarios and computations in this article are **original illustrative examples**, not data, calculations, or endorsements supplied by the linked publishers. Links require internet access; the explanation remains readable offline.

- **C1:** Technical risk management treats potential future performance shortfalls and response plans within technical, cost and schedule domains. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §6.4 Technical Risk Management](https://www.nasa.gov/reference/6-4-technical-risk-management/) · *direct guidance*.
- **C2:** Risk governance and monitoring belong across the system life cycle. **Evidence:** [NIST — SP 800-37 Rev. 2, Risk Management Framework (2018), Risk governance and continuous monitoring lifecycle](https://csrc.nist.gov/pubs/sp/800/37/r2/final) · *direct guidance*.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NIST · SP 800-37 Rev. 2, Risk Management Framework (2018)](https://csrc.nist.gov/pubs/sp/800/37/r2/final) — Risk governance and continuous monitoring in the system life cycle.
- [NASA · Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2 (2016/2017)](https://www.nasa.gov/reference/systems-engineering-handbook/) — Lifecycle engineering, technical management, requirements, verification and validation.

## Follow the knowledge

**Related concepts**

- [Probability, dependence, and technical uncertainty](probability-and-dependence.md)
- [Decision uncertainty and value of information](bayesian-value-of-information.md)
- [Work breakdown structures and technical baselines](wbs-and-baselines.md)
- [Resilience, robustness, and graceful degradation](resilience-adaptability.md)

**Go deeper in the 240-chapter textbooks**

- [Book 2, Chapter 08: Chapter 8 · Risk, Change, and Configuration Are Coupled](../B2/chapters/08-risk-change-and-quality.md)
- [Book 10, Chapter 09: Book 10 · Chapter 09 — Propagate uncertainty with analytic Monte Carlo simulation and sensitivity analysis](../B10/chapters/09-propagate-uncertainty-with-analytic-monte-carlo-simulation-and-sensi.md)
- [Book 7, Chapter 08: Book 7 · Chapter 8: Humans, safety and security](../B7/chapters/08-design-for-human-performance-safety-security-usability-.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
