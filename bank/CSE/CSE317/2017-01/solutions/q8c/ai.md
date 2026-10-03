---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(i) Arc X_i -> X_j is arc-consistent if for every value of X_i there is some value of X_j satisfying the constraint; it fails when some value of X_i has no support; fix it by deleting the unsupported values from D_i. (ii) AC-3: a queue of all arcs; pop (X_i, X_j); if REVISE removes values from D_i, add all (X_k, X_i), k != j; fail if a domain empties. (iii) At most c = O(n^2) arcs; each arc is re-inserted at most d times (once per deletion from D_i); REVISE costs O(d^2), giving O(c d^3) = O(n^2 d^3)."
sources: ["AIMA 3e sec. 6.2.2 (arc consistency, AC-3, Fig. 6.3)"]
---
**(i) Arc consistency.** A directed arc $X_i\to X_j$ is **arc-consistent** if for **every** value $x\in D_i$ there is **some** value $y\in D_j$ such that $(x,y)$ satisfies the binary constraint between $X_i$ and $X_j$.

*How it can fail:* some value $x\in D_i$ has no compatible (supporting) value in $D_j$. For example, with $X_i<X_j$, $D_i=\{1,2,3\}$ and $D_j=\{1,2\}$, the value $X_i=2$ needs $X_j>2$, but there is none.

*Fix (REVISE):* delete every unsupported value from $D_i$. This never removes a solution. Here $D_i$ becomes $\{1\}$, and the arc is consistent.

**(ii) AC-3 algorithm.**

```text
function AC-3(csp) returns false if an inconsistency is found, true otherwise
    queue <- all arcs (Xi, Xj) in csp
    while queue not empty:
        (Xi, Xj) <- REMOVE-FIRST(queue)
        if REVISE(csp, Xi, Xj):
            if size of Di = 0 then return false
            for each Xk in NEIGHBORS(Xi) - {Xj}:
                add (Xk, Xi) to queue          # Di shrank: recheck arcs into Xi

function REVISE(csp, Xi, Xj) returns true iff Di was revised
    revised <- false
    for each x in Di:
        if no value y in Dj satisfies the constraint between Xi and Xj:
            delete x from Di;  revised <- true
    return revised
```

When it finishes, every arc is consistent (or a domain is empty, and there is no solution).

**(iii) Time complexity $O(n^2d^3)$.**

- With $n$ variables, there are at most $c\le n(n-1)$ directed arcs, so $c=O(n^2)$.
- Arc $(X_k,X_i)$ is added to the queue only when a value is deleted from $D_i$. $D_i$ has at most $d$ values, so each arc is inserted **at most $d$ times**.
- Each call to REVISE checks every pair $(x,y)\in D_i\times D_j$: $O(d^2)$.

$$\text{Total}=O(\underbrace{c}_{\text{arcs}}\cdot\underbrace{d}_{\text{insertions}}\cdot\underbrace{d^2}_{\text{REVISE}})=O(cd^3)=O(n^2d^3).$$
