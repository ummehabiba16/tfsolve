---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "SA is hill climbing that picks random moves and sometimes accepts worse ones, like slowly cooling a metal; at high temperature it explores and escapes local optima, at low temperature it behaves greedily. Acceptance (Metropolis) function: P(accept) = 1 if dE > 0, else exp(dE/T) (for minimisation exp(-dC/T))."
sources: ["AIMA 3e sec. 4.1.2"]
---
**Idea.** Annealing in metallurgy: a metal is heated and then cooled slowly, so its atoms settle into a low-energy, regular crystal; cooling too fast freezes defects. Simulated annealing applies this to optimisation: the objective is the "energy", and a **temperature** $T$ controls randomness.

- Pick a **random** neighbour of the current state (not the best one).

- If it is better, move to it.

- If it is worse, still move to it with a probability that is larger for smaller deterioration and higher temperature.

- Decrease $T$ gradually. At high $T$ the search moves almost randomly and can escape local optima; at low $T$ it behaves like hill climbing. With a slow enough cooling schedule it finds the global optimum with probability approaching 1.

**Acceptance function (Metropolis criterion).** For maximisation with $\Delta E=\text{VALUE}(next)-\text{VALUE}(current)$:

$$P(\text{accept})=1 \quad \text{if } \Delta E>0$$

$$P(\text{accept})=e^{\Delta E/T} \quad \text{if } \Delta E\le0$$

For minimising a cost $C$ with $\Delta C=C(next)-C(current)$, accept worse moves with $e^{-\Delta C/T}$. Example: $\Delta E=-2$: at $T=10$, $P=e^{-0.2}\approx0.82$; at $T=1$, $P=e^{-2}\approx0.14$; at $T=0.1$, $P=e^{-20}\approx0$.
