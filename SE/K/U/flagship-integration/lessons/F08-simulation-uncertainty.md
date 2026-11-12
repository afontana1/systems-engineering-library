### F08 extension · Paired experiments and the boundary of a confidence interval

**Experiment purpose.** A synthetic paired wait-time experiment asks whether a proposed service improvement changes *simulated* mean wait under shared scenario seeds. Twelve baseline and integrated observations are paired by experimental condition, producing differences $D_i=W_{baseline,i}-W_{integrated,i}$. Using common random numbers reduces variance when the two outputs are positively correlated; it does not remove model bias.

**Compute the interval.** The twelve differences are $[5,7,6,7,4,7,5,8,7,5,7,6]$ minutes. Their mean is $\bar D=6.1667$ minutes and their estimated standard error is 0.34451 minutes. Assuming independent *pairs*, a sufficiently defensible near-normal difference distribution, and a predeclared comparison, a two-sided 95% Student interval with $t_{11,0.975}\approx2.201$ is $6.1667\pm2.201(0.34451)=[5.4084,6.9249]$ minutes. The interval measures sampling uncertainty **inside this synthetic setup**, not a real-world causal effect or a verified requirement.

**Threats to credibility.** Independence is across pairs, not within each pair; correlated shifts or reused events across pairs would invalidate the standard error. Adaptive tuning on the same twelve cases creates selection bias. If demand distributions, road closures, vehicle behavior, or accessibility rules are wrong, a narrow Monte Carlo interval is false reassurance. Partition *aleatory* arrival variability, *epistemic* capacity and behavior assumptions, and *numerical* integration or event-order errors.

**A second quantitative failure.** The integrated policy meets the normal-scenario timely screen at about 99.35% but fails the other three required stress cases. Its scenario-weight coverage is 45%, well below the illustrative 95% requirement. An excellent paired estimate of one performance measure does not establish robust adequacy.

**Worked exercise and solution.** If every paired difference were doubled (with the same paired pattern), the mean and standard error would both double, giving a new interval approximately [10.8168,13.8499] minutes. The t-statistic would remain unchanged because both numerator and denominator scale; this demonstrates why statistical significance alone is not the same as engineering value, fairness, or validity.

**Reproduce:** [paired results](../flagship-integration/outputs/ns-u4.1-results.json), [D04](../derivations/04-binomial-confidence-and-test-coverage.md), [D05](../derivations/05-factorial-interaction.md).
