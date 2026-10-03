---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Relax the 8-puzzle rule 'a tile can move from A to B if A is adjacent to B and B is blank': (a) the tile may move to any adjacent square: h2 = Manhattan distance; (b) the tile may move to the blank anywhere: Gaschnig's heuristic; (c) the tile may move anywhere: h1 = misplaced tiles. Each is admissible, because the relaxed problem's optimal cost is <= the real optimal cost (every real solution is a relaxed solution), and consistent too, being an exact cost in the relaxed problem."
sources: ["AIMA 3e sec. 3.6.2 (generating admissible heuristics from relaxed problems)"]
---
**Relaxed problem.** A problem with fewer restrictions on the actions. Its state-space graph is a *supergraph* of the original, since edges are added. Every optimal solution of the original problem is also a solution of the relaxed problem, so

$$h_{\text{relaxed}}^*(n)\le h^*(n),$$

and the **exact cost of an optimal relaxed solution is an admissible heuristic**. It is also **consistent**, because it is an exact cost in the relaxed problem (it satisfies the triangle inequality there).

**8-puzzle.** Formal rule: *a tile can move from square A to square B if A is horizontally or vertically adjacent to B **and** B is blank.* Removing conditions gives three relaxed problems:

| Relaxed rule | Exact relaxed cost = heuristic |
|:--|:--|
| (a) A tile can move from A to B *if A is adjacent to B* (ignore "blank") | $h_2$ = **sum of Manhattan distances** of the tiles from their goal squares |
| (b) A tile can move from A to B *if B is blank* (ignore "adjacent") | **Gaschnig's heuristic**: the number of swaps with the blank needed to sort |
| (c) A tile can move from A to B (ignore both) | $h_1$ = **number of misplaced tiles** |

**Can each be used?** **Yes.** Each heuristic is the exact optimal cost of its relaxed problem, so each is admissible and consistent. The relaxed problems are easy to solve: they decompose into independent subproblems, one per tile. Since $h_2\ge h_1$ ($h_2$ dominates $h_1$), $h_2$ is better (fewer nodes expanded). The best combination is $h=\max(h_1,h_2,\dots)$, which is still admissible.
