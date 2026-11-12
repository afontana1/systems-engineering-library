# Healthcare and human-service systems: stocks, flows, access and safety

**Canonical reference · Enterprise & complexity · Technical method and worked example**

## What makes human-service delivery a systems problem?

A healthcare or human-service system is not merely a queue of cases waiting for an appointment. It is a **sociotechnical work system** in which people, tasks, tools, settings, organizational rules, incentives, handoffs and delayed outcomes interact. Efforts to make one step faster can create rework, missed follow-up, inequitable access or exhausted workforce capacity elsewhere. Systems thinking seeks to explain those feedback mechanisms and design improvements that remain desirable **across the entire service journey**.

This article teaches operational modeling, not individual clinical decisions. All numbers describe a fictional community referral program. Service eligibility, safeguarding, privacy and professional judgment must remain explicit constraints; no queue equation can determine safe patient disposition.

## Boundary, populations and measures

Specify the population of need before defining the population recorded by the service. Distinguish: people **needing** help, those who know about it, those who can apply, accepted referrals, appointments completed, satisfactory resolution, re-referrals, and unmet need. Data only on completed visits can hide people excluded by language, geography, disability, connectivity, or eligibility rules. In particular, reducing the count of open referrals is not evidence of improved population health if the intake gate has become harder to cross.

For every population, state the counting rule, time unit, privacy safeguards and data provenance. The relevant outcomes may include time to appropriate service, safety incidents, repeat demand, access disparity, staff workload and sustained resolution. An average alone can conceal the tail of very long waits or adverse effects concentrated in a subgroup.

The SEIPS work-system perspective is useful here: analyze people, tasks, technology/tools, physical context and organization as a connected mechanism that influences **processes and outcomes**. This is a lens for investigation, not a substitute for observing how actual staff and service users work.

## Three complementary modeling views

**Stock-flow models** describe accumulation and feedback at the population level. Let \(B(t)\) be the backlog in referrals, \(a(t)\) the inflow of eligible referrals per day, \(s(t)\) completed referrals per day and \(w(t)\) withdrawals or transfers per day:

\[
\frac{dB}{dt}=a(t)-s(t)-w(t),\qquad B(t)\geq 0.
\]

The algebra is a conservation relationship, not a behavioral explanation. The completion rate must be constrained by the available backlog and effective service capacity; otherwise a numerical model can generate negative counts. Re-referrals can be represented as an additional delayed inflow, with an explicit relationship to quality and previous service.

**Queueing or discrete-event models** represent individual arrivals, priorities, capacities, schedules, timeouts and service-time variability. These are appropriate when the sequence and variation of work matter (for example, shift changes or an urgent-service pathway). **Causal-loop diagrams** capture hypothesized reinforcing and balancing effects, such as workload → fatigue → error → rework → workload. A causal loop by itself does not identify a calibrated causal effect or establish a numerical policy benefit.

## Worked example: capacity and hidden demand

A fictional referral program receives 60 eligible referrals per day and reliably completes 52 per day. Assume no transfers, withdrawals or new feedback during this short observation. The backlog rises by \(60-52=8\) referrals each day, so after 10 days it is **80 higher** than it was initially. This is not a steady queue. If the program increases effective completion capacity to 68/day while arrivals remain 60/day, it could reduce the accumulated 80 by at most \(68-60=8\) per day and therefore needs **10 additional days** to recover. That estimate assumes the higher capacity is sustained and there are enough outstanding cases to work.

A manager might conclude that the service is repaired after capacity expansion. But suppose online-only intake deters 12 additional people per day who still need assistance. Measured arrivals fall from 60 to 48, and the existing capacity of 52 can now reduce the *recorded* backlog by four daily. The dashboard looks better, while total unmet need could be growing. Those **12 are not actual observed people**: this is a counterexample showing why the boundary between need and recorded demand matters.

### When Little's law applies

For a stable system with a consistently defined population and observation window, Little's law relates mean number in system \(L\), throughput \(\lambda\), and mean time in system \(W\):

\[
L=\lambda W.
\]

If a *stable* service completes 50 referrals/day and a referred person spends an average 2 days in that same system boundary, the implied mean work-in-system is \(L=50(2)=100\) referrals. The example with arrivals 60/day and completions 52/day is **not stable**, so inserting its figures into a steady-state Little's law calculation would be unjustified. The counting boundary must also include abandoned or transferred cases consistently.

## Feedback, delays and policy resistance

