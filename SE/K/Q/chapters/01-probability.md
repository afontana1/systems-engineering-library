# Probability models and engineering uncertainty

*Textbook-depth conceptual sequence · EN.645.756 / EN.645.757 / EN.645.784 · Northstar engineering case*

**Prerequisites:** basic algebra, unit discipline, structured requirements and probability as appropriate. **Related books:** [Book 10](../../B10/OPEN-BOOK.html), [Book 11](../../B11/OPEN-BOOK.html), [Book 14](../../B14/OPEN-BOOK.html).

> **Learning outcome:** derive the central method, state its assumptions, evaluate a worked engineering claim, and explain where the conclusion would fail.

## The engineering problem: uncertainty is not one thing

Northstar's regional transport dispatcher must decide how many vehicles to stage during an emergency. A historical average of 12 requests per hour is not a complete description of demand: requests arrive in clusters, some records are missing, and service rates change with route closures. The model's first job is **not** to generate a random number. It is to identify which questions are uncertain and why. Random operational variation is *aleatory* uncertainty. Uncertainty about the value of a parameter, the completeness of observations, or the adequacy of a model is *epistemic*. More simulation replications reduce the Monte Carlo error in a conditional output estimate; they cannot prove that a misspecified demand model is valid.

Suppose the engineering decision is whether two vehicles can serve at least 90% of requested trips during a three-hour window. We must distinguish (a) the probability distribution of demand conditional on an assumed arrival model, (b) our uncertainty about that model's arrival rate, (c) capacity interruptions, and (d) a policy choice about whose requests are eligible. All four affect the claim, but not in the same way. Treating them all as one generic error bar conceals how to improve the decision.

## Random variables and the model contract

A random variable is a mapping from outcomes to numerical values; a distribution gives probabilities to sets of values. A probability model should specify the observation unit, population, time period, conditioning information, dependence assumptions, and measurement process. An expected value is a **weighted average over possible outcomes**, not a typical realized outcome. For discrete demand counts, \(E[N]=\sum_n nP(N=n)\); variance is \(E[(N-E[N])^2]\). The standard deviation is measured in the same units as the variable, but variance is in squared units.

A Poisson count model assumes a constant mean rate and independent increments across disjoint intervals. If requests arrive at rate \(\lambda\) per hour, the interval count has \(N(t)\sim\mathrm{Poisson}(\lambda t)\), with \(E[N(t)]=\mathrm{Var}[N(t)]=\lambda t\). It follows that the probability of zero arrivals in 15 minutes at a rate of 8 per hour is \(e^{-8(0.25)}=e^{-2}\approx0.1353\). This is a model-based conditional probability, not an empirical prediction guaranteed for every neighborhood. If observed demand variance substantially exceeds its mean, time-varying rates, clustered arrivals, or an alternative count model may be needed.

Another useful model is the exponential time to a memoryless event: \(P(T>t)=e^{-\lambda t}\). Its constant hazard assumption is convenient for certain electronic component failures but often unrealistic for mechanical wear-out, preventive maintenance, and weather-driven common-cause events. A reliability engineer chooses a distribution based on mechanisms, usage, and evidence—not mathematical convenience alone.

## Conditioning and dependence

A dispatcher might observe that 80% of all requests succeed and conclude that conditions are acceptable. But success rates could differ sharply by operating mode. Let \(O\) denote an outage and \(S\) denote service success. The law of total probability gives \(P(S)=P(S\mid O)P(O)+P(S\mid\neg O)P(\neg O)\). With outage probability 0.1, outage success 0.3, and normal success 0.9, total success is \(0.3(0.1)+0.9(0.9)=0.84\). Report both conditional rates: the aggregate hides the worst operating context.

Independence is a substantial engineering assumption. If two independent components each have availability 0.95, their parallel availability is \(1-(1-0.95)^2=0.9975\). This value would be optimistic if both depend on the same power supply, map service, or road. Dependence can be represented by explicit shared causes, conditional probabilities, correlated random inputs, or coupled mechanisms. A marginal failure probability by itself does not determine the probability of a joint failure.

## Parameter uncertainty and updating

If the unknown arrival rate is estimated from 120 requests observed over 10 hours, the simple point estimate is \(\hat\lambda=12\) per hour. A plug-in simulation fixes that value. A sensitivity analysis asks what happens when the rate is 10, 12, and 15. A Bayesian analysis instead models the uncertain rate itself, combines a prior with the likelihood of the observed counts, and propagates the resulting posterior uncertainty into the performance calculation. These are related but different operations. A prior cannot replace data; a likelihood cannot resolve an invalid observation process.

A Gamma prior \(\lambda\sim\mathrm{Gamma}(\alpha,\beta)\), using shape and **rate** parameters, is conjugate to a Poisson exposure model. Observing \(n\) arrivals during exposure \(T\) changes the posterior to \(\mathrm{Gamma}(\alpha+n,\beta+T)\). If \(\alpha=2,\beta=0.2,n=120,T=10\), the posterior mean is \(122/10.2\approx11.96\) per hour. Different prior scales or unrecorded outages can affect that inference; the model contract must state them.

