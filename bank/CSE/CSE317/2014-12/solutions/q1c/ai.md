---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "AC-3: put all arcs in a queue; pop (X_i, X_j); if REVISE deletes values from D_i, fail if D_i is empty, else push (X_k, X_i) for every other neighbour X_k. Complexity: c = O(n^2) arcs, each re-inserted at most d times (once per deletion from D_i), REVISE O(d^2), so O(c d^3) = O(n^2 d^3)."
sources: ["AIMA 3e sec. 6.2.2, Fig. 6.3 (AC-3)"]
---
**AC-3 algorithm** (7).

```text
function AC-3(csp) returns false if an inconsistency is found, true otherwise
    queue <- all arcs in csp
    while queue is not empty:
        (Xi, Xj) <- REMOVE-FIRST(queue)
        if REVISE(csp, Xi, Xj):
            if size of Di = 0 then return false
            for each Xk in Xi.NEIGHBORS - {Xj}:
                add (Xk, Xi) to queue

function REVISE(csp, Xi, Xj) returns true iff we revise the domain of Xi
    revised <- false
    for each x in Di:
        if no value y in Dj allows (x, y) to satisfy the constraint between Xi and Xj:
            delete x from Di;  revised <- true
    return revised
```

It ends with an arc-consistent CSP that has the same solutions, or reports failure (an empty domain).

**Proof of the $O(n^2d^3)$ time complexity** (7).

1. A binary CSP with $n$ variables has at most $c\le n(n-1)=O(n^2)$ directed arcs.
2. An arc $(X_k,X_i)$ is (re)inserted into the queue only when **$D_i$ loses a value**. $D_i$ has at most $d$ values, so each arc enters the queue **at most $d$ times** (plus the initial insertion).
3. Each processing of an arc calls REVISE, which checks every pair in $D_i\times D_j$: **$O(d^2)$**.

$$\text{Total time}\le c\cdot d\cdot O(d^2)=O(cd^3)=O(n^2d^3).$$
