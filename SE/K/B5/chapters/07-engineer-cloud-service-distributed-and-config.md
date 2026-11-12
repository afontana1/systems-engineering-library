# Chapter 7 — Distributed systems convert partial failure into design work

*Book V: Software Systems Engineering · Week 7 — Engineer cloud, service, distributed, and configurable architectures*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 7](../labs/lab-07-engineer-cloud-service-distributed-and-config.md) before attempting [the assessed Week 7 coursework](../../../C/P1/EN645764.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-764-w07.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **engineer cloud, service, distributed, and configurable architectures** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Networks can delay, duplicate, reorder or lose messages. Service decomposition distributes transaction boundaries and creates recovery states. Understand idempotent commands, durable outboxes, eventual consistency and backpressure before choosing a cloud topology. Availability and partition tradeoffs should be examined against the precise data consistency needs of each operation.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Distributed software experiences partial failure: one participant may commit a change while another observes only a timeout.

### Distinguishing related ideas

Retries do not automatically restore exactly-once behavior; without idempotency keys and durable deduplication, retries can create duplicate commitments.

### Interpretation and boundary conditions

Design states and recovery rules for ambiguous outcomes, especially when an acknowledged request is not yet durably recorded.


## Deeper theory — partial failure, state and the meaning of acknowledgment

### Why a remote operation differs fundamentally from a local call

A local function call usually returns a result or raises an exception in a process that can observe its own state. A remote service call crosses a network, at least two failure domains and often a durable database. A client that receives no response cannot know merely from silence whether the server never received the request, executed it but lost the reply, or committed it and then failed. This ambiguity is unavoidable in an asynchronous system with failures; it is not a defect that clever timeout settings can eliminate.

Consider booking request R17. The client sends `reserve(R17)`, and the service commits the reservation. The acknowledgment is lost. The client retries. If the retry generates another reservation, the system violates the passenger's expectation of one booking despite every individual network message having been valid. The remedy is not to promise perfect delivery; it is to define the **effect** that repeated delivery is allowed to have.

### Idempotency is a property of the operation's effect

An operation is idempotent if applying it again has the same relevant system effect as applying it once. `set_status(R17, cancelled)` can be idempotent when the target status and transition rules are well defined. `create_new_reservation()` is generally not. A practical API uses a stable request identifier and an atomic database constraint so repeated calls return the same recorded outcome. Crucially, storing the deduplication key and committing the business effect must be coordinated transactionally; storing a key in one system and a reservation in another can recreate ambiguity after partial failure.

An idempotency key is neither authentication nor authorization. A malicious caller must not be allowed to look up another passenger's reservation simply by guessing a key. The server must also define retention, expiration, payload consistency and what happens when the same key is reused with different content. These are design contracts, not implementation details.

### Consistency, ordering and real-time consequences

Two vehicle allocators may race to accept the same request or to book the same wheelchair-equipped vehicle. If both check availability before either commits, both may observe “free” and both may assign it. The consistency requirement is not necessarily “all data everywhere is immediately identical”; it is that a critical resource has a single authoritative allocation decision under the chosen coordination model. A linearizable allocation operation behaves as if it took effect at one instant between invocation and response. That can be implemented with a transactional reservation record, a compare-and-swap operation or an appropriately coordinated state machine, but it carries availability and latency costs under network partitions.

Not every piece of data needs the same consistency. Telemetry dashboards may tolerate eventually consistent updates, provided stale values are labeled and never silently substituted into safety decisions. Vehicle allocation may demand a stronger invariant. Architecture should therefore assign *consistency semantics per operation*, based on the harm caused by conflicting decisions rather than on a blanket slogan about strong or eventual consistency.

### Retries amplify load precisely when capacity is scarce

If each attempt independently fails with probability \(p\) and the client keeps retrying without a cap, the expected number of attempts is \(1/(1-p)\). At \(p=0.2\), that is 1.25 attempts per logical request. This idealized expression assumes independent outcomes and does not represent correlated network outages. In a real incident failures often become more likely as the service overloads, so retries increase demand just as service capacity falls. That positive feedback can generate a retry storm.

Suppose the normal arrival rate is eight bookings per minute and the dispatcher serves ten attempts per minute. Under idealized M/M/1 assumptions, the mean time in the system is \(1/(10-8)=0.5\) minutes. A 25% retry amplification raises the attempt arrival rate to ten per minute, reaching the modeled stability boundary. The simple queue predicts unbounded long-run waiting; the actual service may reject, time out or shed load instead. This example shows why a retry policy is part of the system's capacity architecture.

Backoff, jitter, bounded attempts, circuit breakers and load shedding reduce amplification but introduce their own behavior. A rejected booking must be represented honestly to the passenger; “we are processing your request” must not become an indefinite state. An operational contract needs a terminal result, a bounded uncertainty state or an explicit reconciliation mechanism.

### Recovery semantics and evidence

A dependable service must be able to reconstruct which requests committed after a crash. An append-only event log or durable transactional record can help, but logs are useful only if the semantics are explicit: did `ReservationAccepted` mean an intention, a committed database transaction or successful vehicle acknowledgment? Recovery should preserve safety invariants even when availability is sacrificed temporarily. In the shuttle case, it is generally safer to refuse a new allocation while the authoritative reservation state is uncertain than to silently create conflicting vehicle assignments.

The system-level assurance question is consequently larger than “Do the API tests pass?” It asks whether retries, races, delayed messages, database restoration and human override preserve the passenger-facing promise under specified failures. A robust architecture makes ambiguous outcomes visible, constrains unsafe transitions and provides a documented path to reconcile reality with recorded state.

## Worked Northstar example

A booking confirmation succeeds in the database but the client times out. A retry with the same idempotency key returns the original reservation. A retry with a new key creates a genuinely new command and must re-check capacity. “Exactly once” end-to-end must not be assumed.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.

### A retry is a new message, not necessarily new work

Consider a reservation key `req-42`. The server durably stores the booking but its reply is lost. The client cannot know whether the operation committed. With an idempotency key, the server can return the stored result on retry, provided the mapping survives restart and its retention policy covers the retry window. Without it, duplicate requests can consume a second slot.

This does not imply every distributed operation can be made “exactly once.” Delivery may repeat, side effects may happen in other services and the key's scope matters. Define each guarantee at the system boundary rather than at the message transport alone.

## What can go wrong—and why

Global locks are rarely a free substitute for carefully scoped invariants and operational recovery plans.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 7: Distributed systems convert partial failure into design work](../labs/lab-07-engineer-cloud-service-distributed-and-config.md), you will: Model loss, duplication and reordering of a dispatch command. Define response behavior, recovery logs and duplicate suppression. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 7 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](06-design-and-evaluate-architecture-with-quality.md) and leads toward [next chapter](08-specify-and-analyze-performance-networking-re.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-764-w07.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.


## Advanced worked practice

- [Deep workshop — Distributed Failures, Retry Storms, and Idempotent APIs](../practice/distributed.md)
- [Corresponding independent laboratory](../practice/lab-distributed.md)
- [Interactive workbench](../practice/WORKBENCH.html)


## Step 03 integrated reference: partial failure and delivery semantics

### A timeout is a statement about observation

Distributed callers often cannot distinguish “the server failed before commit” from “the server committed but the reply was lost.” A timeout means the caller did not observe a response within its limit. It does not provide a transaction outcome. For the [IF-02 allocation contract](../case/interfaces.csv), the client should reconcile via a stable idempotency token before trying to create a *new* assignment.

The invariant for vehicle-slot allocation is that at most one *active* reservation owns a `(vehicle_id, slot_id)` pair. An atomic unique constraint protects this database property; token-scoped response reuse protects client semantics. An application-level “check whether free, then insert” without atomic enforcement admits two concurrent readers observing the same unreserved slot. A replicated store or messaging layer changes what an atomic transaction covers; the design must state the chosen consistency boundary.

### Quantify the retry cost

If each attempt fails independently with probability \(p\), and at most two attempts are allowed, expected attempts per original request equal \(1+p\). At \(p=0.06\), this is **1.06 attempts**; the residual two-attempt failure probability is \(p^2=0.0036\). These computations assume independent and identically distributed failures. Real overloads make failures correlated; simultaneous retries can *increase* the queueing delay that caused them. Unbounded retries therefore damage the system exactly when it is least able to serve them.

Introduce deadlines, bounded backoff with jitter, token reuse, a retry budget, and a clear “unknown outcome” reconciliation path. Duplicate deliveries must not duplicate business effects. Outbox-style publication may help align a database transaction with asynchronous event generation, but event consumers still need idempotent processing and explicit recovery semantics.

### Safe degraded behavior

If location data is older than five seconds, NS-SW5.1 denies the dispatch request. It does **not** reuse stale position because availability is poor. If the entire reservation service is down, the operator interface announces unavailable status and follows its approved fallback workflow; this exercise does not claim that software availability measures guarantee physical vehicle safety.

**Exercise.** Under a persistent outage, all first attempts and retries fail together. Is the computed 0.36% two-attempt failure rate valid? **Answer.** No. The independence assumption is violated, and a perfectly correlated outage can yield an unchanged 6% failure probability instead of 0.36%. State the failure model before promising retry-driven reliability improvements.
