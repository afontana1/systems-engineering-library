# System boundaries, outcomes, and emergence

*Core Concepts · Foundations · T01*

> Decide what the engineered system is accountable for, and what remains outside its authority.

**Recommended preparation:** No required prerequisites in this sequence.

**Related course companions:** [Book 1](../B1/OPEN-BOOK.html), [Book 6](../B6/OPEN-BOOK.html), [Book 20](../B20/OPEN-BOOK.html)

## 1. Begin with a claim, not a box
A boundary drawing is not merely a picture of hardware. It is a claim about **responsibility**: which behaviors can the project directly design, test, and change, and which must be managed through agreements with others? Consider an autonomous campus shuttle service. The vehicle is unquestionably a system element. But the service may also depend on a dispatch application, a campus map, charging infrastructure, passengers, the road authority, and a human response team. Calling all of these “the system” obscures who is authorized to change each element. Calling only the vehicle “the system” hides mission-critical dependencies.

Start with the outcome the sponsor wants: *a rider can complete a requested accessible trip within an acceptable time and risk envelope*. Then identify the functions necessary to realize that outcome. Mark each function as controlled by the project, controlled through contract, or only observed. The system-of-interest boundary should be chosen for the engineering decision under consideration; it need not be identical for vehicle certification, service scheduling, and citywide mobility planning.

A useful four-column boundary register contains **element**, **controller**, **expected contribution**, and **failure consequence**. For example, a mobile-network provider may be external, but an outage in the network remains a real failure mode for dispatch. A boundary never authorizes you to ignore external dependencies.

## 2. Distinguish outputs, outcomes, and externalities
The project can count successful dispatch messages, but a passenger cares about completed journeys. A system can satisfy every component-level output target and still miss the mission outcome if information arrives too late, accessible boarding fails, or operators cannot recover from unexpected conditions. A further distinction is an **externality**: an effect on someone who is not the primary user, such as pedestrian conflict near a shuttle stop.

Use a causal chain: engineered capability → operational behavior → beneficiary experience → mission outcome. Add assumptions beside every arrow. For example, a schedule-prediction algorithm does not improve trip completion if the rider has no usable way to receive or act on the prediction. That is a broken causal link, not necessarily a defective algorithm.

### Emergence is an interaction, not magic
Emergent behavior arises when interactions produce a property that cannot be assessed by inspecting elements separately. Congestion, queue spillback, competing optimization policies, and operator workarounds are ordinary examples. The word *emergent* should prompt you to specify the interaction and the measurement, not to abandon analysis. Test the coupled system in scenarios where two individually acceptable elements compete for a shared resource.

## 3. Choose a boundary using decision criteria
A narrow boundary improves design freedom and cost visibility but may externalize essential failure modes. A broad boundary captures more dependencies but may demand authority the sponsor does not have. Compare candidate boundaries against **authority, verifiability, mission coverage, cost of interfaces, and change impact**. The right answer is often a nested model: vehicle subsystem inside shuttle service inside regional mobility ecosystem.

For each boundary, write an interface contract with preconditions, exchanged information or matter, timing assumptions, failure signaling, and a responsible owner. If a dependency has no owner, the boundary decision is incomplete. If the mission cannot be measured end-to-end, the boundary may be too narrow for the claim being made.

## 4. What usually goes wrong
**Boundary-as-inventory:** listing parts without authority or external actors. **Success-by-proxy:** celebrating dispatch response time while riders miss trips. **Environment-as-constant:** assuming connectivity, weather, and road access never change. **Single-view architecture:** using a component view to answer a stakeholder outcome question. Each mistake becomes apparent when a reviewer asks what evidence could falsify the claimed mission success.

## 5. A reviewer’s boundary workshop
**Question:** who can actually change the system element next Tuesday? This deceptively simple question is often more informative than a large context diagram. For each element, separate design authority, operational authority, and accountability for harm. The campus may authorize where stops are placed, while a city controls street signals and the supplier controls embedded firmware. A credible boundary statement marks these distinctions rather than inferring authority from proximity in a drawing.

Run an assumption audit. First imagine the network is unavailable for thirty minutes. Does the service continue, suspend new rides, or fail silently? Next imagine the sponsor changes the mission from scheduled campus circulation to emergency evacuation. Which boundary decisions become invalid? Finally ask a non-user stakeholder to challenge the claimed benefits. A reviewer might identify obstruction of a shared sidewalk or disproportionate wait times for riders using mobility devices. Those effects should remain visible even if they are outside the design authority.

**Two complementary mental models:** the *black-box* view asks which outputs follow from which inputs under defined conditions. The *responsibility network* asks who ensures those conditions hold and who can respond when they do not. Both are needed: the former guides technical validation, while the latter informs operational assurance and governance.

**Check your reasoning:** A consultant argues that network availability is outside the project boundary and therefore must not be included in acceptance testing. That conclusion does not follow. The network can be outside project control while its degradation remains part of the system's operational environment. A more defensible acceptance test assesses the service's response to loss of network connectivity and documents the external service-level assumption.

## Guided worked example

### Worked case: why availability is not the whole mission
Suppose the dispatch service is available 99% of the time and a shuttle is mechanically available 98% of the time. Under an *illustrative independence assumption*, joint availability is \(0.99\times0.98=0.9702\), or 97.02%. But a journey also requires a usable stop, a timely request, and successful boarding. Multiplying two availability numbers is **not** an estimate of rider trip completion unless all other necessary conditions have been represented and the dependence assumptions are defensible. The appropriate top-level test is an end-to-end journey outcome measured under specified operating scenarios.

## Independent transfer exercise

Choose two boundaries for a regional shuttle: vehicle-only and end-to-end service. Produce a stakeholder/outcome table, an interface register with five external interfaces, and a one-page argument identifying a failure neither boundary can directly control.

[Open the companion hypothetical lab](labs/01-boundaries-workshop.md)

<details><summary><strong>What a defensible answer must contain</strong></summary>

An acceptable response distinguishes control from dependency, names an owner for each interface, and includes at least one outcome-level verification measure rather than just component uptime.

</details>

## Next connections

Use the related books above to see how this concept becomes a course assignment. The lab provides a small, deliberately incomplete practice setting; it does not replace verification against real operational data.
