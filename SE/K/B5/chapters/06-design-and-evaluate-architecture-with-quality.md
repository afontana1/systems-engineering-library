# Chapter 6 — Quality attributes must be formulated as scenarios

*Book V: Software Systems Engineering · Week 6 — Design and evaluate architecture with quality attributes*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 6](../labs/lab-06-design-and-evaluate-architecture-with-quality.md) before attempting [the assessed Week 6 coursework](../../../C/P1/EN645764.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-764-w06.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **design and evaluate architecture with quality attributes** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Availability, latency, modifiability, deployability, security and observability compete for limited resources. A quality-attribute scenario identifies source, stimulus, environment, artifact, response and response measure. Architecture tactics are hypotheses to test: redundancy can improve availability while adding common-cause and complexity risks.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Quality attributes become engineering requirements when formulated as measurable scenarios under specific stimuli, loads and operating conditions.

### Distinguishing related ideas

'Fast' or 'secure' is not a design constraint until latency percentiles, threat capabilities, failure conditions or recovery bounds are defined.

### Interpretation and boundary conditions

An architecture can satisfy median latency while violating tail latency during degraded operation, making averages a poor assurance proxy.

## Deeper theory: quality attributes are measurable constraints on architectural behavior

### A quality scenario turns an adjective into a conditional claim

Words such as scalable, resilient, secure, and usable sound like qualities but contain no acceptance boundary by themselves. A quality-attribute scenario identifies the stimulus, source, environment, affected element, expected response, and response measure. “Dispatch shall be fast” provides no testable consequence; “during the declared peak arrival profile, 99 percent of accepted request acknowledgments complete within the allocated duration” at least names a statistical observable. It must still define where latency is measured, how canceled requests count, the observation period, and what percentile-estimation uncertainty is tolerable.

Attributes interact through architecture. Encryption may increase computation and key-management dependencies; caching may reduce response time but create stale authorization state; redundancy may improve availability while increasing operational complexity and common-mode deployment risk. A decision log should describe the tactics employed and the consequences sacrificed. Architecture evaluation is strongest when it exposes *why* a tactic could work in the chosen workload and *where* its assumptions cease to hold.

### Tail performance is not average performance

A service with mean latency of 100 milliseconds can still have a damaging one-percent tail if occasional requests exceed several seconds. For a sequential user transaction, total latency is the sum of stage latencies, but the tail of the sum is not generally the sum of reported stage percentiles. Dependence matters: congestion can make network, queue, and database delays grow together. Similarly, if five independent components each meet a 99-percent availability probability over the same interval, a series service's availability would be approximately `0.99^5 ≈ 0.951`. Independence and matching interval definitions are strong assumptions; shared infrastructure or coordinated maintenance can invalidate this shortcut.

Capacity design requires looking at arrivals, service-time variability, scheduling, retries, and saturation. A utilization target is not equivalent to a latency guarantee. In a simplistic `M/M/1` model, expected time in system is `1/(μ − λ)`, so delay rises nonlinearly as arrival rate `λ` approaches service rate `μ`. Real dispatch architecture may use several server pools, non-Poisson peaks, and priority rules; the elementary formula is a warning about saturation, not a qualification result.

### Evaluation is a portfolio of evidence

Scenario-based reasoning, benchmark measurements, queueing models, architecture tradeoff analysis, and fault injection provide different kinds of evidence. A prototype benchmark measures an implementation under its test workload; it cannot alone validate a capacity claim for a larger deployment. A threat model reveals attack paths; it does not demonstrate that all paths have been eliminated. A quality-attribute decision should therefore record the scenario's intended-use scope, model fidelity, workload provenance, safety margin, and dependencies on other attributes.

In the Northstar example, the architectural question is not whether one service scores better on a generic quality checklist. It is whether passenger-facing timeliness, authorization correctness, recovery after disconnect, and maintainability can jointly meet the mission under credible demand and fault scenarios. Quality attributes are architectural because changing them often changes the allocation of responsibilities and the system's failure boundaries. Their evidence belongs in the same controlled baseline as functional behavior, not in an unrelated performance slide deck.

## Worked Northstar example

A booking API under nominal load must respond within 400 milliseconds at p95, measured at the client edge. Measuring mean database time is not equivalent. A local cache may improve p95 but risks stale capacity unless consistency rules bound its authority.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.

### Quality scenarios are not adjectives

“Fast” is not an architectural requirement. A measurable scenario might say: *under 60 concurrent riders on the nominal production-like deployment, the client-observed booking request reaches an accepted or rejected outcome in at most 400 ms at the 95th percentile over a 30-minute test*. A test reporting mean database query latency does not establish this claim.

To choose a tactic, examine failure and saturation modes. Caching capacity status may lower tail latency but make allocation decisions stale. Replication may raise availability while introducing consistency conflicts. Architecture is a collection of such tradeoffs, evaluated in the specified environments and workloads.

## What can go wrong—and why

Architecture review scores without measured scenarios produce false precision.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 6: Quality attributes must be formulated as scenarios](../labs/lab-06-design-and-evaluate-architecture-with-quality.md), you will: Define three quality scenarios, two tactics per scenario and a test that could reveal a harmful cross-attribute interaction. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 6 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](05-integrate-agile-product-engineering-with-syst.md) and leads toward [next chapter](07-engineer-cloud-service-distributed-and-config.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-764-w06.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.


## Step 03 integrated reference: quality-attribute scenarios with tail-risk calculations

### Specify load, environment and observable

For the peak reservation scenario, the stimulus is ten requests per second; the environment is normal peak operation; the response is an end-to-end acknowledgment; and the measure is 95th-percentile latency below 500 ms for a precisely specified request population. This is more testable than “responsive.” It still needs percentile estimation rules, failure handling, observation boundaries and a measurement duration before operational acceptance.

Use a deliberately simplified M/M/1 queue to expose capacity sensitivity. Let arrivals be Poisson at rate \(\lambda\) and exponentially distributed service capacity at \(\mu\), with \(\lambda<\mu\). In this model the stationary time in system has exponential tail with rate \(\mu-\lambda\), giving

\[t_{0.95}=\frac{-\ln(0.05)}{\mu-\lambda}.\]

With the original 18 requests/s service rate at peak \(\lambda=10\), the 95th-percentile queueing/system time is 374.47 ms. Adding **assumed deterministic** 170 ms for surrounding stages gives 544.47 ms: above the 500 ms threshold. At the candidate rate 20 requests/s, the proxy becomes 299.57 + 170 = **469.57 ms** and satisfies the analytical boundary with only 30.43 ms of modeled margin.

### Why this is not a production percentile

The real server may have multiple workers, non-Poisson arrivals, bursty workloads, correlated network and database delays, priority scheduling, and retries. The analytical distribution does not include those effects. Further, the 95th percentile of a sum is not in general the sum of stage percentiles. Here fixed-stage assumptions make the addition legitimate **within the chosen model**, not in measured operations. Validate with endpoint timestamps, a load generator that preserves realistic arrival patterns, and an uncertainty estimate for the percentile.

### Cross-attribute trade

Increasing capacity can reduce queue delay while introducing new instances, deployment complexity, network dependencies, and monitoring overhead. Record not merely the latency improvement but its effect on availability, security and rollback complexity. A solution is better only relative to the defined weighted and hard constraints, not because one metric improves.

**Exercise.** If \(\mu\) falls to 17/s at the same peak load, recompute the proxy. **Answer.** \(t_{0.95}=2.995732/7\approx427.96\) ms, plus 170 ms = 597.96 ms. That exceeds the limit by almost 98 ms. At near-saturation the same model predicts rapidly increasing delay; it does not justify extrapolating a measurement from low utilization.
