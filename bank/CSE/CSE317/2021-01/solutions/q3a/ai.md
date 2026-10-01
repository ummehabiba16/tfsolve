---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "(i) True: UCS with all step costs equal (e.g. 1) expands nodes in order of depth, exactly BFS. (ii) True: best-first tree search with f(n) = -depth(n) expands the deepest node first, which is DFS. (iii) True: A* with h(n) = 0 has f = g, which is UCS."
sources: ["AIMA 3e Exercise 3.21 and sec. 3.4-3.5"]
---
Best-first search expands the frontier node with the lowest evaluation $f(n)$. UCS uses $f(n)=g(n)$, A* uses $f(n)=g(n)+h(n)$.

**(i) Breadth-first search is a special case of uniform-cost search. True.**

Proof: let all step costs be equal to a positive constant $c$ (e.g. $c=1$). Then $g(n)=c\cdot\text{depth}(n)$. UCS expands the node with the smallest $g$, i.e. the smallest depth, so it expands all nodes at depth $k$ before any at depth $k+1$: exactly the order of BFS (ties broken in FIFO order). So BFS = UCS with uniform step costs.

(The goal-test timing differs slightly: BFS tests on generation, UCS on expansion. This changes only when the goal is reported, not the expansion order; with the test on expansion BFS is literally UCS.)

**(ii) Depth-first search is a special case of best-first tree search. True.**

Proof: use the evaluation function $f(n)=-\text{depth}(n)$. Best-first search then always expands the frontier node of greatest depth, i.e. the most recently generated (deepest) node, which is LIFO order: DFS. (Ties among children of the same node are broken by generation order.)

**(iii) Uniform-cost search is a special case of A* search. True.**

Proof: take the heuristic $h(n)=0$ for all $n$. Then $f(n)=g(n)+0=g(n)$, which is exactly the UCS evaluation function, so A* expands the same nodes in the same order. Moreover $h=0$ is admissible and consistent, consistent with UCS being optimal.
