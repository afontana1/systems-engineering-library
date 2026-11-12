# Model-based behavior: state contracts and executable consistency checks

*Technical method guide · State machines, trace semantics, invariants, and bounded model checking · Phase 2 expansion*

**What this guide enables.** Translate an operational thread into states, events, guards, effects, and safety/liveness requirements; check a small model for counterexample traces; relate results to MBSE traceability and configuration management; and distinguish a bounded exploration from a proof about a deployed system.

**Prerequisites:** [MBSE semantics and evidence](mbse-semantic-modeling-handbook.md), [model, language, method and tool](../encyclopedia/model-language-method-tool.md), [requirements and traceability](../encyclopedia/traceability-graph.md), and [interface control](../encyclopedia/interface-control.md).

## 1. A diagram is not yet a behavioral contract

The fictional Northstar dispatch service lets passengers request a seat on a capacity-limited vehicle. A use-case description may say “passenger submits a reservation.” A sequence diagram can show request and acknowledgement messages, an activity view can show validation and assignment steps, and a state-machine view can define legal lifecycle transitions. These are useful views but are not automatically consistent: one view might interpret `accepted` as receipt of bytes, while another interprets it as a durable seat commitment.

Define a **shared event vocabulary**: `VALIDATE` means input was checked, `ASSIGN` means a uniquely identified resource was committed, `CANCEL` means the reservation was terminated and resources released, and `COMPLETE` means the service outcome was recorded. Every event should carry an identity, source authority, and timestamp or ordering evidence where relevant. Define what happens when a command is duplicated, arrives out of order, or is interrupted by a failure.

A transition system is \(M=(S,E,\rightarrow,S_0)\), where \(S\) is a set of states, \(E\) events, \(\rightarrow\subseteq S\times E\times S\) the transition relation, and \(S_0\) the initial states. A **trace** is an allowed sequence \(s_0\xrightarrow{e_1}s_1\xrightarrow{e_2}\cdots\). A diagram is one view or projection of traces; a contractual claim should say which traces are legal and what observable property they must preserve.

For a single request, use states CREATED, VALIDATED, ASSIGNED, CANCELLED, and COMPLETED. `VALIDATE` may change CREATED to VALIDATED. `ASSIGN` may change VALIDATED to ASSIGNED only when a capacity unit is free and route permission remains valid. `CANCEL` terminates a request and releases a booked unit **once**; `COMPLETE` requires recorded pickup and drop-off evidence. A duplicate `ASSIGN` must not book another capacity unit. A `CANCELLED→ASSIGNED` transition is forbidden unless a new, explicitly defined reopening protocol is present.

## 2. State variables and invariants make assumptions checkable

Model two requests competing for a single vehicle capacity unit. State consists of each request's lifecycle status and the number of capacity units allocated. For this **illustrative abstraction**, the reservation counter is the quantity of interest; payment, vehicle position, distributed database consistency, and network loss are intentionally omitted.

Write the core safety invariant

\[
I(s):\quad 0\le\mathrm{allocated}(s)\le\mathrm{capacity}=1.
\]

A safety property means something bad never occurs: a finite trace may demonstrate a violation. A liveness property expresses expected future progress, for example “every durably accepted request eventually reaches COMPLETED or CANCELLED.” Liveness needs environmental assumptions: a completely unavailable network, permanent capacity shortage, or scheduler that never runs can defeat progress without violating the capacity safety invariant. Do not claim that the safety check proves liveness.

A transition has **preconditions**, **effects**, and **frame conditions** (what does *not* change). For `ASSIGN(i)`, require request \(i\) in VALIDATED and `allocated < capacity`; its effect changes the request state to ASSIGNED and increments allocated once; other requests' statuses remain unchanged. Duplicate `ASSIGN(i)` when already ASSIGNED should be **idempotent**—no further capacity adjustment—or rejected without side effects, depending on the chosen API semantics.

A guard like `allocated < capacity` helps prevent overbooking, but when the real system is distributed the guard and increment must be atomic with respect to competing assignments. A state machine that executes one command at a time can hide a race: two clients might each see `allocated=0` and both commit. The abstraction therefore preserves *sequential state semantics*, not a proof about distributed concurrency. To claim concurrency safety, model interleavings at the read/check/commit level or use an implementation mechanism with verified atomicity.

## 3. Bounded state exploration and counterexample traces

