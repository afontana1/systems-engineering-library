# Architecture, interfaces, and design tradeoffs

*Core Concepts · Modeling & software · T03*

> Separate functional responsibilities from physical choices, and reason about the interfaces that join them.

**Recommended preparation:** [System boundaries, outcomes, and emergence](01-boundaries.md), [Requirements, traceability, and assurance arguments](02-requirements.md)

**Related course companions:** [Book 3](../B3/OPEN-BOOK.html), [Book 6](../B6/OPEN-BOOK.html), [Book 7](../B7/OPEN-BOOK.html)

## 1. Architecture is a set of consequential decisions
An architecture is not the picture of the boxes: it is the collection of allocations and constraints that make some system behaviors possible and others difficult. Separate three questions: **what must happen** (function), **who or what performs it** (logical responsibility), and **what deployed asset does the work** (physical realization). A dispatch function might exist regardless of whether scheduling runs on a vehicle, at the depot, or in a cloud service. Those alternatives differ in latency, loss of connectivity, cybersecurity exposure, maintenance, and cost.

Functional decomposition asks what transformations take place. Physical decomposition asks where those transformations occur. Confusing them locks the concept prematurely to a specific technology and can hide missing responsibilities. For each important function, record trigger, inputs, outputs, timing, state assumptions, failure response, and allocated owner.

## 2. Treat interfaces as first-class design objects
An interface has more structure than a line on a block diagram. For a shuttle reservation API, define request fields, units, permissible values, identity and authorization, timing bounds, retries, duplicate handling, and what happens on failure. Physical interfaces require equally explicit mechanical, electrical, thermal, environmental, or safety conditions. Two components can pass local tests and still fail together because their assumptions disagree.

For a latency budget, start with \(L_{total}=L_{client}+L_{network}+L_{service}+L_{queue}\). If the end-to-end deadline is 500 ms and the first three terms have upper budgets 80, 120, and 100 ms, the queue and margin together have 200 ms. Averages do not prove worst-case deadlines; percentiles and correlated delays require separate analysis.

## 3. A trade study is not a beauty contest
A weighted decision score \(U_j=\sum_i w_i s_{ij}\) is useful only when criteria, scales, and weights have meaning. Normalize criteria carefully; verify whether a score of 4 is genuinely twice a score of 2, or merely an ordinal rating. Screening feasibility constraints should happen **before** scoring: an option violating an accessibility or safety condition must not win by making up points elsewhere.

Explore sensitivity. If architecture A scores \(0.8\) on reliability and \(0.4\) on cost, while B scores \(0.6\) and \(0.9\), and reliability has weight \(w\), then \(U_A=0.4+0.4w\) and \(U_B=0.9-0.3w\). A wins only if \(w>5/7\approx0.714\). This threshold is often more informative than the initial ranking because it reveals which stakeholder preference actually drives the decision.

## 4. Test the architecture under change
Architectural quality includes modifiability and recoverability. Change a data field, remove a network segment, or add a third vehicle. How many contracts, components, and safety arguments must be revisited? The architecture should expose these dependencies rather than bury them. A large number of interfaces is not automatically bad; a small number of poorly specified interfaces can be worse.

The architectural baseline should include decisions rejected and why. Future engineers need to know which tradeoffs were deliberate, which assumptions were temporary, and which interfaces are contractual.

## 5. Turn the drawings into a decision record
Create a decision record for each architectural commitment: the choice, considered alternatives, key constraints, evidence, known disadvantages, and conditions that would trigger reassessment. A cloud-only service might be defensible for a campus with robust coverage and non-critical dispatch, but not for an emergency system requiring continued local operation during communications disruption. The same diagram can represent very different assurance contexts.

An architecture must also reconcile **spatial** and **temporal** dependencies. Physical proximity may reduce network latency but increase correlated exposure to flooding or power failure. Service decomposition may improve team ownership yet introduce retries, version mismatches, and more distributed state. Evaluate the complete interaction cost instead of counting components or interfaces as inherently good or bad.

A practical interface review uses a deliberately adversarial sequence: send a valid message late, send a duplicate, omit a required field, reorder two events, change a unit, and replay a message from an earlier software version. For each case, state the system's expected observable response. This transforms a static interface diagram into a partial behavioral contract.

**Check your reasoning:** Is an alternative with the highest weighted score the preferred design? Only if it survives the hard constraints, the value model reflects stakeholder preferences, and the ranking is robust enough for the intended decision. An architecture review should report the boundary of that claim.

## Guided worked example

### Worked case: choose where dispatch runs
A cloud scheduler may simplify fleet coordination but depend on continuous network coverage. A depot scheduler may improve local continuity but require synchronization after outages. A vehicle scheduler may eliminate some communication delays but complicate global capacity assignment. First screen mission constraints; then score survivors; finally conduct a degraded-mode test. A weighted average alone cannot establish the safety of disconnection handling.

## Independent transfer exercise

Build three architecture candidates. Define one hard feasibility criterion, four weighted soft criteria, and two interface failure scenarios. Calculate the weight at which the leading two candidates reverse.

[Open the companion hypothetical lab](labs/03-architecture-workshop.md)

<details><summary><strong>What a defensible answer must contain</strong></summary>

Correct work shows hard constraints before utility scoring, identifies the units or interpretation of every scale, and reports the ranking sensitivity rather than only one winner.

</details>

## Next connections

Use the related books above to see how this concept becomes a course assignment. The lab provides a small, deliberately incomplete practice setting; it does not replace verification against real operational data.
