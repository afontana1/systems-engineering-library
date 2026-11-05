# One mission, three baselines: the decision-and-evidence chain

*Phase 2 concept library deep dive · Independent instructional synthesis*

## Why the baseline has to evolve
Systems development has a continuity problem. Concept development speaks in outcomes and viable alternatives; design groups speak in allocations, interfaces and parts; test groups speak in articles, environments, procedures and observed results. Teams can each create excellent local documents yet lose the link between what was needed, what was built and what was actually established. The cure is not one enormous table. It is a small set of **typed, revisioned relationships** maintained across three changing baselines.

An operational need links to a scenario and an effectiveness measure. A conceptual requirement links to functions and selected concept rationale. The design baseline adds physical owners, budgets and ICDs. The evidence baseline links the requirements and use scenarios to test procedures, executed configurations and accepted results. Every relationship answers a question: *why does this element exist? what must change if it changes? what evidence supports the claim?* A status icon is not itself evidence.

## A running example
For our fictional dispatch service, `NEED-04` says riders should know whether transport is available. `SC-05` describes a request during normal service; `MOE-02` measures the fraction of eligible requests served. The system requirement `REQ-14/C` defines event delivery under workload `WL-01`, and `IF-03/B` specifies its message contract. The design record `ADR-11` selects an asynchronous event service to meet resilience objectives. Formal test `VT-14` links not merely to REQ-14 but to executed data `RUN-38`, article `LAB-03`, build `D-21` and approved analysis `ANA-14`. A controlled trial with riders adds `VAL-06`, which speaks to usefulness—not only technical latency.

Now suppose the 900 ms requirement becomes 600 ms. A query should find all downstream budget allocations, simulation assumptions, interface constraints, test thresholds and customer communications that require re-review. An old successful 900 ms test does not demonstrate the new limit. A real trace system retains historical versions rather than overwriting old results.

## Build a minimum useful schema
Use IDs and link types such as `motivates`, `derivedFrom`, `allocatedTo`, `constrainedBy`, `testedBy`, `executedAs`, `verifiedBy`, and `validates`. Store link rationale and owner where necessary. A reviewable query is: "show all approved requirements with no accepted test evidence against their current revision". Another is: "find assumptions cited by a concept choice that have no planned experiment". Be prepared to explain why each link is semantically valid.

## Exercise and model answer
**Exercise:** An integration change moves an operator acknowledgement from optional to mandatory. What is affected? **Reasoning:** amend the operational scenario and state machine, specify who provides and times out the acknowledgement, revise interface messages, update timing and staffing budgets, add tests for acknowledgement failure, and update the operational validation plan. The point is not to add links indiscriminately but to show the actual causal consequences.

[Back to Phase 2 companion index](../README.md)
