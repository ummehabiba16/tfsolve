---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Complete: always finds a solution if one exists; optimal: finds the least-cost one. BFS is complete (finite b) and optimal for equal step costs; DFS is complete only in finite graphs (graph search) and not optimal. Worst case: BFS O(b^d) time and space; DFS O(b^m) time, O(bm) space."
sources: ["AIMA 3e sec. 3.3.2, 3.4.1, 3.4.3 (Figure 3.21)"]
---
**Complete**: a search strategy is complete if it is guaranteed to find a solution whenever one exists.

**Optimal**: a strategy is optimal if the solution it finds has the lowest path cost among all solutions.

($b$ = branching factor, $d$ = depth of the shallowest solution, $m$ = maximum depth of the state space.)

**Breadth-first search.**

- *Complete*: yes, if $b$ is finite: it explores level by level, so it reaches the shallowest goal at depth $d$ after a finite number of nodes.

- *Optimal*: yes if all step costs are equal (or path cost is a non-decreasing function of depth), because it finds the shallowest goal; not optimal in general.

- *Time*: $b+b^2+\dots+b^d=O(b^d)$ (or $O(b^{d+1})$ if the goal test is applied on expansion).

- *Space*: $O(b^d)$: it keeps every generated node (frontier is $O(b^d)$). Memory is the bigger problem: $b=10$, $d=12$ needs about 10 petabytes at 1 KB/node.

**Depth-first search.**

- *Complete*: no in infinite state spaces or with loops (tree search may follow an infinite path); the graph-search version is complete in finite state spaces.

- *Optimal*: no; it returns the first solution found, which may be deep (e.g. it may find a goal at depth 10 on the left branch while a goal at depth 1 exists on the right).

- *Time*: $O(b^m)$, where $m$ may be much larger than $d$ (or infinite).

- *Space*: $O(bm)$: only the current path plus unexpanded siblings (backtracking version $O(m)$). This is its main advantage.

So neither is both efficient and robust: BFS is complete and (for unit costs) optimal but needs exponential memory; DFS needs linear memory but is neither complete nor optimal. Iterative deepening combines their advantages.
