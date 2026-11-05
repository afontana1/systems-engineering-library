# Supply-chain assurance: provenance, substitutions, and hidden dependencies

**Canonical reference · Expanded reference · Internal editorial and worked-example checks; independent external peer review not performed**

## Supply chains are part of the engineered system

**Supply-chain assurance** establishes justified confidence in the identity, integrity, availability, and suitability of purchased hardware, software, data, and services over the system life cycle. It covers first-tier suppliers and hidden dependencies such as subcontractors, open-source packages, test labs, build infrastructure, logistics carriers, spare-part brokers, firmware libraries, and cloud services. NIST SP 800-161 emphasizes managing risks from malicious functionality, counterfeit items, vulnerable development practices, and limited visibility throughout the supply chain; it does not assert that one certification removes these risks.

A valid purchase order does not establish item authenticity. A signed software package does not establish that the signing environment was uncompromised. Likewise, evidence that a part passes bench testing may be insufficient to confirm compatibility under thermal cycling, radiation, vibration, long-duration aging, or adversarial interference. Assurance is a chain of conditional arguments connecting sources, processes, item identity, applicable specifications and acceptance evidence.

## Model both provenance and functional dependence

An evidence graph can record original manufacturer, approved distributor, lot number, certificate, receipt inspection, manufacturing process, firmware version, test conditions, calibrated equipment, shipment custody, and installed configuration. Edges should distinguish `supplied-by`, `manufactured-as`, `tested-with`, `derived-from`, `approved-substitute-for`, and `installed-in`. Cryptographic hashes can establish byte-level agreement with a known artifact, but do not by themselves establish authorized production or scientific correctness. Trust is transitive only when every relevant link is assessed against its own threat and error model.

Construct a separate dependency map for availability. A system containing two allegedly independent redundant controllers may still depend on a single timing-chip vendor or shared build server. Supplier concentration and common-mode faults matter even when each controller's local reliability is high. Treat contractual flow-down, inspection, vulnerability response, and replacement qualification as engineering work products.

## Worked decision: substitute part versus assured original

Consider a sensor supplier facing a six-month shortage. An unverified substitute costs 20 thousand dollars initially; a verified-source solution costs 44 thousand. The apparent saving is 24 thousand. If the substitute has a **hypothetical** 15% probability of incurring 180 thousand in integration and requalification consequences, with an additional expected 5 thousand cost common to both choices, the substitute's expected cost is `20 + 0.15×180 + 5 = 52 thousand`, while the verified solution costs `44 + 5 = 49 thousand`. Under these deliberately simplified assumptions, the verified option has lower expected cost by 3 thousand, even before considering consequential service and safety constraints. The 15% and 180-thousand inputs are scenario assumptions, not empirical counterfeit rates.

Expected cost is not the sole acceptance criterion. The substitute might violate a reliability, safety, legal or interface constraint even when cheaper. Conversely, verified-source does not mean zero technical risk. The selection needs a documented fit, form, function, environment, quality and evidence assessment, including owner-approved changes to qualification.

## Detect and respond to drift

Continuous monitoring includes end-of-life notifications, supplier ownership changes, production-site shifts, firmware updates, discovered vulnerabilities, counterfeit alerts, software dependencies and expiring certifications. Record how quickly an affected serial population can be located and isolated. A software bill of materials is valuable for package visibility but does not list every build-time dependency or prove secure provenance. Supplier audits have sampling limits and possible incentives to conceal issues; independently collected acceptance tests and contract enforcement remain relevant.

## Failure modes and decisions

Common errors include assuming a certificate is permanent, approving a substitute from matching nominal specifications alone, ignoring time-dependent material degradation, treating multiple resellers as independent manufacturers, and approving supply-chain changes without updating the product baseline. A credible assurance case names the item and lot, intended use, chain-of-custody evidence, material and software identity, independent checks, open uncertainties, residual risks and acceptance authority.

## Selected source-to-claim references

- **S1 · Risk across suppliers, development, acquisition and delivery, not a guarantee of authenticity.:** [NIST SP 800-161 Rev.1 Update 1, Cybersecurity Supply Chain Risk Management](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final). Risk across suppliers, development, acquisition and delivery, not a guarantee of authenticity.
- **S2 · Security engineering and integrity within systems life cycle.:** [NIST SP 800-160 Volume 1 Rev. 1, Engineering Trustworthy Secure Systems](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final). Security engineering and integrity within systems life cycle.

## Follow the knowledge

- **Prerequisites:** [Risk, issue, uncertainty, and opportunity](risk-vs-issue.md), [Configuration assurance: proving that the tested design is the delivered design](configuration-assurance-and-change-control.md).
- **Related concepts:** [Systems security engineering: protect the mission, not just the network](systems-security-engineering.md), [Obsolescence and technology refresh: planning for vanishing parts](obsolescence-and-technology-refresh.md), [Assurance cases: what evidence supports which engineering claim?](assurance-cases-and-evidence.md).
- **Go deeper:** [Book V · Chapter 8: Performance and security share resource budgets](../B5/chapters/08-specify-and-analyze-performance-networking-re.md), [Book 7 · Chapter 9: Supportability and life-cycle costs](../B7/chapters/09-design-for-supportability-producibility-supply-sustaina.md), [Week 09 · System of Systems Engineering · Chapter 09 — Cascading risk, cyber resilience, safety, and mission assurance](../B18/chapters/09.md).
