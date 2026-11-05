# 13 · Systems of systems, enterprise capability, and distributed governance

**Concept dossier · system of systems / enterprise engineering / management of complexity**

## Technical connections do not grant authority

A system of systems (SoS) is more than many components in a large assembly. Constituent systems may have **operational and managerial independence**, their own lifecycles and owners, and the combined mission exhibits capabilities unavailable to any single constituent. An enterprise is a purposeful socio-technical system of structures, people, policies, information, incentives, technology and relationships.

A well-designed API cannot force a private transit provider to accept an emergency dispatch order. The protocol may work while the mission fails because legal authority, contracts, trust or incentives are absent. System-of-systems design therefore requires both **interoperability** and **coordination rights**.

## Capabilities versus applications

A capability describes the ability to achieve an effect under specified conditions. “Accessible evacuation coordination” is a capability; “purchase a shared platform” is a possible intervention. The capability also depends on trained staff, partner agreements, resources, updated curb data, authority during emergencies and rehearsal under realistic constraints.

A capability map should identify:

| Field | Example |
|---|---|
| Mission outcome | Eligible users transported to safe sites before closure |
| Operating conditions | Smoke, network degradation, variable road access |
| Participants | City, campus, bus contractor, emergency dispatch |
| Key dependencies | Accessible vehicles, route data, mutual-aid agreement |
| Authority | Who can prioritize service and approve exceptions |
| Evidence | Exercises, actual outcomes, incident reports |

## The enterprise objective is often contested

An agency may optimize response time, another cost, a contractor utilization, and a disability-rights group equitable access. A single weighted “enterprise score” can conceal whose values dominate. Governance must name decision rights and appeal routes, explicitly document tradeoffs, and account for those who suffer consequences without formal authority.

## Interoperability is multidimensional

- **Technical:** network connectivity, exchange protocol and authentication.
- **Syntactic:** matching fields and schemas.
- **Semantic:** shared meanings for terms such as “available,” “accessible” and “confirmed.”
- **Procedural:** compatible operations, escalation, timing and exception handling.
- **Organizational/legal:** authority, incentives, responsibility and data-sharing permissions.

A pilot that demonstrates API exchange tests only part of the problem. Real readiness requires mission threads that cross all these layers.

## Work through a disruption

During a regional evacuation, one provider's system reports 20 “available” vehicles. Ten have no qualified operator, four cannot accommodate wheelchairs, and six are under contractual restrictions. The aggregate API field is technically consistent but operationally misleading. An effective design clarifies availability semantics, validates data quality, defines emergency authority and tests cross-party decisions under time pressure.

## Exercises with answers

**A.** Why does a single enterprise diagram fail to show all capability risks? **Answer:** viewpoint and boundary omissions: incentives, independent governance, life-cycle changes and off-nominal interactions may be hidden.

**B.** Is successful data transfer proof of interoperability? **Answer:** only of one technical aspect; shared semantics, procedures, authority and operational usefulness are also necessary.

**C.** Who should own a disputed mission metric? **Answer:** a legitimate governance process with relevant stakeholders, documented definitions, accountability and appeal—not simply the team that builds the dashboard.

**Transfer artifact:** an SoS stakeholder/authority map, capability-to-mission trace, interoperability matrix and incident governance scenario.

## Connections

[Outcomes and boundaries](01-outcomes-boundaries.md) · [Reliability and cascades](10-reliability-resilience.md) · [Intervention design](14-causal-interventions.md).  
**Existing primers:** [SoS characteristics](../../encyclopedia/sos-characteristics.md), [Authority and governance](../../encyclopedia/authority-and-governance.md).
