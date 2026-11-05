# Stakeholders, needs, and value: translating plural interests into engineering decisions

**Reference entry · Foundations and decision science · Expanded reference**

## Definition and distinction

A **stakeholder** can affect, authorize, operate, fund, maintain, experience, or be affected by a system. A **need** describes an outcome or protection valuable to that stakeholder, without prematurely dictating a solution. A requirement is a more specific, testable obligation allocated to a system or element. “Students should have dependable evening access” is a need; “the service shall offer two accessible departures per hour between 18:00 and 22:00 during the academic term” is a candidate requirement that still needs negotiation, feasibility, and acceptance criteria.

Stakeholders do not have uniform power or uniform exposure to risk. Users, maintainers, operators, regulators, neighboring communities, and people excluded by a design may disagree about what successful operation means. Engineering judgment cannot legitimately convert those differences into a single weighted score without first making governance and rights explicit.

## Theory: objectives, measures, and preferences

A useful chain is **stakeholder concern → desired outcome → objective → observable measure → threshold or preference → engineering decision**. Measures of effectiveness describe mission outcomes; performance measures describe system behavior that may contribute to those outcomes. They are related but not interchangeable. Faster vehicles do not necessarily yield shorter end-to-end journeys if scheduling and boarding dominate.

For compensatory decisions, a multiattribute value model can take the form **V(x) = Σ wᵢ vᵢ(x)**, where each attribute value function vᵢ maps a measured consequence onto a defined preference scale, and nonnegative weights sum to one. This additive form is appropriate only when its independence assumptions hold and tradeoffs have actually been elicited. Weights are **not** a substitute for explaining what a one-unit change in each scale represents.

Some obligations must instead be modeled as hard constraints: legal accessibility, a safety minimum, privacy protections, or a regulatory requirement should not be bought off by sufficient convenience elsewhere. Conflict is not automatically an arithmetic problem.

## Worked example: two apparently equivalent concepts

Consider two fictional shuttle concepts. A has average wait **6 minutes** and an accessible-trip completion rate of **88%**; B has a **9-minute** wait and **99%** accessible completion. If a team scores only average wait, A wins. If it uses an arbitrary 50/50 normalized weighted score, the answer depends on the scaling and may hide the serious 88% coverage shortfall.

Suppose the institution has approved a minimum **98% accessible-trip completion** requirement. Then A is *infeasible* regardless of its convenience score. Only after that constraint is enforced should the team compare feasible alternatives using service time, affordability, emissions, and robustness. The constraint is a governance decision that must be recorded, not a number the optimization algorithm discovers.

The data also need proper denominators: a rate computed only for accepted accessible bookings will hide refused or abandoned requests. Thus stakeholder framing directly controls the data definition, which in turn controls the engineering conclusion.

## Application procedure

1. Map actors by **influence, use, exposure, authorization, and lifecycle role**; include affected nonusers.
2. Gather outcome statements through operations observation, interviews, incidents, and relevant obligations—not interviews alone.
3. Separate *needs*, *proposed solutions*, *requirements*, *assumptions*, and *decision preferences*.
4. Define outcome measures with population, scenario, time horizon, denominator, units, and collection method.
5. Identify hard protections before eliciting negotiable preferences.
6. Revisit conflicts in an authorized forum; preserve dissent and unresolved tradeoffs.

## Failure modes and evidence

Avoid treating the loudest stakeholder as representative. Avoid double counting the same outcome in several criteria (e.g., average wait and travel satisfaction without checking dependence). Avoid averaging across population groups when poor service to a smaller group violates an obligation. Avoid presenting value weights as neutral facts: they reflect choices, circumstances, and legitimacy.

A defensible record consists of stakeholder categories; source evidence; scenarios; measure definitions; accepted constraints; elicitation rationale; and change history. Review affected groups after deployment because priorities and the operational population may change.

## Connections

Stakeholder needs determine ConOps, requirements, technical performance measures, test populations, value models, and the system boundary. In enterprise and systems-of-systems work, the authority to resolve conflicting needs is itself an architectural constraint.

## Reference shelf retained from the earlier primer

These links are supplied for deeper reading. Confirm current publication versions before relying on them for compliance.

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — Reference chapters for lifecycle, needs, requirements, design, technical management, integration and V&V.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Breadth-first conceptual encyclopedia and pointers to further references.


## Technical analysis: preference aggregation can hide exclusions

Stakeholder analysis should include who benefits, bears risk, operates the system, pays, and can reject a deployment. Requirements are often formed through negotiated tradeoffs, but averaging preferences can conceal serious losses to a small group. Keep group-specific service constraints separate from aggregate value optimization when basic access, safety, or legal obligations are at stake.

Suppose a transit design serves **90 of 100** general requests on time and **2 of 10** accessible requests on time. Its overall timely-service rate is `(90+2)/(100+10) = 92/110 ≈ 83.64%`. That average hides an **accessible-service rate of 20%** versus **90%** for the general group. Even if a new routing algorithm improves the global score, it can violate a stakeholder-approved equity objective unless group rates and failure consequences are recorded.

**Evidence boundary.** Elicit needs with affected groups, not solely decision sponsors. State which preferences are compensable, which are constraints, and who holds authority to change them. A stakeholder workshop cannot substitute for representative service data, and a technically verified requirement may still be a poor operational requirement.

## Claim-specific sources

The following **selected methodological claims** are tied to identifiable sections or abstracts, not merely generic reading lists. Source scope is stated for each link. Numerical scenarios and computations in this article are **original illustrative examples**, not data, calculations, or endorsements supplied by the linked publishers. Links require internet access; the explanation remains readable offline.

- **C1:** Stakeholder identification includes customers, users and less-visible parties affected by the product. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §4.1 Stakeholder Expectations Definition](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/) · *direct guidance*.
- **C2:** Technical requirements derive from validated expectations, constraints and operating concepts. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §4.2 Technical Requirements Definition](https://www.nasa.gov/reference/4-2-technical-requirements-definition/) · *direct guidance*.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2 (2016/2017)](https://www.nasa.gov/reference/systems-engineering-handbook/) — Lifecycle engineering, technical management, requirements, verification and validation.
- [INCOSE · Systems Engineering Handbook, 5th ed. (2023)](https://www.incose.org/resource/incose-systems-engineering-handbook-a-guide-for-system-life-cycle-processes-and-activities-5th-edition/) — Published practitioner reference; full text may require access.

## Follow the knowledge

**Related concepts**

- [Concept of operations and scenarios](conops-and-scenarios.md)
- [Requirements and acceptance criteria](good-requirements.md)
- [Measures of effectiveness and performance](metrics-hierarchy.md)
- [Pareto frontiers and multiobjective decisions](pareto-and-value.md)

**Explore in the 240-chapter textbooks**

- [Book 1, Chapter 3: Chapter 3 — Turn conflicting human needs into an operational concept](../B1/chapters/03-needs-and-conops.md)
- [Book 6, Chapter 2: Book 6 · Chapter 2: Evidence-based stakeholder needs](../B6/chapters/02-stakeholder-evidence-and-current-state-analysis.md)
- [Book 14, Chapter 2: Book 14 · Chapter 02 — Translate stakeholder values into objectives, measures, and value structure](../B14/chapters/02-translate-stakeholder-values-into-objectives-measures-and-value-stru.md)

**Use this reference responsibly:** examples use hypothetical engineering data; the mathematical results rely on the assumptions stated in each passage. Recheck those assumptions for any real project.

