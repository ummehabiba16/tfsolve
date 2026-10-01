---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "MRV (minimum remaining values / most constrained variable) chooses the unassigned variable with the fewest legal values (fail-first); LCV (least constraining value) tries first the value that rules out the fewest values of neighbouring variables (fail-last). Example: Australia map colouring."
sources: ["AIMA 3e sec. 6.3.1"]
---
**Minimum Remaining Values (MRV).** Also called "most constrained variable" or "fail-first". When choosing the next variable in backtracking search, pick the unassigned variable with the **fewest legal values** remaining in its domain.

- Rationale: this variable is the most likely to cause a failure soon; assigning it first detects dead ends early and prunes the search tree. If a variable has 0 legal values, it is picked immediately and failure is detected without further assignments.

- Tie-breaker: the **degree heuristic** (variable involved in the most constraints on other unassigned variables).

*Example.* Australia map colouring: after WA = red and NT = green, SA has only {blue} and Q only {red, blue}, while V, NSW have 3 values. MRV chooses SA, then Q, etc. Without MRV, choosing V first could lead to wasted work.

**Least Constraining Value (LCV).** When choosing the order of values for the selected variable, prefer the value that **rules out the fewest choices** for the neighbouring variables in the constraint graph ("fail-last").

- Rationale: only one solution is needed, so try first the value most likely to lead to a solution, leaving maximum flexibility for later assignments.

*Example.* With WA = red and NT = green, choose a value for Q. Q = red leaves SA with {blue}; Q = blue leaves SA with nothing. LCV tries Q = red first.

Together MRV and LCV make, e.g., the 1000-queens problem feasible, while plain backtracking cannot get beyond about 25 queens.
