# Experimental design, interactions and causal interpretation

*Textbook-depth conceptual sequence · EN.645.756 / EN.645.784 / EN.645.783 · Northstar engineering case*

**Prerequisites:** basic algebra, unit discipline, structured requirements and probability as appropriate. **Related books:** [Book 10](../../B10/OPEN-BOOK.html), [Book 14](../../B14/OPEN-BOOK.html), [Book 17](../../B17/OPEN-BOOK.html).

> **Learning outcome:** derive the central method, state its assumptions, evaluate a worked engineering claim, and explain where the conclusion would fail.

## What an experiment can—and cannot—identify

Northstar wants to know whether increasing fleet size or improving dispatch software reduces waiting time more effectively. Merely comparing historical performance before and after a software release is weak evidence: weather, demand mix, road closures, and staffing may have changed simultaneously. Controlled experiments attempt to isolate the effect of an intervention by structuring how conditions are assigned and compared. But design quality does not follow from a sophisticated regression equation; it follows from the data-generating process.

An experiment needs a response variable with a decision-relevant definition, factors that the experimenter can deliberately manipulate, nuisance variables that influence the response, experimental units, and a plan for randomization, replication and blocking. A simulation experiment must also identify its stochastic seed allocation and transient/warm-up handling. An actual field experiment adds ethical and operational constraints that may prevent random assignment.

## The smallest useful factorial design

Take two factors: fleet size A (two or three vehicles), and algorithm B (old or revised). Code the low and high levels as \(-1,+1\). Suppose the simulated mean waits (minutes) are:

| | Old B− | Revised B+ |
|---|---:|---:|
| Two vehicles A− | 18 | 14 |
| Three vehicles A+ | 12 | 7 |

The main effect of A is the high-A mean minus the low-A mean: \(((12+7)-(18+14))/2=-6.5\) minutes. The main effect of B is \(((14+7)-(18+12))/2=-4.5\) minutes. The interaction contrast is \(y_{++}-y_{+-}-y_{-+}+y_{--}=7-12-14+18=-1\). In the coded regression \(y=\beta_0+\beta_A A+\beta_B B+\beta_{AB}AB\), the interaction coefficient is this contrast divided by four: \(-0.25\). The **interaction effect** convention based on difference-of-differences is \(-1\) minute; stating which convention is used avoids a common factor-of-two or factor-of-four error.

The interaction means software benefit differs by fleet size: it cuts 4 minutes with two vehicles, but 5 with three. This illustrative interaction is small relative to the main effects. In a real experiment, whether it is distinguishable from noise requires replicated observations, error estimates, and diagnostics. A table of cell means alone gives no uncertainty interval.

## Why one factor at a time is usually inadequate

One-factor-at-a-time experimentation changes A while B stays fixed, then B while A stays fixed. That may miss interactions and fail to find a joint optimum. A full factorial design tests combinations so interactions can be estimated. With \(k\) two-level factors, a full factorial uses \(2^k\) settings before replication. This can become expensive, motivating fractional factorial screening designs. But fractional factorials intentionally confound some effects. The alias structure must be understood before declaring a variable harmless. Large main effects may also conceal curvature; adding center points or response-surface designs can test whether a linear approximation suffices.

Blocking handles known nuisance variation. If response depends strongly on the day, assign configurations within comparable day blocks or use identical demand seeds for paired simulator comparisons. Randomize execution order when practical to avoid conflating treatment with drift, machine load, or analyst choices. Replication means repeating a design point with independently generated noise—not rerunning exactly the same deterministic code with the same seed.

## Model specification and residual diagnosis

A fitted regression is a model of conditional average response, not a proof of causal effect. Examine residual structure, nonlinear response, heteroscedasticity, influential observations, and dependency between experimental runs. For a response like waiting time, raw normal-error assumptions may fail because times are nonnegative and right-skewed. Consider transformed responses, generalized models, or nonparametric/bootstrapped comparisons when justified by the design.

Distinguish **statistical significance** from engineering significance. A change that saves 0.1 minute may be detectable with many replications yet irrelevant to an emergency-access objective. Conversely, a potentially important six-minute reduction may have a wide uncertainty interval in a small pilot. Set practical acceptance thresholds in advance, then use uncertainty and cost to decide what additional evidence is necessary.

