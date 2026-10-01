---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Variations: steepest-ascent (best neighbour), stochastic (random uphill neighbour, probability by steepness), first-choice (first random better successor), plus random-restart and sideways moves. Random-restart hill climbing is best: it is complete with probability approaching 1, while the others still get stuck at local maxima; first-choice is best when there are very many successors."
sources: ["AIMA 3e sec. 4.1.1"]
---
**1. Steepest-ascent hill climbing.** Generate all successors and move to the best one if it is better than the current state; otherwise stop. Fast to converge, but gets stuck at local maxima, ridges and plateaux; on 8-queens it solves only 14% of random instances (average 4 steps when it succeeds, 3 when stuck).

**2. Stochastic hill climbing.** Choose at random among the uphill moves, with probability that may depend on the steepness. Converges more slowly than steepest ascent but in some landscapes finds better solutions, because it does not always take the same path.

**3. First-choice hill climbing.** A form of stochastic hill climbing: generate successors randomly one by one and take the first one that is better than the current state. Good when a state has very many (thousands of) successors, because it avoids generating them all.

(Also: **sideways moves** on plateaux, which raise 8-queens success to 94% with a limit of 100 sideways moves, and **random-restart hill climbing**: repeat hill climbing from random initial states and keep the best result.)

| | Steepest ascent | Stochastic | First-choice | Random-restart |
|:--|:--|:--|:--|:--|
| Move | best successor | random uphill successor | first random better successor | any of these, restarted |
| Cost per step | all successors | all uphill successors | few successors | as the base method |
| Escapes local maxima | no | no | no | yes, by restarting |
| Complete | no | no | no | with probability $\to1$ |

**Which is best?** **Random-restart hill climbing**: the basic variants all stop at a local maximum, whereas restarting from random states eventually generates a start in the basin of the global optimum, so it is complete with probability approaching 1. If each run succeeds with probability $p$, the expected number of restarts is $1/p$: about 7 for 8-queens (with sideways moves, about 1.06), and it finds solutions to 3-million-queens problems in under a minute. Among the three single-run variants, first-choice is preferred when the number of successors is very large, and steepest ascent when the landscape is smooth.