The accompanying [state-space explorer](code/state_space_checker.py) enumerates all reachable states and commands for a small, fixed finite model (two requests, capacity one). At every state it checks the capacity invariant and a consistency condition: the counter equals the number of requests in ASSIGNED state. It records the shortest sequence of commands reaching a violation, if any.

For the corrected model, `VALIDATE(0)`, `ASSIGN(0)`, and then `ASSIGN(0)` does **not** allocate twice. The duplicate is idempotent. For an intentionally defective transition relation that allows a repeated assignment to increment a counter without enforcing capacity or request-state preconditions, the explorer finds a counterexample:

\[
\mathrm{VALIDATE}(0)\;\rightarrow\;\mathrm{ASSIGN}(0)\;\rightarrow\;\mathrm{ASSIGN}(0).
\]

The final state has `allocated = 2` despite `capacity = 1`. It violates both the capacity invariant and the agreement between the counter and request statuses. This is a **constructed defect**, not a discovered issue in real Northstar software.

The script uses breadth-first search and a fixed finite state model; it does not require a SysML interpreter or SAT/SMT solver. Its usefulness is pedagogical: the model has explicit state meaning and produces a witness trace that can drive a corrective requirement, a test, and a design review.

A passed finite exploration only supports the statement: “no violation was reachable in the modeled state space under the implemented transition semantics.” It does not prove correctness when the implementation adds retries, partial failures, queues, clocks, authorization rules, or more requests. Record the abstraction assumptions and which properties were checked, not just a green test status.

## 4. Reconcile requirements, behavior, structure, and verification

A model-based evidence chain for this case should include:

| Engineering claim | Model element | Evidence needed |
|---|---|---|
| No capacity overbooking | Invariant `allocated <= capacity` | Finite model check for abstraction; concurrency stress test and atomicity review for implementation |
| Duplicate assignment is idempotent | `ASSIGN` transition, request identity | API contract, retry tests, data-store operation review |
| Cancellation returns capacity | `CANCEL` transition and effect | State-transition tests and reconciliation of capacity ledger |
| Accepted requests terminate under declared assumptions | Fairness/liveness requirement | Operational failure and retry analysis; scheduler fairness model |
| Evidence applies to the release | Model and implementation baseline IDs | Configuration linkage, executable version and test-environment records |

A typed traceability relationship such as `satisfy` or `verify` does not turn a linked diagram into proof. The relationship needs a declared source, target, rationale, configuration, and reviewed evidence. An invariant checked against a model from release A cannot close a requirement in release B without explaining what changed and why the evidence still applies. See the [typed traceability and baseline audit](mbse-semantic-modeling-handbook.md) for a complementary example.

## 5. Connections to SysML and executable formalism

SysML v2 provides standardized language facilities for structure, behavior, requirements, analysis and verification, built on KerML semantics, as well as an API/services ecosystem. Its textual and graphical forms are ways of expressing formalized modeling information; the presence of syntactically valid SysML does not guarantee that the engineering semantics are correct or the model is complete.

