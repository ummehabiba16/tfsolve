---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "IDA* is iterative deepening with an f-cost cutoff instead of a depth limit: run depth-first search that prunes any node with f = g + h > cutoff; if no goal is found, raise the cutoff to the smallest f-value that exceeded it, and repeat. It is complete and optimal with admissible h, and uses O(bd) memory."
sources: ["AIMA 3e sec. 3.5.3 (memory-bounded heuristic search: IDA*)", "Korf 1985"]
---
**Idea.** IDA\* (Korf, 1985) applies the iterative-deepening idea to A\*. Instead of a depth limit, each iteration uses an **$f$-cost cutoff**. A depth-first search explores every node with $f(n)=g(n)+h(n)\le$ cutoff and prunes the rest. If the goal is not found, the next cutoff is the **smallest $f$ that exceeded** the current cutoff. The first cutoff is $f(\text{root})=h(\text{root})$.

**Pseudocode.**

```text
function IDA*(problem) returns a solution or failure
    root <- MAKE-NODE(problem.INITIAL-STATE)
    bound <- h(root)
    loop
        t <- DFS-CONTOUR(root, 0, bound)
        if t = FOUND then return the solution path
        if t = infinity then return failure
        bound <- t                       # smallest f that exceeded the old bound

function DFS-CONTOUR(node, g, bound) returns FOUND or a new bound
    f <- g + h(node)
    if f > bound then return f           # prune; report the overflow value
    if GOAL-TEST(node) then return FOUND
    min <- infinity
    for each child in EXPAND(node):
        if child not on current path then            # avoid cycles
            t <- DFS-CONTOUR(child, g + cost(node, child), bound)
            if t = FOUND then return FOUND
            if t < min then min <- t
    return min
```

**How it works.** Each iteration is a depth-first search that explores one more "$f$-contour" of the state space. Within an iteration, memory is only the current path, $O(bd)$, unlike A\*'s exponential frontier.

- **Complete and optimal** if $h$ is admissible (and costs are $\ge\epsilon$). The first goal found has $f=g\le$ the current bound, which is $\le C^*$.
- **Time:** if $f$ values are integers from a small range (e.g. the 8- or 15-puzzle with Manhattan distance), there are few iterations, and the total work is dominated by the last one, like IDS. It was the first algorithm to solve random 15-puzzles optimally.
