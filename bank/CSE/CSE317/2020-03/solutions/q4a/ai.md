---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "MRV picks the variable most likely to fail (fail-first) to prune the tree early; LCV tries the value leaving most options (fail-last) since one solution suffices. AC-3 queues arcs, REVISE deletes unsupported values and re-queues incoming arcs; worst case O(cd^3) = O(n^2 d^3)."
sources: ["AIMA 3e sec. 6.2.2 and 6.3.1"]
---
**Heuristics.**

- **Most constrained variable (MRV, minimum remaining values)**: choose the unassigned variable with the fewest legal values. All variables must be assigned anyway; picking the one most likely to fail first ("fail-first") discovers dead ends near the root, so the subtree that is pruned is large. A variable with no legal values is detected immediately.

- **Least constraining value (LCV)**: try first the value that removes the fewest values from the neighbours' domains ("fail-last"). We need only one solution, so we choose the value most likely to lead to one, keeping maximum flexibility for later variables.

Example: Australia map colouring with WA = red, NT = green: MRV chooses SA (only blue left); for Q, LCV prefers red over blue (blue would leave SA with no colour).

**AC-3 algorithm.**

```text
function AC-3(csp) returns false if an inconsistency is found, else true
    queue <- all arcs (Xi, Xj) in csp
    while queue is not empty:
        (Xi, Xj) <- REMOVE-FIRST(queue)
        if REVISE(csp, Xi, Xj):
            if size of Di = 0: return false
            for each Xk in Xi.NEIGHBOURS - {Xj}:
                add (Xk, Xi) to queue
    return true

function REVISE(csp, Xi, Xj) returns true iff Di was revised
    revised <- false
    for each x in Di:
        if no value y in Dj allows (x, y) to satisfy the constraint:
            delete x from Di
            revised <- true
    return revised
```

It makes every arc consistent: each value of $X_i$ has a supporting value in $X_j$. When $D_i$ shrinks, arcs into $X_i$ must be rechecked. An empty domain means the CSP has no solution.

**Worst-case complexity.** $n$ variables, $c$ binary constraints ($2c$ arcs), domain size $\le d$. An arc $(X_k,X_i)$ is re-inserted only when $D_i$ loses a value, at most $d$ times, so there are $O(cd)$ calls of REVISE, each costing $O(d^2)$:

$$O(cd)\cdot O(d^2)=O(cd^3)=O(n^2d^3)$$
