# Problem framing and baseline audit

**Reference entry · Systems definition, stakeholder evidence, and design maturation**

## What must be true before a proposed solution is credible?

Problem framing separates an **observed condition**, an **unmet stakeholder need**, a **testable causal hypothesis**, and a **preferred intervention**. These are different claims. A problem statement such as “the fleet needs more vehicles” already assumes a solution; “95th-percentile passenger wait exceeds the agreed service threshold during weekday peak periods” is a measurable condition whose causes still need investigation. An incumbent-system baseline is a dated, configuration-controlled description of performance, interfaces, operating modes, hazards, costs, and known evidence gaps. It is not an uncritical list of current specifications.

Start with the system-of-interest boundary and its enabling services. In a Campus Mobility example, dispatch software, vehicles, communication links, pickup infrastructure, staff and maintenance are possible parts of the operating system. Weather, the campus population, roadway rules and external network providers may be environmental or interacting systems. Explicitly record who owns each boundary decision and whose experience is absent.

## From testimony to evidence

Create an evidence register with fields `claim_id`, `source`, `time_window`, `configuration`, `measurement_definition`, `sample_frame`, `uncertainty`, `known_bias`, and `status`. Different kinds of evidence answer different questions. Interviews reveal goals, failure modes and blind spots but do not estimate failure probability on their own. Logs provide empirical frequencies only if event definitions, missing records and sampling are understood. Requirements specify intended performance; they are not proof of actual capability.

### Worked baseline audit: late dispatches

In a hypothetical month, a dispatch ledger contains 180 requests, of which 45 exceeded a defined response deadline. The observed late fraction is

\[
\hat p=45/180=0.25.
\]

An operator attributes 18 late requests to stale vehicle-availability data, 12 to dispatch conflicts, and 15 to other or unclassified causes. These are **classifications**, not yet causal findings. The conditional fraction labeled stale data among the 45 late events is \(18/45=0.40\), not 40% of all requests. If only 160 of the 180 requests had reliable timestamps, a 25% claim for the whole population needs a missing-data sensitivity analysis, not a more precise decimal.

A candidate intervention is a freshness alarm. Its testable hypothesis: “when availability messages are more than two seconds old, the dispatch service inhibits allocation and requests an updated state; this reduces stale-data misallocations without unacceptably increasing wait.” Evaluate *both* negative consequences and benefits; alarm-driven cancellations can increase delay while reducing unsafe allocations.

## Convert an audit into engineering decisions

Use a structured chain: observation → source and uncertainty → problem hypothesis → stakeholder outcome → measure of effectiveness → candidate requirement → responsible architecture element → discriminating experiment → decision record. A requirement might say “the allocation decision shall not use an availability record older than 2.0 seconds, measured at the allocator clock” with explicit clock synchrony assumptions. It does **not** establish that two seconds is safe; that threshold must come from hazard and performance evidence.

Before accepting a successor design, check configuration continuity: which interfaces, calibration versions, datasets, policies and operational scenarios transfer? Mark unknowns “open” rather than treating missing evidence as favorable evidence. Record reversible and irreversible decisions separately. A changed controller baseline may invalidate earlier acceptance tests even if the requirements text is unchanged.

## Practice: challenge the framing

Recalculate the late fraction if 10 of the 45 allegedly late records prove to be timestamp duplicates and the duplicates were also counted among the 180 requests. The revised fraction is \(35/170\approx20.6\%\). Explain why this correction can change the apparent urgency but not prove that the actual system improved. Produce a three-row evidence register and at least two competing explanations for the remaining late events. State what observation would reject each explanation.

## Limits and connections

Aggregate service statistics conceal time-of-day, disability accessibility, route and geographic inequity. Causal attributions require stronger designs than descriptive tabulations. The recommended sequence is a discipline for problem analysis, not a substitute for user research, safety engineering or regulatory review. Connect to [stakeholder needs](stakeholders-and-needs.md), [system boundaries](boundaries-and-interfaces.md), [requirements quality](good-requirements.md), and [design-risk retirement](design-risk-retirement.md).

## Primary sources

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — stakeholder expectations, system definition, technical baselines, validation and decision analysis.
- [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/) — sampling, uncertainty and statistical interpretation.

*Scope:* All numerical values and system descriptions are invented instructional data; no operational performance or safety claim is made.
