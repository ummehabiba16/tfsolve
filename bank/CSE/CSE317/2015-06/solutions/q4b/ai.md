---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "A*'s main problem is memory: it keeps every generated node, exponential in the depth. RBFS mimics best-first search in linear space O(bd): it is a recursive DFS that tracks the f-value of the best alternative path; when the current node's f exceeds that limit it backs up, replacing each node's f with the best f of its children (remembering the forgotten subtree's value), so it can return later. Example: Romania, from Arad via Rimnicu Vilcea, then Fagaras, then back to Rimnicu Vilcea and Pitesti to Bucharest (418)."
sources: ["AIMA 3e sec. 3.5.3 (RBFS, Fig. 3.26-3.27)"]
---
**Main problem of A\*.** It keeps **all generated nodes** in memory (the frontier and explored sets). The number of nodes within the goal contour is usually exponential in the solution depth, so A\* runs out of **memory** long before it runs out of time on large problems.

**Recursive best-first search (RBFS)** imitates best-first search using only **linear space**, $O(bd)$.

- It is a recursive depth-first search that keeps track of the **$f$-limit**: the $f$-value of the **best alternative** path available from any ancestor of the current node.
- If the current node's $f$ exceeds this limit, the recursion **unwinds** back to the alternative path.
- While unwinding, RBFS **replaces each node's $f$-value with the best $f$ of its children** (the backed-up value). It thus remembers the quality of the best leaf in the forgotten subtree, and can decide later whether to re-expand that subtree.

```text
function RBFS(problem, node, f_limit) returns a solution or failure, and a new f-cost limit
    if GOAL-TEST(node) then return SOLUTION(node)
    successors <- children of node; if empty return failure, infinity
    for each s in successors: s.f <- max(s.g + s.h, node.f)
    loop
        best <- lowest-f successor
        if best.f > f_limit then return failure, best.f
        alternative <- second-lowest f among successors
        result, best.f <- RBFS(problem, best, min(f_limit, alternative))
        if result != failure then return result
```

**Example: Romania, Arad to Bucharest**, with $h$ = straight-line distance.

1. From Arad, the best child is Sibiu (393). Its best child is Rimnicu Vilcea (413); the alternative is Fagaras (415).
2. Below Rimnicu Vilcea, the best child is Pitesti (417), which exceeds the limit 415. Unwind: Rimnicu Vilcea's $f$ becomes **417**.
3. Expand Fagaras (415): its child Bucharest has $f=450>417$. Unwind: Fagaras's $f$ becomes **450**.
4. Re-expand Rimnicu Vilcea (417), then Pitesti, then **Bucharest (418)**, the optimal solution.

RBFS is optimal if $h$ is admissible, and uses $O(bd)$ memory. Its drawback is that it may regenerate nodes many times.
