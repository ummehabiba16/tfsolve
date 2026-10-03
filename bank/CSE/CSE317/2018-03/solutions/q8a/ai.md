---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Variable ordering decides which variable to assign next: MRV (fewest legal values), with the degree heuristic as a tie-breaker; e.g. in Australia colour SA first (degree 5), and after WA = red, NT = green, choose SA (only blue left). Value ordering decides which value to try first: least-constraining value, ruling out fewest choices for neighbours; e.g. after WA = red, NT = green, for Q prefer red over blue, because blue would leave SA no colour."
sources: ["AIMA 3e sec. 6.3.1 (variable and value ordering)"]
---
In backtracking search for a CSP, two choices are made at each step: **which variable** to assign next, and **in what order** to try its values.

**Variable-ordering heuristics** choose the variable.

- **Minimum-remaining-values (MRV, "most constrained variable", "fail-first"):** pick the variable with the fewest legal values left. If it is going to fail, it fails early, which prunes the tree.
- **Degree heuristic:** pick the variable involved in the most constraints with *unassigned* variables. It is used to choose the first variable, and as a tie-breaker for MRV.

*Example* (map of Australia: WA, NT, SA, Q, NSW, V, T; colours R, G, B). At the start all regions have 3 values, and the degree heuristic picks **SA**, which has 5 neighbours. Or, after WA = red and NT = green, MRV picks **SA**, which has only blue left, rather than Q (2 values left).

**Value-ordering heuristic** chooses the value for the chosen variable.

- **Least-constraining value (LCV):** try first the value that rules out the fewest choices for neighbouring variables, leaving maximum flexibility for later assignments. Value ordering does not change the size of the tree when all solutions are wanted, but it finds *a* solution sooner.

*Example:* after WA = red and NT = green, choose a colour for Q. **Blue** would remove SA's last legal value (SA neighbours WA, NT and Q), while **red** leaves SA with blue. LCV tries **red** first.

**Difference:** variable ordering uses fail-first, to prune failures early. Value ordering uses succeed-first, to reach a solution quickly.
