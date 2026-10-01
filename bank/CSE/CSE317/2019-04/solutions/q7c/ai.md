---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "IDA* is iterative deepening with an f-cost limit: depth-first search pruning nodes with f = g + h above the current bound, and the next bound is the smallest f that exceeded it. It is complete and optimal with an admissible h, uses only O(bd) memory, but re-expands nodes and suffers with many distinct f values."
sources: ["AIMA 3e sec. 3.5.3 (Memory-bounded heuristic search)", "Korf (1985)"]
---
**Idea.** A* is optimal but stores every generated node, so it runs out of memory. IDA* (Korf, 1985) applies the iterative-deepening idea to A*: instead of a depth limit it uses an **f-cost limit**. Each iteration is a depth-first search that cuts off any node whose $f(n)=g(n)+h(n)$ exceeds the current threshold. The threshold for the next iteration is the **smallest f-value that exceeded the threshold** in the previous iteration.

**Pseudo-code.**

```text
function IDA-STAR(problem):
    bound <- h(start)
    path  <- [start]
    loop:
        t <- SEARCH(path, 0, bound)
        if t = FOUND: return path
        if t = infinity: return failure          // no solution
        bound <- t                               // smallest f that exceeded bound

function SEARCH(path, g, bound):
    node <- LAST(path)
    f <- g + h(node)
    if f > bound: return f                       // cut off; report its f
    if GOAL-TEST(node): return FOUND
    min <- infinity
    for each succ in SUCCESSORS(node), ordered by g + c + h(succ):
        if succ not in path:                     // avoid cycles on the current path
            append succ to path
            t <- SEARCH(path, g + c(node, succ), bound)
            if t = FOUND: return FOUND
            if t < min: min <- t
            remove succ from path
    return min
```

**How it works.**

1. The first threshold is $f(\text{start})=h(\text{start})$, a lower bound on the solution cost.

2. A depth-first search explores every path while $f\le$ bound. All nodes inside the current $f$-contour are expanded.

3. If no goal is found, every cut-off node had $f>$ bound; the smallest such $f$ becomes the new bound, so the next iteration expands the next contour.

4. Because the bound grows to the next smallest $f$, the first goal found has $f=g\le$ the cost of every unexplored path: with an **admissible** $h$, IDA* is **optimal** and **complete** (positive step costs, finite branching).

**Properties.** Space $O(bd)$ (only the current path), like DFS. Time: similar to A* when $f$-values take few distinct values (e.g. 8-puzzle with integer costs), since the last iteration dominates. It has no explored set, so it may re-expand states reached by different paths, and with real-valued costs each iteration may add only one new node, giving $O(N^2)$ work. It was the first algorithm to solve random 15-puzzle instances optimally.
