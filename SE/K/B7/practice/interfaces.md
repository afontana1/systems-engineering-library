# Advanced Workshop · Interface Contracts and End-to-End Timing Budgets

*Book 7 · Week 6 · interface ownership · units · critical paths · synchronized failure*

**Placement:** After the relevant chapter, use this workshop to extend the reasoning, then try [the corresponding hypothetical lab](lab-interfaces.md). The assessed course obligations remain in [the curriculum](../../../C/P2/EN645768.html).

## 1. An interface is an enforceable agreement

A physical or software interface is not merely a connector on an architecture diagram. It is the boundary where different owners exchange data, material, energy, timing obligations, authority, and fault responsibility. A useful **interface control document** identifies the supplier and consumer, units, schemas, allowed states, version compatibility, timing behavior, security permissions, error responses, and change authority. Without those elements, both neighboring teams can satisfy their local specifications while the system fails.

Consider a fictional route authorization interface between Northstar dispatch and a vehicle. A permission message may contain a route identifier, permitted operating window, issuing authority, validity signature, and sequence number. A cryptographically valid signature is not enough if the permission has expired or refers to the wrong route revision. Interface verification must exercise negative conditions and recovery paths, not just valid-message decoding.

## 2. Use budget arithmetic carefully

For a sequence of deterministic operations, total latency is the sum. For a fork-join structure, the critical path includes the slowest parallel branch, not the sum of independent branches. Let authentication take 120 ms, route evaluation take 200 ms, vehicle-capacity validation take 150 ms, and commitment take 80 ms. If route and capacity checks are sequential, the total is 550 ms. If their results are independent and they can run concurrently, the path is

\[
T=120+\max(200,150)+80=400\ \mathrm{ms}.
\]

For a 500 ms deadline this leaves 100 ms nominal deterministic margin. If a 90 ms retry occurs before commitment, the scenario rises to 490 ms and only 10 ms remains. This is a useful budget argument, **not a p99 latency prediction**. Real execution times fluctuate, branching introduces dependence, and retries can change the load distribution. Measure the full critical path in representative conditions.

## 3. Distinguish tolerance stacks from probabilistic estimates

Suppose a location timestamp is accurate to ±20 ms and network transport adds 35–65 ms. Adding 20 and 65 to estimate a conservative timing guard may be justified if both are independent bounded maxima of relevant delays, but not if one is a statistical p95 and the other a stated maximum. It is common to mix percentiles, hard limits, and averages in one spreadsheet, producing a number with no defensible interpretation.

Units are another quiet source of failures. A component may publish velocity in miles per hour while another expects meters per second; an energy budget may mix kilowatt-hours and kilowatts. Interface contracts should define units at the schema boundary and include automated checks or typed quantities where possible. A successful parser cannot detect a perfectly formatted but physically nonsensical value unless the contract includes range and unit semantics.

## 4. Integration evidence is interface-specific

An integration test should not simply “verify the interface.” Identify exactly what is claimed: message schema compatibility, semantic consistency, authorization, latency, timeout behavior, freshness, and safe fallback. A time-sync failure can make valid data stale; a retry can create conflicting decisions; and an operator override can introduce a second authority. The interface test matrix should include both nominal and faulted scenarios and should tie every test to a specific configuration.

## 5. When optimization changes safety

Parallelization may reduce nominal latency but create a race between route evaluation and capacity assignment. A cached route may reduce a 200 ms call to 20 ms but return obsolete restrictions. Therefore a performance improvement proposal needs an accompanying assurance argument: which existing hazards are unchanged, which new hazards are introduced, and what evidence would support release? The fastest design is not automatically the mission-effective design.

## Worked problem set — attempt before revealing solutions

### Problem 1

Compute serial latency for 120, 200, 150, and 80 ms stages.

<details><summary>Show solution 1</summary>

120+200+150+80=550 ms, exceeding the 500 ms requirement.

</details>

### Problem 2

Compute the parallel critical path when 200 and 150 ms branches may run concurrently.

<details><summary>Show solution 2</summary>

120+max(200,150)+80=400 ms, providing 100 ms nominal deterministic margin.

</details>

### Problem 3

A 90 ms retry is introduced. What is the scenario duration and margin?

<details><summary>Show solution 3</summary>

400+90=490 ms with 10 ms margin; it is not an end-to-end percentile guarantee.

</details>

### Problem 4

Why does an interface document need units and valid-time rules?

<details><summary>Show solution 4</summary>

A message can be syntactically compatible but physically wrong or stale. Units, time windows and authorization are part of semantic compatibility.

</details>

## Independent transfer to the Northstar case

Create an interface contract for the booking–dispatch–vehicle path with explicit units, deadlines and owner responsibilities. Compare serial and parallel timing using `book7.py`, then add a retry and a stale-permission rejection. Draw a critical-path diagram, write a negative-test matrix, and propose which timing and security claims need real measurements rather than deterministic budget estimates.

## Further reading and conventions

The worked numbers are synthetic instructional fixtures. Do not use them as empirical transportation predictions, certification evidence, or claims about a particular deployed product. Foundational references (external and optional):

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/)

- [SEBoK — Guide to Systems Engineering](https://sebokwiki.org/wiki/SEBoK_Introduction)

- [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final)

**Continue:** [Hypothetical application lab](lab-interfaces.md) · [Python source](book7.py) · [Experiment dataset](book7-interfaces.csv) · [Interactive workbench](WORKBENCH.html).
