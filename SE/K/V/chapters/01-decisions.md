# 1 · Choosing a concept when the evidence is incomplete

*Graduate methods companion · Conceptual Design (Book VI) · Northstar case*

A concept review is not a contest to find the highest score in a spreadsheet. It is a decision under constraints, imperfect knowledge, competing values, and often irreversible commitments. We will distinguish **feasibility**, **preference**, **uncertainty**, and **learning**. Confusing these questions is a common source of apparent precision and poor design.

## 1.1 Establish decision authority before computing

Northstar is selecting a regional dispatch architecture. Two designs are under consideration. The compact design, C, has a capital cost of $6.3 million, tested capacity of 98 trips per peak period, and a modeled 90th-percentile wait of 18 minutes. The larger design, R, costs $7.0 million, has capacity 112 and a modeled 90th-percentile wait of 14 minutes. Stakeholders have specified capacity of at least 105 and a 90th-percentile wait of at most 16 minutes under the *specified peak scenario*. Under those conditions C is not feasible, regardless of any attractive cost score. A weighted sum should not be allowed to trade away a hard safety, accessibility, or mission constraint without a separately authorized change to that constraint.

Let $x$ be the selected architecture and $\omega$ a scenario. Define the feasible set

$$\mathcal F(\omega)=\{x:g_j(x,\omega)\leq0,\ j=1,\ldots,m\}.$$

A robust feasible design satisfies these constraints for every scenario in an agreed uncertainty set $\Omega$. A chance-constrained design might instead require $\Pr[g_j(x,\omega)\leq0]\geq 1-\alpha$. These are not equivalent policies. Robust feasibility is sensitive to the chosen uncertainty set; chance constraints require defensible probability distributions and loss consequences. The selection of $\Omega$ and $\alpha$ is therefore a governance choice, not merely a mathematical convenience.

## 1.2 Preference is conditional on feasibility

After removing infeasible designs, multiple objectives may remain: cost, timeliness, energy use, maintenance burden, and operational flexibility. A normalized additive model is

$$U(x)=\sum_{j=1}^{k}w_j u_j(x),\qquad w_j\geq0,\quad \sum_j w_j=1.$$

The expression is meaningful only if scores represent a defensible utility or value scale, tradeoffs are acceptable, and the chosen criteria are not counted twice. For example, 'response time' and 'customer waiting-time satisfaction' might encode much the same underlying consequence. Weighted sums can be useful for transparent deliberation, but their decimals are not evidence of objective truth.

For a simple sensitivity calculation, suppose two **feasible** designs have normalized cost scores of 0.90 and 0.60, respectively, and reliability scores of 0.65 and 0.85. If $w$ is the cost weight, the preference difference is

$$U_A-U_B=0.30w-0.20(1-w)=0.50w-0.20.$$

The designs tie at $w=0.40$. A recommendation that ignores the threshold is concealing how dependent it is on stakeholder priorities. Present the threshold, not just the winning label.

## 1.3 Decision trees and the value of information

Consider a separate Northstar risk: a critical data-exchange component has prior probability 0.25 of failing its acceptance demonstration. A failure would cause a $2.4 million recovery cost. A mitigation costs $0.34 million and leaves a **residual unconditional failure probability of 0.04**. All money is in millions, and we deliberately ignore discounting in this one-period example.

Without mitigation, expected cost is $0.25(2.4)=0.600$. With mitigation it is $0.34+0.04(2.4)=0.436$. The lower expected-cost decision is to mitigate. This calculation is not a risk assessment by itself: tail consequences, non-financial harms, and the assumption of risk neutrality remain explicit conditions.

Now suppose a diagnostic test has sensitivity $\Pr(+\mid F)=0.85$ and specificity $\Pr(-\mid\neg F)=0.90$. Bayes' rule gives

$$\Pr(F\mid+)=\frac{0.85(0.25)}{0.85(0.25)+0.10(0.75)}=0.73913,$$

$$\Pr(F\mid-)=\frac{0.15(0.25)}{0.15(0.25)+0.90(0.75)}=0.05263.$$

The positive test occurs with probability 0.2875, the negative with probability 0.7125. Under the simplified treatment model, mitigation after a positive result costs 0.436; after a negative result, doing nothing costs $0.05263(2.4)=0.12632$. The expected post-test cost is approximately $0.2875(0.436)+0.7125(0.12632)=0.2154$ million. If the diagnostic costs $0.05$ million, test-first costs $0.2654$ million, saving about $0.1706$ million versus immediate mitigation. In a real program, mitigation efficacy may depend on underlying conditions and the test outcome; that assumption must be modeled rather than silently inherited.

The *expected value of sample information* is the decrease in optimized expected loss **before paying the test cost**. Information has no value merely because it reduces uncertainty. It matters only if it can change an action or its expected consequences.

## 1.4 Robust decisions are not the same as conservative guesses

