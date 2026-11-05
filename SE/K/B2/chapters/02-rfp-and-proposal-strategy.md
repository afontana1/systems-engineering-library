# Chapter 2 — A Proposal Is a Testable Promise

*EN.645.667 · Week 2 · Opportunity analysis, RFP compliance and bid decisions · Preceded by [Chapter 1](01-governance-and-technical-authority.md); continue with [Chapter 3](03-wbs-and-work-authorization.md).*

> **Study contract.** This chapter teaches the concepts behind Week 2; practice them in [Hypothetical Lab 2](../labs/lab-02-rfp-and-proposal-strategy.md), then complete the [original Week 2 coursework](../../../C/P0/EN645667.md). These fictional examples are not contractual or safety approvals.

## The management problem

The shuttle pilot is not yet a funded project. It is an opportunity with uncertain customer expectations, evaluation rules, and contractual commitments. Proposal teams often begin by describing an attractive solution, only to discover that they omitted a mandatory submission format or promised performance they cannot substantiate. A technical proposal should be treated as a collection of claims that will later be implemented, measured and judged.

Separate **instructions to offerors** (how to submit), **evaluation criteria** (how offers are compared), **statement of objectives** (desired outcomes), and **statement of work or performance work statement** (contractual work or outcomes). Not all sentences carry the same authority. A mandatory response item and a desirable design preference must not be merged. An ambiguity should become a clarification question and an explicit assumption, not an invisible estimate.

A bid/no-bid decision asks more than whether the project is interesting. Is the required competence available? Is the target acceptance regime credible? Can the team propose within the cost ceiling? Does accepting the opportunity expose it to obligations whose cost or safety implications cannot be estimated? An honest no-bid can be better than an unexecutable win.

## Develop the method

Construct a compliance matrix with requirement ID, source paragraph, binding language, proposal location, responsible writer, planned evidence, and compliance status. Every affirmative claim should link backward to a customer demand and forward to an execution artifact. If the proposal claims a 98% trip-completion rate, identify the denominator, operating conditions, measurement method, and activities needed to prove it. The compliance matrix is not just for submission; it becomes the beginning of contract-to-project traceability.

Proposals have different levels of persuasion. A claim such as “our approach is low risk” is weak; “we will demonstrate degraded-mode dispatch in a controlled scenario before passenger testing, using the specified acceptance protocol” gives the evaluator a concrete plan to scrutinize. Evidence-backed themes should be few, relevant, and consistent with the baseline.

### The proposal creates a future obligation under uncertainty

A proposal is not merely a persuasive description of a design. It is an attempt to convert uncertain future work into a set of commitments that another organization can authorize and assess. This requires separating the proposed **result** from the **strategy for obtaining it**. A bidder may know exactly what acceptance evidence must eventually exist while knowing only approximately which subsystem architecture will prove feasible. Good proposals make that distinction visible instead of turning assumptions into unqualified promises.

An RFP compliance matrix maps statements in a request to planned responses, but compliance is not the same as technical credibility. A response may be present yet unsupported by a staffing plan, acquisition lead time, integration strategy, or test capacity. Conversely, proposing extra capability can increase risk when it expands verification burden beyond what the client values. The central intellectual task is consistency across scope, cost, schedule, quality, evidence, and authority. If one element changes, the others must be reconsidered before the proposal remains a coherent commitment.

## Worked Northstar project example

In a fictional RFP, the customer requires an 18-month delivery and a proposal price not exceeding $8.8 million. The planning team proposes a $7.2 million performance measurement baseline, $0.6 million management reserve and a $0.6 million fee, or $8.4 million total under this simplified pricing convention. Headroom is $0.4 million. That arithmetic only checks compliance with the ceiling; it does **not** establish estimate credibility. The customer also requires an accessibility demonstration. If there is no corresponding test in the WBS and schedule, the proposal may be nominally compliant but operationally incoherent.

## Reading solicitation language as engineering constraints

Start with three imagined clauses. “Provide a mobility capability for qualified users” defines a desired outcome but leaves service boundaries uncertain. “Submit a cost volume of at most 25 pages” is a proposal instruction; satisfying it says nothing about technical fitness. “Demonstrate operation under one simulated communications outage” is a verifiable performance obligation if the test conditions are defined. The analyst must distinguish the **kind** of clause before deciding what to design and price.

A common source of later dispute is an undefined denominator. “99% availability” might mean scheduled service minutes, individual request successes, vehicle uptime, or an end-to-end mission thread. Each interpretation can imply a different architecture and evidence plan. Before pricing the clause, record an interpretation, owner and clarification question. If the customer cannot clarify before bid submission, the proposal should disclose the assumption and assess whether it is commercially and technically acceptable. Simply choosing the cheapest interpretation in an internal spreadsheet is not a valid risk response.

