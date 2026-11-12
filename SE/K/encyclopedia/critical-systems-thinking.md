# Critical systems thinking: boundaries, power, and methodological choice

**Reference entry · Systems of systems, enterprise and complexity · Worked technical treatment**

## Why a mathematically optimal answer can still be wrong

**Critical systems thinking** asks whose purposes define a system, who has authority to draw its boundary, whose knowledge counts, and which consequences remain outside the chosen model. It does not reject formal methods. It clarifies when an apparently rigorous optimization represents only a narrow decision-maker's values, omits affected people, or makes uncertain institutional assumptions look like objective facts.

A classical systems model may define the Campus Mobility system as vehicles, dispatch software and charging stations. Students might optimize mean wait time over completed rides. But riders unable to access the reservation app are absent from those observations; campus staff responsible for accessibility or maintenance may not be represented in the objective function. A solution can be *technically efficient within its selected boundary* while socially or operationally invalid.

## Boundary critique as an engineering method

Record at least two versions of the system boundary: the officially declared boundary and a challenger boundary constructed from affected stakeholders. For each, explicitly identify the client or beneficiary, decision-maker, experts, affected but non-participating parties, intended measures of success, and costs pushed outside the boundary. Separate descriptive claims (“who currently decides?”) from normative claims (“who ought to decide?”).

A boundary review should yield a **decision log**, not just a discussion. For example, an initial optimization objective might be mean wait time conditional on completed rides. A challenged objective could add probability of service denial, accessibility coverage, shift changes for drivers, and local traffic risk. This changes data collection, model scope, and possibly the preferred alternative. Document who accepted or rejected those revisions and with what authority.

## Choose methods for the problem situation

Hard systems methods are useful when objectives, boundaries and causal relations are reasonably stable and measurable. Participatory or soft-systems methods can surface conflicting interpretations, contested problem definitions, and institutional constraints. Critical systems practice combines methods while making assumptions and exclusions visible. A system dynamics model can explore feedback; a stakeholder workshop can uncover missing incentives; an optimization model can evaluate a negotiated set of objectives. The techniques are complementary, not interchangeable.

No particular method removes politics or power from an engineering decision. Workshop participants may not represent affected communities; a feedback model may encode disputed causal assumptions; an optimization may bury values in weights. Report limitations instead of claiming that engagement or formalization created consensus.

## Example: the fairness denominator

In a hypothetical week, group A submits 80 eligible requests and receives 72 on-time rides, while group B submits 20 requests and receives 10. Overall, on-time service is \((72+10)/(80+20)=82\%\). Group-specific rates are 90% and 50%. Reporting only the aggregate conceals a 40-percentage-point disparity. The counts are synthetic and do not establish the cause of that disparity. A boundary critique asks whether all affected users could submit requests in the first place, whether the service definition is fair, and whether equal rates are the appropriate design objective.

A technical follow-up could formulate a constrained allocation: maximize total served demand subject to a negotiated minimum access threshold. But the threshold itself is a value choice needing consultation and governance, not a number derivable from queueing theory alone.

## Practical review protocol

1. Describe the problem from at least three roles: sponsor, operator, and affected party without formal authority.
2. List boundary inclusions and exclusions, including omitted risks and data populations.
3. Identify the method used and why alternatives were not chosen.
4. Make the decision criteria and value assumptions explicit.
5. Test a counter-framing using a changed objective or boundary; note whether conclusions change.
6. Preserve dissent, residual uncertainty and authority for the final choice.

The output can be a short boundary-and-method audit linked to the ConOps, metric hierarchy, models and decision record.

## Intellectual and engineering references

- Werner Ulrich, *Critical Heuristics of Social Planning* (1983) — foundational boundary critique and critical systems heuristics.
- Gerald Midgley, *Systemic Intervention: Philosophy, Methodology, and Practice* (2000) — methodological pluralism and boundary judgments.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — stakeholder and technical decision processes; not a substitute for normative critique.
- Related: [stakeholder needs](stakeholders-and-needs.md); [enterprise as a system](enterprise-as-system.md); [systems thinking and feedback](stocks-flows-feedback.md); [decision metrics](metrics-hierarchy.md).

*Scope:* This article explains a critical methodology and a hypothetical diagnostic case; it does not imply any specific organizational decision is ethically settled.
