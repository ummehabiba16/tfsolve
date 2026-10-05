---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Backtracking search: depth-first search that assigns one variable at a time and backtracks when a variable has no legal value; it is complete. Heuristics: variable ordering by MRV (fail-first) with the degree heuristic as tie-breaker; value ordering by least-constraining value; inference by forward checking or MAC (arc consistency); intelligent backtracking (conflict-directed backjumping, constraint learning)."
sources: ["AIMA 3e sec. 6.3 (backtracking search for CSPs, Fig. 6.5)"]
---
**Backtracking search** (9). A depth-first search specialized to CSPs:

- the variables are assigned **one at a time** (assignments commute, so only one variable is considered at each level, giving $d^n$ leaves instead of $n!\,d^n$);
- after each assignment, the constraints with already-assigned variables are checked (**consistency check**);
- if a variable has **no legal value**, the search **backtracks** to the previous variable and tries its next value.

```text
function BACKTRACK(assignment, csp):
    if assignment is complete: return assignment
    var <- SELECT-UNASSIGNED-VARIABLE(csp)
    for each value in ORDER-DOMAIN-VALUES(var, assignment, csp):
        if value is consistent with assignment:
            add {var = value}; inferences <- INFERENCE(csp, var, value)
            if inferences != failure:
                result <- BACKTRACK(assignment, csp); if result != failure: return result
            remove {var = value} and inferences
    return failure
```

It is complete, and uses linear memory.

**Heuristics to improve performance** (6).

1. **Variable ordering:** **MRV** (minimum remaining values, "most constrained", "fail-first") chooses the variable with the fewest legal values left; the **degree heuristic** (tie-breaker) chooses the variable involved in the most constraints with unassigned variables.
2. **Value ordering:** **least-constraining value**, which rules out the fewest values in neighbouring domains ("succeed-first").
3. **Inference / look-ahead:** **forward checking**, which removes inconsistent values from the neighbours of the assigned variable, or **MAC** (maintaining arc consistency with AC-3). Failures are detected early.
4. **Intelligent backtracking:** conflict-directed **backjumping** to the real cause of a failure, and **constraint learning** (no-goods).
