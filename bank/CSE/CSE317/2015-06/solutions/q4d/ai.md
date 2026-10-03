---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Local beam search keeps k states; at each step it generates all successors of all k states and keeps the k best overall (stopping if a goal appears), so information is shared and search concentrates where progress is made. Random-restart search runs k independent hill climbs that share nothing. Stochastic beam search chooses successors with probability proportional to their value, to keep diversity."
sources: ["AIMA 3e sec. 4.1.3 (local beam search)"]
---
**Local beam search.**

1. Start with $k$ randomly generated states.
2. At each step, generate **all successors of all $k$ states**.
3. If any is a goal, stop. Otherwise select the **$k$ best successors from the complete pool** and repeat.

```text
states <- k random states
loop:
    pool <- all successors of all states
    if some s in pool is a goal: return s
    states <- the k best states in pool
```

**Difference from random-restart hill climbing.** Running $k$ random restarts in parallel looks similar, but the $k$ searches are **independent**: each climbs its own hill and they share no information. In local beam search, **information is passed between the parallel threads**. If one state generates several good successors while the others generate poor ones, the next generation is dominated by the good ones: "Come over here, the grass is greener!". The search concentrates its effort where progress is being made.

**Drawback and fix.** The $k$ states can quickly crowd into a small region, losing diversity, so the method becomes an expensive version of hill climbing. **Stochastic beam search** chooses the $k$ successors at random, with probability increasing with their value, much like natural selection. It is a precursor of genetic algorithms.
