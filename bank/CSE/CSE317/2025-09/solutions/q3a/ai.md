---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A CSP has variables X, domains D and constraints C; LCV orders a variable's values so that the value ruling out the fewest choices for neighbouring variables is tried first, which keeps the most options open and finds a solution with less backtracking."
sources: ["AIMA 3e sec. 6.1 and 6.3.1 (Variable and value ordering)"]
---
**Components of a CSP.**

1. **Variables** $X=\{X_1,\dots,X_n\}$.

2. **Domains** $D=\{D_1,\dots,D_n\}$, $D_i$ is the set of allowed values of $X_i$.

3. **Constraints** $C$: each constraint is a pair $\langle\text{scope},\text{relation}\rangle$ specifying the allowed combinations of values for the variables in its scope (e.g. $WA \ne NT$).

A *state* is a (partial) assignment; a *solution* is a complete, consistent assignment (all variables assigned, no constraint violated).

Example: map colouring of Australia: variables WA, NT, Q, NSW, V, SA, T; domains {red, green, blue}; constraints: adjacent regions differ.

**Least Constraining Value (LCV) heuristic.** Once a variable has been chosen, LCV orders its values so that we try first the value that **rules out the fewest values in the domains of the neighbouring unassigned variables**.

Example: with WA = red, NT = green, we choose Q next. Q = red leaves SA with {blue}; Q = blue leaves SA with {} (no value). LCV prefers Q = red.

**Why it is useful.** We only need *one* solution, so for value ordering we should be "fail-last": pick the value most likely to lead to a solution. By keeping the maximum flexibility for future assignments, LCV reduces the chance of dead ends and therefore the amount of backtracking. (If we wanted all solutions or the problem had no solution, value ordering would not matter.)
