---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Min-conflicts: start with a complete (random or greedy) assignment; repeatedly pick a conflicted variable at random and give it the value that minimizes the number of violated constraints (ties broken randomly), until no conflicts remain or a step limit is reached. Example: 8-queens with one queen per column, moving a conflicted queen within its column to the row with the fewest attacks; it solves even million-queens problems in about 50 steps."
sources: ["AIMA 3e sec. 6.4 (local search for CSPs, MIN-CONFLICTS, Fig. 6.8-6.9)"]
---
**Min-conflicts** is a local-search algorithm for CSPs that works on **complete** assignments:

```text
function MIN-CONFLICTS(csp, max_steps) returns a solution or failure
    current <- an initial complete assignment for csp (random or greedy)
    for i = 1 to max_steps:
        if current is a solution for csp then return current
        var   <- a randomly chosen conflicted variable from csp.VARIABLES
        value <- the value v for var that minimizes CONFLICTS(var, v, current, csp)
        set var = value in current
    return failure
```

`CONFLICTS(var, v, ...)` counts the constraints violated if $var=v$, given the other current values. Ties are broken randomly. Plateaux are escaped by sideways moves and tabu lists.

**Example: 8-queens** (variables = columns, values = the row of each queen).

1. Start with one queen per column in random rows. Several pairs of queens attack each other.
2. Pick a **conflicted** queen at random, say the queen in column 8, attacked by 2 queens.
3. For each row of column 8, count the attacks it would receive. Move the queen to the row with the **fewest** attacks (e.g. 1).
4. Repeat: pick another conflicted queen and move it to its min-conflict row, until the number of attacks is 0.

In AIMA's example, a solution is reached in **two steps**. In general, min-conflicts solves $n$-queens in a roughly constant number of steps (about 50), even for $n=1{,}000{,}000$, because solutions are densely distributed. It also works well for scheduling problems (Hubble telescope observations) and for **online** repair when the problem changes, since it starts from the current assignment.
