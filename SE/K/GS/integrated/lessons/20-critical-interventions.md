## NS-GS4.1 extension — a favorable population average can hide imposed harm

Management of a complex emergency-access service requires explicit scrutiny of who sets the system boundary, what outcomes are counted, and whose losses may be compensated by others' gains. A synthetic intervention lowers urban waits from 12 to 8 minutes while rural waits rise from 24 to 29 minutes. The stated urban population share is 75%; no real community is described by these figures.

### Boundary arithmetic and the non-compensation rule

The initial population-weighted mean wait is \(0.75(12)+0.25(24)=15.0\) minutes. After the intervention it is \(0.75(8)+0.25(29)=13.25\) minutes: the mean improves by 1.75 minutes. Rural wait simultaneously worsens by \(29-24=5\) minutes. A decision rule of **no additional rural harm** cannot be satisfied by a better overall mean. The two measurements are not substitutes. The explicit acceptance predicate is \(\Delta W_{rural}\le0\), which is false.

### Critical methods and decision rights

Before labeling the program a success, identify rural patients, dispatch workers, accessibility advocates, hospital staff and emergency authority holders. Ask what each group considers a valid outcome, whose data are missing and whether an appeals process exists. A causal estimate is also not permission: the case explicitly has unsigned road-authority, labor and privacy decisions. Consent is represented as a required approval record, not a numerical weight to optimize away.

Constructing a better weighted index or rerunning a Monte Carlo study does not answer who may authorize the experiment. Stop conditions should be explicit: evidence stale, safety guard failure, unconsented data use, or material harm to a protected service group. Retain negative findings so decision makers see the intervention's distribution of effects.

### Worked exercise and explained solution

**Problem.** If urban share rises to 90% with all group-specific delays unchanged, what happens to the average and rural-harm decision?

**Solution.** Before: \(0.9(12)+0.1(24)=13.2\) minutes; after: \(0.9(8)+0.1(29)=10.1\) minutes. The average improvement grows to 3.1 minutes, but rural harm remains **+5 minutes**. The intervention still fails the non-compensation rule. In the [integrated laboratory](../integrated/labs/INTEGRATED-CASE.html), document whose authority is missing and what would justify a reversible pilot.

**Canonical overlap.** [Human-factors-and-safety flagship](../../U/flagships/F07-human-factors-and-safety.html) develops the safety context; this study emphasizes explicit beneficiary/affected-party boundaries.

**Reproducibility record.** Re-run the [controlled executable model](../integrated/code/ns_gs_case.py) using the [shared case data](../integrated/data/ns-gs4.1-case.json), then compare with the [computed evidence record](../integrated/outputs/ns-gs4.1-results.json). The numerical outputs do not establish field validation or an authorized operating decision.