A rushed-completion policy can improve short-term throughput while increasing repeat referrals after a delay. A minimal structural model might include two stocks—open referrals \(B\) and trained available staff \(H\)—with service capacity \(\mu(H,f)\) reduced by fatigue \(f\). Workload can raise fatigue; fatigue can lower effective completion quality and increase rework; rework increases demand and workload. Because training and hiring are delayed, a policy that maximizes today's throughput may cause future capacity decline.

Model each arrow as a **hypothesis to test**. Gather observations of repeat contact, safety exceptions, staff overtime, workforce turnover and waiting-time distributions. Compare alternative structural explanations, including seasonal demand, changed recording practices, referral appropriateness and external capacity constraints. An attractive stock-flow diagram cannot distinguish these without evidence.

## Compare policy portfolios rather than one lever

For a pilot, consider (A) extra appointment slots; (B) upstream navigation support; and (C) staff-support and quality review. Record cost, access, wait distribution, safety events, re-referral, and workload across relevant groups. Capacity-only interventions can fail if people cannot reach the service; navigation-only interventions can expose insufficient capacity; staffing-only interventions can fail without reliable handoffs. Evaluate interactions rather than adding independent advertised benefits.

A practical comparison plan states the unit of analysis (person, referral, episode or facility), the intervention date, comparison group, baseline trends, spillovers, follow-up period and stopping rules. Under a nonrandom rollout, changes may reflect seasonality, coding changes or differences in case mix. Use stratification and sensitivity analysis; do not claim causal improvement merely because performance changed after deployment.

## Model credibility, ethics and privacy

Model validity is **purpose-specific**. Check units, stock conservation, non-negativity, limiting behavior and sensitivity to demand. Validate against holdout periods and independent operational observations when possible. If a model is useful for strategic capacity discussions, that does not mean it is accurate enough for triage, prioritization or clinical scheduling. Clearly prohibit unvalidated individual-level use.

Protect confidential information through aggregation, access controls, retention rules and purpose limitation; even aggregate combinations can disclose small groups. Invite care workers, service users and accessibility advocates to critique boundaries and assumptions. Distinguish efficiency from equity and legitimate safety constraints. A recommendation is incomplete if it improves the average by shifting harm to less visible groups.

### Practice problem and solution

**Exercise.** A service has 90 open referrals and receives 25 new eligible referrals/day. It can complete 30/day for six days, with no transfers or withdrawals. Compute the new backlog. Then describe two observations required before asserting the change improves services.

**Solution.** \(B_6=90+6(25-30)=60\). This arithmetic is valid within the stated accounting boundary, but does not show that waiting times, clinical quality or equity improved. Check at least (1) whether any needy people were turned away or lost before entering the recorded system and (2) whether completed cases had appropriate outcomes and whether new re-referrals followed. A further valid observation would examine subgroup waits or staff safety incidents.

## Sources and limits of inference

- [AHRQ, *Using Human Factors Engineering and the SEIPS Model to Advance Patient Safety in Care Transitions*](https://psnet.ahrq.gov/perspective/using-human-factors-engineering-and-seips-model-advance-patient-safety-care-transitions) — Work-system, process and outcome framing; transitions as sociotechnical arrangements.
- [Carayon et al., *Work system design for patient safety: the SEIPS model* (2006)](https://pubmed.ncbi.nlm.nih.gov/17142610/) — Foundational description of SEIPS relationships in care settings.
- [NICE, *Service Delivery Operational Research Methods Reference* (2012)](https://www.nice.org.uk/media/default/About/what-we-do/NICE-guidance/NICE-guidelines/Clinical-guidelines/service-delivery-operational-research-methods-reference.pdf) — Distinctions between queueing, simulation and system dynamics for service planning.
- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/) — Statistical design, measurement and inference methods. The numerical referral scenarios in this article are original teaching assumptions, not estimates drawn from these sources.

## Follow the knowledge

**Related concepts:** [Stocks, flows and feedback](stocks-flows-feedback.md); [System dynamics model checks](systems-dynamics-model-checks.md); [Flow, work-in-process and bottlenecks](flow-wip-and-queues.md); [Human-systems integration](human-systems-integration.md); [Measures of effectiveness](metrics-hierarchy.md); [Critical systems thinking](critical-systems-thinking.md).

**Curriculum:** [EN.645.781 week 10](../../C/P3/EN645781.md); [Book 13 chapter 10](../B13/chapters/10-apply-systems-thinking-to-healthcare-and-human-service-delivery.md).

**Scope:** This guide does not provide medical advice, clinical triage criteria or evidence that any real healthcare service meets an acceptance threshold.
