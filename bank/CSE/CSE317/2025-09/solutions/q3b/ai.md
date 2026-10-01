---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Min-conflicts starts from a complete assignment and repeatedly picks a conflicted variable and gives it the value with the fewest conflicts; constraint propagation uses constraints to shrink domains (node/arc/path consistency, forward checking), reducing the search space and detecting failures early."
sources: ["AIMA 3e sec. 6.2 (Constraint propagation) and 6.4 (Local search for CSPs)"]
---
**Min-conflicts (local search for CSPs).** Local search works on *complete-state* formulations:

1. Start with a complete assignment of all variables (random or greedy), usually violating some constraints.

2. Repeatedly pick a **conflicted variable** at random and assign it the value that **minimises the number of conflicts** with other variables (ties broken randomly).

3. Stop when no constraint is violated, or after a maximum number of steps.

```text
function MIN-CONFLICTS(csp, max_steps):
    current <- an initial complete assignment
    for i = 1 to max_steps:
        if current is a solution: return current
        var   <- a randomly chosen conflicted variable
        value <- the value v of var that minimises CONFLICTS(var, v, current)
        set var = value in current
    return failure
```

Example: $n$-queens with one queen per column: move a queen that is attacked to the row in its column with the fewest attacks. Min-conflicts solves even million-queens in about 50 steps on average, because solutions are densely distributed. It is also good for online repair (e.g. rescheduling after a change). Plateaux can be handled by sideways moves or tabu search.

**Constraint propagation.** Using the constraints to **reduce the domains** of variables, which in turn reduces the domains of other variables, and so on. It can be done as preprocessing or interleaved with search. Kinds of local consistency:

- *Node consistency*: every value in a domain satisfies the unary constraints.

- *Arc consistency*: for every value of $X_i$ there is some consistent value of $X_j$ for each binary constraint (AC-3 algorithm).

- *Path consistency / k-consistency*: extends this to triples or $k$ variables.

- *Forward checking*: after assigning $X$, remove inconsistent values from the domains of $X$'s neighbours.

**How it improves performance.** (1) Smaller domains mean a smaller search tree; (2) an empty domain shows that the current partial assignment cannot be completed, so search backtracks **early** instead of discovering the failure many levels deeper; (3) sometimes propagation alone solves the problem (e.g. many Sudoku puzzles are solved by AC-3 alone). Example: in Australia map colouring, after WA = red and Q = green, forward checking/arc consistency leaves NT and SA with only blue, they are neighbours, so the failure is detected immediately.
