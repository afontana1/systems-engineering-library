# NS-G4.1 — Advanced systems engineering integrated evidence laboratory

*Six linked stations · Synthetic emergency-dispatch teaching case · Rev. 1.0*

This laboratory connects system safety, human workload, software contracts, technical resilience, independently managed constituents, and enterprise legitimacy. It does **not** implement a dispatch service, verify cryptographic signatures, calibrate operational risk, or supply legal permissions. All numeric inputs are invented and labeled in [the controlled case](../data/ns-g4.1-case.json). Do not use this model to direct vehicles or allocate real emergency services.

## Reproducible setup and evidence record

Use Python 3.10+ and only the standard library, from the repository root:

```bash
python3 SE/K/G/code/ns_advanced_case.py
python3 -m unittest discover -s SE/K/G/code -p 'test_ns_advanced_case.py'
python3 scripts/check_step04_advanced_studies.py
```

The first command writes [computed results](../outputs/ns-g4.1-results.json). Keep the JSON revision, file SHA-256 input fingerprint, method version, all five disruption cases, and every failed check. The published result is a deterministic calculation for the same controlled inputs; changing parameter assumptions is a new experiment, not evidence of real field performance. Use [the cross-claim evidence register](../data/ns-g4.1-claim-evidence.csv) as the starting point for the student's assurance report.

## Station 1 — Safety constraint and time uncertainty

Build a loss–hazard–constraint–test chain. Calculate the conservative bound

\[
A_{max}=(t_d-t_o)+\Delta_{execute}+\epsilon_{clock}.
\]

For baseline observations at 100 s and decision at 126 s, plus execution delay 5 s and skew 3 s, verify **34 s > 30 s**. Refreshing observation to 110 s gives **24 s**, which passes this one numeric constraint. Introduce 7 extra seconds of skew (not 5) and explain the resulting 31-second violation. Introduce route-interface R3 without updating the policy's R2 token: why is the otherwise fresh route still unauthorized? Name the actual authority that would approve a degraded operating mode; the model has no such approval feature.

## Station 2 — Human workload and alarm quality

Derive \(W_q=\lambda/[\mu(\mu-\lambda)]\) hours under M/M/1 assumptions and report utilization. Compare baseline **43.75 min** to coordinated **10.87 min**. Increase arrivals to \(8.4(1.17)=9.828\) per hour and reproduce **20.38 min**. Derive alarm PPV via Bayes' rule: baseline false-positive rate 0.10 yields approximately **21.77%**, coordinated rate 0.04 yields approximately **41.03%**. Design a human-participant test that would detect mode confusion, fatigue, and unequal delays not represented by the M/M/1 queue.

## Station 3 — Software state, contracts and retry storms

Run `trace_audit` on the six synthetic events. Verify that the first three events are accepted; E4 is an exact replay; E5 is an illegal early ACK; E6 changes the idempotency payload. Show why an ACK is not equivalent to durable commitment. At 80 external requests/s and 25% retry probability, offered attempts are **106.67/s**, less than 112/s capacity. Raise retries to 30% to show instability; implement no real network, concurrency control, or security credentials in the demonstration. Specify the production evidence needed to test crash recovery and replay.

## Station 4 — Dependence and resilience

Compute

\[
A=(1-q)[1-(1-A_L)^2]A_R A_D.
\]

Compare baseline joint availability approximately **98.19%** against the guarded nominal result approximately **99.10%**, then compound-disruption result approximately **95.62%**. Explain why shared grid loss invalidates a naive independent-replica calculation. Define the recovery-time and observability evidence still missing before claiming emergency resilience.

## Station 5 — SoS mission thread and change governance

Draw directed arcs for Request → Dispatch → Rail/Paratransit → Care. Use the supplied augmenting-path model to calculate nominal maximum flow **68 baseline trip slots**, nominal coordinated **70**, and rail-outage coordinated **32**. Compare the latter with **55 required**. In the compound grid/flood case, explain **58 available versus 62.15 required**. Identify which authority must accept each interface revision; route revision mismatch is an evidence failure even if capacity stays positive.

## Station 6 — Enterprise decisions, equity and causal uncertainty

Calculate group waiting-time gaps: baseline **22 minutes**, coordinated **9 minutes**. Compare policy costs against the invented $1.8M cap. Reproduce the illustrative difference-in-differences result of **−5 minutes** from treated 26→17 and comparison 23→19, and verify equal historical two-period slopes; explain why those pretrends do not prove exchangeability or no interference. Read the permission register: road, labor and privacy permissions remain ungranted. Write a reversible pilot plan including accessible-rider review, service-denial metrics, stop rules, owners and independent verification.

## Integrating the evidence and defending the disposition

The coordinated policy passes the nominal numerical screen but fails the surge, rail outage, compound hazard, and revision-drift scenarios. The five *invented* scenario weights assign only **55%** to passing technical conditions. This must **not** be reported as an estimated probability of mission success. Enterprise permissions are incomplete, and favorable technical results cannot substitute for signed rights, operational qualification, or a public-interest review. The allowed decision is **HOLD for deployment**, while retaining a limited educational design-screening conclusion.

**Submission:** (1) reproducibility command and input hash; (2) six technical worksheets with intermediate calculations, units and assumptions; (3) at least two deliberate negative tests; (4) a linked claim/evidence/owner matrix; (5) ethical and institutional limitations; (6) a reviewable recommendation with approval gates. Keep rejected traces and failed scenarios visible rather than deleting them from the result set.

**Evaluation guide (100 points):** mathematical correctness 25; software conformance and adverse cases 20; cross-owner interfaces and evidence provenance 20; uncertainty and causal skepticism 20; completeness and transparent recommendations 15.
