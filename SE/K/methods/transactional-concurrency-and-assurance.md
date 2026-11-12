# Transactional concurrency and software architecture assurance

## 1. Why an invariant is not yet an implementation

An object model can say “a worker may be allocated to at most one active reservation” and still deploy software that double-allocates under concurrent requests. This chapter extends [UML/OCL software contracts](uml-ocl-software-contracts.md) from **single-state assertions** to **interleavings and persistence mechanisms**. It uses a fictional dispatch allocation service in the Campus Mobility case.

The safety-relevant invariant is

\[
\forall w,\quad \sum_{r\in R}\mathbf1(r.\mathrm{worker}=w
\land r.\mathrm{status}=\mathrm{active})\le 1.
\]

This does not require “all requests eventually get a worker”; that is a separate *liveness* or service objective. Stating both is important: a system that rejects every reservation can satisfy the exclusion invariant but completely fail its mission.

**Prerequisites:** [behavioral contracts and state-space checking](mbse-behavioral-contracts.md), [model and evidence baselines](model-baselines-and-evidence.md), and [the Campus Mobility case](campus-mobility-engineering-case.md).

## 2. A sequentially correct design with a race

Consider application code that first reads `count(active reservations for W1)` and inserts a new active row if the count is zero. Under isolated sequential use, it appears correct:

```text
A: count(W1) → 0
A: insert(R1, W1, active)
B: count(W1) → 1; reject
```

A possible concurrent ordering is:

```text
A: count(W1) → 0
B: count(W1) → 0
A: insert(R1, W1, active); commit
B: insert(R2, W1, active); commit
```

The final state violates the invariant. A prior application-level check is insufficient unless it is protected by an isolation/locking/constraint mechanism that actually prevents the conflicting commit. Such a race is a **time-of-check to time-of-use** failure; it is not detected by running a snapshot audit after every individual development unit test unless that interleaving is tested.

## 3. Protect the invariant at a shared serialization point

For this local SQLite illustration, a **partial unique index** is a database-level enforcement mechanism:

```sql
CREATE TABLE reservations (
  request_id TEXT PRIMARY KEY,
  worker TEXT NOT NULL,
  status TEXT NOT NULL
);
CREATE UNIQUE INDEX one_active_worker
  ON reservations(worker) WHERE status='active';
```

Even if both clients read zero before either inserts, the database rejects the second conflicting active row. The [self-contained Python demonstration](code/transaction_exclusivity.py) reproduces the two orders without relying on fragile thread timing:

| Deliberate interleaving | Without unique index | With unique index |
|---|---|---|
| A and B both inspect an empty allocation | Both see zero | Both see zero |
| A inserts active `R1` | Accepted | Accepted |
| B inserts active `R2` for same worker | Accepted: **invalid state** | Rejected with constraint error |
| Resulting active rows for `W1` | 2 | 1 |

This demonstration uses two SQLite connections and a deterministic interleaving of reads and commits; it **does not** prove that all possible schedule, retry and crash interleavings are correct. The uniqueness condition also needs domain review: “one active reservation per worker” only holds if status changes and historical rows are correctly modeled. Retiring a reservation must update it atomically; otherwise a later valid request might be blocked or a premature status change might release a worker still in use.

## 4. Model the transaction boundary, not just a table

A real assignment operation may need to atomically coordinate multiple facts: reservation status, capacity accounting, a resource lease, a request idempotency key, and an outgoing command. A success response cannot be sent before durable commit if the client is supposed to rely on it. Where the database is the shared serialization point, a conceptual transaction is:

1. Verify the request ID's prior disposition (deduplication).
2. Validate worker eligibility and the current lease/state.
3. Insert or update the allocation with a constraint enforced by the database.
4. Record a durable event or outbox record in the same transaction if downstream work is needed.
5. Commit. Only then acknowledge success to the caller.

A transaction may fail because of a uniqueness violation, deadlock, serialization failure or timeout. The caller needs a bounded retry rule and an idempotent way to distinguish “the first attempt committed but its response was lost” from “the first attempt never committed.” Retrying blindly with a new request identity can create duplicate *logical* work despite preserving a particular table's uniqueness rule.

