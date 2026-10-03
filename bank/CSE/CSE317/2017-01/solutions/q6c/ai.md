---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Yes, always admissible: h is a convex combination of h1 and h2, so h(s) <= max(h1(s), h2(s)) <= h*(s). Example: h1 = misplaced tiles, h2 = Manhattan distance in the 8-puzzle, alpha1 = alpha2 = 0.5, h = (h1 + h2)/2 <= h2 <= h*. Admissibility holds for any non-negative weights summing to at most 1."
sources: ["AIMA 3e sec. 3.5.2 and 3.6 (admissible heuristics, combining heuristics)"]
---
**Claim:** $h=\alpha_1h_1+\alpha_2h_2$ with $\alpha_1,\alpha_2\ge0$ and $\alpha_1+\alpha_2=1$ is **always admissible**.

**Proof.** Admissible means $h_i(s)\le h^*(s)$ for every state $s$, where $h^*$ is the true optimal cost to the goal. Then, for every $s$,

$$h(s)=\alpha_1h_1(s)+\alpha_2h_2(s)\le\alpha_1h^*(s)+\alpha_2h^*(s)=(\alpha_1+\alpha_2)\,h^*(s)=h^*(s).$$

A convex combination lies between the two values, $\min(h_1,h_2)\le h\le\max(h_1,h_2)\le h^*$, so it never overestimates.

**Example: 8-puzzle.** $h_1$ = the number of misplaced tiles and $h_2$ = the sum of Manhattan distances; both are admissible. For the AIMA start state, $h_1=8$, $h_2=18$ and the true cost $h^*=26$. With $\alpha_1=\alpha_2=0.5$: $h=0.5(8)+0.5(18)=13\le26$, which is admissible.

**Comment.** Admissibility is guaranteed, but $h$ is **never better** than $\max(h_1,h_2)$, which is also admissible and dominates every convex combination. Here $\max=18>13$. So it is better to take the maximum. (Weights with $\alpha_1+\alpha_2>1$ could overestimate, and then admissibility is lost.)
