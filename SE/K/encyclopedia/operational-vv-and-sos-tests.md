# Operational V&V across distributed systems of systems

**Reference entry · Deployed systems, constituent autonomy and operational assessment**

## Why constituent qualification is not enough

A system of systems combines constituent systems that may retain separate missions, owners, release cadences and operational authority. Local verification shows conformance to a constituent specification; it does not guarantee interoperability, collective mission outcomes or safe degraded operation. Test plans need **cross-boundary** objectives: message semantics, time alignment, failure propagation, joint command authority, human handoff, independently updated software, and emergent behavior under realistic scenario distributions.

Distinguish three claims. (1) **Verification:** the integrated configuration meets a specified requirement under the procedure. (2) **Validation:** the deployed operation serves the intended stakeholder mission. (3) **Operational evaluation:** evidence about performance, suitability, resilience and sustainment in representative use. These can overlap in test activities but have different decision questions. Failure-free laboratory exercises cannot automatically be generalized to field safety or mission reliability.

## Worked statistical decision bound

Suppose the fictional Campus Mobility fleet must demonstrate a per-mission failure probability below 0.5% with a one-sided 95% confidence method, assuming **independent, identically distributed Bernoulli missions** and exactly defined failure events. With no failures in \(n\) independent trials, the exact one-sided upper bound is

\[
p_U=1-0.05^{1/n}.
\]

For 300 trials, \(p_U\approx0.00994\), about **0.994%**: insufficient for the 0.5% target under this rule. The minimum \(n\) satisfying \(p_U\le0.005\) is

\[
n\ge\frac{\log(0.05)}{\log(0.995)}\approx597.65,
\]

or **598 independent zero-failure trials**. This is an *illustrative statistical calculation*. Correlated missions, changes in weather, repeated operators, shared code or nonrandom scenarios can invalidate the iid interpretation. The bound also does not establish the absence of hazards not exercised by the trial definition.

## Build an operational evidence matrix

For each mission thread record: operational mode; participating constituent versions; network and clock assumptions; stakeholder objective; system-level measure; safety or cybersecurity constraint; procedural test; observed dataset; exclusions; failure-injection scenarios; and accountable approving authority. Include provider loss during a dispatch, delayed hazard alarms, conflict between autonomous local and centralized decisions, restoration after power interruption, and safe fallback. A configuration change in one constituent triggers an *impact assessment* even if the neighboring constituents remain unchanged.

A multi-owner test federation should define time synchronization, data usage rights, fault containment and authority to stop a test. An interface handshake can pass while semantic units are incompatible; test a realistic end-to-end mission with negative and boundary cases. For autonomy, include operator attention, mode confusion, distribution shifts and explicit constraints on learning or policy updates. Report representativeness rather than labeling every test “operational.”

## Practice and checks

A team runs 600 missions with zero observed failures and quotes the formula above. Under iid conditions the bound is \(1-0.05^{1/600}\approx0.00498\), just under 0.5%. Challenge the claim: if the 600 trials repeat the same route, controller version, weather and support crew, what target population can the statistic validly describe? Draft a test matrix row for a stale-data cross-constituent failure and state what evidence would constitute validation rather than merely integration verification.

## Sources and limitations

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — distinction among requirements, verification, validation and lifecycle operations.
- [NIST/SEMATECH Statistical Handbook](https://www.itl.nist.gov/div898/handbook/) — inference and sampling assumptions.

Related: [system-of-systems characteristics](sos-characteristics.md), [V&V](v-and-v.md), [statistical acceptance](statistical-acceptance-and-confidence.md), [configuration control](configuration-assurance-and-change-control.md). This example does not constitute a release or safety assurance decision for a real system.
