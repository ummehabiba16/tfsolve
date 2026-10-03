---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "RBFS is a recursive best-first search in linear space: it explores the best child while its f is within f_limit (the best alternative f from the ancestors); if it is exceeded, it unwinds and replaces the node's f with the best child f (backed-up value). Preferred to A* because it needs only O(bd) memory, while A* stores all generated nodes (exponential), and it is still optimal with admissible h."
sources: ["AIMA 3e sec. 3.5.3 (RBFS, Fig. 3.26)"]
---
**Pseudocode** (12).

```text
function RECURSIVE-BEST-FIRST-SEARCH(problem) returns a solution or failure
    return RBFS(problem, MAKE-NODE(problem.INITIAL-STATE), infinity)

function RBFS(problem, node, f_limit) returns a solution or failure, and a new f-cost limit
    if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
    successors <- [ ]
    for each action in problem.ACTIONS(node.STATE):
        add CHILD-NODE(problem, node, action) to successors
    if successors is empty then return failure, infinity
    for each s in successors:                # update f with the value from the previous search
        s.f <- max(s.g + s.h, node.f)
    loop
        best <- the lowest f-value node in successors
        if best.f > f_limit then return failure, best.f
        alternative <- the second-lowest f-value among successors
        result, best.f <- RBFS(problem, best, min(f_limit, alternative))
        if result != failure then return result
```

**How it works.** RBFS behaves like a depth-first search that always follows the currently best child. It keeps track of `f_limit`, the $f$-value of the **best alternative path** available from any ancestor. When the best child's $f$ exceeds this limit, the recursion **unwinds**, and on the way back it replaces each node's $f$ by the **best $f$ of its children** (the backed-up value). The value of the forgotten subtree is remembered, so RBFS can decide later whether to re-expand it.

**Why use it instead of A\*** (3). A\* keeps every generated node in memory, which is **exponential** in the depth, so it runs out of memory on large problems. RBFS needs only **$O(bd)$** memory (the current path and its siblings). It is still **optimal** if $h$ is admissible, and it is more efficient than IDA\*. The price is that nodes may be regenerated several times.
