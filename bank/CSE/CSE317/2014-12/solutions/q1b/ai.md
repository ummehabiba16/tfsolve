---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Example: X_i < X_j with D_i = {1, 2, 3} and D_j = {1, 2, 3}: the value X_i = 3 has no y > 3 in D_j, so the arc fails. Fix it by REVISE: delete the unsupported values from D_i (D_i = {1, 2}); this removes no solution."
sources: ["AIMA 3e sec. 6.2.2 (REVISE, AC-3)"]
---
**Example of an arc that is not consistent.** Variables $X_i$ and $X_j$ with $D_i=D_j=\{1,2,3\}$ and the constraint $X_i<X_j$.

- Arc $X_i\to X_j$: for $X_i=3$ there is **no** $y\in D_j$ with $3<y$. So the arc is **not** arc-consistent.
- (Likewise, for $X_j\to X_i$, $X_j=1$ has no support.)

Another example: map colouring with $D_{WA}=\{red\}$ and $D_{NT}=\{red, green\}$. The arc $NT\to WA$ fails for $NT=red$.

**How to fix it.** Apply **REVISE**$(X_i,X_j)$: delete from $D_i$ every value with no support in $D_j$.

- $D_i\leftarrow\{x\in D_i:\exists y\in D_j,\ x<y\}=\{1,2\}$. Now $X_i\to X_j$ is consistent.
- Deleted values cannot be part of any solution, so no solution is lost.

When $D_i$ shrinks, arcs $X_k\to X_i$ that were consistent may now fail, so they must be rechecked. AC-3 does this with a queue of arcs.
