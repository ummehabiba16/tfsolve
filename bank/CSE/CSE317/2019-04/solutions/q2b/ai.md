---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "A planning graph is a layered graph of alternating literal levels S_i and action levels A_i (with persistence actions), plus mutex links, built in polynomial time. Two actions at a level are mutex if they have inconsistent effects, interfere, or have competing needs."
sources: ["AIMA 3e sec. 10.3 (planning graphs) / AIMA 4e sec. 11.3.4"]
---
**Planning graph.** A directed, leveled graph for a planning problem (propositional or ground actions):

- **Levels $S_0, A_0, S_1, A_1, \dots$** alternate. $S_0$ contains the literals true in the initial state. $A_i$ contains every action whose preconditions all appear in $S_i$ without being mutex. $S_{i+1}$ contains all effects of the actions in $A_i$.
- **Persistence (no-op) actions** carry each literal from $S_i$ to $S_{i+1}$.
- **Mutex links** join pairs of actions or literals that cannot occur together at that level.

The literals in $S_i$ over-approximate those that could be true after $i$ steps. The graph grows polynomially and "levels off" (two consecutive levels identical). It is used to derive admissible heuristics (level cost, max-level, level-sum, set-level) and to extract plans (GraphPlan).

**Mutex between two actions at the same level.**

1. **Inconsistent effects:** one action negates an effect of the other. *Example:* $Eat(Cake)$ has effect $\neg Have(Cake)$, while the persistence of $Have(Cake)$ has effect $Have(Cake)$.
2. **Interference:** one action's effect negates a **precondition** of the other. *Example:* $Eat(Cake)$ deletes $Have(Cake)$, which is the precondition of the persistence of $Have(Cake)$.
3. **Competing needs:** a precondition of one action is mutex with a precondition of the other at the previous literal level. *Example:* $Bake(Cake)$ needs $\neg Have(Cake)$ and $Eat(Cake)$ needs $Have(Cake)$; those literals are mutex.

(Two literals are mutex if one is the negation of the other, or if every pair of actions that could achieve them is mutex: *inconsistent support*.)
