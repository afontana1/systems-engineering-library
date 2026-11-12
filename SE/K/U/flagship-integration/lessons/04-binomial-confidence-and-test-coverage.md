### D04 extension · Wilson bound and the acceptance fallacy

For $k=72,n=80$, $\hat p=.9$ and $z=1.96$, define $d=1+z^2/n$; then the two-sided Wilson lower endpoint is

$$L=\frac{\hat p+z^2/(2n)-z\sqrt{\hat p(1-\hat p)/n+z^2/(4n^2)}}{d}.$$

Computing this gives about 0.8149 (exact digits depend on rounding). Thus a 90% **sample** success rate does not demonstrate that a population success probability is at least 90% with this confidence procedure. Under conservative timing, the point estimate is only 67/80=.8375, and accessible performance is 10/16=.625. The formula requires independent representative Bernoulli trials; correlated failures reduce effective information.

**Exercise and solution.** If 0 failures occur in 20 independent tests, the one-sided 95% upper failure-probability bound is $1-.05^{1/20}\approx0.1391$; zero observed failures is not proof of zero true risk. [Acceptance fixture](../flagship-integration/data/ns-u4.1-case.json).
