# Measurement, estimation and statistical evidence

*Textbook-depth conceptual sequence · EN.645.756 / EN.645.769 / EN.645.632 · Northstar engineering case*

**Prerequisites:** basic algebra, unit discipline, structured requirements and probability as appropriate. **Related books:** [Book 8](../../B8/OPEN-BOOK.html), [Book 10](../../B10/OPEN-BOOK.html), [Book 9](../../B9/OPEN-BOOK.html).

> **Learning outcome:** derive the central method, state its assumptions, evaluate a worked engineering claim, and explain where the conclusion would fail.

## Start with a claim, not a formula

Suppose Northstar claims that average emergency-trip wait is below 12 minutes. The phrase is ambiguous. Does waiting begin when a phone application submits a request, when a dispatcher accepts it, or when a vehicle is assigned? Are rejected requests assigned infinite wait, excluded, or reported separately? Is the claim about peak periods, all hours, or a particular deployment configuration? Statistical inference begins with a precisely defined **estimand**: the population quantity that a decision needs. Only after defining it should you choose a sampling plan and confidence method.

Distinguish measurement validity (does the sensor or log represent the intended quantity?) from measurement precision (does repeated measurement agree?). A timestamp can be recorded with millisecond precision but be systematically late because different devices use unsynchronized clocks. Increasing numerical resolution does nothing for that bias. An engineering measurement plan should identify the measured object, units, calibration or synchronization method, missingness policy, environmental conditions, and chain of custody.

## Sampling distributions and intervals

Let \(X_1,\ldots,X_n\) represent independent observations from an approximately stable population with finite variance. The sample mean is \(\bar X=\frac1n\sum X_i\); the standard error is approximately \(s/\sqrt n\). Under normal data or suitable large-sample conditions, a two-sided interval for the population mean takes the form \(\bar X\pm t_{n-1,1-\alpha/2}s/\sqrt n\). The numerical endpoints depend on the sampling design and model. This construction is not a guarantee that an arbitrary realized interval contains the true mean with 95% posterior probability; under repeated eligible sampling it has nominal 95% coverage.

If 25 independent trips have mean wait 10.2 minutes and sample standard deviation 4 minutes, then \(SE=4/\sqrt{25}=0.8\) minute. With \(t_{24,0.975}\approx2.064\), the two-sided 95% interval is approximately \([8.55,11.85]\). Because the upper endpoint is below 12, the data support the mean-threshold claim under the method's assumptions. But they do **not** establish that 95% of passengers wait less than 12 minutes. An interval for a mean is not a percentile or a population tolerance interval.

When the data are serially dependent—such as individual requests during the same congestion burst—\(s/\sqrt n\) may seriously understate uncertainty. The independent unit might be the day or a replicated demand stream, not the individual passenger. Use cluster-level analysis, time-series methods, or batch means when their assumptions fit the design.

## Failure probabilities and zero-event campaigns

A common verification trap occurs when no failures are observed. If \(n\) independent Bernoulli trials have unknown fixed failure probability \(p\), and all n succeed, then \(P(0\text{ failures}\mid p)=(1-p)^n\). A one-sided upper confidence bound at confidence \(1-\alpha\) solves \((1-p_U)^n=\alpha\), yielding \(p_U=1-\alpha^{1/n}\). At \(n=30,\alpha=0.05\), \(p_U\approx0.0950\). Thirty successes do not establish that failure probability is below one percent. To get the one-sided bound below 0.01 under these assumptions requires at least \(n=\lceil\log(0.05)/\log(0.99)\rceil=299\) independent failure-free trials.

This is not an argument to run 299 copies of the same easy test. Identical trials in an unrealistically friendly environment can provide a narrow mathematical bound that is irrelevant to actual operational modes. Environmental representativeness, configuration control, measurement quality, and failure definitions are part of the assurance case.

## Experimental unit, randomization and missing data

The experimental unit is the smallest unit independently allocated to a treatment or condition. If five buses use the same routing algorithm for one week, logging thousands of trips does not create thousands of independently assigned buses. Treating correlated trips as independent is pseudoreplication. A defensible study distinguishes assignment units, observation units, and analysis units. Randomization reduces systematic treatment confounding when implemented as designed; it does not guarantee balance in small samples or protect against post-assignment attrition.

Missing requests pose a particularly serious problem. Suppose a communications failure prevents the system from logging requests that never reach a server. An analysis of only logged requests will systematically overstate service performance. You need an external observation method, audit trail, or sensitivity bounds for the unobserved cases. Missing data are not merely a software inconvenience but a source of selection bias.

