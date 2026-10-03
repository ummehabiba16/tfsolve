---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(1) Real-valued or widely varying costs make almost every iteration add only one new node, so the number of iterations explodes (up to N^2 work); fix: increase the bound by a fixed epsilon or a percentage (epsilon-admissible), or use RBFS. (2) No memory beyond the current path, so repeated states and transpositions are re-expanded many times in graphs with many paths; fix: a transposition table, or memory-bounded A* (SMA*), which uses all available memory."
sources: ["AIMA 3e sec. 3.5.3 (IDA*, RBFS, SMA*)"]
---
**Reason 1: many distinct $f$-values (real-valued step costs).** IDA\* raises the cutoff to the next smallest $f$ value seen. If costs are real numbers or vary a lot (for example road distances), almost every node has a different $f$. Each iteration then adds only **one new node**, and IDA\* does about $N$ iterations re-expanding everything, so the work grows to $O(N^2)$ instead of $O(N)$.

*Solution:* increase the threshold by a larger step, a fixed $\epsilon$ or a percentage. This gives at most $\epsilon$ suboptimality (an $\epsilon$-admissible search). Or use **RBFS**, which remembers the best alternative $f$-value of each path.

**Reason 2: too little memory, so repeated states are re-expanded.** IDA\* keeps only the current path, so it cannot detect states reached by different paths (transpositions). In graphs with many cycles or alternative paths (grid maps, puzzles with many transpositions), the same states are explored an exponential number of times, both within one iteration and across iterations. It does not use the memory that is available.

*Solution:* add a **transposition table** (a cache of visited states with their $g$ values) to prune duplicates, or use a memory-bounded algorithm such as **SMA\*** (simplified memory-bounded A\*), which uses all available memory and drops only the worst nodes when memory is full.
