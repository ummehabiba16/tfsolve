---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A* expands the frontier node with minimum f(n) = g(n) + h(n) and stops when a goal is selected. With a monotonic (consistent) heuristic, f is non-decreasing along paths, so nodes are expanded in non-decreasing f and each node's first expansion is via an optimal path; hence the first goal expanded is optimal."
sources: ["AIMA 3e sec. 3.5.2"]
---
**Operation of A*.** A* is best-first search with evaluation function

$$f(n)=g(n)+h(n)$$

where $g(n)$ is the cost of the path from the start to $n$ and $h(n)$ is the estimated cost of the cheapest path from $n$ to a goal; $f(n)$ estimates the cost of the cheapest solution through $n$.

```text
function A-STAR(problem):
    frontier <- priority queue ordered by f, containing the start node
    explored <- empty set
    loop:
        if frontier is empty: return failure
        n <- POP(frontier)                      // lowest f
        if GOAL-TEST(n.state): return SOLUTION(n)
        add n.state to explored
        for each action a in ACTIONS(n.state):
            child <- CHILD-NODE(problem, n, a)  // g(child) = g(n) + c(n, a, child)
            if child.state not in explored and not in frontier:
                insert child into frontier
            else if child.state in frontier with higher g:
                replace that frontier node with child
```

**Monotonic (consistent) heuristic.** For every node $n$ and successor $n'$ reached by action $a$:

$$h(n)\le c(n,a,n')+h(n')$$

and $h(G)=0$ for goals (a triangle inequality).

**Proof of optimality.**

*Lemma 1: $f$ is non-decreasing along any path.* For a successor $n'$ of $n$:

$$f(n')=g(n)+c(n,a,n')+h(n')\ge g(n)+h(n)=f(n)$$

*Lemma 2: when A* selects $n$ for expansion, the optimal path to $n$ has been found.* Suppose not. Then some node $n''$ on the optimal path to $n$ is still on the frontier (the frontier separates explored from unexplored states). Because the path through $n''$ to $n$ is cheaper than the path found, and $f$ is non-decreasing along that path, $f(n'')\le g^*(n)+h(n)<g(n)+h(n)=f(n)$, so $n''$ would have been selected before $n$. Contradiction.

*Conclusion.* By the two lemmas, A* expands nodes in non-decreasing order of $f(n)$, each with its optimal $g$. When a goal $G$ is selected, $f(G)=g(G)$ (since $h(G)=0$) is the true cost of the path found, and any other goal $G_2$ selected later has $g(G_2)=f(G_2)\ge f(G)$. Hence the first goal selected is an optimal solution: A* graph search with a monotonic heuristic is optimal. (Consistency implies admissibility, so A* tree search is optimal too.)
