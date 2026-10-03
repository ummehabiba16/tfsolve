---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Variable: choose the MOST constrained variable (MRV, fail-first): it is the one most likely to fail, so failure is detected early and the tree is pruned near the root, and it often has a forced value. Value: choose the LEAST constraining value: since only one solution is needed, keep the most options open for the remaining variables, maximizing the chance that this branch leads to a solution."
sources: ["AIMA 3e sec. 6.3.1 (variable and value ordering)"]
---
The two heuristics seem opposite. They aim at different things.

**Most-constrained variable (MRV, "fail-first").** Choose the variable with the fewest remaining legal values.

- Every variable must be assigned eventually, so the order of variables does not change *whether* a solution exists, only how quickly failure is detected.
- The variable with the fewest options is the one most likely to cause a failure. Trying it first exposes failures **early**, near the root of the search tree, where a backtrack prunes a large subtree, instead of deep in the tree after much wasted work.
- If it has only one value left, assigning it now is forced anyway. If it has zero, we fail immediately.

*Example:* after WA = red and NT = green in the Australia map, SA has only blue left, so it is chosen next.

**Least-constraining value ("succeed-first").** For the chosen variable, try first the value that rules out the fewest values in the neighbours' domains.

- We need only **one** solution, so we want the branch most likely to succeed. The least constraining value leaves the most flexibility for the remaining variables, maximizing the chance that a complete assignment exists below it. Backtracking to try other values then happens less often.
- If we wanted *all* solutions, or the problem had none, value ordering would not matter: every value would be tried anyway.

*Example:* with WA = red and NT = green, choosing Q = red (rather than blue) leaves SA with blue available.

So, **fail-first for variables** prunes dead ends early, and **succeed-first for values** finds a solution quickly.
