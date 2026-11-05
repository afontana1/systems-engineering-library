# 2 · Interfaces as executable engineering contracts

*Graduate methods companion · System Design and Integration (Book VII)*

An interface is not merely a collection of field names in a diagram. It is a contractual boundary between independently implemented elements whose assumptions, time scales, failure modes, and configuration states must remain compatible. Integration failures often arise because each component passes its local tests while the composed system violates a temporal, semantic, or resource constraint.

## 2.1 Contracts have assumptions and guarantees

A contract can be expressed as $(A,G)$: under environment assumptions $A$, a component guarantees $G$. A dispatch authorization service might assume a trusted clock and route-status update not older than 250 milliseconds; it guarantees that an accepted departure command refers to the current approved route revision and a unique request identifier.

For a design of components $C_1,\dots,C_n$, it is insufficient to check guarantees independently. Each consumer's assumptions must be established by its upstream provider or by an explicit environmental contract. A diagram arrow reading 'route status' tells us little about units, timestamp meaning, validity, out-of-order delivery, missing data, and failure behavior.

A useful interface specification states schema, units, encoding, identity, authority, permissible state transitions, timing, freshness, timeout handling, version compatibility, observability, and verification evidence. Each property must have a test method and responsible owner.

## 2.2 Distinguish invariants from liveness

For a request $r$, a safety invariant might be

$$\square(\operatorname{Dispatched}(r)\Rightarrow\operatorname{Authorized}(r)).$$

Here $\square$ means 'at all times.' A liveness claim is

$$\square(\operatorname{Accepted}(r)\Rightarrow\Diamond\operatorname{Resolved}(r)),$$

where $\Diamond$ means 'eventually.' Liveness without a fairness assumption can be false if requests can be postponed forever. Eventual completion also says nothing about a response deadline. A timed requirement needs a bounded temporal property such as 'every accepted request is resolved within five minutes,' with explicit treatment of overload or unavailable services.

An idempotent command must tolerate duplication. For a state transformer $f$, an ideal mathematical idempotence property is $f(f(s))=f(s)$. Real systems additionally require that repeated commands with the same idempotency key return consistent externally observable outcomes, even after process restart. This implies persistent keys, transactional updates, and retention policies. A local in-memory set does not establish distributed idempotence across two replicas.

## 2.3 Temporal composition and budgets

Suppose an authorization chain consists of telemetry (85 ms), broker delivery (210 ms), authorization evaluation (150 ms), and dispatch application (80 ms). The **sum of reported component 99th-percentile delays** is 525 ms, below a 600-ms requirement. But this does not prove that the chain's 99th percentile is below 600 ms. Percentiles of random variables generally do not add. Their joint dependence matters, and bounding each component below its own 99th percentile only provides a union-bound probability of at least $1-4(0.01)=0.96$ that all four stay within their separate limits.

If hard per-stage upper bounds are respectively 120, 240, 170 and 90 ms, the deterministic composed worst-case bound is 620 ms, **exceeding** the 600-ms limit. This reveals a real integration risk even though the 525-ms point estimate appears acceptable. Engineering responses include reducing a stage's worst-case service time, pipelining where causality permits, imposing backpressure, or changing the deadline with approval. Simply adding more favorable percentile figures is not a corrective action.

Under a stochastic model, the end-to-end latency is $T=\sum_i T_i$. Its distribution must be estimated from a justified joint model or measured on the integrated chain. Common load spikes, shared network queues, and clock errors create dependence. A covariance term appears even in the variance:

$$\operatorname{Var}(T)=\sum_i\operatorname{Var}(T_i)+2\sum_{i<j}\operatorname{Cov}(T_i,T_j).$$

Positive covariance makes naïve independent-stage predictions optimistic.

## 2.4 Interface versions and monotonic safety

Two deployments can disagree on what the same field means. A new route revision may add a restriction, while an older consumer ignores it and accepts a structurally valid message. A safe compatibility policy must specify which fields are mandatory, what unknown values mean, and whether backward compatibility is allowed for safety-relevant decisions. 'Ignore unrecognized fields' is not always a benign choice.

