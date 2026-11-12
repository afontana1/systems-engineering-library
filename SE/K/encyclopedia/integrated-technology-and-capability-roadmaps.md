# Integrated technology and capability roadmaps

**Canonical reference · Enterprise & complexity · Technical method and worked example**

## Engineering question and scope

An **integrated capability roadmap** is a time-phased, evidence-backed argument that an enterprise can deliver and sustain a desired outcome. It connects *capability demand* to the technologies, standards, information assets, suppliers, workforce, operations, funding, and authorizations required to realize it. A technology-release timeline is only one input. A standards adoption plan without conformance testing, or a procurement plan without the staff needed to support it, is not yet an enterprise roadmap.

The central question is: **Which enabling elements must become usable together, what depends on what, and what decision will we make if one element is delayed?** A credible roadmap states the target operational capability, its use conditions and measures of success before listing products or release dates. It shows the transition state explicitly; a future architecture that cannot be reached safely from today's configuration is not a feasible recommendation.

## Decompose the capability without confusing readiness scores

For each needed capability, record: (1) stakeholder outcome and operational scenario; (2) technology and interface maturity; (3) governing information semantics, quality and stewardship; (4) standards and demonstrated conformance; (5) qualified suppliers and exit provisions; (6) workforce roles, competencies and training capacity; (7) facilities and operational procedures; (8) legal/privacy or safety approvals; and (9) acceptance evidence. Add an accountable owner and versioned source for each item.

Technology readiness level, organizational maturity and operational acceptance are not interchangeable numbers. A prototype may work in a laboratory but have no qualified production supplier, documented maintenance process, conforming interface or accountable data steward. Treat these as separate gates. If using a scorecard, define the scale and *the evidence for each score*; do not average ordinal grades and then call the result a probability of success.

### Dependency graph and critical path

Represent the roadmap as a directed acyclic graph for **mandatory precedence constraints**. For activity \(i\) of duration \(d_i\) months and predecessor set \(P_i\), its earliest completion is

\[
F_i=d_i+\max_{j\in P_i}F_j,\qquad \max\varnothing=0.
\]

This is a deterministic planning model, not a prediction. Durations can be uncertain, activities can compete for resources, and contracts or approvals can introduce calendar constraints. A credible schedule therefore includes ranges, critical assumptions, dependency owners and contingency options. Conditional dependencies should be made explicit: two suppliers may offer alternatives, rather than both being required.

## Worked case: regional service interoperability

Northstar's fictional service coalition wants to exchange dispatch availability data between agencies without changing each agency's legal authority. A public-facing launch is proposed for month 7. The engineering team constructs the following **illustrative** plan; durations are not empirical forecasts.

| ID | Required enabling activity | Duration (months) | Immediate predecessors | Evidence at completion |
|---|---|---:|---|---|
| S | Agree exchange semantics and data stewardship | 3 | — | Versioned schema, use/retention authority |
| Q | Qualify gateway supplier and interface | 6 | S | Conformance results, contractual exit/export rights |
| W | Train frontline and support staff | 4 | — | Competency demonstration, accessible fallback procedure |
| D | Run parallel operations and reconcile records | 2 | Q, W | Exception log, integrity checks, rollback rehearsal |
| G | Authorize public cutover | 1 | D | Signed acceptance and residual-risk decision |

Compute the earliest completion: \(F_S=3\), \(F_Q=6+3=9\), \(F_W=4\), \(F_D=2+\max(9,4)=11\), and \(F_G=12\). The feasible launch is **month 12**, not month 7, before schedule uncertainty or scarce-resource conflicts are considered. The critical chain is S → Q → D → G. Buying a faster gateway does not cure an unapproved data definition or a late supplier qualification.

Suppose the supplier activity can be shortened from six to three months but costs an extra $90,000, and delayed launch causes an *assumed* $15,000/month in avoidable opportunity cost. A three-month reduction avoids \(3(15,000)=\$45,000\), less than the premium: accelerated qualification is not justified on this simplified monetary model. Recalculate if a safety mandate, contractual deadline, or discounted multi-year benefit changes the decision. Neither figure is a real Northstar estimate.

## Standards, information and supplier contracts

