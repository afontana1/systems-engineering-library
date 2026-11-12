## Step 04 integrated case — NS-CE4.1: executable interface obligations

The resilient concept's finite-scenario capacity screen is favorable, but downstream dispatch messages can still violate the integrated service. Here the **provider** publishes sequenced dispatch events and the **consumer** must either process contiguous, fresh messages for the agreed revision or stop and request recovery. A packet's syntactic validity is not sufficient to establish a correct state transition.

### Contract and temporal obligations

Let $s_k$ be the sequence number of accepted message $k$, $t_k$ its embedded event timestamp, and $r_k$ the local observation time, all in seconds on a common assumed clock. A simple safety contract is

$$s_{k+1}=s_k+1,\qquad 0\le r_k-t_k\le2,\qquad v_{\rm contract}=v_{\rm observed}.$$

The age test is meaningful only if both timestamp sources share a sufficiently synchronized clock, and the two-second threshold is an *assumed contract*, not a derived safety limit. If receive order is not guaranteed, reordering requires explicit bounded buffering and a timeout state. A consumer must not silently treat a missing sequence as an empty/no-op command. The corresponding liveness property would require eventual delivery, recovery, or safe abort under an explicit fairness/retry assumption; the finite trace alone cannot prove liveness.

The controlled four-message trace is:

| Arrival | Sequence | Event / observed (s) | Violation |
|---|---:|---|---|
| 1 | 1 | 0.0 / 0.4 | None |
| 2 | 2 | 0.5 / 0.8 | None |
| 3 | 4 | 1.0 / 1.4 | Missing sequence 3 |
| 4 | 2 | 0.5 / 4.0 | Repeated/reordered; age 3.5 s |

The provider announces revision **2.1** but the consumer's verified contract is **2.0**. The [executable interface checker](../code/ns_evidence_case.py) reports four independently identifiable defects: `gap`, `duplicate_or_reordered`, `stale`, and `revision_mismatch`. The checker compares event integers and bounded ages; it is **not** a conforming formal-language parser, a distributed protocol implementation, or a timing proof.

### Why checking the entire composition matters

A dispatch command may pass schema validation while its semantics are unsafe because it refers to an event skipped during synchronization. For example, if sequence 3 revoked a route, processing sequence 4 as if 3 did not exist can apply an obsolete authorization. The precondition for applying sequence 4 is therefore a verified predecessor state. A useful assume-guarantee statement is: *given a synchronized clock, authenticated sender, and consecutive revision-compatible events, the consumer never transitions on a message older than its freshness bound*. The contract says nothing about what happens if the assumptions fail unless that failure response is separately specified.

A real deployment would need protocol semantics for idempotent replay, exactly-once or at-least-once delivery, monotonic sequence scopes, clock resets, partition handling, access control, and emergency fallback. Revision strings alone do not establish semantic compatibility. Pair a machine-readable change notice with explicit impact analysis and rerun tests against the current producer and consumer builds.

### Calculation and counterexample

For message 4, $r_4-t_4=4.0-0.5=3.5$ seconds; lateness above the bound is $1.5$ seconds. Merely discarding message 4 does not restore correctness: sequence 3 remains missing, so the consumer still lacks the acknowledged state transition between 2 and 4. To repair the chain, provide event 3 or a verified state snapshot with declared semantics, replay valid later events, and establish current 2.1 interface acceptance evidence. Increasing `max_age_seconds` to 4 would suppress the stale-age flag but not repair the gap, duplicate, or revision mismatch.

**Worked exercise 1 — trace repair.** An engineer reorders arrival 4 before arrival 3 to make sequence 2 precede 4. Is the contract satisfied? **Solution:** No. The event with sequence 2 already appeared at arrival 2, and sequence 3 is still absent; the stream contains a duplicate and a gap. Sequence reordering does not synthesize a missing validated state transition.

**Worked exercise 2 — version change.** The provider changes from 2.0 to 2.1 without altering the JSON field names. May the consumer reuse its 2.0 verification evidence? **Solution:** Not automatically. Unchanged syntax does not establish identical retry, ordering, or safety semantics. A reviewed compatibility argument and regression evidence are required.

**Adverse case.** In a copy of the controlled JSON, set `observed_at_seconds` earlier than `timestamp_seconds`. Input validation must reject the impossible age rather than interpret negative age as unusually fresh. Test unvalidated timestamps and missing authentication as separate required security evidence. An interface trace test is a necessary *counterexample finder*, not an operational qualification of the complete distributed system.
