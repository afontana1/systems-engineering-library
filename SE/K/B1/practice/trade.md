# Workshop 2 · A defensible architecture trade study

*Companion to Book I, Chapter 8 · Trade studies, decision sensitivity and feasibility*

## Why the highest score can still be the wrong design

Northstar must choose among three shuttle dispatch architectures. Candidate A uses a lean controller and costs 4.5 fictional million dollars; B adds fault-tolerant coordination and costs 5.0; C costs only 4.2 but has lower service coverage and longer waits. The engineering team must separate three distinct tasks: **rule out infeasible alternatives**, compare *feasible* designs using an explicit preference model, and test whether the preference changes under plausible assumptions.

A weighted sum is not an engineering decision by itself. It is a model of preferences over already-normalized attributes, and different normalization bounds change the resulting scores. Hard requirements—such as mandatory accessibility or a maximum response time—must not be converted into a small preference penalty unless the stakeholder and acceptance authority have explicitly authorized a trade.

## Step 1. Apply the non-negotiable constraints

The fictional gate requires cost no more than 5.0, completed-trip p90 wait no more than 20 minutes, and service coverage at least 0.95. A reports (4.5, 18, 0.96), B (5.0, 12, 0.99), C (4.2, 24, 0.90). C fails both wait and coverage conditions. Its low cost cannot compensate for that failure. Only A and B are candidates for preference scoring.

## Step 2. Normalize carefully

For this teaching example, normalize cost between 4 and 5 million, wait between 10 and 30 minutes, and coverage between 0.90 and 1.00. Higher normalized utility is better:

\[
u_c=1-\frac{c-4}{1},\quad
u_w=1-\frac{w-10}{20},\quad
u_s=\frac{s-0.90}{0.10}.
\]

A has utilities (0.50, 0.60, 0.60), B has (0, 0.90, 0.90), and C has (0.80, 0.30, 0). C must remain excluded even if it earns a high score. With weights (cost 0.25, wait 0.35, coverage 0.40), A scores 0.575 and B scores 0.675. B is preferred **under this particular model**, not universally.

## Step 3. Solve the decision-reversal question

Suppose the sponsor adjusts the *cost* weight \(x\), dividing the remaining preference weight between wait and coverage in their original proportion. Because A earns 0.60 for both noncost attributes and B 0.90 for both, the scores reduce to

\[
U_A=0.5x+0.6(1-x)=0.6-0.1x,\qquad
U_B=0.9(1-x)=0.9-0.9x.
\]

The crossover is \(U_A=U_B\), or \(0.8x=0.3\), so **\(x=0.375\)**. At higher cost weight A wins, if the assumed value functions remain legitimate. The fact that a modest weight change reverses the outcome is a meaningful review finding: clarify sponsor priorities before committing to B.

## Step 4. Challenge the model, not merely the weights

Coverage and waiting time may share underlying operating causes; rewarding both can double-count performance. The p90 wait is computed only for completed trips and may paradoxically improve when requests are dropped. Cost estimates can have different confidence levels. The normalization limits were elicited assumptions, not objective physical facts. An adversarial reviewer should request raw scenario results, uncertainty intervals and acceptance constraints, and should test correlated demand spikes and single-vehicle loss before finalizing the architecture.

## Worked problems

**Problem 1.** Why can't candidate C win if a change in weights gives it the highest numerical utility?

<details><summary>Worked solution 1</summary>

It violates the explicitly specified hard constraints. Preference ranking starts only *after* feasibility screening. Changing that gate requires an authorized requirements decision, not a spreadsheet weight change.
</details>

**Problem 2.** Compute A's weighted score from the stated utilities and weights.

<details><summary>Worked solution 2</summary>

\(0.25(0.50)+0.35(0.60)+0.40(0.60)=0.125+0.210+0.240=0.575\).
</details>

**Problem 3.** At cost weight 0.50 (with the other half allocated to wait/coverage), which design wins?

<details><summary>Worked solution 3</summary>

A scores \(0.6-0.1(0.5)=0.55\); B scores \(0.9-0.9(0.5)=0.45\). A now wins. Report the reversal as a sensitivity result, not as proof that the original study was mistaken.
</details>

**Problem 4.** If 10% of B's requests are lost during the rare outage scenario, why can reporting “p90 wait = 12 min” be misleading?

<details><summary>Worked solution 4</summary>

Completed-trip wait excludes the unserved requests. It is a conditional metric. Pair it with coverage, failure probability, and ideally a measure of end-to-end passenger burden that explicitly accounts for requests never served.
</details>

## Transfer to engineering work

Use the provided alternatives CSV and trade-study calculator. Submit a decision table, feasibility exclusions, a cost-weight sensitivity plot or table, and a separate paragraph arguing against your own preferred candidate. Identify at least one missing stakeholder judgment and one uncertainty that would justify further testing. Compare your conclusions against Book I Chapter 8's original architectural review assignment.
