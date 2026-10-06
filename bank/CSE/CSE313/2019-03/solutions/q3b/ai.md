---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Detection algorithm with matrices E, A, C, R; for the given state P2 and P3 can finish, P1 and P4 stay unmarked, so P1 and P4 are deadlocked."
sources: ["Tanenbaum MOS 4e, sec. 6.4.2 (deadlock detection with multiple resources of each type)"]
---
**Matrices.** $n$ processes, $m$ resource classes.

- $E=(E_1,\dots,E_m)$: **existing** resource vector (total number of instances of each class).
- $A=(A_1,\dots,A_m)$: **available** resource vector (instances currently free).
- $C$ ($n\times m$): **current allocation** matrix; $C_{ij}$ = instances of resource $j$ held by process $i$.
- $R$ ($n\times m$): **request** matrix; $R_{ij}$ = instances of resource $j$ that process $i$ still wants.

Invariant: $\sum_i C_{ij}+A_j=E_j$.

**Algorithm.**

1. Look for an **unmarked** process $P_i$ whose row of $R$ is $\le A$ (component-wise).
2. If found, add the $i$-th row of $C$ to $A$ (the process could finish and release its resources), **mark** the process and go to step 1.
3. If no such process exists, stop. Every process that is **unmarked** is **deadlocked**.

**Given state.**

$$C=\begin{pmatrix}0&1&1&1&2\\0&1&0&1&0\\0&0&0&0&1\\2&1&0&0&0\end{pmatrix}$$

$$R=\begin{pmatrix}1&1&0&2&1\\0&1&0&2&1\\0&2&0&3&1\\0&2&1&1&0\end{pmatrix}$$

$E=(2,4,1,4,4)$, $A=(0,1,0,2,1)$. (Check: column sums of $C$ are $(2,3,1,2,3)$, plus $A$ gives $E$.)

| Step | Candidate | $R_i\le A$? | Result | New $A$ |
|:-:|:-:|:--|:--|:-:|
| 1 | P1 $(1,1,0,2,1)$ | $1>0$: no | | |
| 2 | P2 $(0,1,0,2,1)$ | yes | mark P2, add $C_2=(0,1,0,1,0)$ | $(0,2,0,3,1)$ |
| 3 | P1 | $1>0$: no | | |
| 4 | P3 $(0,2,0,3,1)$ | yes | mark P3, add $C_3=(0,0,0,0,1)$ | $(0,2,0,3,2)$ |
| 5 | P1 | $1>0$: no | | |
| 6 | P4 $(0,2,1,1,0)$ | $1>0$ (RS3): no | | |

No more process can be satisfied. **P1 and P4 are unmarked, so the system is deadlocked and P1 and P4 are the deadlocked processes** (P1 holds the only instance of RS3 and wants RS1, which is held by P4; P4 wants RS3).
