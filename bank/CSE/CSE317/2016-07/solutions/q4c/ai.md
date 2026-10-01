---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "(i) k = 1: hill climbing (steepest ascent). (ii) k = infinity: breadth-first search (all successors kept at each step). (iii) SA with T = 0: first-choice hill climbing (random successor, only improving moves). (iv) GA with N = 1: crossover of an individual with itself returns it, so only mutation acts: a random walk (stochastic hill climbing if selection keeps the better of parent and child)."
sources: ["AIMA 3e sec. 4.1 and Exercise 4.4"]
---
**(i) Local beam search with $k=1$: hill climbing.** Beam search keeps the best $k$ states among all successors of the current states. With $k=1$ it keeps one state and moves to its best successor, which is steepest-ascent hill climbing. (Strictly it moves even if the best successor is worse, which hill climbing would not do; usually it stops when no successor is better.)

Example (8-queens, $h$ = number of attacking pairs): from a state with $h=17$ it moves to the best neighbour ($h=12$), and so on, stopping at a local minimum: exactly hill climbing.

**(ii) Local beam search with $k=\infty$: breadth-first search.** With unlimited $k$ no successor is ever discarded: at step 1 it keeps all successors of the initial state, at step 2 all states at depth 2, etc. This is exactly breadth-first search, expanding level by level (with memory $O(b^d)$).

Example: on the 8-puzzle, beam search with $k=\infty$ from the start generates all states reachable in 1 move, then all in 2 moves, ..., until the goal: the BFS order.

**(iii) Simulated annealing with $T=0$ at all times: first-choice hill climbing.** SA accepts a worse move with probability $e^{\Delta E/T}$; as $T\to0$ this is $0$ for any $\Delta E<0$. So it picks random successors and accepts only improving ones (and stops/never moves down), which is first-choice (stochastic) hill climbing. (With the AIMA pseudocode, which returns when $T=0$, it would return the initial state immediately; the intended answer is the limiting behaviour.)

Example: 8-queens: randomly pick a queen move; take it only if it reduces the number of attacks.

**(iv) Genetic algorithm with population size $N=1$: random walk (mutation-only search).** Selection always picks the single individual as both parents; crossover of an individual with itself returns the same individual. The only operator that changes anything is mutation, so the GA becomes a random walk through the state space. If the GA keeps the better of parent and offspring (elitism), it becomes a (1+1) evolution strategy, i.e. stochastic hill climbing with random mutations.

Example: 8-queens string `24748552`: crossover with itself gives `24748552`; a mutation changes one digit, e.g. `24748252`, and the next generation is this new string.
