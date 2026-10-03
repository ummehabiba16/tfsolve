---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "3-consistency (path consistency): a set {X_i, X_j} is consistent with X_m if every consistent assignment to X_i and X_j can be extended to a value of X_m satisfying the constraints on (X_i, X_m) and (X_m, X_j). Example: a triangle A, B, C with domains {red, green} and pairwise != is arc-consistent, but the pair (A = red, B = green) has no value for C, so it is not 3-consistent. Impose it by tightening the binary constraint (A, B) to the pairs that can be extended (here none, which proves there is no solution), as PC-2 does."
sources: ["AIMA 3e sec. 6.2.3 (path consistency, k-consistency)"]
---
**Extending arc consistency to three variables** (5). **Path consistency (3-consistency):** a two-variable set $\{X_i,X_j\}$ is path-consistent with respect to a third variable $X_m$ if, for **every** assignment $\{X_i=a,X_j=b\}$ consistent with the constraints on $\{X_i,X_j\}$, there is a value $c\in D_m$ such that $\{X_i=a,X_m=c\}$ and $\{X_m=c,X_j=b\}$ are also consistent. Every consistent pair can be extended to the third variable.

(In general, $k$-consistency: any consistent assignment to $k-1$ variables can be extended to any $k$-th variable. 2-consistency is arc consistency.)

**Example of failure, and how to impose it** (5). Colour three mutually adjacent regions $A$, $B$, $C$ (a triangle), each with domain {red, green} and constraints $A\neq B$, $B\neq C$, $A\neq C$.

- *Arc-consistent:* every value has a supporting value in each neighbour, so AC-3 deletes nothing.
- *Not 3-consistent:* the consistent pair $\{A=red, B=green\}$ cannot be extended to $C$. $C=red$ violates $A\neq C$, and $C=green$ violates $B\neq C$. The same holds for $\{A=green, B=red\}$.

**Imposing 3-consistency** (as in PC-2, the path-consistency analogue of AC-3): for each triple $(X_i,X_m,X_j)$, **tighten the binary constraint** $R_{ij}$ by deleting every allowed pair $(a,b)$ that has no extension $c$ in $D_m$:

$$R_{ij}\leftarrow\{(a,b)\in R_{ij}:\exists c\in D_m,\ (a,c)\in R_{im}\land(c,b)\in R_{mj}\}.$$

Repeat with a queue until no relation changes. In the example, $R_{AB}$ loses both pairs (red, green) and (green, red) and becomes **empty**, which proves the CSP has no solution, something arc consistency could not detect. The cost is higher: $O(n^3d^3)$ for path consistency.
