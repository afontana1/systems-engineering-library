# Chapter 09 — Apply feedback modeling to supply management and inventory dynamics

*Book 13 · EN.645.781 · Systems Thinking and Systems Dynamics · Week 9 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 9](../labs/lab-09-apply-feedback-modeling-to-supply-management-and-inventory-dynamics.md) → attempt the [original Week 9 assessment](../../../C/P3/EN645781.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-781-w09.md) remains available for a quick recap.

## The decision behind the theory

Supply systems exhibit accumulation, ordering delays, information distortion, shortage gaming, expediting, and oscillation. **Essential question:** Why can reasonable local ordering and production rules amplify demand and destabilize the supply network?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the systems thinking and systems dynamics perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

A canonical supply model contains inventory, backlog, and supply-line stocks. Demand depletes inventory or increases backlog. Orders initiate a delayed replenishment process. Managers often order based on expected demand plus correction for inventory and supply-line gaps. If correction is too aggressive relative to delay, orders oscillate.

The bullwhip effect is not simply “bad forecasting.” It can emerge from rational local policies operating with delayed, partial information. Batching, promotions, rationing, and performance incentives can strengthen it.

Policy analysis should compare portfolios: reducing physical lead time, sharing end-demand data, limiting order volatility, adjusting target coverage, reserving capacity, changing allocation rules, and improving visibility of the supply line. A single parameter change may shift cost or shortage burden to another tier.

For critical supplies, evaluate resilience, expiration, substitution, equity, and emergency allocation—not only average inventory cost.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Test structure and behavior, use data responsibly, and make a credibility claim**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Apply systems thinking to healthcare and human-service delivery**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Inventory dynamics couple ordering, lead times, perceived demand and stock accumulation, creating the possibility of a bullwhip effect.

### Distinguishing related ideas

A downstream demand change can create larger upstream order fluctuations without any actor intentionally destabilizing the system.

### Interpretation and boundary conditions

Stabilization may require better information and ordering rules, not simply more inventory or a higher nominal supply rate.

## Deeper theory: an inventory is an accumulation with a delayed view of demand

Inventory problems are often presented as arithmetic about ordering quantities. The more illuminating systems-dynamics view is that inventory is a stock whose level reflects the **historical imbalance between inflow and outflow**. Managers cannot directly set inventory to a desired value; they can influence ordering and replenishment processes, and the stock evolves through their consequences. This distinction explains why well-intended corrections can create cycles instead of stability.

### Conservation first, policy second

Let \(I(t)\) be usable stock, \(R(t)\) deliveries, and \(D(t)\) actual demand. Ignoring losses for the moment,

\[\frac{dI}{dt}=R(t)-D(t).\]

The equation is a physical accounting identity. The management policy determines the order rate and therefore influences future \(R(t)\); it does not alter the conservation relationship. If demand exceeds deliveries for a week, inventory must decline regardless of the dashboard's optimistic forecast. An explicit backlog stock may be needed once unmet demand is permitted rather than assumed lost.

The pipeline matters. Orders placed today may not arrive until a lead time \(L\) later. With deterministic lead time in an idealized model, deliveries might be related to earlier releases by \(R(t)=O(t-L)\). A manager reacting to low current inventory by placing an order sees no immediate recovery. If new orders are placed each day while earlier orders remain in transit, total future supply may greatly exceed the original shortage. The resulting overshoot is not an individual's irrationality; it emerges from the combination of delayed actuation and a policy that ignores the inventory already on order.

### Position rather than visible shelf stock

A common improvement is to regulate **inventory position**—on-hand stock plus outstanding orders minus backorders—rather than on-hand stock alone. This makes the controller aware of work already in the pipeline. Yet it does not eliminate uncertainty. If lead time or demand varies, an order-up-to policy must balance holding cost against shortage risk. The reorder point often includes expected demand during replenishment lead time plus a safety-stock allowance. If demand \(D_L\) during lead time has estimated mean \(\mu_L\) and standard deviation \(\sigma_L\), a simplified service-level rule is \(r=\mu_L+z\sigma_L\), with \(z\) chosen for a one-sided probability under an appropriate distributional assumption. It is not a universal safety-stock formula: correlations, intermittent demand, and supplier constraints may make it unreliable.

The **bullwhip effect** is an amplification of demand variability as orders propagate upstream. Local actors may smooth, forecast, batch, or overreact to the same observed demand. Each transforms the signal according to its information delays and incentives. A supply chain therefore becomes a network of feedback controllers, not merely a sequence of warehouses.

### Why local optimization can destabilize the whole chain

Suppose a depot's target is to minimize its own holding cost while guaranteeing a high fill rate. It may order aggressively after one spike and then stop ordering after inventory rises. A supplier receiving those volatile orders experiences a different demand process from end customers. Capacity scheduling becomes less efficient, which can increase replenishment lead times, which encourages the depot to order even more. The loop couples information, material, and behavior. Even when each organization follows a locally understandable policy, the network-level result can be costly oscillation.

A stock-and-flow model makes the mechanism visible by explicitly separating actual demand, perceived demand, orders, shipments, backlog, and work in the pipeline. In the Northstar case, replace physical products with spare battery modules or available maintenance slots. A shortage of parts can increase vehicle downtime, which increases pressure on remaining vehicles, which raises failure rates and further increases maintenance demand. The feedback crosses the boundary between logistics and system reliability.

### Nonlinearities and model credibility

Real systems impose limits: warehouse capacity, supplier production limits, perishability, minimum order batches, transportation disruptions, and priority allocation. These nonlinearities can change the character of the response. A model in which delayed shipments always arrive eventually may underestimate prolonged disruption. Likewise, a model that assumes backorders are remembered forever will behave differently from one in which riders or customers abandon the service.

The central insight is that inventory control is not primarily choosing a number of units. It is managing a delayed information-and-material feedback system. A good explanation of inventory policy begins with conservation, represents pipeline states explicitly, and asks which signals the decision maker observes—and how old those signals are—before drawing conclusions about stability or service performance.

## Worked engineering example from the course

A hospital orders a critical component using recent consumption plus a four-week inventory-gap correction. Supplier lead time is six weeks. A shortage causes departments to inflate orders, increasing apparent demand. The model shows large order oscillations, temporary overstock, and expiration after supply recovers. A policy portfolio combining end-use visibility, anti-gaming allocation, and moderate correction outperforms a policy that merely increases target inventory.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Order-up-to inventory can oscillate when managers react to delayed shipment and misread pipeline stock as shortage. Distinguish inventory on hand from orders in transit; the latter is a separate stock.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A service backlog begins at 40 requests, with 12 new requests and 9 completions per day for 5 days. Compute the ending stock.

<details><summary>Show a reasoned solution</summary>

Backlog = 40 + 5×(12−9)=55. This is a stock balance, not a claim about service quality.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* orders, demand, shipments, inventory, and backlog are conflated;
* the supply-line stock is omitted despite material delay;
* bullwhip is asserted without a mechanism;
* policy analysis tracks only average inventory;
* rationing, expiration, substitution, or critical-service impact is ignored where relevant.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What does this conclusion depend on?

<details><summary>Explain the answers</summary>

**1. What does this conclusion depend on?** The configuration, intended use, input provenance, model assumptions, uncertainty and decision rule.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 9](../labs/lab-09-apply-feedback-modeling-to-supply-management-and-inventory-dynamics.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[08 — Previous chapter](08-test-structure-and-behavior-use-data-responsibly-and-make-a-credibil.md) · [10 — Next chapter](10-apply-systems-thinking-to-healthcare-and-human-service-delivery.md) · [Book index](../README.md)
