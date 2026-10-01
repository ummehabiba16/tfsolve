---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "AC-3 queues arcs and REVISEs domains until every value has a support (O(cd^3)). 3-consistency (path consistency): for every consistent assignment to two variables there is a consistent value of any third variable. Modified AC-3 (PC-2 style) keeps a queue of triples/paths and revises the binary constraint between Xi and Xj with respect to every Xm, removing pairs with no support, re-queuing paths that involve a changed constraint."
sources: ["AIMA 3e sec. 6.2.2-6.2.3 (Arc and path consistency)", "Mackworth (1977), PC-2"]
---
**AC-3 (arc consistency / 2-consistency).** $X_i$ is arc-consistent with respect to $X_j$ if every value in $D_i$ has some value in $D_j$ satisfying the binary constraint on $(X_i,X_j)$.

```text
function AC-3(csp):
    queue <- all arcs (Xi, Xj)
    while queue not empty:
        (Xi, Xj) <- REMOVE-FIRST(queue)
        if REVISE(csp, Xi, Xj):
            if Di is empty: return false
            for each Xk in NEIGHBOURS(Xi) - {Xj}: add (Xk, Xi) to queue
    return true

function REVISE(csp, Xi, Xj):
    revised <- false
    for each x in Di:
        if no y in Dj satisfies C(Xi, Xj) with (x, y):
            delete x from Di;  revised <- true
    return revised
```

Complexity $O(cd^3)$ for $c$ constraints and domain size $d$.

**Extending to three variables (3-consistency / path consistency).** A set of two variables $\{X_i,X_j\}$ is path-consistent with respect to a third variable $X_m$ if for **every pair of values** $(a,b)$ that is consistent with the constraint on $\{X_i,X_j\}$, there is a value $c\in D_m$ such that $(a,c)$ satisfies the constraint on $\{X_i,X_m\}$ and $(b,c)$ satisfies the constraint on $\{X_m,X_j\}$. (A CSP is 3-consistent if any consistent assignment to any two variables can be extended to any third.)

So where arc consistency removes **values** from domains, path consistency removes **pairs of values** from binary constraints (it tightens constraints, represented as relations/matrices). Every pair of variables is treated as constrained (with the universal relation if no explicit constraint exists).

Example: colouring a triangle A, B, C with only 2 colours. Each arc is consistent (for any colour of A, B can take the other), so AC-3 finds nothing. Path consistency: the pair (A = red, B = green) has no colour for C that differs from both, so it is removed; likewise every pair; the constraint on $\{A,B\}$ becomes empty and the inconsistency is detected.

**Modified AC-3 for 3-consistency (PC-2 style).**

```text
function PC-3CONSISTENCY(csp):
    queue <- all triples (Xi, Xm, Xj) with i < j, m != i, m != j
    while queue not empty:
        (Xi, Xm, Xj) <- REMOVE-FIRST(queue)
        if REVISE-PATH(csp, Xi, Xm, Xj):
            if R(Xi, Xj) is empty: return false
            for each variable Xk not in {Xi, Xj}:     // paths that use the changed constraint
                add (Xi, Xj, Xk) and (Xj, Xi, Xk) to queue    // i.e. triples with Xi-Xj as an edge
    return true

function REVISE-PATH(csp, Xi, Xm, Xj):
    revised <- false
    for each pair (a, b) in R(Xi, Xj):
        if no c in Dm with (a, c) in R(Xi, Xm) and (c, b) in R(Xm, Xj):
            delete (a, b) from R(Xi, Xj)        // also delete (b, a) from R(Xj, Xi)
            revised <- true
    return revised
```

Changes from AC-3: the queue holds **triples** (paths of length 2) instead of arcs; REVISE deletes **pairs** from the relation $R(X_i,X_j)$ instead of values from a domain; when $R(X_i,X_j)$ changes, every triple in which $X_i$-$X_j$ is one of the two "legs" is re-queued. Unary domains can be included as $R(X_i,X_i)$ so that values with no supporting pairs are also removed (strong 3-consistency). Cost: $O(n^3d^3)$ per sweep; total $O(n^3d^5)$ in the worst case for PC-2.
