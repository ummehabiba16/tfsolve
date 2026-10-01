---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Completeness: UCS expands nodes in order of g; with step costs >= e > 0 and finite b there are finitely many nodes with g <= C*, so it reaches the goal. Optimality: when a node is selected for expansion its cheapest path has been found (frontier separation + non-negative costs), so the first goal selected has minimum cost."
sources: ["AIMA 3e sec. 3.4.2 (Uniform-cost search)"]
---
UCS expands the frontier node with the lowest path cost $g(n)$ and applies the goal test when a node is **selected for expansion**. Assume step costs $\ge\epsilon>0$ and finite branching factor $b$.

**Completeness.** Let $C^*$ be the cost of an optimal solution. Every path of cost $\le C^*$ has at most $\lfloor C^*/\epsilon\rfloor$ steps, so with finite $b$ there are only finitely many nodes with $g(n)\le C^*$. UCS expands nodes in non-decreasing order of $g$, so after expanding finitely many nodes it must select the goal node on the optimal path (its $g=C^*$). Hence UCS is complete. (If some step cost were 0, it could loop forever along zero-cost cycles, which is why $\epsilon>0$ is needed.)

**Optimality.**

1. *Path costs never decrease along a path*, since step costs are non-negative: $g(n')=g(n)+c(n,a,n')\ge g(n)$.

2. *When UCS selects a node $n$, it has found the optimal path to $n$.* Suppose not: there is a cheaper path to $n$. By the graph separation property, some node $n'$ of that cheaper path is on the frontier. Then $g(n')\le$ cost of the cheaper path $<g(n)$, so UCS would have selected $n'$ before $n$. Contradiction.

3. Since nodes are selected in non-decreasing order of $g$ and the goal test is applied at selection, the first goal selected $G$ has $g(G)\le g(G')$ for every goal $G'$ selected later, and $g(G)$ is the cost of the optimal path to it. Hence the solution returned is optimal. $\blacksquare$
