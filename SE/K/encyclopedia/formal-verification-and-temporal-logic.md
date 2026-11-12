# Formal verification: state, invariants, temporal logic, and proof boundaries

**Canonical reference · MBSE and software-intensive systems · Expanded reference · Internal editorial review; independent peer review not performed**

## What formal verification actually establishes

Formal verification uses a mathematically specified model and logical rules to determine whether **stated properties follow from stated assumptions**. A correct proof of the wrong property, or of an abstraction that omits a critical interface, can still leave the deployed system unsafe. The distinction between *property*, *model*, *implementation*, *environment assumptions*, and *evidence of correspondence* is central. NIST describes formal methods as mathematically based techniques for specifying and verifying software and systems and notes that testing remains needed even when proofs are available.

A transition system comprises states, an initial condition, admissible transitions, and possibly environment inputs. A safety property asserts that something bad **never** happens; a liveness property asserts that something good **eventually** happens, usually subject to fairness assumptions. For cyber-physical systems, real-time guarantees add time and scheduling assumptions not captured in untimed state models.

## Model a concurrency bug before writing code

A dispatch service maintains available vehicles. The required invariant is that **no vehicle has two simultaneously active assignments**. Let `active(v,r)` mean vehicle `v` is currently assigned to request `r`. The safety invariant is: for every vehicle `v`, the number of distinct active requests for `v` is at most one. In a temporal notation, `G(no_duplicate_assignments)` means the invariant holds in every reachable state. Formalizing this property forces the designer to define when an assignment begins and ends, what cancellation means, and whether pending reservations count.

Suppose two workers perform the following non-atomic sequence: (1) check whether vehicle V is free; (2) compute an assignment; (3) write the new reservation. A possible interleaving is `W1 reads free → W2 reads free → W1 writes R1 → W2 writes R2`. Even if both workers pass all their local unit tests, the global invariant can be violated by duplicate external notifications. A transition-system checker can enumerate this counterexample for a suitably bounded model. An atomic conditional update or serialized allocator changes the transition relation so that only one successful reservation is possible.

A model-checker result cannot establish correctness if the actual database update is not atomic, a retry bypasses the guard, or a third service writes the same record. The design assurance chain must connect the model's atomic operation to real transaction semantics and deployment versions.

## Liveness requires more than a safety invariant

The property `G(request_received → F(decision_issued))` says every received request eventually leads to a decision. In ordinary linear temporal logic `F` means **eventually**, with no quantitative deadline. A two-second deadline requires a timed logic or equivalent bounded scheduling analysis. Liveness may also require fair scheduling, progress assumptions and bounded external service outages; otherwise a legitimate counterexample is an environment that never responds.

A practical proof portfolio distinguishes invariant checking, deadlock analysis, termination, response bounds, numerical range constraints, and refinements between abstract and implementation-level states. Finite model checking explores a particular bounded or abstract state space; theorem proving may reason about unbounded classes of states but requires formal assumptions and often more manual work. Static analysis, runtime monitoring, property-based tests and fault injection complement rather than replace this reasoning.

## Worked reasoning: an invariant as an audit control

Assume a service implements a conditional transaction: `reserve(v,r)` succeeds only if `owner(v)=none`, and successful reservation changes `owner(v)` to `r` atomically. Begin with `owner(v)=none` for all `v`. By induction over serialized successful transactions, the invariant `owner(v)` has at most one value in the database after every step. This is not yet an end-to-end proof: duplicate commands may be emitted before the transaction commits; replicas can expose stale reads; a crash may separate persistence from notification. The claim must say exactly **which state** is covered and which execution model provides atomicity.

This is a useful engineering trade: formalization can make a small but critical concurrency claim precise even when proving the entire platform is infeasible. Select properties by consequence, change frequency, and evidence cost. Where abstraction is coarse, record concretization tests that seek mismatches at interfaces.

## Common proof failures

- Informal requirements are translated into a property that omits an exception or hazard.
- The environment assumptions exclude overload, loss of synchronization, or malicious messages without justification.
- A model's state space suppresses interleavings that occur in the implementation.
- A “proved correct” label is transferred to a new build without assessing changed compilers, libraries, interfaces or configurations.

Formal proofs are powerful *conditional assurance arguments*; they should be versioned with the executable model, specification, assumptions, solver configuration and checking result.

## Selected source-to-claim references

- **F1 · Model checking as property evaluation over state machines:** [NISTIR 6777, Model Checkers in Software Testing — abstract](https://www.nist.gov/publications/model-checkers-software-testing).
- **F2 · Formal methods and limits of proof-to-implementation correspondence:** [NIST, Formal Methods and Combinatorial Testing — formal-methods section](https://csrc.nist.gov/Projects/automated-combinatorial-testing-for-software/autonomous-systems-assurance/formal-methods).
- **F3 · NASA executable-semantics example:** [NASA PLEXIL5 Formal Interactive Verification Environment — overview](https://software.nasa.gov/software/LAR-19339-1).

## Step 02 deeper treatment: bounded temporal behavior and counterexamples

A safety property prohibits bad finite prefixes: for example, *the door must never be commanded open while the shuttle is moving above the defined safe limit*. A liveness property says something good will eventually happen under stated fairness assumptions: for example, *an accepted request eventually receives a terminal response*. The distinction matters because checking a finite trace with no collision is different from demonstrating eventual progress.

Let \(m\) mean motion above the safe speed, \(o\) mean door-open command, and \(a\) mean an accepted dispatch request. In linear-time temporal notation, the safety invariant is \(\mathbf G\neg(m\land o)\). A bounded acknowledgement requirement can be written informally as \(\mathbf G(a\Rightarrow\mathbf F_{\le 2\mathrm{s}} r)\), where \(r\) is a terminal response. The latter bounded-time expression is **not** standard LTL syntax as written; it represents an extension with explicit timing, such as metric temporal logic, and needs a tool whose supported semantics match that notation.

**Construct a counterexample.** Model three discrete states: `Stopped`, `Moving`, and `DoorOpen`. Valid transitions include stopped-to-moving only with door closed, and stopped-to-door-open only under a fresh speed and brake confirmation. Introduce an erroneous transition `Moving -> DoorOpen`. A breadth-first checker finds the short path `Stopped -> Moving -> DoorOpen` and violates the invariant. A useful report includes the path, input events, software/model version and assumptions. Remove the defective transition, rerun the negative and positive tests, and test whether any new state is unreachable.

**Scope caution.** Exhaustive exploration of a finite abstraction does not prove distributed implementation correctness or physical safety. Clock drift, message reordering, unmodeled hardware faults and infinite-state timing behavior may lie outside the state graph. Record abstraction boundaries, fairness assumptions, test coverage and links to hardware verification evidence. See [behavioral contracts](../methods/mbse-behavioral-contracts.md), [model queries](model-queries-and-validation.md), and [configuration evidence](../methods/model-baselines-and-evidence.md).

## Follow the knowledge

- **Prerequisites:** [Good requirements](good-requirements.md), [Object responsibilities](object-responsibilities.md).
- **Related concepts:** [Verification](v-and-v.md), [Software lifecycle evidence](software-lifecycle-evidence.md), [System safety and hazards](system-safety-and-hazards.md).
- **Go deeper:** [Book 4, Chapter 10 — Executable constraints](../B4/chapters/10-express-precise-constraints-with-ocl-and-exec.md); [Book 9, Chapter 4 — State, modes and temporal consistency](../B9/chapters/04-model-state-based-behavior-modes-exceptions-hazards-and-temporal-con.md).
