---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Literal levels grow monotonically and mutexes shrink monotonically, while the numbers of literals and actions are finite, so the graph must level off. Once it has leveled off, if the goals are still mutex or missing, or the set of nogoods stops changing between two consecutive stages, no plan exists and GraphPlan returns failure. So it always terminates, and since extraction is exhaustive it is complete."
sources: ["AIMA 3e sec. 10.3.2 (termination of GraphPlan) / AIMA 4e sec. 11.3.4"]
---
**GraphPlan.** Repeatedly extend the planning graph by one level. Whenever all goals appear in the last level and are pairwise non-mutex, try EXTRACT-SOLUTION, a backward search for a plan. Record every failed (level, goal set) pair as a **nogood**. Stop with failure when the graph and the nogoods have both leveled off.

**Monotonicity properties** (the key lemmas):

1. **Literals increase monotonically.** If a literal is in $S_i$, it is in $S_{i+1}$ (persistence actions carry it forward).
2. **Actions increase monotonically.** If an action is in $A_i$, it is in $A_{i+1}$ (its preconditions are still present and, by 4, still non-mutex).
3. **Mutexes decrease monotonically.** If two actions are mutex at $A_i$, they are mutex at every earlier level. If they are non-mutex at $A_i$, they remain non-mutex later. (Inconsistent effects and interference are permanent; competing needs can only disappear as more ways of achieving the preconditions appear.) The same holds for literal mutexes.
4. **Nogoods decrease monotonically.** If a goal set is unachievable at level $i$, it is unachievable at every earlier level, because fewer actions and more mutexes are available there.

**Termination.** There are finitely many ground literals and actions. By 1-3, after finitely many levels the graph **levels off**: $S_{i+1}=S_i$ with the same mutexes, and from then on all levels are identical. By 4, the set of nogoods at a level can only shrink as levels are added, and it is finite. So it cannot shrink forever: eventually two consecutive stages have the same nogoods.

**Completeness.** If a plan of length $n$ exists, its literals and actions appear in the graph at levels up to $n$ without mutexes, and EXTRACT-SOLUTION, an exhaustive backward search, finds it. Suppose instead the graph has leveled off and either (a) some goal is missing or two goals are mutex at the leveled-off level, or (b) the nogoods stopped changing between two consecutive extensions. Then extending the graph further cannot add any new possibility, since every future level is identical. So **no plan exists**, and GraphPlan correctly **returns failure**.

Therefore GraphPlan always terminates: with a plan if one exists, and with failure otherwise.
