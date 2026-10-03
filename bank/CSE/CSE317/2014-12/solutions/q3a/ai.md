---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Greedy (hill-climbing) search: simple, fast, constant memory, works in huge or continuous spaces, often good enough; but it gets stuck at local maxima, ridges and plateaux and is incomplete. Simulated annealing picks random moves and accepts worse ones with probability e^{Delta E/T}, T decreasing, so it can escape local maxima; slow cooling gives the global optimum with probability approaching 1."
sources: ["AIMA 3e sec. 4.1.1-4.1.2"]
---
**Facilities of greedy search** (hill climbing: always move to the best neighbour).

- Very **simple and fast**: it moves straight towards higher values, with no backtracking.
- **Constant memory**: only the current state is kept, so it can work in very large or continuous state spaces where systematic search is impossible.
- It often finds a good solution quickly (for example, 8-queens in about 4 steps when it succeeds).

**Problems.** It never makes a downhill move, so it gets stuck at:

- **local maxima**: peaks that are not the global maximum;
- **ridges**: sequences of local maxima that are hard to navigate;
- **plateaux and shoulders**: flat regions with no uphill direction.

It is therefore incomplete: 8-queens succeeds only 14% of the time from a random start.

**How simulated annealing addresses the main problem (local maxima)** (4). Instead of the best move, pick a **random** neighbour. Always accept it if it is better. Otherwise accept it with probability $e^{\Delta E/T}$, where $\Delta E<0$ is how much worse it is. The temperature $T$ starts high (many bad moves accepted, so the search can **escape local maxima** and explore) and is gradually reduced (fewer bad moves, so it converges). With a slow enough cooling schedule, it finds a global optimum with probability approaching 1.
