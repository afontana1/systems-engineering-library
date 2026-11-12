### F07 extension · Safety control is not a favorable risk score

**Unsafe control action.** A route-approval action is unsafe if issued before current closure evidence exists, if delivered after a closure changes, or if it overrides a human-authority boundary. In the NS-U4.1 trace, a stale interface revision and an acknowledgement without prior commitment are separate hazardous control conditions. A software filter should reject them, but that does not prove operators can diagnose, communicate, or recover under emergency workload.

**Interpreting alarm evidence.** A positive blockage alarm has posterior $P(B|+)=0.5854$ from prior 0.15, sensitivity 0.80 and false-positive rate 0.10. This number is not a permission to enter a restricted road or automatically evacuate a group. To avoid automation bias, show the alarm source, data age, corroboration status, degraded mode, and available operator actions. The hypothetical second positive raises the calculated posterior to 0.9187 only *if conditional independence holds*.

**Subgroup harm is separately measurable.** Overall conservative dispatch timing in the fixture is 67/80 = 83.75%; accessible timing is 10/16 = 62.5%. The gap is $0.8375-0.625=0.2125$, or 21.25 percentage points. This comparison is descriptive, not a causal attribution: requests may be clustered by weather, priority, location, or radio condition. The safety case must examine whether the system transfers risk or waiting burden to people with fewer alternatives.

**Safety argument structure.** Identify loss (denied/unsafe evacuation), hazardous state (dispatch without valid route clearance), constraints (fresh authorization required), enforcement controls (revision/age checks and bounded stop), evidence (scenario traces, operator studies, assurance review), and residual gaps (actual workload, training, governance). A 1–5 risk-priority-number product cannot replace this control argument.

**Worked exercise and solution.** Suppose the dispatch team's average improves by 2 minutes but subgroup guarded performance stays 10/16 against a target of 85%. The group still fails its target, so the change cannot be counted as fully accepted merely because average waiting improves. Require a stratified re-test and an accountable mitigation before expanding the operating domain.

**Reproduce:** [alarm and subgroup computations](../flagship-integration/outputs/ns-u4.1-results.json), [D03](../derivations/03-bayesian-test-and-information.md), [D12 provenance](../derivations/12-digital-provenance-and-assurance.md).