## Worked engineering decision

Consider a two-hour stress scenario with arrival rates 10, 12, and 15 per hour, representing alternative plausible operating conditions. A simulation of 1,000 demand streams under each rate may estimate conditional service fractions of 0.97, 0.92, and 0.79. These three values are **synthetic teaching results**, not derived analytically here. The problem is not to average them without justification. What probability, if any, should be assigned to each scenario? Are rate changes correlated with road disruptions? Is the decision an expected-cost decision or a minimum-service guarantee? A robust decision may reject a design that performs well on average but violates a hard safety or access constraint in the high-demand mode.

To decide whether more data are useful, separate which uncertainty can be reduced by measuring arrivals, which requires observing outage behavior, and which concerns disputed objectives. Then design a collection plan that targets the decision-sensitive uncertainties.

## Diagnostic misconceptions

- **"Large simulation sample means certainty."** It reduces random simulation error conditional on the model. It does not repair structural or measurement bias.
- **"The mean is enough."** Two distributions with the same mean can have very different tails and capacity risks.
- **"Redundant means independent."** Shared infrastructure can defeat nominal redundancy.
- **"A point estimate is a fact."** It is an inference whose precision and bias depend on data quality and modeling assumptions.


## Further depth: compound uncertainty and correlated causes

A useful improvement over an independent Poisson rate is a **mixture model**. Suppose the rate depends on an unobserved operational regime \(Z\). Conditional on that regime, requests may be Poisson, but the unconditional count distribution is a mixture. By the law of total variance, \(\operatorname{Var}(N)=E[\operatorname{Var}(N\mid Z)]+\operatorname{Var}(E[N\mid Z])\). For a Poisson mixture, the first term equals the unconditional mean, while the second is nonnegative. Thus day-to-day shifts in demand regime naturally produce overdispersion. This mathematical decomposition shows why fitting one Poisson model to all observations may understate the probability of severe surges.

The same mechanism appears in failures: conditional independence given weather does not imply unconditional independence. Two vehicles may have independent mechanical failures on dry days but experience correlated immobilization during a flood. The probability of at least one operational vehicle is \(1-P(F_1\cap F_2)\), not automatically \(1-P(F_1)P(F_2)\). If a weather scenario causes both failures with probability 0.03, no independent component reliability calculation can ignore that common shock. In a fault tree, shared components should appear as shared basic events rather than copied independent nodes.

A sensitivity tornado chart is helpful only if parameter ranges are meaningful. The range for a well-measured service time should not be treated as equally credible as a speculative rare-outage probability. A stronger analysis classifies uncertainty as reducible with data, reducible with model improvement, or irreducible under the present physical process. The decision report should state which evidence would be sufficient to change a chosen architecture, and which uncertainties would remain afterward.

### Concept transfer

The same uncertainty taxonomy governs reliability prediction, cost estimating, mission simulations and digital twins. Before combining distributions from different disciplines, establish common units, time horizons and conditional contexts. A resource shortage that both lengthens trips and increases failures should be modeled as a shared driver, not as two independent adverse multipliers. The engineering artifact is a **dependency-aware uncertainty register** containing parameter, mechanism, evidence source, assigned model, confidence, and decision sensitivity.

## Problems — attempt before opening the answers

1. A Poisson model has 6 arrivals/hour. Calculate the probability of no arrival in 20 minutes. Interpret the statement carefully.
2. Two parallel independently failing devices each have availability 0.9. Compute combined availability. Give one practical shared-cause counterexample.
3. Outages occur 20% of the time; success is 40% in outage and 95% otherwise. Find the marginal success probability and explain why it is incomplete.
4. You record 48 requests in four hours. Describe one aleatory, one parameter, and one structural uncertainty that remains.

<details><summary>Worked answers and engineering interpretation</summary>

1. Exposure is \(6(1/3)=2\), so \(P(N=0)=e^{-2}\approx0.1353\). This answer is conditional on homogeneous Poisson arrivals over the selected interval.
2. \(1-0.1^2=0.99\). A single upstream communications network can disable both devices simultaneously.
3. \(0.2(0.4)+0.8(0.95)=0.84\). The conditional 40% success rate during outage may be unacceptable even when the marginal result appears favorable.
4. Arrivals may fluctuate daily (aleatory); the true mean arrival rate is estimated from limited observations (epistemic parameter); demand may vary by hour or weather so a homogeneous Poisson model may be unsuitable (structural).
</details>

## Practice laboratory and further learning

[Open the lab for this chapter](../labs/01-probability.html) · [Download editable Markdown lab](../labs/01-probability.md) · [Open the associated notebook](../notebooks/01-probability.ipynb) · [Download the calculation source](../code/engineering_math.py)

