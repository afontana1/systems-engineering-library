# Experimental design: ask a question the evidence can answer

*Core Concepts · Quantitative methods · T16*

> Build factorial experiments, control confounding, estimate interactions, and plan meaningful decisions.

**Recommended preparation:** [06 Inference](06-inference.md), [10 Decisions](10-decisions.md)

**Related companion books:** [Book 8](../B8/OPEN-BOOK.html), [Book 10](../B10/OPEN-BOOK.html), [Book 17](../B17/OPEN-BOOK.html)

## 1. Separate the research question from the simulation run
A simulation run is an observation produced by a particular model and a particular set of inputs. It becomes an *experiment* when we specify a question, control the design, and define how evidence will be interpreted. “Run the scheduler a hundred times” is not a question. “Does a second vehicle reduce the 90th-percentile waiting time by at least ten minutes under the defined demand distribution, without reducing completed requests?” is much closer.

Before selecting trial count, define the estimand: the average response over demand streams, the tail delay for served requests, the probability of a service failure, or the interaction between a fleet change and a dispatch policy. Distinguish the **unit of randomization** (a synthetic demand stream), the **unit of observation** (a trip), and the **unit of analysis** (often the replication). Treating 400 trips generated within only four correlated days as 400 independent replications creates false confidence.

## 2. Use factorial designs to see interactions
A two-factor experiment might compare fleet size (one versus two vehicles) and dispatch policy (first-come versus priority-aware). Let the response be the mean delay in minutes for the hypothetical scenarios in a balanced $2\times2$ design:

| | First-come | Priority-aware |
|---|---:|---:|
| One vehicle | 38 | 30 |
| Two vehicles | 22 | 18 |

The average effect of adding a vehicle is $[(22+18)-(38+30)]/2=-14$ minutes. The average effect of the priority-aware policy is $[(30+18)-(38+22)]/2=-6$ minutes. The interaction as a **difference of differences** is $(18-22)-(30-38)=4$ minutes: the policy's improvement is 8 minutes with one vehicle but 4 with two. It is misleading to attribute a single universal improvement to the policy.

These values are deliberately illustrative cell means. If each cell contains one simulation run, you cannot estimate between-replication variability. Add several independently generated demand streams per cell, record the random seeds, and analyze both performance and uncertainty.

## 3. Pairing is a design choice, not a trick
If the same demand stream is run under alternatives A and B, compare paired differences $D_i=Y_{B,i}-Y_{A,i}$. The standard error of the average difference is $s_D/\sqrt{n}$, where $s_D$ is the sample standard deviation of the paired differences. Pairing removes some variability from differences in demand intensity, but it is not automatically valid if one architecture changes the population being observed. If B rejects more trips, comparing delay among completed trips may introduce selection bias.

Never reuse a random seed across scenarios and then claim the runs are independent observations. Common random numbers create deliberate *correlation between alternatives*; independent replication groups still need genuinely distinct streams.

## 4. Control confounding and learning effects
A field trial might compare an old interface in Week 1 with a new interface in Week 2. Any improvement could result from staffing, weather, increased familiarity, or changed demand—not the interface itself. Random assignment, crossover design, matched comparison groups, and prespecified covariates can help, but each imposes assumptions. If emergency deployment prevents randomization, state exactly which causal claims the design cannot support.

Simulation studies have confounders too. A model comparison that changes routing, trip duration, and vehicle count simultaneously cannot isolate which change drove the outcome. Treat model configuration as part of the recorded experimental unit.

## 5. Failure of a null test is not evidence of equivalence
An effect that is not statistically significant might be small, or the experiment might be underpowered. Define the smallest important effect before collecting data. A decision board may prefer a noninferiority test if the goal is “new policy no more than 3 minutes worse, while improving safety.” In that case the uncertainty bound must be interpreted relative to the 3-minute margin, not relative only to zero.

Multiple exploratory comparisons increase the chance of spurious discoveries. Use a prespecified primary outcome for an operational gate, and label exploratory searches honestly. If a test campaign stops early when a favorable result appears, ordinary fixed-sample uncertainty formulas are no longer automatically calibrated.

## 6. Worked example: what does the interaction mean?
Suppose the two-vehicle system already has ample capacity. The priority-aware algorithm yields only a modest mean-time improvement because queues are already short. In the one-vehicle system, the same policy reallocates scarce capacity toward urgent requests, reducing their delays but potentially increasing the wait for nonurgent users. Mean waiting time alone hides distributional effects. Include completion rate, urgent-service performance, and an equity measure in the response vector.

The experiment should report an interaction and a policy tradeoff, not one headline percentage. Ask what the result would look like under a burstier demand distribution. If that distribution is poorly estimated, run a sensitivity analysis rather than multiplying replications of a single optimistic model.

## 7. Interpretation and evidence boundaries
A factorial design identifies modeled effects within tested factor ranges; it does not automatically generalize to untested fleet sizes, locations, or vehicle failures. For each claimed benefit, record the model version, warm-up handling, demand source, random seeds, outcome definition, and uncertainty procedure. Independent replication, reproducible analysis, and model validation are different obligations.

## Problems
**A.** Calculate the effects and interaction in the table above. **B.** Explain why paired replications do not justify counting every passenger as independent. **C.** Write a practical decision rule for accepting the priority-aware policy that includes a safety or fairness constraint.

<details><summary>Worked-answer guidance</summary>

Fleet effect $-14$, policy effect $-6$, interaction $+4$ minutes under the stated cell means and effect definitions. A sound design compares independent demand-stream replications, evaluates all required outcomes, and prespecifies the decision threshold. A favorable mean does not cancel a failed safety constraint.

</details>

## Further connections
[Statistical inference](06-inference.md), [multiobjective decisions](10-decisions.md), and [simulation credibility](19-simulation-credibility.md) explain why a statistically tight estimate may still be an inadequate system decision.

## Guided laboratory

[Open the corresponding case-based lab](labs/16-experimental-design-workshop.md)