The state-space program in this guide is **notation-independent teaching code**, not a claim of SysML v2 conformance, executable SysML interchange, or an OMG certified tool. The proper place to check language syntax, conformance, model interchange and mapping is the [official OMG SysML 2.0 specification](https://www.omg.org/spec/SysML/2.0/) and a suitable conforming implementation. A real migration from SysML v1 should inventory semantics that do not automatically map, including stereotypes, allocations, constraints, behaviors, tool extensions and identifiers.

An executable engineering modeling workflow would: (1) identify the governed requirement and behavior property; (2) express the candidate behavioral model in a declared language/abstraction; (3) run checks; (4) retain witness traces and model build IDs; (5) trace a counterexample to a corrected requirement or architecture decision; and (6) rerun checks and implementation tests after change. The tool is part of an evidence chain, not the owner of design authority.

## 6. Exercises and review gates

**Exercise A:** add a rule preventing cancellation of a COMPLETED request, then explain whether a late cancellation request should be rejected or processed as a separate refund/complaint event. Update the event vocabulary rather than quietly repurposing `CANCEL`.

**Exercise B:** change the capacity from 1 to 2 and add a third request. Identify the growth in the reachable state space. Explain where partial-order reduction or compositional modeling would help larger systems.

**Exercise C:** refine `ASSIGN` into separate `CHECK_CAPACITY` and `COMMIT` events. Construct the concurrency interleaving in which two simultaneous requests both pass the check. Propose an atomic commit rule and a verification strategy.

A sound review identifies which safety properties were actually proven for a finite model, which liveness properties remain unverified, which assumptions are external, which evidence is tied to a particular baseline, and which real-world implementation mechanisms require independent validation. A model that cannot express the failure that matters should be revised before it is used for a safety or acceptance claim.

## 7. Safety versus liveness in temporal reasoning

A property over a single state, such as \(\mathrm{allocated}\le1\), becomes a **trace invariant** when it must hold at every reachable step. In temporal-logic shorthand, \(\mathbf{G}(\mathrm{allocated}\le1)\) means “globally, at all points in a trace, capacity is not exceeded.” A progress claim can be written informally as \(\mathbf{G}(\mathrm{ASSIGNED}(i)\Rightarrow\mathbf{F}[\mathrm{COMPLETED}(i)\lor\mathrm{CANCELLED}(i)])\), where \(\mathbf{F}\) means “eventually.” The second property needs fairness and environmental assumptions; otherwise a request might remain assigned forever because no terminal event is processed.

The small Python explorer checks the two **safety** predicates it implements. It does **not** evaluate temporal logic, fairness, time bounds or liveness. A false liveness claim is not rescued by the absence of a safety counterexample. If completion within five minutes is an actual requirement, clocks and progress assumptions must be explicitly added to the model, and a suitable verification technique chosen.

## 8. Refine an atomic transition to expose a concurrency race

The abstract `ASSIGN(i)` transition checks free capacity and increments the ledger in one step. A naïve distributed implementation may instead use separate operations:

| Step | Request 0 | Request 1 | Shared recorded allocation |
|---|---|---|---:|
| 1 | Reads capacity 1 and allocated 0 | — | 0 |
| 2 | — | Reads capacity 1 and allocated 0 | 0 |
| 3 | Concludes a seat is available | — | 0 |
| 4 | — | Concludes a seat is available | 0 |
| 5 | Commits booking for request 0 | — | 1 |
| 6 | — | Commits booking for request 1 without rechecking atomically | **2** |

Both request-local checks passed, but the global invariant failed. This is a **time-of-check to time-of-use race**. An atomic conditional write, transaction lock, single-writer queue, or compare-and-swap operation can support an implementation contract, depending on failure and persistence requirements. To verify the implementation, test or formally analyze concurrent interleavings and crash recovery, rather than simply re-running the sequential checker.

A useful design rule is to specify **linearization points**: the operation at which the system has durably made a seat commitment and from which later clients must see its result. If retries are allowed, use a stable idempotency key and define whether a duplicate returns the existing result or a rejection. The term “exactly once” is not a free property of a network; semantics must include message duplication, recovery and persistent identity.

## 9. Manage the abstraction boundary as a controlled artifact

A model-checking report is incomplete without a table of preserved and omitted behaviors:

| Present in the small model | Deliberately outside the model |
|---|---|
| Two request identities | Arbitrarily many users and vehicles |
| Finite lifecycle states | Continuous-time scheduling and deadlines |
| Sequential event transitions | Overlapping read/check/commit transactions |
| Capacity counter invariant | Database durability, crash recovery and network partitions |
| Duplicate assignment event | Retries after ambiguous external acknowledgements |

The document reviewer should use the **omitted** column to decide whether the model is adequate for the intended claim. If the requirement primarily concerns collision-free *concurrent* seat assignment, a sequential abstract check is only one part of an assurance case. The appropriate next step is a refinement that introduces interleavings, then a real implementation test with bounded faults, load and recovery.

A well-governed modeling repository should record invariant identifiers, model tool/library version, abstraction assumptions, checker version, input set, counterexamples, correction rationales, and the configuration of the implementation to which the claim is being applied. These are knowledge artifacts, not user-progress records or browser checkpoints.


### Sources and curriculum connections

- [OMG SysML 2.0 formal specification](https://www.omg.org/spec/SysML/2.0/) and [OMG SysML v2 overview](https://www.omg.org/sysml/SysML-2.htm) for language scope, semantics and interoperability.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) for requirements, design assurance and lifecycle evidence.
- [Book 3, Chapter 5 — Behavior modeling](../B3/chapters/05-behavior-modeling-use-cases-activities-action.md), [Chapter 10 — Model V&V and configuration](../B3/chapters/10-verification-and-validation-modeling-configur.md), [Chapter 11 — Model queries and quality](../B3/chapters/11-model-quality-queries-reports-change-impact-g.md).
- **Curriculum:** EN.645.631 (behavioral and model-quality topics), EN.645.632 (analyzable model assumptions), EN.605.704 (object lifecycle and concurrency), EN.645.768 (architecture and interface assurance).
