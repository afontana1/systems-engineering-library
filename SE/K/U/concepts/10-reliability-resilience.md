# 10 · Reliability, dependence, resilience, and cascading failures

**Concept dossier · design / simulation / systems of systems / assurance**

## Three questions, three different answers

**Reliability:** does the system perform the required function over a stated time interval under stated conditions? **Availability:** is it operable when needed, considering failures and restoration? **Resilience:** can it absorb disruption, adapt and recover an acceptable function, potentially in a changed state? The three overlap but are not interchangeable.

A system with frequent repairable outages may have high steady-state availability yet be unsuitable for a one-time emergency mission. A service may recover quickly while still disproportionately failing a vulnerable subgroup.

## Simple reliability mathematics and its assumption

If two independent components must both work (a series success structure), `R_system = R_A × R_B`. Two components each with reliability 0.98 over the mission imply system reliability `0.98²=0.9604`. For genuinely independent **parallel** redundancy where either component succeeds, `R_system = 1 − (1−R_A)(1−R_B)`, yielding `1−0.02²=0.9996`.

Those calculations may be wildly optimistic under **common-cause failures**. Two redundant gateways sharing the same power supply or authentication provider are not independent under that failure mode. Correlation, maintenance behavior, software defects and human decisions belong in the system model. Fault-tree “AND/OR” expressions require clear definitions of success, time and dependence.

## Minimal cut sets expose critical dependencies

A minimal cut set is a smallest combination of component failures sufficient for the top event. In a notional service that requires a dispatcher `D` and at least one of two providers `A` or `B`, total failure occurs if `D` fails **or** both A and B fail. Minimal cut sets are `{D}` and `{A,B}`. D is a single point of failure even though providers have redundancy.

The model can be extended to control-plane policy, data trust, identity, charging, human escalation and emergency authority. A network graph alone is insufficient because *who can authorize an action* may matter as much as *who can exchange messages*.

## Resilience as time-varying performance

A resilience profile describes performance before, during and after disruption: time to detect, depth of degradation, recovery rate, sustained minimum service and post-event adaptation. One illustrative metric is integrated mission loss `∫(Q_target−Q(t))_+ dt`, where `Q(t)` is mission quality. A rapid but incomplete recovery might have a smaller integral than a severe prolonged outage; the metric still needs distributional and equity analysis.

Avoid collapsing all resilience into a single number. In emergency access, a 90% network-wide recovery may conceal that isolated communities remain unreached. Disaggregate outcomes by geography, time and affected people.

## A cascading failure scenario

During a heat wave, electricity failures disable chargers. Fewer vehicles remain available, causing increased assignment delays. Users retry requests; retry storms overload dispatch services, which reduces accurate availability information. Operators may manually bypass controls to restore service, introducing authorization risk. This is a coupled technical, behavioral and governance cascade. A credible intervention might include power diversity, controlled retry backoff, degraded-mode dispatch and pre-authorized emergency coordination—tested together.

## Exercises with answers

**A.** Does redundancy always improve system reliability? **Answer:** not necessarily; shared dependencies, switching logic, correlated bugs, maintenance and added interfaces can negate benefits.

**B.** In `D AND (A OR B)` success structure, name failure cut sets. **Answer:** `{D}` and `{A,B}`.

**C.** A network recovers average throughput in one hour; is resilience established? **Answer:** no. Examine critical service minima, impacted subgroups, safety, recovery costs and persistence of degradation.

**Transfer artifact:** dependency graph, fault tree, cut-set list, time-varying mission-quality plot and scenario-dependent recovery options.

## Connections

[Software partial failures](04-software-quality.md) · [Simulation credibility](08-model-credibility.md) · [Enterprise governance](13-sos-enterprise-governance.md).  
**Existing primer:** [Resilience and adaptability](../../encyclopedia/resilience-adaptability.md).
