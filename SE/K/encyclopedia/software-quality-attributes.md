# Software quality attributes and architectural tactics

**Reference entry · MBSE and software-intensive systems · Expanded reference**

## Definition and diagnostic distinction

**Software quality attributes** describe observable behavior under conditions that matter: performance, availability, security, modifiability, usability, safety contribution, recoverability, and others. “The system shall be scalable” is not a testable quality requirement. A usable **quality-attribute scenario** names a stimulus, source, environment, affected artifact, expected response, and response measure. Architectural tactics are decisions intended to influence the scenario; they create tradeoffs and new failure modes.

## Theory: performance and dependability are coupled

At equilibrium, Little's law gives `L = λW` for a stable system, where `L` is average work in process, `λ` is throughput, and `W` is mean time in the system. It does not imply that every request has mean latency, nor does it hold across arbitrary unstable transient windows. As utilization approaches capacity, queueing delay becomes extremely sensitive to service-time variability. Redundancy can improve availability against independent faults, but replicas sharing power, identity services, or update pipelines may fail together.

Security controls also consume latency and operational budgets. An authentication step adds service time; aggressive retries amplify load during outages; encryption and auditing may be necessary despite their performance cost. Quality is a constrained architecture problem: choose a design satisfying non-negotiable safety and security bounds, then optimize remaining objectives. A high average throughput cannot compensate for unsafe worst-case reaction time.

## Worked example: a tail-latency surprise

Suppose a dispatch API averages 60 ms processing, and 99% of requests respond within 180 ms under a 40-request/s test load. Peak demand raises arrival rate near available capacity, producing a 99th-percentile latency of 850 ms while the mean remains 95 ms. If an operational acknowledgement must occur within 250 ms at the 99th percentile, the service fails its quality scenario despite an impressive mean. Caching may reduce reads but risks stale vehicle availability; adding replicas may help throughput but requires consistent reservation semantics.

## Engineering use and evidence

Record measurable scenarios for normal, peak, degraded, and attack conditions. For each candidate tactic, document which attribute it improves and which attribute it may worsen. Test end-to-end behavior with realistic dependency latency, workload mixtures, timeouts, failure injection, and representative user devices. Preserve build identity and configuration because performance and security evidence are version-specific.

## Limitations and connections

Benchmark results are conditional on workload, hardware, caching state, and measurement instrumentation. “Five nines” availability cannot be inferred from a short clean test. Connect quality attributes to **requirements**, **object responsibilities**, **flow and queues**, **software lifecycle evidence**, and **resilience**.

## Technical analysis: performance distributions and quality conflicts

Software quality attributes are system-level tradeoffs: throughput, latency, safety, security, modifiability, availability, and observability interact through shared resources. A mean response time is not sufficient evidence for tail-sensitive services, and a cryptographic or auditing control may improve trustworthiness while increasing capacity demand. State the workload, population, environment, and measurement percentile.

Suppose **95%** of requests complete in **100 ms** and the remaining **5%** in **2,100 ms**. Mean latency is `0.95(100)+0.05(2100)=200 ms`, but the **95th percentile is 100 ms** under a nearest-rank definition and the **99th percentile is 2,100 ms**. A requirement on 99th-percentile delay therefore cannot be inferred from the apparently acceptable 200-ms mean. Changing the population (e.g., excluding timeouts) may change these statistics more than a code optimization does.

**Evidence boundary.** Specify service-level objectives and qualifying loads, monitor resource contention, and analyze the quality-attribute scenario that triggers design tradeoffs. Performance tests with security logging disabled cannot verify the production architecture; conversely, a single worst-case trace does not estimate a tail percentile.

## Claim-specific sources

The following **selected methodological claims** are tied to identifiable sections or abstracts, not merely generic reading lists. Source scope is stated for each link. Numerical scenarios and computations in this article are **original illustrative examples**, not data, calculations, or endorsements supplied by the linked publishers. Links require internet access; the explanation remains readable offline.

- **C1:** Security and trustworthiness should be engineered as system-wide concerns rather than treated solely as coding properties. **Evidence:** [NIST — SP 800-160 Vol. 1 Rev. 1, Engineering Trustworthy Secure Systems (2022), System security engineering concepts, activities, tasks, and trustworthiness principles](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) · *direct guidance*.
- **C2:** Technical requirements should express measurable performance constraints in the operating context. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §4.2 Technical Requirements Definition](https://www.nasa.gov/reference/4-2-technical-requirements-definition/) · *direct guidance*.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NIST · SP 800-160 Vol. 1 Rev. 1, Engineering Trustworthy Secure Systems (2022)](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) — System-level security and trustworthiness engineering.
- [INCOSE · Systems Engineering Handbook, 5th ed. (2023)](https://www.incose.org/resource/incose-systems-engineering-handbook-a-guide-for-system-life-cycle-processes-and-activities-5th-edition/) — Published practitioner reference; full text may require access.

## Follow the knowledge

**Related concepts**

- [Flow, work in process, and bottlenecks](flow-wip-and-queues.md)
- [Object-oriented domain models and responsibilities](object-responsibilities.md)
- [CI/CD, configuration, and software assurance](software-lifecycle-evidence.md)
- [Resilience, robustness, and graceful degradation](resilience-adaptability.md)

**Go deeper in the 240-chapter textbooks**

- [Book 5, Chapter 06: Book V · Chapter 6: Quality attributes must be formulated as scenarios](../B5/chapters/06-design-and-evaluate-architecture-with-quality.md)
- [Book 5, Chapter 08: Book V · Chapter 8: Performance and security share resource budgets](../B5/chapters/08-specify-and-analyze-performance-networking-re.md)
- [Book 5, Chapter 09: Book V · Chapter 9: Dependability is a claim supported by argument and evidence](../B5/chapters/09-build-the-dependability-safety-resilience-and.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
