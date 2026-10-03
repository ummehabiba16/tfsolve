---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(i) UCS with all step costs equal (c) expands nodes in order of g = c x depth, i.e. level by level, which is BFS. (ii) Best-first with f = depth gives BFS, f = -depth gives DFS, f = g gives UCS. (iii) A* with h(n) = 0 (admissible) has f = g, which is UCS."
sources: ["AIMA 3e sec. 3.4-3.5 and Exercise 3.21"]
---
**Best-first search:** always expand the frontier node with the lowest evaluation function $f(n)$ (a priority queue ordered by $f$).

**(i) BFS is a special case of uniform-cost search.** UCS expands the node with the lowest path cost $g(n)$. Suppose every step costs the same constant $c>0$. Then $g(n)=c\cdot\text{depth}(n)$, so UCS expands all nodes at depth $d$ (cost $cd$) before any node at depth $d+1$ (cost $c(d+1)$). With ties broken first-in-first-out, this is exactly the order of BFS. (The goal test applied at expansion versus at generation only changes when a goal is detected, not which goal is found.) So **BFS = UCS with equal step costs**.

**(ii) BFS, DFS and UCS are special cases of best-first search**, for these choices of $f$:

- $f(n)=\text{depth}(n)$: the shallowest node first, a FIFO order. This is **BFS**.
- $f(n)=-\text{depth}(n)$: the deepest node first, a LIFO order. This is **DFS**.
- $f(n)=g(n)$: the cheapest path so far first. This is **UCS**.

Each is best-first search with a particular $f$, so all three are special cases.

**(iii) UCS is a special case of A\*.** A\* uses $f(n)=g(n)+h(n)$. Take the heuristic $h(n)=0$ for all $n$. It is admissible (it never overestimates, since costs are $\ge0$) and consistent. Then $f(n)=g(n)$, and A\* expands exactly as UCS does. So **UCS = A\* with $h\equiv0$**.
