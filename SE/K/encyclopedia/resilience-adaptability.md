# Resilience, robustness, and graceful degradation

**Reference entry · Systems of systems, enterprises and complexity · Expanded reference**

## Definition and diagnostic distinction

**Robustness** is the ability to maintain acceptable performance under specified disturbances. **Resilience** emphasizes absorbing disruption, maintaining essential function, recovering, and learning. **Adaptability** concerns changing behavior or structure when conditions evolve beyond the original operating envelope. Redundancy can contribute to robustness but is not synonymous with resilience; duplicate components sharing the same failure cause may collapse together.

## Theory: service loss, recovery, and correlated failure

Define mission service level `Q(t)` on a declared scale, and a minimum acceptable threshold `Q_min`. A simple disruption-loss measure over horizon `[t0,t1]` is `L = ∫(Q_ref(t) - Q(t))_+ dt`, where `(x)_+` denotes the positive part. Lower loss reflects less severe or shorter degradation, but must not replace explicit safety constraints or equity analysis. Recovery time, time to detect, fraction of users affected, and retained minimum capability provide complementary views.

For two redundant independent components with failure probabilities `p1` and `p2` over a specified interval, probability both fail is `p1 p2`; this favorable result depends on independence. With a shared power supply or software defect, the joint failure probability may be much higher. Diversity, isolation, bounded retries, graceful degradation, manual fallback, and rehearsed restoration address different failure mechanisms. Recovery processes themselves need capacity and authority.

## Worked example: choosing between redundancy and fallback

A dispatch system uses two servers with individual monthly failure probability 0.05. An independence assumption yields combined probability `0.05 × 0.05 = 0.0025`. If a common identity service fails with probability 0.03 and disables both servers, overall availability can be dominated by that shared dependency; the naive 0.25% figure is misleading. An independently operated radio dispatch fallback may maintain reduced service during identity outages, but must be exercised with realistic staffing and demand. The correct design choice depends on mission loss during each failure mode, not only server count.

## Engineering use and evidence

Identify critical service thresholds, failure domains, correlated dependencies, repair logistics, recovery authority, and graceful-degradation modes. Run exercises spanning cyber incidents, supplier outages, severe demand, communications loss, and human overload. Measure time to detect, time to restore, unserved demand, and post-recovery data integrity. Include restoration and reconstitution in the architecture—not as an undocumented operational assumption.

## Limitations and connections

A highly redundant system can still be brittle when all alternatives share information or governance. Mean downtime can hide rare catastrophic loss. Connect resilience to **risk and dependence**, **mission engineering**, **interfaces**, **complexity**, and **enterprise capability planning**.

## Technical analysis: compare recoveries by lost service, not only outage duration

Resilience can be quantified against a specified service trajectory. Define normalized mission service `S(t)` with `0≤S(t)≤1`, and over a declared horizon `[0,T]` define total lost service `A_loss = ∫₀ᵀ[1−S(t)]dt` (units of equivalent full-service time). A total outage lasting four hours has `A_loss = 4 hours`. A disruption in which service falls to 50% for six hours has `A_loss = 3 equivalent hours`. On this measure, a longer *partial* disruption may be preferable to a shorter *complete* one; some critical functions may reverse that preference.

If 20% of customers have no accessible fallback, a single aggregate service score can hide unacceptable inequity. Define service by mission-critical customer class and specify hard limits (for instance, maximum time with zero emergency access). Model dependencies among power, communications, personnel, and suppliers: two redundant assets on one shared power feed do not provide independent resilience. Recovery claims should be stress-tested against cascading failures, limited spare capacity, and human coordination delays.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NIST · SP 800-160 Vol. 1 Rev. 1, Engineering Trustworthy Secure Systems (2022)](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) — System-level security and trustworthiness engineering.
- [INCOSE · Systems Engineering Handbook, 5th ed. (2023)](https://www.incose.org/resource/incose-systems-engineering-handbook-a-guide-for-system-life-cycle-processes-and-activities-5th-edition/) — Published practitioner reference; full text may require access.


## Step 02 review exercise: degraded service rather than nominal availability

Consider a fictitious information service with two identical providers. Each independently fails on a demand with probability \(p=0.02\). Under independence, both failing has probability \(p^2=0.0004\), so the modeled success probability is **99.96%**. If a shared power or identity service fails on a demand with probability \(q=0.01\) and always disables both providers, while independent failures apply only when the shared service works, total failure is \(q+(1-q)p^2=0.010396\). The nominal redundant design's success falls to **98.9604%**. The difference comes from the dependency assumption, not from a change in the individual provider failure estimate.

**Resilience** also requires defining *what survives* a disruption, how long degraded function persists, and what constitutes acceptable recovery. An alternate channel may preserve emergency messages but not normal routing. State the service floor, allowed outage duration, restoration priority, manual fallback, reconstitution evidence, and distinct controls for common-cause hazards.

**Exercise (answer).** If q falls to 0.002 while p stays 0.02, shared-plus-independent failure is \(0.002+0.998(0.0004)=0.0023992\), or **0.23992%**. Do not infer recovery-time or mission outcomes from these one-demand probabilities; resilience needs temporal and operational evidence.

## Follow the knowledge

**Related concepts**

- [Risk, issue, uncertainty, and opportunity](risk-vs-issue.md)
- [Probability, dependence, and technical uncertainty](probability-and-dependence.md)
- [Mission threads and capability analysis](mission-engineering.md)
- [Complexity, emergence, and adaptation](complexity-emergence.md)

**Go deeper in the 240-chapter textbooks**

- [Book 18, Chapter 09: Week 09 · System of Systems Engineering · Chapter 09 — Cascading risk, cyber resilience, safety, and mission assurance](../B18/chapters/09.md)
- [Book 7, Chapter 07: Book 7 · Chapter 7: Reliability and maintainability](../B7/chapters/07-design-for-reliability-availability-and-maintainability.md)
- [Book 19, Chapter 09: Week 09 · Enterprise Systems Engineering · Chapter 09 — External factors, strategic scenarios, risk, opportunity, and resilience](../B19/chapters/09.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
