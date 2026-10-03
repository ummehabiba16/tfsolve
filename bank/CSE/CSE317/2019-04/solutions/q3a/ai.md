---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "A relaxed problem has fewer restrictions, so its optimal cost is an admissible heuristic. Ignore-preconditions: every action applies anywhere, so h is about the number of unsatisfied goal literals (a set-cover bound). Ignore-delete-lists: actions never undo goals, so progress is monotonic; computing h+ exactly is NP-hard but approximations (hill climbing on the relaxed problem, FF) work well."
sources: ["AIMA 3e sec. 10.2.3 (heuristics for planning) / AIMA 4e sec. 11.3.2"]
---
**Relaxed problem.** Remove some restrictions from the action schemas, so that the state space gains edges (more actions apply, or they have fewer bad effects). Any solution of the original problem is also a solution of the relaxed one, so the relaxed optimal cost is $\le$ the true cost. Hence **the cost of an optimal relaxed solution is an admissible heuristic**, and it should be cheap to compute.

**Blocks world schemas** (example):

$$Move(b,x,y):\ \textit{Pre: } On(b,x)\land Clear(b)\land Clear(y)\quad \textit{Eff: } On(b,y)\land Clear(x)\land\neg On(b,x)\land\neg Clear(y)$$

$$MoveToTable(b,x):\ \textit{Pre: } On(b,x)\land Clear(b)\quad \textit{Eff: } On(b,Table)\land Clear(x)\land\neg On(b,x)$$

**Ignore-preconditions heuristic.** Drop all preconditions. Every action applies in every state, and one action can achieve each of its effects directly.

- If each action achieves one goal literal, $h(s)$ = the **number of unsatisfied goal literals** (slightly more care is needed if an action also undoes a goal).
- More precisely, $h$ = the minimum number of actions whose effects cover all unsatisfied goals, a **set-cover** problem. Greedy set cover approximates it (but then $h$ may lose admissibility).
- *Blocks world:* $h(s)$ = the number of $On(\cdot,\cdot)$ goals not yet true. For example, the goal $On(A,B)\land On(B,C)$ from a state where neither holds gives $h=2$: each $Move$ achieves one $On$ goal, because a block can be moved even if something is on top of it.

**Ignore-delete-lists heuristic.** Remove all negative effects (assume all goals and preconditions are positive literals). Now no action can undo progress: the relaxed problem is **monotonic**, and a plan never has to re-achieve anything.

- *Blocks world:* moving $A$ onto $B$ no longer deletes $On(A,x)$ or $Clear(B)$. Blocks can be "in two places", and $Clear(B)$ stays true, so other moves stay possible.
- The optimal relaxed plan length $h^{+}$ is admissible but NP-hard to compute exactly. In practice it is approximated quickly: by **hill climbing** on the relaxed problem, or with the planning graph as in FF. This gives a very informative heuristic.