The Northstar lab uses an authorization record containing `request_id`, `route_revision`, `valid_until`, `issued_at`, and `approved_by`. A valid signature proves that some key signed a given byte sequence; it does not prove that the route is current, the signer is authorized for the requested action, or the observation applies to the specific vehicle and corridor. Provenance and policy must be checked together.

## 2.5 Integration tests as counterexamples

A good integration test attempts to falsify the composed contract. Vary order, delay, duplication, process restarts, clock skew, stale data, service exhaustion, and simultaneous route changes. Observe both positive outcomes (authorized dispatch) and forbidden outcomes (unauthorized dispatch). Use a reference model or test oracle independent of the implementation where possible.

In a model-based review, turn each interface claim into a chain: requirement → owning component → interface contract → measurable property → test → evidence object → revision. Missing links are not paperwork issues; they identify claims for which the team cannot demonstrate responsibility or proof.

## Worked problems with explained solutions

**Problem A.** Why is the sum of four component p99 latencies not necessarily an end-to-end p99 bound? **Solution:** Quantiles do not generally add, dependencies are unknown, and the event that all four stages remain under their p99 can have probability as low as 96% by the union bound.

**Problem B.** What margin remains under hard bounds 120, 240, 170, 90 ms and a 600-ms deadline? **Solution:** $600-(120+240+170+90)=-20$ ms. The deterministic budget is infeasible without redesign or changes in the assumptions.

**Problem C.** Does a valid message signature authorize dispatch using an outdated route revision? **Solution:** No. Authenticity of bytes is distinct from freshness, semantic scope, current policy, and authorization.

**Problem D.** A duplicate reservation reaches two server replicas. Both check an in-memory key set; each observes 'not seen' and commits a different reservation. Which property failed? **Solution:** The global idempotency/uniqueness invariant. The check and state update must be coordinated atomically through a shared transaction or equivalent consistency mechanism.

## Independent research question

Specify an assume-guarantee contract for route authorization under temporary network partition. Decide what must fail closed, which actions can continue in degraded mode, and what test evidence would establish safe recovery when connectivity returns.

**Practice:** [Interface adversarial testing lab](../labs/02-interfaces.html) · [Python model](../code/graduate_models.py) · [Notebook](../notebooks/02-interfaces.ipynb).

## 2.6 Compositional reasoning and refinement

Formal verification of every possible integrated execution is often infeasible. Compositional reasoning reduces the problem by proving component contracts and then checking that assumptions align. Let component A guarantee route-revision validity if it receives a current policy snapshot, while component B guarantees that snapshots are at most 250 ms old if synchronization is available. The integrated guarantee is conditional: a network partition can invalidate B's assumption, which means A's guarantee may cease to apply. In a correctly designed degraded mode, A detects that condition and refuses authorization or moves to a separately justified safe behavior.

Refinement asks whether a more detailed implementation preserves the observable properties of an abstract specification. Adding a cache must not introduce behavior the abstract contract forbids. Behavioral refinement is stronger than schema compatibility: two services can exchange valid JSON while disagreeing about whether an accepted reservation is tentative or committed.

A useful review table lists each state transition and its preconditions, postconditions, allowed errors, side effects, and audit events. The table becomes a basis for model-based test generation. Aim to test forbidden transitions as deliberately as permitted transitions, including the moments just before and after timeouts, restarts, and revision changes.

## 2.7 Backpressure is a cross-layer design choice

When requests arrive faster than a service can process them, unlimited queues convert overload into increasing latency and memory consumption. Admission control and bounded queues make the system more predictable, but they introduce rejection. This moves the problem from a purely technical performance concern into a service-policy decision: which demands receive priority, what must a rejected requester be told, and how is equity monitored? Queue capacity, resource utilization, and emergency override must be designed together. An interface contract is therefore a bridge between software correctness and stakeholder outcomes.
