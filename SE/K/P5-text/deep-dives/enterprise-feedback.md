# Enterprise feedback, stocks, flows and policy resistance

**Graduate companion concept essay · EN.645.753 · Phase 5**

*All case data are invented teaching examples; models and calculations are not approved operational or safety evidence.*

Organizations develop inertia through accumulations: trained staff, service backlog, deferred maintenance, public trust proxies and contracted capacity. **Stocks** change through **flows**. A simple workforce model is `Staff(t+1)=Staff(t)+Trained(t)-Departures(t)`. Hiring authorizations are not trained staff; a training delay makes the difference matter.

### Worked example

At the start of a quarter, the coalition has 120 qualified operators. Fifteen graduate from training and 22 depart, so it ends with 113. If leaders celebrate 15 hires while ignoring departures, they misread capability. If more operators must be reassigned as trainers, the short-term flow of available service may decline before the training investment pays off.

### Closed-loop explanation

Poor reliability reduces rider trust; reduced ridership may lower fare revenue; reduced revenue may lead to service cuts; service cuts further lower reliability. This is a reinforcing loop that can drive undesirable decline. A separate balancing loop—public funding triggered by unmet service thresholds—may counteract it with an administrative delay. Loops are causal hypotheses requiring investigation; their qualitative signs do not reveal numerical strength.

### Modeling discipline

Define stocks with units, flows in units/time, realistic bounds, initial conditions, delays and measured series. Perform dimensional checks and stress extremes. Use simulations to compare interventions robustly across uncertain assumptions rather than to predict one exact trajectory. Pay attention to induced behavior: a new performance target can change how data are recorded.

**Exercise.** Start with 120 staff and simulate four quarters with completion rates `[15,18,23,25]` and departure rates `[22,21,19,18]`. Identify the first quarter in which capacity stabilizes, and propose what external validation is needed before using the results for staffing decisions.

---

[← Phase 5 contents](../README.md) · [Concept pathways](../KNOWLEDGE-THREADS.md) · [Further reading](../RESOURCE-SHELF.md)
