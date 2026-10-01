---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Complete: guaranteed to find a solution whenever one exists (and report failure otherwise). Optimal: the solution found has the lowest path cost. Completeness ensures the agent does not fail or loop forever; optimality ensures it does not pay more than necessary."
sources: ["AIMA 3e sec. 3.3.2"]
---
**Complete.** A search algorithm is complete if it is guaranteed to find a solution whenever one exists (and to terminate with failure when none exists). Example: BFS is complete for finite branching factor; DFS is not, because it can follow an infinite path.

**Optimal.** A search algorithm is optimal if the solution it returns has the lowest path cost among all solutions. Example: UCS and A* with an admissible heuristic are optimal; DFS and greedy best-first are not.

**Why they are important.**

- **Completeness** guarantees reliability: an incomplete algorithm may run forever or give up although a solution exists, so the agent fails at its task (e.g. a route planner that cannot find any route).

- **Optimality** guarantees quality: the solution cost is the agent's performance (time, distance, money, risk). A suboptimal plan wastes resources, e.g. a longer route or a slower schedule.

- Together with time and space complexity they let us compare algorithms and choose the right one: sometimes we trade optimality for speed (greedy, weighted A*), but we should know that we are doing it. In safety-critical or costly domains, both properties are usually required.
