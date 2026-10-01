---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "AC-3 keeps a queue of arcs, revises each arc by deleting values without support, and re-queues the arcs into a variable whose domain shrank; worst case O(c d^3). Time is reduced by re-adding only the arcs (Xk, Xi) with k != j, keeping the queue duplicate-free, and remembering the last support of each value (AC-2001 / AC-4) to get O(c d^2)."
sources: ["AIMA 3e sec. 6.2.2 (Arc consistency, AC-3)", "Bessiere and Regin, AC-2001"]
---
**Arc consistency.** $X_i$ is arc-consistent with respect to $X_j$ if for every value $x$ in $D_i$ there is some value $y$ in $D_j$ satisfying the constraint on $(X_i,X_j)$. A CSP is arc-consistent if every arc is.

**AC-3.**

```text
function AC-3(csp):
    queue <- all arcs (Xi, Xj) of csp          // both directions
    while queue is not empty:
        (Xi, Xj) <- REMOVE-FIRST(queue)
        if REVISE(csp, Xi, Xj):
            if Di is empty: return false        // inconsistency found
            for each Xk in NEIGHBOURS(Xi) - {Xj}:
                add (Xk, Xi) to queue
    return true

function REVISE(csp, Xi, Xj):
    revised <- false
    for each x in Di:
        if no y in Dj satisfies the constraint between Xi and Xj:
            delete x from Di
            revised <- true
    return revised
```

When $D_i$ shrinks, arcs $(X_k,X_i)$ pointing *into* $X_i$ may lose their support, so they are re-checked.

**Time requirement.** With $n$ variables, $c$ binary constraints and domain size $d$: each arc $(X_k,X_i)$ can be re-inserted only when $D_i$ loses a value, i.e. at most $d$ times, so at most $O(cd)$ arc revisions; REVISE costs $O(d^2)$. Total $O(cd^3)$.

**Reducing the time.**

1. *Re-add only necessary arcs.* After revising $(X_i,X_j)$, do not re-add $(X_j,X_i)$: values removed from $D_i$ had no support in $D_j$, so they cannot have been supports for $D_j$'s values. (Already done above with NEIGHBOURS $-\{X_j\}$.)

2. *Duplicate-free queue.* Keep the queue as a set; an arc already waiting is not added again.

3. *Remember supports (AC-2001).* For each value $x$ of $X_i$ and each neighbour $X_j$ store `last[Xi, x, Xj]`, the support found last time. When the arc is revised again, first check whether that support is still in $D_j$; only if it was deleted, continue scanning $D_j$ **after** it, never from the beginning:

```text
function REVISE-2001(csp, Xi, Xj):
    revised <- false
    for each x in Di:
        y <- last[Xi, x, Xj]
        if y is still in Dj: continue           // O(1) check, support still valid
        y <- next value in Dj after y that is compatible with x (or none)
        if y = none:
            delete x from Di;  revised <- true
        else:
            last[Xi, x, Xj] <- y
    return revised
```

Each value scans each neighbouring domain only once in total over the whole run, so the total work per arc is $O(d^2)$ and the algorithm runs in $O(cd^2)$, which is optimal (AC-4 achieves the same bound by keeping a counter of supports for every value).

4. *Ordering heuristics:* process arcs whose variables have the smallest domains first, which tends to discover wipe-outs earlier.