A minimax decision minimizes the maximum loss over allowed scenarios. Minimax regret minimizes the largest difference between a selected alternative and the best alternative one would have chosen with hindsight in each scenario. Neither is universally preferred. Minimax is driven by the absolute worst modeled case; regret compares opportunity loss. Both depend on credible scenario boundaries.

A design review should present a decision table that separates: (i) hard constraints, (ii) nominal expected performance, (iii) sensitivity to weights, (iv) sensitivity to probability assumptions, (v) consequences that are not commensurable in dollars, and (vi) what additional experiment could change the recommendation. Trace each input to an evidence source and configuration revision. When no concept is feasible, the correct output is 'redesign or renegotiate requirements,' not 'select the least infeasible alternative.'

## 1.5 Failure modes and counterarguments

**False precision:** a utility score of 0.782 has no significance unless input uncertainty and elicitation reliability justify the reported digits. **Hidden dependencies:** wait time and missed-trip consequences may be correlated; treating them as separate independent criteria can double count. **Convenient priors:** the prior failure probability can dominate Bayes' result. **Unmodeled tail losses:** a small expected dollar cost can coexist with unacceptable safety exposure. **Moving assumptions:** the diagnostic only has value if the decision can wait and its results remain relevant to the build configuration.

To defend an architecture choice, write an argument that could be overturned by evidence. Specify the hard constraint, the relevant uncertainty, a weight or probability threshold, and the experiment whose result would cross that threshold. This is the difference between a polished ranking and an engineering decision.

## Worked problems with explained solutions

**Problem A.** The compact concept passes every economic objective but delivers only 98 of 105 required peak trips. Can a favorable weighted utility score authorize release? **Solution:** No. The acceptance requirement is a hard feasibility condition unless authorized governance changes it. Compare feasible designs or reopen the capacity requirement with stakeholders.

**Problem B.** Using $U_A-U_B=0.50w-0.20$, decide for $w=0.25$ and $w=0.60$. **Solution:** At 0.25 the difference is $-0.075$ (B preferred); at 0.60 the difference is $+0.10$ (A preferred). The threshold is 0.40.

**Problem C.** What is the expected net benefit of a $0.05-million diagnostic in the example? **Solution:** About $0.436-(0.2154+0.05)=0.1706$ million. This is conditional on the stated test properties and mitigation model.

**Problem D.** A new integration experiment narrows the 90th-percentile wait for design R to 14–19 minutes across plausible weather conditions. Is robust feasibility demonstrated? **Solution:** No. A 16-minute upper limit is exceeded in some modeled conditions. Review whether the uncertainty set is credible and whether operational restrictions or redesign can close the gap.

## Independent research question

Write a two-page position defending either robust constraints, chance constraints, or explicit scenario-based decisions for emergency mobility dispatch. Compare how each treats rare events, stakeholder risk tolerance, uncertain probability estimates, and the temptation to hide requirements behind preferences.

**Practice:** [Concept selection laboratory](../labs/01-decisions.html) · [Python model](../code/graduate_models.py) · [Executable notebook](../notebooks/01-decisions.ipynb).

## 1.6 Sensitivity surfaces rather than single-point answers

The one-variable threshold $w=0.40$ is only a section of a larger decision surface. If reliability scores themselves are uncertain, write $u_{R,A}=0.65+\epsilon_A$ and $u_{R,B}=0.85+\epsilon_B$. Then the difference becomes $0.50w-0.20+(1-w)(\epsilon_A-\epsilon_B)$. A low cost weight may not protect B from reversal if the reliability performance estimate is biased. A practical sensitivity analysis evaluates combinations of weight, performance, and scenario parameters, then reports the region of the assumption space in which a recommendation remains unchanged. This is more informative than a tornado chart with every parameter varied separately while all others are frozen.

Dependence between uncertain inputs is also consequential. Demand intensity and vehicle charging delay both increase during severe weather. Sampling them independently creates scenarios that may be unrealistic and can understate simultaneous stress. A scenario-based sensitivity matrix should therefore include coherent correlated conditions. When probabilities are not credible, stress-test named scenarios without assigning false precision to their likelihood.

## 1.7 An engineering review protocol

A reviewer should ask who defines the constraints, whether any are really objectives disguised as mandatory requirements, what evidence establishes feasibility, and which stakeholder bears the consequences if the model is wrong. The decision author should maintain an explicit assumption ledger: *assumption*, *why adopted*, *effect if false*, *evidence required*, and *owner*. The final recommendation should distinguish what has been **measured**, **predicted**, **elicited**, and **assumed**. These verbs are not interchangeable.

For a reversible pilot, the expected value of learning may justify a temporary less-efficient configuration. For an irreversible acquisition, uncertain long-term capacity requirements may justify modular options or deferring a component commitment. This is a real-options idea: flexibility has value because later information may make different actions optimal. But not every delay is rational. Delay can incur cost, miss a mission window, or eliminate procurement capacity. The choice itself needs a decision tree.

