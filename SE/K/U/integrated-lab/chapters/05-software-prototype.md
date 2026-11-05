# L05 · Build a constrained software prototype and test its invariants

**Learning time:** 5–8 hours. **Gate:** Software demonstration. **Prior reading:** [F05](../../flagships/F05-software-intensive-architecture.md), [F07](../../flagships/F07-human-factors-and-safety.md).

## Why a deliberately small program is educational

The reference [northstar.py](../src/northstar.py) is less than a production service. It is an executable description of assumptions, states, invariants, and error cases. That makes it useful for learning engineering discipline. A large framework with logging, messaging, and cloud deployment would add moving parts without supplying missing validity evidence. The important distinctions are **specified behavior**, **implementation behavior**, and **operational behavior**—only the first two can be explored here.

The pipeline reads `requests.csv` and validates data at its boundary. `deduplicate` admits exact replays but rejects conflicting reuse of IDs or delivery keys. `dispatch` allocates an available vehicle with `heapq`, advances each vehicle's next-free time, labels requests as completed within the horizon or unserved for lack of capacity, and computes nearest-rank p90 on the served subset. A request that has waited beyond the desired p90 is still considered served if it fits; this is a modeling convention, not necessarily an acceptable real service policy.

## Think like a test designer

A good test checks a claim that might fail. The baseline test should not merely assert that a function returns a dictionary. It should assert that 13 delivery events yield 12 unique requests, that every accepted assignment interval is free of overlap, and that a conflicting duplicate raises an error. Boundary-condition tests matter: empty input, non-finite arrival, zero vehicles, late arrival just before the horizon, and incompatible passenger count. See [the automated test suite](../tests/test_lab.py).

A *regression test* detects changes from expected behavior under a fixed configuration. A *property test* exercises a general invariant (no overlap). A *fault-injection test* forces a failure mode (one vehicle). A *validation exercise* asks whether your model is actually a plausible representation of real use. These are different forms of evidence; one cannot replace another.

## Model flaw investigation

An operational system must not silently mis-handle a `request_id` conflict or a request with two passengers. The prototype rejects both. However, its scheduling is a batch operation over known inputs. It is not a true online dispatcher where requests arrive while assignments execute. The audit hash is deterministic but not a secure chain of custody. The payload's `delivery_key` is validated only within one process. These limitations must remain visible in any release claim.

## Engineering activity

1. Run `python -m unittest discover -s tests -v` from the lab root. Pick one test and explain the failure mechanism it prevents.
2. Add a test that reveals the lack of geographical time dependence. Explain why this is not a defect relative to the *current* specification but is a limitation of the mission model.
3. Deliberately break `no_vehicle_overlap` by changing an assignment's `start_min` to overlap a previous interval; check that the checker detects it.
4. Write a change proposal for real-time event ingestion with atomic allocation. Specify which prior assurance claims become invalid until new tests are run.

## Knowledge check and explained answer

**Question.** Does a deterministic audit digest guarantee no tampering?

<details><summary>Show explanation</summary>

No. A digest detects differences only when a trusted comparison value exists. It does not authenticate the author, protect the storage system, establish an independent time source, or resist a malicious party who can replace both the record and its digest. Those properties need additional security architecture.

</details>

**Gate evidence:** passing unit tests, an invariant argument, a negative test that detects a defect, and a written limitation register.
