## NS-GS4.1 extension — an improvement estimate is not a causal certificate

The course-wide program includes a small illustrative pilot. Treated operations' average wait changes from 22 to 15 minutes; a nominal comparison group changes from 20 to 17 minutes. These four values are deliberately generated, and no real randomization or parallel-trends evidence has been supplied.

### Difference in differences and interpretation

Let \(Y_{gt}\) denote mean wait for group \(g\) before or after. The simple two-group difference-in-differences estimator is

\[\widehat\tau=(Y_{T,post}-Y_{T,pre})-(Y_{C,post}-Y_{C,pre}).\]

With the case numbers this yields \((15-22)-(17-20)=-7-(-3)=-4\) minutes. It is tempting to say the intervention **caused** a four-minute improvement. That conclusion requires the unobserved counterfactual trend in the treated group to match the control trend, absent treatment. It also requires stable definitions, limited spillover, and credible timing.

### Threats to the design

The synthetic pilot has only one pre-observation per group, so a pre-trend check is impossible. If regional storm intensity fell more sharply in the treated area, the estimate could be biased. If a dispatch redesign shifts difficult cases to the control group, interference invalidates comparison. If denied requests disappear from the mean-wait denominator, the outcome changes meaning. A stronger design needs repeated pre-periods, an event study, cohort balancing, preregistered metrics and segment-level negative checks.

A confidence interval cannot be responsibly calculated without sample sizes and dispersion. Do not invent one from these four group means. A reproducible arithmetic test checks the subtraction, not the causal assumptions.

### Worked exercise and explained solution

**Problem.** Suppose the control post-period wait had instead fallen to 13 minutes. Recalculate the estimator and interpret the sensitivity.

**Solution.** New control change \(13-20=-7\); treated change remains −7; DID becomes \(0\) minutes. The observed treated improvement alone has not changed, yet the estimated *additional* improvement disappears. The result is sensitive to the counterfactual group. In the [integrated lab](../integrated/labs/INTEGRATED-CASE.html), record what field data would substantiate parallel trends.

**Canonical overlap.** This extension complements [statistical-assurance flagship](../../U/flagships/F03-statistical-assurance.html) by focusing on causal assumptions rather than merely computing a difference.

**Reproducibility record.** Re-run the [controlled executable model](../integrated/code/ns_gs_case.py) using the [shared case data](../integrated/data/ns-gs4.1-case.json), then compare with the [computed evidence record](../integrated/outputs/ns-gs4.1-results.json). The numerical outputs do not establish field validation or an authorized operating decision.
