## NS-GS4.1 extension — preference models behind non-compensatory gates

The Northstar design alternatives are status quo, throughput push, assurance first, and integrated controls. Their timely and accessible service fractions are **synthetic conditional outcomes** for clear, storm and compound conditions, not estimated population statistics. Scenario weights are deliberately illustrative: 0.50, 0.30 and 0.20.

### Model the constraint before the utility

Let \(t_{ps}\) and \(a_{ps}\) be the timely and accessible fractions for policy \(p\) in scenario \(s\). Hard acceptance criteria require \(t_{ps}\ge0.90\) and \(a_{ps}\ge0.90\), for every declared required scenario. The integrated policy has \(t=(0.97,0.92,0.86)\) and \(a=(0.96,0.91,0.82)\). Its scenario-weighted timely value is \(0.5(0.97)+0.3(0.92)+0.2(0.86)=0.933\), while accessible value is \(0.917\). Those weighted means exceed 0.90, but **compound disruption fails both hard constraints**. Weighted utility cannot compensate for a nonnegotiable safety or equity failure.

### Failure probability versus probability estimates

Under the invented weights, the integrated policy passes both screens in clear and storm, giving 0.80 scenario-weight screening coverage. The assurance-first policy passes only clear, giving 0.50. This is arithmetic on a constructed scenario set, **not** a verified 80% or 50% probability of mission success. Choosing the “best” among infeasible alternatives would conceal the need for redesign or scope negotiation. Value of information should target decisions likely to change with new data, for example whether the compound scenario's service mechanisms are captured accurately.

### Worked exercise and explained solution

**Problem.** A sponsor proposes selecting the integrated policy based on its 0.933 weighted timely score. What two counterchecks prevent approval?

**Solution.** First compute the **worst scenario**: compound \(t=0.86<0.90\) and \(a=0.82<0.90\). Second inspect the separate [digital evidence](../integrated/outputs/ns-gs4.1-results.json): only one of four requirement paths is actionable, and authorities are missing. Approval remains HOLD even if utility weights are unanimously endorsed. Recompute threshold changes in the [integrated lab](../integrated/labs/INTEGRATED-CASE.html), preserving the non-compensatory distinction.

**Canonical overlap.** [Decisions-and-architecture flagship](../../U/flagships/F02-decisions-and-architecture.html) provides general decision theory; the new method focuses on a cross-scenario constraint misread.

**Reproducibility record.** Re-run the [controlled executable model](../integrated/code/ns_gs_case.py) using the [shared case data](../integrated/data/ns-gs4.1-case.json), then compare with the [computed evidence record](../integrated/outputs/ns-gs4.1-results.json). The numerical outputs do not establish field validation or an authorized operating decision.