**Authoritative follow-up reading:** [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/), [NIST/SEMATECH Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook), and [Systems Engineering Body of Knowledge](https://www.incose.org/resources-publications/technical-publications/systems-engineering-body-of-knowledge/). These are independent references, not endorsements of the fictional cases.

[Return to the quantitative textbook collection](../INDEX.html)

<!-- STEP04-QUANTITATIVE-START -->
## Step 04 integrated case — NS-QSE4.1: uncertainty is conditional on a mechanism

The **Northstar Emergency Dispatch Quantitative Laboratory (NS-QSE4.1)** joins all eight advanced chapters. The controlled input is [`ns-qse4-case.json`](../data/ns-qse4-case.json), and the calculations are implemented in [`ns_qse_case.py`](../code/ns_qse_case.py). Every arrival count is invented for teaching, not collected from the Northstar program. Each count represents one hour; there are twelve *clear* and twelve *storm* windows. The scenarios are separated deliberately, because a single fitted hourly rate hides the change in operating regime.

### Derive the difference between a Poisson count and a Poisson mixture

The clear windows contain 120 requests over 12 hours; storm windows contain 216 requests over 12 hours. The conditional maximum-likelihood rates are therefore \(\widehat\lambda_c=10\) and \(\widehat\lambda_s=18\) requests/hour. Let \(Z\in\{c,s\}\) be the regime and let an illustrative mixture assign \(P(Z=c)=P(Z=s)=0.5\). For a one-hour count, \(N\mid Z=z\sim\operatorname{Poisson}(\lambda_z)\). Applying total expectation and variance gives

\[
E[N]=E[\lambda_Z],\qquad
\operatorname{Var}(N)=E[\lambda_Z]+\operatorname{Var}(\lambda_Z).
\]

Using the unregularized rates gives \(E[N]=14\) requests/hour and \(\operatorname{Var}(N)=14+\tfrac12(10-14)^2+\tfrac12(18-14)^2=30\) requests\(^2\) per one-hour observation. A single homogeneous Poisson model with mean 14 predicts variance 14 instead. This difference is **overdispersion caused by a changing latent regime**, not a proof that any one-hour record is independent or Poisson. The executable case instead uses posterior means of 10.000 and 17.869 requests/hour, giving a mixture variance of approximately **29.414**.

### Propagate parameter uncertainty without confusing it with demand variation

With a shape–rate Gamma prior \(\lambda\sim\operatorname{Gamma}(\alpha=2,\beta=0.2\ \mathrm h)\), and \(n\) Poisson requests during \(T\) hours, the likelihood contributes \(\lambda^n e^{-\lambda T}\). Multiplication by the prior density yields \(\lambda\mid n,T\sim\operatorname{Gamma}(2+n,0.2+T)\). Thus the clear posterior is Gamma(122,12.2 h), with mean **10.000/hour**; the storm posterior is Gamma(218,12.2 h), mean **17.869/hour**. The seeded Monte Carlo approximation gives central conditional 95% intervals of about **[8.32, 11.90]** and **[15.59, 20.25]** requests/hour, respectively. A posterior interval describes uncertain *parameters under a model and prior*; the future hourly count has additional aleatory dispersion.

A common-cause warning follows directly. Weather can both raise arrival counts and reduce road capacity. Sampling an increased arrival rate independently from a road-failure indicator would understate joint stress. The controlled **compound** scenario deliberately combines both: its demand count is the ceiling of 1.2 times each storm count and its per-request service duration is multiplied by 1.1. These factors are scenario assumptions, not fitted probabilities.

### Reproduce and challenge the claim

Run `python3 SE/K/Q/code/ns_qse_case.py` from the repository root. The JSON report contains `posterior`, `conditional_mixture`, and an input SHA-256. Modify a **copy** of the storm counts and repeat. Raising storm counts changes the posterior mean and the queue simulation; increasing Monte Carlo draws without changing the input cannot cure an incorrect observation process. Before interpreting any result, request arrival-time timestamps, missing-record counts, accessible-service classification, and weather-stratified evidence.

<details><summary>Worked exercises and interpretation</summary>

1. **Equal-weight mixture.** Replace the storm rate by 20/hour while keeping clear at 10/hour. Then \(E[N]=15\) and \(\operatorname{Var}(N)=15+25=40\). The variance-to-mean ratio rises to \(40/15\approx2.67\); assuming one Poisson process would suppress tail uncertainty.
2. **Unequal-weight mixture.** If clear has weight 0.8 and storm weight 0.2, \(E[N]=0.8(10)+0.2(18)=11.6\); \(\operatorname{Var}(\lambda_Z)=0.8(10-11.6)^2+0.2(18-11.6)^2=10.24\), so count variance is 21.84. These weights are a thought experiment, not measured exposure frequencies.
3. **Adverse case.** Why is a 95% Gamma credible interval not a 95% guarantee that next-hour demand will be within it? It describes the uncertain Poisson *rate*, whereas the future realized *count* is random even at a fixed rate.

</details>

**Transfer:** This same decomposition applies to Book 10 metrics, Book 11 simulation, and Book 18 interdependent constituent demand. It does not authorize extrapolation to real emergencies.
<!-- STEP04-QUANTITATIVE-END -->
