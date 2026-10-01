---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Greedy algorithms make the locally best choice and never revise it, so they get trapped in local optima (also ridges, plateaux). An EA keeps a population and uses selection plus variation; mutation (with crossover) keeps diversity and can jump out of local optima. Mutation is the operator best suited to avoid the pitfall."
sources: ["AIMA 3e sec. 4.1.1 and 4.1.4", "Eiben and Smith, Introduction to Evolutionary Computing, ch. 3"]
---
**Main pitfall of greedy algorithms: local optima.** A greedy algorithm (e.g. hill climbing) always takes the locally best move and never goes back. When it reaches a state where no neighbour is better, it stops, even though a much better solution exists elsewhere. Related problems:

- **Local maxima**: peak higher than its neighbours, lower than the global maximum.

- **Ridges**: sequences of local maxima that are hard to navigate with single moves.

- **Plateaux/shoulders**: flat areas giving no direction.

So greedy search is incomplete and not optimal; the result depends on the initial state. Example: 8-queens, steepest-ascent hill climbing gets stuck 86% of the time. TSP: the nearest-neighbour greedy tour is typically 20-25% longer than optimal.

**How an evolutionary algorithm solves it.**

1. It maintains a **population** of many solutions spread across the search space, not one, so it does not depend on a single starting point.

2. **Selection** favours fitter individuals but also gives weaker ones some chance (stochastic selection), so the search does not commit to one peak immediately.

3. **Crossover** combines parts of different solutions, producing offspring in new regions, possibly between peaks.

4. **Mutation** randomly changes genes, making jumps that a greedy step would never take (it can produce a temporarily worse solution).

Together, an individual stuck on a local optimum can be overtaken by offspring that found a different, better peak.

**Most suitable operator: mutation.** Mutation is the operator that introduces new genetic material and maintains diversity. Crossover can only recombine what is already in the population; if the whole population has converged to one local optimum, crossover of identical parents produces the same individual, and only mutation can move it away. A sufficiently high (or adaptive) mutation rate prevents premature convergence.

**Example.** Maximise $f(x)$ over 5-bit strings, where $f(\texttt{01111})=15$ is a local optimum and $f(\texttt{10000})=16$ is the global optimum, but every single-bit neighbour of 01111 is worse. Greedy bit-flipping from 01111 stays there. If the GA population converges to individuals like 01111, crossover of them gives 01111 again; mutation (flipping bits, possibly several, and accepting temporarily worse children in the population) can produce 11111, 10111, ... and eventually 10000, which selection then spreads.
