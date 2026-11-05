# L06 · Simulation, sensitivity, and what statistics cannot prove

**Learning time:** 5–8 hours. **Gate:** Model credibility review. **Prior reading:** [F08](../../flagships/F08-simulation-uncertainty.md) and [F03](../../flagships/F03-statistical-assurance.md).

## A deterministic fixture is not a population

The reference fixture has 12 equally spaced arrivals and a chosen 12-minute trip duration. It is excellent for regression testing but poor as a representation of real demand. The lab's [simulation function](../src/northstar.py) generates independent synthetic interarrival gaps from an exponential distribution with mean 4 minutes, then repeats the scenario with a fixed seed. This is not field calibration: the assumed exponential law, lack of geographic correlations, and no boarding dynamics mean the results support **model sensitivity analysis only**.

The stochastic output records the mean served fraction over 200 independent replications, a rough normal interval for the **Monte Carlo estimated mean**, and the proportion of runs that satisfy the same synthetic demonstration targets. A Monte Carlo interval quantifies replication noise *conditional on the model*, not error in model structure or input assumptions. A low fraction of replications meeting targets is a warning that the fixed fixture is optimistic relative to this chosen stress model; it is not a measured probability of operational failure.

## Derivation: confidence interval of a replication mean

Let `X_i` be the fraction of requests completed within scenario replication `i`, for `i = 1..n`. Estimate `x̄ = ΣX_i/n` and sample standard deviation `s = sqrt(Σ(X_i−x̄)^2/(n−1))`. Under approximate normality of the sample mean and independence of replications, a rough two-sided 95% interval is `x̄ ± 1.96 s/√n`. The population here is the *constructed simulation distribution*, not real regional service days. A 95% interval means the procedure has a long-run coverage property under those assumptions; it does not mean there is a 95% probability that a fixed unknown truth lies in this observed numerical interval.

**Example:** with 200 independent replications and sample `s ≈ 0.097`, the half-width is roughly `1.96 × 0.097 / √200 ≈ 0.0134`. More replications can tighten Monte Carlo precision but cannot repair unobserved real boarding delays or correlated fleet failures.

## Credibility ladder

Verification asks whether the code correctly implements its stated algorithm. Validation asks whether the model represents its intended use sufficiently well. Accreditation or acceptance for a decision is a contextual judgment by responsible stakeholders, based on consequences, evidence, residual uncertainty, and governance. A code unit test does not establish the latter two. The experiment plan captures unanswered questions and plausible factors to vary.

## Engineering activity

1. Run the simulation with means 3, 4 and 6 minutes and service times 10, 12 and 15. Produce a sensitivity table with seed, sample count, conditional model, response, and comparison.
2. Re-run a scenario with seeds 7 and 8; explain why numerical differences are legitimate and why uncontrolled random seeds hinder reproducibility.
3. Increase replications from 200 to 800. Confirm that the interval half-width generally shrinks at about `1/√n` even if the outcome remains poor.
4. Propose how you would validate arrival distributions, service duration, and accessibility needs in a real-world study, including consent and privacy safeguards.

## Knowledge check and explained answer

**Question.** Can 10,000 synthetic replications prove that the real system meets a 95% completion goal?

<details><summary>Show explanation</summary>

No. Larger `n` reduces Monte Carlo estimation error for the specified simulation, but not structural/model-form error, sampling bias, unknown real-world correlations, or mismatch between simulation assumptions and the deployed environment. Validation evidence must come from outside the simulation itself.

</details>

**Gate evidence:** reproducible experiment table, at least one confidence-interval calculation, sensitivity analysis, and an explicit credibility assessment.
