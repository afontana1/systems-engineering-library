# Cascading failures, cut sets and resilient mission paths

**Graduate companion concept essay · EN.645.771 · Phase 5**

*All case data are invented teaching examples; models and calculations are not approved operational or safety evidence.*

A mission capability is vulnerable when dependencies create paths for failures to propagate. Network drawings can help, but connectivity alone does not encode operational meaning, time, capacity or failure probability. A cut set is a set of components whose loss defeats a defined mission claim. A **minimal cut set** has no proper subset that also defeats it.

### Logical structure

Let mission success require `(bus OR paratransit) AND hospital AND (city_network OR backup_radio)`. Failure occurs if both transport alternatives fail, if hospital intake fails, or if both communication alternatives fail. The minimal failure sets are `{bus, paratransit}`, `{hospital}`, and `{city_network, backup_radio}`. Listing minimal sets suggests where redundancy could help—but shared dependencies may defeat apparent independence.

### A common-cause trap

Suppose the city network and backup radio both require one regional identity service to authenticate dispatch staff. The identity service is itself a single-point cut set despite two communications channels. A typical architecture diagram that omits authentication misses this. One response is a preauthorized local break-glass mode with audit and limited privileges; another is genuine independence of the backup path. Neither is cost-free or universally safe.

### Resilience sequence

Specify mission-essential function, detection threshold, absorption margin, graceful degradation, recovery time objective, restoration authority and subsequent learning. Verify these as scenarios, not as generic labels. A rapid recovery may restore technical availability while violating accessibility or information-integrity requirements.

**Exercise.** Add a shared power supply to the two transport coordination paths. Update the minimal cut sets, then explain what evidence would prove that the proposed backup is actually independent.

---

[← Phase 5 contents](../README.md) · [Concept pathways](../KNOWLEDGE-THREADS.md) · [Further reading](../RESOURCE-SHELF.md)