A standard is a specification; interoperability is a **tested relationship between versions and implementations**. Record the exact edition/version, supported profiles, data types, units, reference frames, timestamps, character encodings and error semantics. Check conformance using negative cases, not only successful message exchange. For example, an incoming field named `arrival_time` could mean a forecast time at one agency and a confirmed stop time at another; syntactic JSON compatibility is insufficient.

For each supplier and data asset, record the party with rights to access, modify, export and retain it. Inspect proprietary adapters, licensing restrictions, incident-notification obligations, support horizons, workforce dependence and second-source feasibility. A transition may require dual operation, record reconciliation and retained legacy access; include these as funded roadmap activities, not footnotes. The highest-value gate may be a **reversible pilot** that validates semantics and training before an irreversible procurement commitment.

## Workforce and organizational adoption

Competence is a deliverable with acceptance evidence, not simply a count of staff attending training. Identify critical tasks, qualifications, duty coverage, accommodations, supervision and certification intervals. A plan for 12 operators needing 24 hours each requires 288 trainee-hours. If the training capacity is only 12 trainee-hours per week, it requires at least 24 weeks *unless* capacity or working assumptions change; this lower bound ignores absences, shifts and retesting. The schedule graph above assumes the four-month training estimate is feasible; a resource calculation that contradicts it forces the roadmap to be revised.

For workforce rollout, verify competency through scenario performance, error handling and safe recovery, not attendance alone. Include those who maintain the capability after initial deployment. Knowledge concentration can be as dangerous as technical single sourcing.

## Decision gates, scenarios and reversal criteria

Use decision gates tied to observations: (a) approving shared semantics; (b) accepting supplier conformance; (c) completing parallel-operation evidence; (d) authorizing migration and retirement. Each gate states the responsible decision-maker, released configuration, acceptance threshold, failed-case handling and fallback. Evaluate at least two scenarios—for example, supplier delay and a change in data-sharing authority—and recompute the dependency graph. If a required element fails, identify whether the enterprise should **pause, substitute, restrict scope, or reverse**. A single committed date without alternatives is not a robust roadmap.

### Exercise and solution

**Exercise.** In the table, gateway qualification Q takes **eight** rather than six months, while all else is unchanged. When can G finish? What happens if W instead takes ten months while Q remains six?

**Solution.** With Q = 8, \(F_Q=3+8=11\), \(F_D=2+\max(11,4)=13\), and \(F_G=14\). With W = 10 and Q = 6, \(F_D=2+\max(9,10)=12\) and \(F_G=13\). In the second case, the critical predecessor for D changes to W. This is why readiness decisions require a cross-domain dependency graph rather than separate technology and people slides.

## Limitations and evidence boundaries

A dependency schedule cannot prove political acceptance, supplier solvency, information legitimacy, safety or real-world adoption. Assign dates only after obtaining evidence from responsible owners. Enumerate what would invalidate the plan: standards changes, supplier insolvency, workforce attrition, inaccessible service pathways, emergency demand and data-governance objections. Maintain a versioned record of decisions and measure actual operational outcomes after rollout. Use the roadmap as a controlled hypothesis, not as a forecast of guaranteed success.

## Source-to-method references

- [NIST, *Roadmap to Strengthen the U.S. Manufacturing Supply Chain via Digital Thread Technology* (2024)](https://www.nist.gov/publications/roadmap-strengthen-us-manufacturing-supply-chain-digital-thread-technology) — Example of explicitly connecting digital-thread technology, standards and workforce enablers; this article's roadmap schedule is original and hypothetical.
- [NIST Communications Technology Laboratory roadmapping framework (updated 2026)](https://www.nist.gov/ctl/ctl-roadmaps) — Roadmapping process, stakeholder research and technical priorities.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — Lifecycle baselines, requirements, interfaces and technical management.

## Follow the knowledge

**Related concepts:** [Enterprise portfolio decisions](enterprise-portfolio-decisions.md); [Supportability and end-of-life](supportability-and-end-of-life.md); [Technical data governance and lineage](technical-data-governance-and-lineage.md); [Supply-chain assurance](supply-chain-assurance-and-provenance.md); [Engineering decision rights](engineering-decision-rights-and-learning.md).

**Curriculum:** [EN.645.753 week 8](../../C/P5/EN645753.md); [Book 19 chapter 08](../B19/chapters/08.md).

**Editorial note:** All named Northstar examples, dates and dollar values are invented for instruction. Standards and contract requirements must be checked against the editions and jurisdictions actually governing an engineering project.
