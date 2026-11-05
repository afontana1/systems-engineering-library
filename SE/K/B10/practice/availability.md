# Workshop 8 · Why redundancy does not erase common-cause risk

*Companion to Book X, Chapter 8 · Reliability, availability and maintenance*

## An attractive availability estimate

The Northstar dispatch platform has two nominally redundant servers. Each server has a mean uptime of 200 hours and a mean repair time of 5 hours. In a simplified alternating up/down model, its steady-state availability is

\[
A=\frac{MTTF}{MTTF+MTTR}=\frac{200}{205}\approx0.97561.
\]

If server outages are independent and either server can provide the necessary service, the nominal parallel availability is

\[
A_{\mathrm{ind}}=1-(1-A)^2\approx0.999405.
\]

That looks excellent. It is also conditional on independence, perfect failover, adequate capacity, shared-network availability and the definition of “service available.” A design can have two independent servers powered by one failing facility or routed through one identity provider. Those dependencies invalidate the naive independence argument.

## Introduce common-cause outage

Assume a common-cause event makes both servers unavailable with probability \(q\) at a randomly sampled instant; conditional on no common-cause event, component outages remain independent. Under **that explicit stylized model**, system availability becomes

\[
A_{\mathrm{sys}}=(1-q)\bigl[1-(1-A)^2\bigr].
\]

At \(q=0.008\), \(A_{\mathrm{sys}}\approx0.99141\). This is below a fictional requirement of 0.995. A mere **0.8% probability of shared outage** overwhelms much of the apparent benefit of dual servers. If a mitigation reduces \(q\) to 0.002 without changing the conditional component assumptions, availability rises to approximately 0.99741 and the numerical gate passes.

The improvement is meaningful only if the reduction in common-cause probability is supported by engineering evidence. Examples might include independent power feeds, separate networks, resilient identity infrastructure, controlled updates, and verified fault isolation. A parameter reduction written into a spreadsheet is not a mitigation.

## Steady state is not mission reliability

Steady-state availability is the fraction of time a service is up under a long-run stochastic model. Reliability is the probability a required function survives a defined interval without failure. Maintainability is the ability to restore function under specified conditions and resources. The ratios and models differ. A fleet can have high annual availability yet experience an unacceptable 30-minute interruption during an emergency event. Mission windows and consequence therefore belong in the acceptance claim.

Redundancy also incurs operational dependencies: replication lag, duplicate actions, quorum behavior, failover time, degraded capacity and synchronized software defects. Fault injection and restoration testing are needed to demonstrate that redundant components actually implement the assumed fault-tolerance behavior.

## Worked problems

**Problem 1.** Compute single-server availability using the given means.

<details><summary>Worked solution 1</summary>

\(200/(200+5)=0.975609756\), or about 97.56% under the alternating renewal assumptions.
</details>

**Problem 2.** Compute parallel availability assuming independence.

<details><summary>Worked solution 2</summary>

\(1-(5/205)^2\approx0.999405\), or about 99.9405%. The conditional assumption is essential.
</details>

**Problem 3.** Compute common-cause-adjusted availability when \(q=0.008\).

<details><summary>Worked solution 3</summary>

\(0.992[1-(5/205)^2]\approx0.991410\). This is below 0.995, so the modeled architecture fails the gate even though the independence-only model passes.
</details>

**Problem 4.** Why might moving one server to a second building not reduce a shared-outage probability sufficiently?

<details><summary>Worked solution 4</summary>

The two buildings might retain shared identity services, network routing, software releases, operations staff, geographical hazards or external dependencies. Common-cause mitigation requires a dependency model and evidence, not merely physical separation.
</details>

## Transfer to engineering work

Run the availability tool at several common-cause probabilities and repair times. Produce a dependency diagram identifying at least five sources of shared failure, a sensitivity table and an evidence plan for validating a proposed mitigation. Revisit Book X Chapter 8's reliability discussion and distinguish demonstrated availability from model-predicted availability.
