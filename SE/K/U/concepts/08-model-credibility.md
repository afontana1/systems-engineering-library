# 08 · Modeling and simulation: purpose, numerical error, and credibility

**Concept dossier · model-based engineering / simulation / system test**

## A model is a claim about usefulness for a purpose

Models omit detail by design. A traffic queue model may represent vehicles as arrivals and departures; an electric drivetrain model may represent continuous power flows and thermal states. Neither is “the true system.” Model credibility asks whether a particular model and use of its results are **adequately justified for a particular decision** in a specified context. Credibility does not come from how sophisticated the software looks.

Start with the **question of interest**: Should the fleet grow from three vehicles to four? What output matters: mean waiting time, 95th-percentile wait, missed accessible pickups or total energy cost? Under which demand and weather scenarios? Which fidelity and uncertainty are necessary for that decision?

## Four distinct checks

1. **Conceptual validity:** does the chosen abstraction include relevant mechanisms, boundaries and causal dependencies? A queue model without inaccessible-boarding delays can be wrong even if its code is bug-free.
2. **Implementation verification:** does the code correctly implement the equations or event logic? Unit tests, invariants, convergence checks and independent calculations help.
3. **Validation:** do model outputs and behavior correspond acceptably to observations for the intended context? Calibration against one dataset and prediction on the same data are weak tests.
4. **Use credibility:** have uncertainty, scenario coverage, configuration, expert review and decision consequences been evaluated sufficiently?

These processes complement one another. A validated-looking average does not prove correct tail behavior or rare-event predictions.

## Numerical discretization matters

Consider `dx/dt = -k x` with `x(0)=100` and `k=0.5 per hour`. The exact solution is `x(t)=100 exp(-0.5t)`, giving about `60.65` at one hour. Forward Euler with step `h=1 h` gives `x_1=100 + 1*(-0.5*100)=50`, a sizable error. Using two steps of `h=0.5 h` gives `100*(1-0.25)^2=56.25`, closer but not exact. At `h=0.25 h` four steps give about `58.62`.

For Euler's method to be numerically stable on this simple decay problem, the amplification factor satisfies `|1-kh| < 1`, or `0 < kh < 2`; stability is not the same as accuracy. Step refinement is one useful test, but matching results under two steps is not sufficient model validation.

## Separate kinds of uncertainty

- **Aleatory:** modeled variability among future operating events, such as arrivals.
- **Epistemic:** limited knowledge of parameters or mechanisms, such as unknown storm-related delay distribution.
- **Numerical:** solver and discretization error.
- **Implementation:** mistakes in code, units, indexing, random number generation and configuration.
- **Structural:** omitted causal mechanisms or incorrect assumptions about dependence.

A single Monte Carlo histogram often mixes some of these while ignoring others. Use a designed uncertainty budget and scenario analysis instead of giving a solitary “±” range.

## A credible simulation study

For the shuttle case, build a simple discrete-event queue with arrivals, assignment, travel and charging constraints. Compare its predictions with controlled historical data **not used in calibration**. Test invariants (no negative queue, no double-assignment), extreme scenarios (zero arrivals; fleet outage; all vehicles busy), random-seed variation and convergence of estimated statistics. Report what the model excludes (pedestrian interference, particular weather hazards, coordination failures) and how exclusions could change the decision.

A model's predictions cannot by themselves certify safety-critical deployment. They can inform which design to prototype or which physical test is most informative.

## Exercises with answers

**A.** A detailed simulation matches average waiting time. Is it validated? **Answer:** only partially, if at all. Evaluate variability, tails, scenarios, dependencies, independent data and intended use.

**B.** Why run the same stochastic simulation with several seeds? **Answer:** to estimate Monte Carlo sampling uncertainty and diagnose unexpected seed sensitivity. Seeds are not substitutes for input-uncertainty analysis.

**C.** A smaller time step changes results markedly. What should you do? **Answer:** examine numerical convergence, event/order logic, solver stability and units before using model output in a decision.

**Transfer artifact:** a model-purpose statement, credibility matrix, explicit assumptions, one convergence experiment and a validation comparison.

## Connections

[Experimental evidence](07-experimental-evidence.md) · [Queues and feedback](09-queues-feedback.md) · [Trade decisions](05-trades-uncertainty.md) · [Digital twin claims](11-digital-thread.md).  
**Legacy primer:** [Model V&V and credibility](../../encyclopedia/model-vv-and-credibility.md).
