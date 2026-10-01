---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Most-constrained variable (MRV) is 'fail-first': it picks the variable most likely to fail soon, pruning the tree early; least-constraining value is 'fail-last': it keeps the most options for the remaining variables, since only one solution is needed."
sources: ["AIMA 3e sec. 6.3.1 (Variable and value ordering)"]
---
In backtracking search for a CSP we must decide (1) which unassigned variable to assign next and (2) in what order to try its values. The two choices have opposite goals.

**Most constrained variable (MRV, "fail-first").** Choose the variable with the fewest legal values left.

- Every variable must be assigned eventually, so the order of variables does not change the set of solutions, only the *size of the search tree*.

- A variable with few values is the one most likely to cause a failure. Assigning it first detects a dead end at a shallow level, so the subtree pruned is large. If a variable has zero legal values, MRV picks it immediately and the failure is found without assigning anything else.

- Tie-breaker: the *degree heuristic* (variable in the most constraints with unassigned variables).

**Least constraining value (LCV, "fail-last").** For the chosen variable, try first the value that rules out the fewest values for the neighbouring variables.

- We only need **one** solution, so we want the first value tried to be the one most likely to lead to a solution. Keeping neighbours' domains as large as possible keeps the most flexibility for the rest of the assignment and reduces backtracking.

- (For finding all solutions, or if there is none, value ordering would not matter, but variable ordering still would.)

**Example: colouring Australia** (WA, NT, SA, Q, NSW, V, T with red/green/blue, neighbours must differ).

1. Start: all have 3 values. Degree heuristic picks SA (5 neighbours): SA = blue.

2. Suppose WA = red. Now NT has {green} only (1 value), Q, NSW, V have {red, green}. MRV picks NT: NT = green.

3. Q now has {red} only: Q = red; then NSW = green; V = red; T = any. No backtracking at all.

LCV example: with WA = red and NT = green, choosing Q: Q = red leaves SA with {blue}, Q = blue leaves SA with nothing. LCV tries Q = red first, avoiding a dead end. With these heuristics, $n$-queens for $n=1000$ becomes feasible, whereas plain backtracking manages only about 25 queens.