**Worked bid decision.** Imagine two architectures: an integrated supplier package priced at $7.9M but with limited evidence for degraded operations, and a modular proposal at $8.4M with a well-defined bench test but greater integration work. The more expensive option is not automatically superior. Compare compliance, strength of supporting evidence, team competence, contingent liabilities, schedule realism and the economic consequences of failing the customer acceptance test. A bid/no-bid analysis should include organizational risk appetite, not just a cost arithmetic pass/fail check.

The proposal should later survive a continuity test: select any customer clause and follow it to a work package, budget, schedule activity, test and acceptance record. A broken chain is not merely weak prose; it may be an unrecognized project obligation.

## Boundary of the method

Do not treat a compliant-looking matrix as proof that the contract is executable. Check the same commitments against resources, interfaces, cost basis and schedule logic.

## Retrieval questions and explained answers

1. **Question:** Why retain the source paragraph in a compliance matrix?
   **Explanation:** It allows precise review of the obligation and guards against a paraphrase that changes meaning.
2. **Question:** What is the difference between bid compliance and delivery credibility?
   **Explanation:** The former tests a response against solicitation rules; the latter tests whether the team can fulfill the proposed work.
3. **Question:** Does $8.4 million below an $8.8 million ceiling prove affordability?
   **Explanation:** Only a narrow price-ceiling comparison; it does not validate assumptions or customer value.


## Graduate depth: proposals as commitments with real-option consequences
### Solicitation compliance and delivery feasibility are different predicates

A responsive proposal satisfies the buyer's submission conditions; a credible proposal shows how the offered system could be delivered. These are logically distinct. For each requirement, distinguish an instruction governing the offer, an evaluation preference, a contractual obligation, and an operational outcome. A proposal may earn a high technical score while leaving infeasible resource assumptions unresolved. Conversely, an elegant architecture can be nonresponsive if it omits a mandatory deliverable. Compliance matrices identify obligations and page locations, but engineering review must still verify the plausibility of each promised outcome.

The proposal translates uncertainty into commitments before engineers have complete knowledge. Price, schedule, acceptance criteria, intellectual-property conditions, and change mechanisms shape later design freedom. Where the contract rewards a single narrow metric, teams may optimize the metric while harming unmeasured mission performance. Therefore, a bid strategy should map each promised measure to its definition, boundary, baseline assumption, method of verification, and ownership. A target such as “95% on-time journeys” is incomplete unless “on time,” the eligible journeys, excluded failures, and the observation period are defined.

### Expected profitability is not sufficient for a bid decision

A simplified risk-neutral bid value can be written `V_bid = p_win (R - C - E[loss | win]) - C_bid`, with revenue `R`, estimated delivery cost `C`, exposure to penalties and failures, bid expense `C_bid`, and probability of award `p_win`. This expression hides assumptions: revenues may be delayed, costs uncertain and correlated, contractual penalties capped or uncapped, and capacity consumed by a bid may prevent more valuable work. Estimates should expose distributions and conditions instead of treating one point forecast as certain.

A hypothetical vendor offers Northstar a fixed-price service at $8.4 million under an $8.8 million ceiling. Ceiling compliance says little about feasibility if fleet replacement prices, permitting, and integration labor have broad uncertainty. A reserve derived by adding unrelated “10% buffers” may understate a common inflation shock or overstate diversified independent risks. Scenario-based cost modeling and a documented baseline of contractual assumptions provide more useful decision support.

### Sequential commitments preserve learning options

Contracts can sometimes be structured as staged commitments: prototype, measured demonstration, limited deployment, and scale-up contingent on evidence. This resembles a real option. The buyer pays for early information while delaying a harder-to-reverse investment. The value of staging is greatest when uncertainty can actually be reduced before the irreversible decision, the cost of delay is tolerable, and the contracting mechanism gives both sides incentives to disclose bad results. It is smaller when the relevant uncertainty cannot be resolved by a pilot or when integration costs make staged deployment uneconomic.

Proposal evidence must survive the transition to project execution. The work breakdown structure should contain the activities needed to substantiate each claim, while interface assumptions and third-party dependencies must be assigned owners. If a bidder promises service reliability based on a simulated demand model, later reviewers should recover the simulation version, demand profile, uncertainty assumptions, and scope exclusions. A proposal is therefore the first operational form of a technical baseline, not just a sales document. Its quality is judged by whether the promised decision logic remains coherent when real constraints appear.

## Put this into practice

Work through [Lab 2: The Bid/No-Bid Table](../labs/lab-02-rfp-and-proposal-strategy.md), then write a short paragraph on how the laboratory simplifies the real-world management problem. Use the [existing short Week 2 primer](../../P0-text/lessons/645-667-w02.md) for a second explanation. The assessed deliverable is defined in the original course guide, not by the hypothetical lab.
