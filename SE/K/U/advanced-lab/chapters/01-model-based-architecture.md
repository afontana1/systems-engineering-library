# A01 — Architecture as a testable engineering model

**Competency:** construct a bounded logical model whose components, interfaces, requirements and hazards can be checked for internal consistency, then explain what those checks cannot establish.

## Why model-based architecture matters

A block diagram can convey an appealing picture while hiding the most consequential engineering questions: where does a message fail, who owns a decision, which requirement constrains that interface, and what evidence would show the chosen behavior? A useful model makes those relationships explicit. Northstar's model is intentionally tool-neutral JSON, not a certified SysML model and not a substitute for semantic review. Its declarations are structured enough for automated graph checks.

Start by inspecting [architecture.json](../models/architecture.json). There are seven components, eight directed interfaces, six allocated requirements, four hazard links and request lifecycle transitions. The *DemandGenerator* represents the invented environment, not an operational transportation service. The *FaultInjector* is part of the test harness; including it as a first-class component prevents the common mistake of treating injected faults as unexplained behavior. The *EvidenceRecorder* records outcomes, while *AssuranceReviewer* is assigned to judge limitations—not merely to count passing tests.

## Three different kinds of correctness

1. **Syntactic correctness** asks whether identifiers are unique, interface endpoints exist and required fields are present. `validate_model` automates these checks.
2. **Behavioral correctness** asks whether implementation traces obey the intended transitions and scheduling rules. A graph checker cannot establish this; runnable tests must exercise the state machine.
3. **Fitness for purpose** asks whether this model captures the phenomena required for the actual decision. The Northstar prototype lacks geography, boarding time, accessibility variation, route choices and real operator authority. Passing both prior checks does not resolve these omissions.

A valid graph with a misallocated safety control is syntactically sound but engineering-invalid. Conversely, an unfamiliar state transition may be intentionally correct but fail the current validator; a reviewer should investigate, not simply silence the check. This is why models require both machine checks and independent engineering scrutiny.

## Worked analysis: a broken interface

Change `IF-03`'s `to` endpoint to `UnknownScheduler` and run:

```python
from src.architecture import load_model,validate_model
m=load_model('models/architecture.json')
m['interfaces'][2]['to']='UnknownScheduler'
assert not validate_model(m)['valid']
```

The checker should identify an unknown endpoint. Notice what it **does not** detect: that `IF-03` could use an incorrect time unit even when the endpoint exists. The contract must include units and validation rules, and a separate boundary test must verify them.

## Architecture decision

Should the intake service acknowledge a received request before or after it is persisted? Acknowledging early improves apparent latency but risks losing a request after confirmation. Delaying acknowledgement improves the chance that retry semantics reflect durable state, but adds response time and potential duplicate delivery. Neither policy can be chosen from the graph alone; use failure scenarios, requirements and a traceable decision record.

## Practice and deliverable

**Exercise 1.** Why isn't an arrow between two components sufficient to claim interoperability?

<details><summary>Worked answer</summary>Interoperability also requires agreement on schema and units, timing, ordering, error semantics, identity, versioning and authority. An arrow establishes only intended communication.</details>

**Exercise 2.** Add a component `OperatorConsole`. What should change?

<details><summary>Worked answer</summary>Add it to the components array, define producer/consumer interfaces with failure behavior, allocate any new requirements, update hazards, and review human authority. Validate the graph, then add behavior tests; a passing graph is not a demonstration of human usability.</details>

**Submit:** a revised model, a one-page model assurance argument, and one deliberately malformed model with its diagnostic output. Related: [v11 architecture stage](../../integrated-lab/chapters/03-architecture-interfaces.md), [architecture flagship](../../flagships/F01-requirements-to-assurance.md).

## U2 cross-lab credibility challenge — NS-U2.1

**Focus: Architecture scope and model correspondence.** This adds a controlled cross-version analysis to the original learning stage, which remains unchanged.

The v12 architecture graph can pass endpoint, uniqueness and declared-trace checks while representing a false real-world architecture. A JSON relationship from `Dispatcher` to `FleetModel` means that the model *declares* the interface; it does not test a real network or physical interface protocol.

**Cross-lab method:** Compare U2's two source/input digest inventories. v11 and v12 share a 12-request fixture, but the advanced model has additional fault parameters and may use different scheduling semantics. The bridge tests agreement only on the nominal completed count and refuses to infer protocol or vehicle equivalence from it.

**Exercise and solution:** Suppose an interface is renamed while every numeric output stays identical. What must be updated? Architecture interface versions, producer/consumer contracts, trace links, test configuration and evidence freshness. Source hash agreement is necessary for reproducing the original computation, never proof of conforming architecture.

**Reproduce:** [Cross-lab lab guide](../../lab-credibility-u2/README.md) · [Evidence gates](../../lab-credibility-u2/data/gates.json) · [Computed results](../../lab-credibility-u2/outputs/u2-cross-lab-results.json).
