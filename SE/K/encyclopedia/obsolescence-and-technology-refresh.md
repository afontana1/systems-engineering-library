# Obsolescence and technology refresh: planning for vanishing parts

**Canonical reference · Expanded reference · Internal editorial and worked-example checks; independent external peer review not performed**

## Systems outlive their components

**Obsolescence management** anticipates the loss or imminent loss of sources for parts, materials, software platforms, tools, and services needed to operate or maintain a system. Diminishing manufacturing sources and material shortages (DMSMS) are not merely procurement inconveniences; they can affect safety, certification, cybersecurity, availability, repairability, technical-data rights and the ability to reproduce a previously qualified configuration. Department of Defense DMSMS guidance emphasizes monitoring supplier availability, investigating parts and managing alternatives before an emergency shortage.

An automated transit control system may be supported for fifteen years while its network modules are sold for only five. A part that is no longer manufactured may have inventory in the channel, but availability is not equivalent to authenticity, environmental suitability or indefinite support. Software obsolescence can be less visible: unsupported compilers and operating systems may make security updates or qualified builds difficult even when the physical controller remains functional.

## Model the decision rather than the purchase price

Typical choices include life-of-need buys, controlled inventory, alternate qualified suppliers, emulation, redesign, technology insertion, and retirement. Compare each against remaining service horizon, failure and demand forecasts, storage degradation, requalification cost, design integration time, security exposure, and impacts on adjacent systems. Delaying replacement can have option value when new technology is improving, but delay can also increase shortage and outage risk.

A simple spare-inventory model is `ClosingStock = OpeningStock + Receipts − InstalledReplacements − Scrap`. It conserves *count* but does not guarantee usable stock; expired parts, damaged packaging and wrong revisions must be accounted for. Estimate the required quantity from the maintainable population, expected replacements, uncertainty, fleet growth and lead time. A single point forecast cannot justify a critical last-time buy where consumption variance and common-cause failures are material.

## Worked example: spares versus redesign

Suppose a program expects to need 50 legacy modules over its remaining service horizon. A last-time buy costs 250 dollars per module, plus a **hypothetical** 2,000-dollar aggregate storage and screening expense: `50×250 + 2,000 = $14,500`. A redesign and requalification package is estimated at $25,000. The buy seems $10,500 cheaper before losses, but this conclusion assumes all 50 modules remain usable, capacity is sufficient and no additional security or support problem arises. If 20% of purchased units were unusable, an illustrative expected usable count would be 40 under an independent simplified spoilage model, producing a likely shortfall; the actual distribution matters. An unsatisfied spares constraint can make the cheaper option infeasible.

Conversely, redesign may introduce functional regressions and requalification delays. A new part with matching connectors and headline specifications is not proven equivalent across environmental, timing, thermal, software and mission interactions. Qualification must follow the revised configuration.

## Maintain an obsolescence risk register

For each critical item record original manufacturer, approved variants, known production status, forecast end-of-life dates, inventory by lot and revision, predicted consumption, design dependencies, cybersecurity support status, replacement candidates, change authority, and relevant verification artifacts. Monitor notices and reconcile apparent differences across supplier and parts intelligence tools; an automated database error can create a false urgency or a false sense of assurance. Publish effectivity rules for substitutions.

## Failure modes and decision trigger

Common mistakes include buying a lifetime quantity without accounting for shelf life, extending unsupported software without compensating controls, assuming distributor stock is genuine, and selecting a substitute from nominal datasheets alone. The responsible decision authority should establish triggers—for example, remaining qualifying stock below a lead-time demand threshold or loss of critical vulnerability support—rather than hoping an emergency buy will be available.

## Selected source-to-claim references

- **O1 · Diminishing manufacturing sources and material shortages management principles.:** [Defense Standardization Program, DMSMS program and guidebook links](https://www.dsp.dla.mil/Programs/DMSMS/). Diminishing manufacturing sources and material shortages management principles.
- **O2 · Monitoring part availability and investigating alleged substitutes:** [DLA DMSMS Guidebook SD-22, January 2016, parts availability analysis](https://www.nasa.gov/wp-content/uploads/2023/06/dmsms-guidebook-sd-22-jan2016-tagged.pdf). Monitoring part availability and investigating alleged substitutes; no product endorsement.

## Follow the knowledge

- **Prerequisites:** [Life-cycle sustainment economics: cost after delivery is a design variable](lifecycle-sustainment-economics.md), [Supply-chain assurance: provenance, substitutions, and hidden dependencies](supply-chain-assurance-and-provenance.md).
- **Related concepts:** [Configuration assurance: proving that the tested design is the delivered design](configuration-assurance-and-change-control.md), [Reliability, availability, and maintainability: three different promises](reliability-availability-maintainability.md), [Risk, issue, uncertainty, and opportunity](risk-vs-issue.md).
- **Go deeper:** [Book 7 · Chapter 9: Supportability and life-cycle costs](../B7/chapters/09-design-for-supportability-producibility-supply-sustaina.md), [Book 12 · Chapter 09 — Integrate technical performance with lifecycle cost, resources, maintenance, and affordability](../B12/chapters/09-integrate-technical-performance-with-lifecycle-cost-resources-mainte.md), [Book 11 · Chapter 12 — Apply M&S to production and sustainment, survey advanced methods, and defend the final baseline](../B11/chapters/12-apply-m-s-to-production-and-sustainment-survey-advanced-methods-and-.md).
