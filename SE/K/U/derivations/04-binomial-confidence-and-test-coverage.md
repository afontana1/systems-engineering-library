# D04 · Confidence bounds, zero failures and the coverage trap

**Skill:** Calculate a legitimate statistical bound while refusing to extrapolate beyond the test population.

## Derive the zero-failure bound

Suppose `n` independent tests have a common but unknown failure probability `p`. The probability of observing zero failures is `(1−p)^n`. For a one-sided 95% frequentist upper confidence bound `p_U`, solve:

`(1−p_U)^n = 0.05`, so `p_U = 1−0.05^(1/n)`.

For `n=300`, `p_U≈0.009936` (about 0.994%). The familiar rule of three approximates this by `3/n=0.01` for moderately large n. This is a **coverage statement about a procedure**, not a 95% posterior probability that p lies below the bound.

## Why sample design matters

A 300-run campaign at one fixed speed on a dry track is not 300 independent and representative trials of every possible route, weather and traffic condition. Defect mechanisms can be dependent; a single untested scenario can dominate operational risk. A valid statistical model demands a clearly defined population, sampling process and exchangeability/independence assumptions.

For a practical acceptance claim, define the operating domain, the failure mode being counted, censored runs, and whether a “trial” has equal exposure time. Tests with varying durations may require a time-to-event or reliability model rather than a single Bernoulli p.

## Measurement uncertainty

If timing is measured using two clocks whose errors each may reach ±0.3 s, a 0.2 s compliance margin is not supported without clock synchronization or an uncertainty model. Independent random error may combine by root-sum-square under suitable assumptions, but hard interval bounds should be combined conservatively when no probabilistic model is justified.

## Sample-size inversion

Suppose a design goal is to demonstrate an upper one-sided failure-probability bound below 0.1% with zero failures. Rearranging gives `n ≥ ln(0.05)/ln(0.999)≈2994.2`, requiring at least **2995** independent identical trials. Even that number proves nothing about untested operational modes or dependent failures.

## Practice

**Question:** A team logs zero failures from 300 simulations and calls the design “99.9% reliable in service.” Identify two mistakes.

<details><summary>Solution</summary>

First, the one-sided 95% upper bound on failure probability is about 0.994%, not 0.1%, under the Bernoulli assumptions. Second, simulator runs and real operating events may not have representative, independent failure behavior; model credibility and coverage are separate obligations.

</details>

**Transfer artifact:** A trial definition, exposure record, exact bound, applicability envelope, and list of uncovered failure modes. See [verification and validation](../../encyclopedia/v-and-v.md).

<!-- STEP04-FLAGSHIP-U1-START -->
### D04 extension · Wilson bound and the acceptance fallacy

For $k=72,n=80$, $\hat p=.9$ and $z=1.96$, define $d=1+z^2/n$; then the two-sided Wilson lower endpoint is

$$L=\frac{\hat p+z^2/(2n)-z\sqrt{\hat p(1-\hat p)/n+z^2/(4n^2)}}{d}.$$

Computing this gives about 0.8149 (exact digits depend on rounding). Thus a 90% **sample** success rate does not demonstrate that a population success probability is at least 90% with this confidence procedure. Under conservative timing, the point estimate is only 67/80=.8375, and accessible performance is 10/16=.625. The formula requires independent representative Bernoulli trials; correlated failures reduce effective information.

**Exercise and solution.** If 0 failures occur in 20 independent tests, the one-sided 95% upper failure-probability bound is $1-.05^{1/20}\approx0.1391$; zero observed failures is not proof of zero true risk. [Acceptance fixture](../flagship-integration/data/ns-u4.1-case.json).
<!-- STEP04-FLAGSHIP-U1-END -->
