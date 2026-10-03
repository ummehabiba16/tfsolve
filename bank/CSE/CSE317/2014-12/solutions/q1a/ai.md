---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "A solution is a complete, consistent assignment: every variable gets a value from its domain and every constraint in C is satisfied. Arc X_i -> X_j is arc-consistent if for every value x in D_i there is some y in D_j such that (x, y) satisfies the constraint on (X_i, X_j)."
sources: ["AIMA 3e sec. 6.1 and 6.2.2"]
---
**Solution of a CSP** (3). An **assignment** gives values to some or all variables, $\{X_i=v_i\}$ with $v_i\in D_i$.

- It is **consistent** (legal) if it violates no constraint in $C$.
- It is **complete** if every variable is assigned.

A **solution** is a **complete and consistent** assignment: every $X_i\in X$ gets a value from $D_i$, and every constraint $C_k$ is satisfied by the values of the variables in its scope. (Some CSPs also need a solution that maximizes an objective.)

**Arc consistency** (3). For a binary constraint between $X_i$ and $X_j$, the directed arc $X_i\to X_j$ is **arc-consistent** iff

$$\forall x\in D_i\ \ \exists y\in D_j:\ (x,y)\text{ satisfies the constraint on }(X_i,X_j).$$

Every value of $X_i$ must have at least one compatible ("supporting") value in $X_j$. The arc relation is directional: $X_i\to X_j$ may be consistent while $X_j\to X_i$ is not. A network is arc-consistent if every arc is.
