---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Uninformed search uses only the problem definition (expands by depth or path cost); informed search also uses a heuristic h(n) estimating the distance to the goal, so it expands promising nodes first. In route-finding on a map with straight-line distances, A* explores far fewer cities than BFS/UCS."
sources: ["AIMA 3e sec. 3.4-3.5"]
---
**Uninformed (blind) search** uses only the information in the problem definition: initial state, actions, goal test, step costs. It can only distinguish goal from non-goal states and orders nodes by depth or path cost (BFS, DFS, UCS, DLS, IDS, bidirectional). It does not know whether one non-goal state is closer to the goal than another, so it explores in all directions.

**Informed (heuristic) search** additionally uses problem-specific knowledge in the form of a **heuristic function** $h(n)$ = estimated cost of the cheapest path from $n$ to a goal. It expands the most promising nodes first (greedy best-first: $f=h$; A*: $f=g+h$). With a good admissible heuristic, A* is still optimal and expands far fewer nodes.

| | Uninformed | Informed |
|:--|:--|:--|
| Knowledge | problem definition only | plus heuristic $h(n)$ |
| Node ordering | depth or $g(n)$ | $h(n)$ or $g(n)+h(n)$ |
| Efficiency | explores blindly, often exponential | focuses toward the goal |
| Examples | BFS, DFS, UCS, IDS | greedy best-first, A*, IDA*, RBFS |

**Environment where informed search is better.** Route finding on a road map (e.g. Arad to Bucharest in Romania) with the straight-line distance to the destination as heuristic. UCS expands cities in circles of increasing cost around Arad, including cities in the wrong direction (Zerind, Oradea, Timisoara, ...). A* with straight-line distance expands only Arad, Sibiu, Rimnicu Vilcea, Fagaras, Pitesti and Bucharest, and still finds the optimal route (cost 418). Similarly, the 8-puzzle with the Manhattan-distance heuristic: at depth 24 IDS would generate on the order of $10^{10}$ nodes, A* with Manhattan distance about $10^3$-$10^4$.
