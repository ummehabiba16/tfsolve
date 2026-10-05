---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "A CSP is a triple (X, D, C): variables X = {X_1..X_n}, domains D = {D_1..D_n} with X_i taking values in D_i, and constraints C = {C_1..C_m}, each a pair (scope, relation) on a subset of the variables; a solution is a complete, consistent assignment. Examples: map colouring, 8-queens, Sudoku, job-shop scheduling (also cryptarithmetic, timetabling)."
sources: ["AIMA 3e sec. 6.1 (defining constraint satisfaction problems)"]
---
**Formal definition** (3). A constraint satisfaction problem consists of three components $\langle X,D,C\rangle$:

- $X=\{X_1,\dots,X_n\}$, a set of **variables**;
- $D=\{D_1,\dots,D_n\}$, a set of **domains**, one for each variable ($X_i$ takes values from $D_i$);
- $C=\{C_1,\dots,C_m\}$, a set of **constraints**. Each $C_j=\langle scope,rel\rangle$ specifies a tuple of variables (its scope) and a relation listing (or describing) the allowed combinations of their values, e.g. $\langle(X_1,X_2),\ X_1\neq X_2\rangle$.

A state is an assignment of values to some or all variables. A **solution** is a **complete** and **consistent** assignment: every variable has a value and no constraint is violated.

**Four CSPs** (4):

1. **Map colouring:** variables are regions, domains are colours, and adjacent regions differ.
2. **$n$-queens:** variables are the columns, domains the rows, and no two queens attack each other.
3. **Sudoku:** variables are the cells, domains $\{1..9\}$, with all-different constraints on rows, columns and boxes.
4. **Job-shop scheduling:** variables are task start times, with precedence and resource constraints.

(Also: cryptarithmetic puzzles, timetabling, crossword construction.)
