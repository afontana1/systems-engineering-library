# Systems of systems: autonomy, governance and emergence

**Graduate companion concept essay · EN.645.771 · Phase 5**

*All case data are invented teaching examples; models and calculations are not approved operational or safety evidence.*

A large integrated system and a system of systems can look similar in a component diagram. What separates them is not necessarily the number of components, but the **independent purposes and decision rights** of the participating systems. A city bus operator can run routes without a regional emergency-transfer coalition; its managers can also decide to replace a dispatcher independently. The regional capability must survive or adapt to those choices.

### A diagnostic rather than a slogan

Ask of every claimed constituent: What useful independent service does it provide? Who funds and governs it? Who can change its software, hardware, staff rules and service contract? Who can reject an SoS request? What is the notice period? A coalition may be directed for one mission yet collaborative for another. Governance is context-specific.

### Why emergence complicates guarantees

Imagine a hospital evacuation mission requiring an accessible vehicle, an available route and a receiving bed. Every constituent can pass its own availability test while the mission fails because all vehicles converge on one hospital at once. The failure arises through **coordination timing**, not necessarily a broken device.

A simple series approximation, `P(mission)=P(vehicle)×P(route)×P(bed)`, gives `0.95×0.90×0.90≈0.77` only if the events are independent and appropriately defined. If weather simultaneously affects routes and vehicle availability, multiplication overstates success. Use an explicit dependence model or explore bounded conditional cases.

### How to build a useful model

1. Define the mission outcome and time window.
2. Identify independent constituents and the decision owners.
3. Draw logical AND/OR dependencies with timing, alternatives and fallback.
4. Mark shared dependencies and autonomy constraints.
5. Stress-test one constituent's unannounced change, including who could authorize a response.

**Practice.** Suppose an agency refuses to share raw location but will provide area-level availability. Explain whether the mission remains feasible, what uncertainty changes, and which fallback is justified. Do not confuse information access with authority to direct the agency.

---

[← Phase 5 contents](../README.md) · [Concept pathways](../KNOWLEDGE-THREADS.md) · [Further reading](../RESOURCE-SHELF.md)