<!-- STEP04-CONNECTED-EVIDENCE-START -->
## Step 04 integrated case — NS-CE4.1: a feasible design is not an approved design

The six connected chapters use the **same controlled synthetic emergency-dispatch baseline**, revision 2.1. Inputs live in [the editable case JSON](../data/ns-evidence4-case.json); results are regenerated by [the Python analysis](../code/ns_evidence_case.py) and preserved in [the output record](../outputs/ns-evidence4-results.json). These datasets are teaching assumptions, not recovered field measurements. The scenario is related to the Northstar mobility curriculum but is not a continuation of a qualified vehicle or service baseline.

### Deriving a two-scenario feasibility decision

The authority's *illustrative* hard constraints are capital cost no greater than $7.8 million, capacity of at least 105 peak trips, and a 90th-percentile wait no greater than 16 minutes, each evaluated in **both** the nominal and storm scenarios. For design $x$, define

$$F(x)=I[c_x\le 7.8]\prod_{s\in\{N,S\}} I[q_{xs}\ge105]I[w_{xs}\le16],$$

where $c_x$ is capital cost in millions of dollars, $q_{xs}$ is trips per peak period, $w_{xs}$ is the modeled p90 wait in minutes, and $I[\cdot]$ equals 1 when its condition holds and 0 otherwise. This is a finite-scenario screen, not proof for every physical weather or demand state.

| Concept | Cost, $M | Nominal trips / wait | Storm trips / wait | Two-scenario screen |
|---|---:|---|---|---|
| Compact | 6.30 | 98 / 18 min | 90 / 23 min | Fail |
| Regional | 7.00 | 112 / 14 min | 100 / 20 min | Fail |
| Resilient | 7.65 | 110 / 15 min | 107 / 16 min | Pass |

For the regional concept, the nominal screen is true but storm capacity is short by $105-100=5$ trips and storm p90 wait is over by $20-16=4$ minutes. The resilient concept satisfies the exact stated inequalities in both modeled conditions. Its storm capacity **margin is two trips** ($107-105=2$), and its wait margin is **zero minutes**. An unquantified extra delay invalidates that screen. No claim about statistical uncertainty follows from a deterministic inequality.

### Keep decision preference downstream of evidence quality

A weighted utility ranking over the three concepts would be invalid as a final recommendation if it allowed cost savings to compensate for unmet mandatory capacity or accessibility. The proper sequence is to identify the authoritatively approved feasible set, analyze uncertainty, then apply a justified preference model within that set. If the storm scenario is missing an extreme flood-and-grid disruption, $F(x)=1$ does not imply robust feasibility for a larger set $\Omega'$. Similarly, an interface contract at revision 2.0 cannot automatically support release 2.1 simply because vehicle performance is unchanged.

Consider two follow-up options: **Option A**, invest in a storm-specific capacity trial, and **Option B**, invest in interface repair and full-population accessibility evidence. The case's current screen already favors resilient on modeled physical performance; Option A cannot by itself resolve the separately observed interface and verification defects. The rational experiment is one that is expected to change a *blocked decision*: repair the interface semantics, then test accessibility outcomes and evidence lineage under the current build. The expected value of information is zero if the information cannot change an authorized choice, even if it improves a model score.

### Sensitivity and limits

Relaxing the storm capacity requirement from 105 to 100 and storm wait limit from 16 to 20 would admit the regional concept, but those are **policy changes** requiring explicit authorization. Increasing the storm wait for resilient from 16.0 to 16.1 minutes makes the stated screen fail without any change to capex. The sharp discontinuity illustrates why rounding, measurement resolution, and guard bands need to be fixed before a review, not optimized after seeing the results. A probability-weighted feasibility calculation would also require genuine scenario probability evidence, not invented weights.

**Worked exercise 1 — margin.** A reviewer claims the resilient concept has 'ample weather robustness.' Compute the storm margins. **Solution:** capacity margin = $107-105=2$ trips; p90 wait margin = $16-16=0$ minutes. The claim of ample robustness is unsupported. A measurement uncertainty interval extending above 16 would require a guarded acceptance rule or another experiment.

**Worked exercise 2 — infeasible trade.** An analyst gives the regional concept a higher utility than resilient because it costs $0.65 million less. Should it replace resilient? **Solution:** Not under the stated hard constraints: regional fails storm capacity and wait. A re-negotiation of mission requirements is a governance decision, not a hidden weight adjustment.

**Adverse case.** Change `storm_p90_wait_minutes` for resilient to 16.1 and rerun the checker. It must change its two-scenario screen to false. Restore the baseline before committing outputs. The chapter's result is a *conditional architecture screen*, not a vehicle qualification, an approved procurement choice, or a verified accessibility assurance claim.
<!-- STEP04-CONNECTED-EVIDENCE-END -->