## Comparing two configurations

When evaluating a software revision, expose both configurations to **paired** synthetic demand seeds. Let \(D_i=W_{A,i}-W_{B,i}\) be a performance difference for the same demand stream. Then \(\bar D\) estimates the mean difference and the confidence interval should use the standard deviation of the paired differences. This usually reduces noise from demand variation and offers a more direct estimate of the engineering change's effect than comparing two unrelated batches. Pairing should not conceal structural asymmetry: both configurations must be evaluated over the intended conditions, and the seeds must represent the intended scenario distribution.

For operational decision-making, distinguish a superiority question (is the new system better?), an equivalence question (are differences acceptably small?), and a noninferiority question (is degradation smaller than a predeclared margin?). Failing to reject a difference does not establish equivalence. The engineering acceptance margin must come from stakeholder and mission consequences, not a convenient p-value.


## Further depth: confidence, tolerance and acceptance are different questions

A one-sided upper confidence bound for the mean can support \(\mu<12\). It cannot certify a requirement such as "99% of trips under 12 minutes," which concerns \(P(W\le12)\). Even a sample quantile needs uncertainty about the tail probability. A distribution-free nonparametric approach uses order statistics and binomial arguments to support a population coverage claim, but the sample size required for extreme coverage and high confidence can be substantial. For a clean threshold property, counting violations is often preferable to pretending a normal waiting-time distribution is known.

A sample size should be driven by the decision's consequence and variability. If the goal is a desired mean margin \(m\), a rough normal-approximation planning equation is \(n\approx(z_{1-\alpha/2}\sigma/m)^2\) for independent observations and known approximate \(\sigma\). This is not a universally valid design formula: skewed tails, clustering, selection, or sequential looks require more care. In a paired experiment use the SD of the **paired difference** rather than the SD of either design in isolation.

A subtle issue arises with **optional stopping**. Analysts who examine each new batch and stop as soon as an ordinary 95% confidence interval excludes a threshold can inflate false-positive rates. Sequential designs, alpha spending, or anytime-valid procedures should be specified if repeated checking is anticipated. Likewise, trying many endpoints and reporting only the favorable one changes the inference problem. A valid claim includes the number of tested endpoints, chosen decision threshold, and how multiplicity was handled.

### Measurement audit exercise

Take a sample in which three requests are missing from server logs but appear in an independent passenger survey. Define two estimands: (i) logged-request response time; (ii) eligible-user timely service. Show precisely how each denominator changes, whether missingness is likely related to unsuccessful service, and what external instrumentation would distinguish communication loss from absence of demand. This exercise teaches that statistical procedure, telemetry design and system requirements form one inseparable assurance chain.

## Problems — attempt first

1. Compute the standard error and approximate 95% mean interval from \(n=25,\bar x=10.2,s=4\) using \(t=2.064\).
2. Calculate the one-sided 95% zero-failure upper bound for 100 independent trials.
3. A deployment reports 90th-percentile wait from completed trips only; 20% of requests are dropped. Explain the inferential defect.
4. Compare a claim about the **mean** wait to a claim that **at least 95%** of trips wait below the limit. Which estimands and methods are needed?

<details><summary>Worked answers and engineering interpretation</summary>

1. Standard error is 0.8 minutes, margin 1.6512, and interval about [8.55, 11.85] minutes.
2. \(1-0.05^{1/100}\approx0.02951\) or 2.95%, conditional on independent identical Bernoulli trials and adequate failure detection.
3. The statistic conditions on success; discarded requests might represent the worst failures. Report service fraction and a defensible treatment of incomplete requests, with a traceable denominator.
4. A mean claim uses inference about \(E[W]\). A 95%-below-limit claim concerns a population quantile or exceedance probability and needs methods appropriate to that quantity, not a confidence interval for the mean.
</details>

## Practice laboratory and further learning

[Open the lab for this chapter](../labs/02-estimation.html) · [Download editable Markdown lab](../labs/02-estimation.md) · [Open the associated notebook](../notebooks/02-estimation.ipynb) · [Download the calculation source](../code/engineering_math.py)

**Authoritative follow-up reading:** [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/), [NIST/SEMATECH Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook), and [Systems Engineering Body of Knowledge](https://www.incose.org/resources-publications/technical-publications/systems-engineering-body-of-knowledge/). These are independent references, not endorsements of the fictional cases.

[Return to the quantitative textbook collection](../INDEX.html)
