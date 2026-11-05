# D10 · Causal evaluation and difference-in-differences

**Skill:** Explain what a before/after comparison measures, and what assumptions turn it into a causal estimate.

## The counterfactual problem

Suppose a region pilots an accessible dispatch policy. Its mean wait falls from 12 to 8 minutes, a four-minute reduction. A comparable untreated region falls from 10 to 9 minutes over the same period, perhaps due to weather or seasonal demand. The *difference-in-differences* (DiD) estimate is:

`(treated after − treated before) − (control after − control before)`

`= (8−12)−(9−10)=−4−(−1)=−3 minutes`.

Under the required assumptions, the policy may have reduced wait by about 3 minutes beyond the shared time trend. This is not automatically a randomized causal effect.

## The critical parallel-trends assumption

Without treatment, the treated and control locations must have had comparable trends in the relevant outcome. Their baseline levels can differ; the **trends** matter. Use multiple pretreatment observations to inspect plausibility, but no finite visual check can prove the unobserved counterfactual. Also consider composition changes, spillovers between locations, concurrent interventions and changes to measurement.

If riders move from the control service to the treated service after the intervention, or the control adjusts its policies in response, “no interference” fails. If only satisfied users remain in the sample, selection bias can make both methods appear to improve.

## Engineering use

Apply the same logic to process improvements: compare pilot teams with similar non-pilot teams, preserve definitions of escaped defects and review time, and assess distributions as well as averages. Predeclare adverse outcomes and stopping criteria; a favorable throughput effect may accompany higher rework or worse access for a subgroup.

## Practice

**Question:** If the treated region reduced wait by four minutes, why isn't −4 the intervention effect?

<details><summary>Solution</summary>

Because some improvement could have happened even without the policy. The control's one-minute improvement suggests a shared time trend, producing an illustrative DiD estimate of −3 minutes if parallel trends and other assumptions are credible.

</details>

**Transfer artifact:** Hypothesized causal graph, treatment/control selection rationale, pretreatment trend plot, DiD estimate with uncertainty, spillover audit and adverse-impact review. See [intervention and learning](../../encyclopedia/intervention-and-learning.md).
