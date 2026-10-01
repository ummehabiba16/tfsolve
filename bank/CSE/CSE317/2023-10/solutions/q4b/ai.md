---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "There are at most 2c directed arcs; an arc (Xk, Xi) is re-queued only when Di loses a value, at most d times, so at most O(cd) revisions; each REVISE compares all value pairs, O(d^2); total O(cd^3), i.e. cubic in d (O(n^2 d^3) since c <= n^2)."
sources: ["AIMA 3e sec. 6.2.2 (AC-3 complexity)"]
---
**AC-3 recap.** A queue initially holds every directed arc $(X_i,X_j)$. Repeatedly remove an arc and call REVISE$(X_i,X_j)$, which deletes from $D_i$ every value with no supporting value in $D_j$. If $D_i$ shrank, every arc $(X_k,X_i)$, $X_k$ a neighbour of $X_i$ other than $X_j$, is added back to the queue.

**Complexity.** Let $n$ = number of variables, $c$ = number of binary constraints, $d$ = maximum domain size.

1. *Number of arcs.* Each binary constraint gives two directed arcs, so there are at most $2c$ arcs, i.e. $O(c)$.

2. *How often an arc is processed.* An arc $(X_k,X_i)$ enters the queue at the start, and afterwards only when the domain of $X_i$ loses at least one value. $D_i$ has at most $d$ values, so this happens at most $d$ times. Hence each arc is processed at most $d+1$ times, and the total number of REVISE calls is

$$O(c)\cdot O(d)=O(cd)$$

3. *Cost of one REVISE.* For each of the at most $d$ values $x\in D_i$ we search $D_j$ (at most $d$ values) for a $y$ consistent with $x$: $O(d^2)$ constraint checks.

4. *Total.*

$$O(cd)\times O(d^2)=O(cd^3)$$

which is cubic in the domain size. Since $c\le n(n-1)/2=O(n^2)$, the bound can also be written $O(n^2d^3)$.

Note: checking arc consistency once does not reveal every inconsistency, but this polynomial bound is why AC-3 is a cheap preprocessing/propagation step compared with exponential backtracking. With support bookkeeping (AC-4, AC-2001) it improves to $O(cd^2)$.
