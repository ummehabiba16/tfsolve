---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Uninformed search uses only the problem definition (orders nodes by depth or path cost); informed search also uses a heuristic h(n) estimating the cost to the goal, so it expands promising nodes first and is usually far more efficient."
sources: ["AIMA 3e sec. 3.4-3.5"]
---
| Uninformed (blind) search | Informed (heuristic) search |
|:--|:--|
| Uses only the problem definition: states, actions, goal test, step costs | Also uses problem-specific knowledge: a heuristic $h(n)$ = estimated cost from $n$ to a goal |
| Cannot tell whether one non-goal state is more promising than another | Expands the most promising nodes first |
| Orders nodes by depth or path cost $g(n)$ | Orders by $h(n)$ (greedy) or $g(n)+h(n)$ (A*) |
| Explores in all directions, usually exponential | Focused toward the goal, far fewer nodes with a good $h$ |
| BFS, DFS, UCS, DLS, IDS, bidirectional | Greedy best-first, A*, IDA*, RBFS, SMA*, hill climbing |
| Completeness/optimality depend only on the algorithm | Also depend on properties of $h$ (admissible, consistent) |

Example: route finding to Bucharest: UCS spreads out in circles from Arad; A* with straight-line distance heads toward Bucharest and expands only a few cities.
