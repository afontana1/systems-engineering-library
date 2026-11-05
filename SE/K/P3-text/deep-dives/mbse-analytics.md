# Executable models and trustworthy traceability queries

**Cross-course pathways:** Applied MBSE Analytics 1–12; Model-Based Systems Engineering Phase 1; Decision Science 8.

## A model element is more than a named box

A queryable digital model requires stable IDs, types, meaningful relations, controlled configurations and validation rules. A requirements graph might contain `Need N1 → Requirement R1 → Function F2 → Component C3 → Test T4`. Traversing that graph checks *coverage*, not correctness. If R1 contains an impossible performance target, complete traceability merely reveals a well-documented error.

Record a validation question for each relation: Is the need justified? Does the requirement logically derive from it? Is the function sufficient? Does the component provide the function under the scenario? Does the test actually exercise the specified condition? Automated traversal can catch missing links but does not answer those semantic questions without richer rules and evidence.

## Parametric constraint discipline

A model quantity `cycle_time_min = 60 route_km / mean_speed_kmh + boarding_min + dwell_min` has a defined dimension. For 5 km at 30 km/h plus 4 min boarding and 2 min dwell, cycle time is 16 min. If the route length is accidentally entered in meters while labeled kilometers, the constraint can produce a plausible-looking but absurd answer. Include ranges, unit conversion tests and parameter provenance.

An analytic model might then constrain `throughput ≤ vehicles × riders_per_vehicle × 60 / cycle_time_min`, but that is an upper bound: schedules, state, headways and load distribution can lower realized throughput. It is not automatically a performance guarantee.

## Change-impact graph exercise

Suppose a message field changes from `eta_s` to `eta_ms`. A graph query should identify publishers, consumers, transformations, test fixtures, dashboards and verification procedures. The units, not the name, carry the core semantic change. Require a test that demonstrates conversion before closing the change.

**Practical handoff:** Build a CSV matrix with elements and relationships, rerun a missing-trace query after deleting one edge, and keep the query output with the model baseline.

---

[Back to Phase 3 knowledge library](../README.md) · [Toolkit](../tools/README.md)
