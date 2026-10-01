---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "BFS: complete (finite b), optimal only for equal step costs, O(b^d) time and space. DFS: not complete in infinite spaces, not optimal, O(b^m) time, O(bm) space. UCS: complete, optimal, O(b^(1+C*/e)) time/space. A*: complete and optimal with admissible/consistent h, exponential time/space in the worst case."
sources: ["AIMA 3e sec. 3.4.7 (Figure 3.21) and 3.5.2"]
---
Notation: $b$ = branching factor, $d$ = depth of the shallowest goal, $m$ = maximum depth, $C^*$ = cost of the optimal solution, $\epsilon$ = minimum step cost.

| Criterion | BFS | DFS | UCS | A* |
|:--|:-:|:-:|:-:|:-:|
| Complete? | Yes (if $b$ finite) | No (infinite/looping paths); yes in finite graph search | Yes (if step cost $\ge\epsilon>0$) | Yes (finite $b$, cost $\ge\epsilon$) |
| Optimal? | Only if all step costs equal | No | Yes | Yes if $h$ admissible (tree) / consistent (graph) |
| Time | $O(b^d)$ | $O(b^m)$ | $O(b^{1+\lfloor C^*/\epsilon\rfloor})$ | exponential in the error of $h$; $O(b^d)$ worst case |
| Space | $O(b^d)$ | $O(bm)$ | $O(b^{1+\lfloor C^*/\epsilon\rfloor})$ | keeps all generated nodes: exponential |

**Comments.**

- **BFS** expands the shallowest node first (FIFO queue). It finds the shallowest goal, which is the cheapest only for uniform costs. Memory is the main problem: at depth 10 with $b=10$ it needs about $10^{10}$ nodes.

- **DFS** expands the deepest node (LIFO). Only one path plus siblings is stored, so memory is linear, but it can go down an infinite branch and returns the first solution found, not the best.

- **UCS** expands the node with the lowest path cost $g(n)$. It is optimal for any positive costs, but explores in all directions, so it may do more work than BFS when costs are equal.

- **A*** expands the lowest $f=g+h$. It is *optimally efficient*: no other optimal algorithm using the same $h$ expands fewer nodes. Its practical limit is memory, since it keeps all generated nodes (it runs out of space before time).
