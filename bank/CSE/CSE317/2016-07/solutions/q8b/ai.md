---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A CSP is strongly k-consistent if it is j-consistent for every j <= k (any consistent assignment to j-1 variables extends to any j-th variable). With strong n-consistency over n variables, assign X1 any value, then for each next Xi pick a value consistent with the previous ones; one always exists, so no backtracking: O(n^2 d) time."
sources: ["AIMA 3e sec. 6.2.3 (K-consistency)"]
---
**k-consistency.** A CSP is **k-consistent** if, for any set of $k-1$ variables and any consistent assignment to them, a consistent value can always be assigned to **any** $k$-th variable. 1-consistency is node consistency, 2-consistency arc consistency, 3-consistency path consistency.

**Strongly k-consistent.** A CSP is strongly $k$-consistent if it is $j$-consistent for **every** $j\le k$ ($1,2,\dots,k$-consistent).

**Solving a strongly n-consistent CSP with n variables without backtracking.**

```text
function SOLVE-STRONG-N-CONSISTENT(csp with variables X1..Xn):
    for i = 1 to n:
        for each value v in D(Xi):
            if v is consistent with the values of X1..X(i-1):
                assign Xi = v;  break
    return the assignment
```

**Why it never backtracks.**

- $X_1$: by node (1-)consistency every value in $D_1$ satisfies the unary constraints, so pick any.

- $X_2$: by 2-consistency, the consistent assignment to $X_1$ can be extended to $X_2$, so a value exists.

- In general, after consistently assigning $X_1,\dots,X_{i-1}$, $i$-consistency (implied by strong $n$-consistency for $i\le n$) guarantees a value for $X_i$ consistent with all of them. So each step finds a value and the search reaches a full solution without ever backtracking.

**Time.** For each variable $X_i$ we scan at most $d$ values and check each against at most $n$ assigned variables: $O(nd)$ per variable, $O(n^2d)$ total, which is polynomial.

**Catch.** Establishing strong $n$-consistency in the first place takes time exponential in $n$ in the worst case (and exponential space), so in practice one enforces only 2- or 3-consistency.