### The CAP slogan is not a concurrency design

Distributed allocation brings additional failure modes: partitions, leader changes, duplicate messages, delayed acknowledgements and incompatible replicas. A local uniqueness index cannot enforce a global invariant across independent writable databases without an appropriate coordinating protocol or restrictive architecture. Claiming “exactly once” for arbitrary distributed effects is especially hazardous; more defensible systems specify an idempotent business operation, stable request identity, deduplicated effects and compensation where atomicity cannot span boundaries.

## 5. Preconditions, invariants and linearizability

Write an operation as a state transition \(s\xrightarrow{\mathrm{allocate}(r,w)}s'\). Its preconditions may include `request is accepted`, `worker eligible`, `worker unallocated`, and `request not already fulfilled`. The postconditions should specify the durable new allocation and no conflicting active assignment. An operation is **linearizable** if concurrent histories can be understood as though each operation took effect at one point between its invocation and response, while respecting real-time precedence. It is stronger than merely ending each test with the correct count.

A database uniqueness constraint gives one important safety property. It does not alone establish a correct end-to-end reservation history, causal ordering of notifications, complete failure recovery, fairness or bounded response time. Event histories and retry semantics must be tested separately.

## 6. Test the right claims

A verification plan for the allocation service should include:

| Claim | Focused test | Remaining limitation |
|---|---|---|
| Two active allocations never share a worker | Commit-conflict test with distinct request IDs | Does not prove distributed global exclusion |
| Duplicate request does not make duplicate work | Retry same request after lost response | Does not prove remote side effect is idempotent |
| Cancel frees worker once | Crash/rollback tests around status transition | Late external commands may still execute |
| Accepted command is traceable | Outbox record and consumer idempotency checks | Does not prove physical dispatch acted correctly |
| Response satisfies timing requirement | Measured end-to-end latency under bounded load | Percentile claims need sampling and uncertainty analysis |

Configuration matters: log schema version, database engine, isolation setting, migration history, service software build, test workload and production topology. The synthetic results in this guide are **not** evidence about the Campus Mobility field system. See [the project verification matrix](data/campus-verification-matrix.csv) for controlled example formatting.

## 7. Reproduce and falsify

From the repository root:

```sh
python3 SE/K/methods/code/transaction_exclusivity.py
```

The run creates temporary databases with and without the unique index, checks the same interleaving and destroys the temporary files. Expected output shows two rows without enforcement and one row with enforcement. Both cases use `request_id` as a primary key, so a repeated attempt to insert `R1` is rejected; note that this **database duplicate-key rejection is not automatically a complete user-facing idempotency protocol**.

**Exercises:** (1) Explain how a check-then-act race can pass all purely sequential tests. (2) If a reservation can be temporarily `held`, propose whether the partial index should protect `held` as well as `active`; state the system-specific rule. (3) Describe a failure after commit but before acknowledgement; show how a stable request key allows a safe response on retry. (4) Design a two-service failure scenario where a local database constraint cannot enforce global exclusivity. (5) Write a test that prevents a “cancel” event from applying to an allocation generation newer than the event's observed generation.

## 8. Further technical sources and curriculum

- [SQLite partial indexes](https://www.sqlite.org/partialindex.html) and [SQLite transaction semantics](https://www.sqlite.org/lang_transaction.html) — actual mechanisms used in the executable example. Other database products have different features and isolation behaviors.
- [PostgreSQL documentation: transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — practical differences among isolation levels, serialization and retry handling.
- [Book 3, chapter 5](../B3/chapters/05-behavior-modeling-use-cases-activities-action.md); [Book 9, chapter 11](../B9/chapters/11-extend-the-modeling-language-and-automate-queries-validation-rules-m.md); courses EN.605.704, EN.645.631, and EN.645.764.

**Scope:** one controlled local persistence experiment. Not a verified distributed protocol, physical safety control, or blanket guarantee of concurrent correctness.
