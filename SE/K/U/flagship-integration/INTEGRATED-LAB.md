# NS-U4.1 · Flagship and depth-method integration laboratory

*Step 04 U1 · Nine linked stations · all data are synthetic.* This laboratory deliberately does **not** model vehicle travel, field-safe operations, human fatigue, legal authority, or real emergency dispatch. Its purpose is to catch faulty engineering conclusions before a real project relies on them.

## Starting evidence and reproduction

- [Controlled input JSON](data/ns-u4.1-case.json) — demands, capacities, scenario assumptions, diagnostic likelihoods, evidence statuses and event trace.
- [Standard-library Python model](code/ns_u_case.py) — conservation, conservative timing classification, factorial contrast, paired sampling, Bayesian calculation, event conformance and claim gates.
- [Computed results](outputs/ns-u4.1-results.json) — generated from that JSON; never hand-edit the output to make a policy pass.
- [Claim-to-method crosswalk](data/ns-u4.1-crosswalk.csv) — lesson, calculation, input and limitation.
- [Nine flagship chapter readers](../flagships/README.html) and [twelve depth derivations](../derivations/01-from-need-to-verification.html).

From the repository root run:

```bash
python3 SE/K/U/flagship-integration/code/ns_u_case.py
python3 -m unittest discover -s SE/K/U/flagship-integration/code -p 'test_*.py' -v
python3 scripts/check_step04_flagship_u1.py
```

Keep two copies of the input when experimenting: an untouched baseline and an explicitly named scenario variant. Do not use output differences as evidence of real-world improvements.

## Station 1 — Define the engineering claim (F01, D01, D12)

Reconstruct the acceptance condition from dispatch latency $T=8$ s and worst-case timestamp uncertainty $u=.25$ s. Why are 72/80 nominal cases reduced to 67/80 conservative cases? Locate claims C2–C5 in the evidence register and classify their separate deficiencies. **Answer:** five 7.9 s cases cannot be guaranteed within 8 s; the five-claim register has one actionable record and four blocked records. Changing an evidence label without verifying scope and revision is not a valid repair.

## Station 2 — Separate feasible design from preference (F02, F06, D02)

Compare the baseline, capacity-only, guardrails and integrated alternatives over normal, surge, grid and compound scenarios. Apply both the all-rider threshold of 90% and accessible threshold of 85% in **each** required scenario. Compute the total weight of passing scenarios as $\sum_s w_s I_s$, and identify the smallest cost among *robustly feasible* designs. **Answer:** integrated passes normal only, with scenario-weight coverage .45; the robust feasible set is empty, so there is no lowest-cost feasible design. Do not choose a weighted-score winner instead.

## Station 3 — Statistical and diagnostic assurance (F03, F08, D03, D04)

Derive a two-sided 95% Wilson confidence interval for 72 successes in 80 independent Bernoulli trials, and compare its lower endpoint with .90. Recompute the prior-to-posterior update for a 15% prior route blockage, 80% alarm sensitivity and 10% false-positive rate. **Answer:** Wilson lower endpoint ≈ .8149, and one positive alarm gives posterior ≈ .58537. A second positive gives ≈ .91866 *only under conditional independence*. The traffic fixture is not a representative random field sample.

## Station 4 — Conservation and numerical error (F04, D06, D08)

For each rider group and scenario, check $B_{end}=B_{start}+\sum A-\sum S$ in the result traces. Use $\dot B=4-0.4 B$, $B_0=20$ to calculate two forward-Euler steps with $h=2$ minutes and one with $h=6$ minutes. **Answer:** $h=2$ gives 12 then 10.4 requests; $h=6$ gives −4, an invalid physical backlog. Stable continuous dynamics do not guarantee stable discretization.

## Station 5 — Contract violations and safety (F05, F07, D11)

Inspect `interface_events`. Identify the accepted exact duplicate and the three invalid operations. Explain why a later commit does not make an earlier acknowledgement valid. **Answer:** E2 is an idempotent replay; E3 is acknowledged before its commit; E1 is replayed with altered contents; E4 uses stale revision 1.0. The runner does not implement authentication, network concurrency, or a certified protocol parser.

## Station 6 — Fault dependence and mission resilience (F04, F09, D07)

With two elements at $a=.985$, independently redundant availability is $1-(1-a)^2=.999775$. Include the common-cause failure probability .03 and compare with a .99 target. **Answer:** .96978175 fails. A more favorable independent-elements diagram is not permission to ignore one shared power or firmware vulnerability. Change the common-cause probability to .005 and observe the model sensitivity, labeling the new assumption explicitly.

## Station 7 — Factorials, paired runs and inference (F08, D05)

Compute $I=y_{11}-y_{10}-y_{01}+y_{00}$ using [18,15,14,8] minutes; compute the twelve paired differences and their Student 95% interval. **Answer:** interaction −3 min; paired improvement mean 6.1667 min, 95% sample-based interval ≈ [5.4084,6.9249] min under pair independence and normality assumptions. An accurate simulated estimate can still be biased if the input process is unrealistic.

## Station 8 — Schedule metrics and intervention evaluation (F02, F09, D09, D10)

Determine the critical path of A–B–C (3,4,2 days) versus A–D–C (3,5,2 days). With EV=100, AC=130 and PV=120 compute CPI and SV. Then calculate the difference-in-differences with treated waits 22→13 and comparison 20→18. **Answer:** critical path A–D–C at 10 days; CPI=.76923, SV=−20; DiD=−7 minutes. Parallel untreated trends have not been demonstrated, and cost indices alone cannot establish the delivery date.

## Station 9 — Decision board and negative cases (F01–F09, D12)

Write a one-page technical disposition identifying the required scenarios, timing/measurement method, rejected event history, reliability dependence, subgroup performance and institutional permission status. Include an explicit no-go/rollback rule. **Answer:** HOLD for deployment. Normal performance passes for the integrated policy, but 0.45 scenario-weight coverage is below 0.95, guarded dispatch timing is 67/80, subgroup timing is 10/16, joint availability is below .99, four of five claim records are not actionable and road/labor/privacy approvals are missing. The proper next work is verified scope repair, reproducible stress testing, independent validation, and accountable stakeholder review—not a declaration of qualification.

## Controlled negative experiments

Try each change in a new file or a Python deep copy, and confirm that the checking code refuses or reclassifies it: (1) weights summing to 1.1, (2) negative capacity, (3) an unreachable alarm likelihood, (4) a duplicated claim ID, (5) a conflicting event replay, (6) marking a stale claim reviewed without updating its revision. Distinguish a rejected *invalid input* from a well-formed but *nonconforming engineering scenario*.

## Evidence boundary and student submission

Submit the changed JSON, executed outputs, conservation summary, one deliberately failing case, and a short decision memo that separates mathematical verification, statistical inference, model validation, release authorization, and any ethical conflict. This case cannot authorize real vehicles, clinical services, emergency routing, or public infrastructure. All numeric targets and weights were invented for instruction; they must be replaced by approved requirements and representative data in any real program.
