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