## Causality under operational constraints

A field deployment may have only one region, no randomization, and policy changes at the same time. Difference-in-differences can help under a credible parallel-trends assumption, but cannot automatically make confounded data causal. Interrupted time-series analyses need a model for seasonality and autocorrelation. Synthetic control methods need a plausible donor pool. Qualitative process tracing and negative controls can reveal alternative mechanisms. An engineer should document which claims are identified by design, which depend on untestable assumptions, and which are only descriptive.

For Northstar, an ethical experiment might compare synthetic alternatives or low-risk scheduling policies before altering emergency dispatch. High-risk or access-denying treatments require governance and safeguards beyond numerical study design. The experimental protocol should identify stop criteria, data protection, responsible decision-makers and remediation.


## Further depth: aliasing, power and confirmation

With three two-level factors A, B and C, a half fraction may use the generator \(C=AB\), giving the defining relation \(I=ABC\). In such a design, the estimated main effect A is aliased with the two-factor interaction BC, B with AC, and C with AB. If we declare that interactions are negligible, we can screen main effects cheaply—but that declaration is a scientific assumption. In connected cyber-physical systems, interactions can be the central phenomenon, so selecting a resolution that conceals them may defeat the experiment's purpose.

Power analysis begins with a smallest practically important effect \(\delta\), an estimate of noise SD, significance criterion and desired detection probability. Replication controls uncertainty; it does not compensate for confounding. A pilot that estimates the noise level can inform a properly powered confirmatory experiment. Beware of designing sample sizes from the smallest noisy pilot effect: estimates selected because they looked promising may exaggerate expected gains.

A good confirmatory stage reserves a fresh dataset or new experimental runs. If the same data are used to choose features, tune a simulator, set thresholds and then test a claim, the stated interval may fail to account for selection. Pre-register the primary objective and decision rule when possible. Report the full response table, not only statistically favorable contrasts. When feasibility includes safety, distinguish experimental *performance improvement* from proof that all relevant hazards are bounded.

### Interpretation drill

Suppose the software-revision benefit is −4 minutes with a two-vehicle fleet and −5 minutes with three vehicles. The interaction difference-of-differences is −1 minute. If measurement noise is 3 minutes per independent replication, do not declare this interaction significant from the four cell means alone. Estimate variation through replicated runs, preferably using common demand streams across corresponding treatments, and plot uncertainty before recommending a different algorithm for each fleet size.

## Problems — attempt first

1. Compute the two main effects and interaction contrast from the table above.
2. Why are 100 deterministic runs with exactly the same seed not 100 independent replications?
3. Explain how blocking by day can reduce noise without changing treatment definition.
4. Propose a safety-aware evaluation for a routing algorithm that may disadvantage remote neighborhoods.

<details><summary>Worked answers and engineering interpretation</summary>

1. Main effects A = −6.5 minutes and B = −4.5 minutes. Interaction difference-of-differences = −1 minute; coded regression coefficient = −0.25.
2. Identical seeded runs contain no new stochastic evidence and do not estimate variance across demand realizations.
3. Comparing A and B within the same day removes some systematic day-to-day variation, improving precision if treatments are suitably randomized within blocks.
4. Define underserved-subgroup outcomes, simulate realistic demand, monitor refusal and wait outcomes, add a hard minimum-service constraint, evaluate before deployment, and require governance approval with stop criteria.
</details>

## Practice laboratory and further learning

[Open the lab for this chapter](../labs/03-experiments.html) · [Download editable Markdown lab](../labs/03-experiments.md) · [Open the associated notebook](../notebooks/03-experiments.ipynb) · [Download the calculation source](../code/engineering_math.py)

**Authoritative follow-up reading:** [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/), [NIST/SEMATECH Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook), and [Systems Engineering Body of Knowledge](https://www.incose.org/resources-publications/technical-publications/systems-engineering-body-of-knowledge/). These are independent references, not endorsements of the fictional cases.

[Return to the quantitative textbook collection](../INDEX.html)
