---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A CSP is defined by variables X, domains D and constraints C; a solution is a complete consistent assignment. Yes, there is a standard (factored) representation: every problem is stated as variables, domains and constraints (often drawn as a constraint graph), which lets general-purpose, domain-independent algorithms and heuristics (backtracking, MRV, AC-3) solve any CSP."
sources: ["AIMA 3e sec. 6.1"]
---
**Constraint satisfaction problem (CSP).** A CSP consists of three components:

- $X=\{X_1,\dots,X_n\}$: a set of **variables**;

- $D=\{D_1,\dots,D_n\}$: a **domain** of possible values for each variable;

- $C$: a set of **constraints**, each a pair $\langle$scope, relation$\rangle$ specifying the allowed combinations of values of the variables in its scope (e.g. $\langle(X_1,X_2), X_1\ne X_2\rangle$).

An **assignment** gives values to some variables; it is **consistent** if it violates no constraint. A **solution** is a complete, consistent assignment. Example: map colouring of Australia with variables WA, NT, ..., domains {red, green, blue}, constraints "adjacent regions differ".

**Is there a standard representation?** **Yes.** Unlike general search, where a state is an atomic "black box" and each problem needs its own successor function, goal test and heuristic, every CSP uses the same **factored representation**: a set of variables, each with a value. The goal test is the same for all CSPs (all constraints satisfied), and the structure can be drawn as a **constraint graph** (nodes = variables, edges = binary constraints; hypergraph for higher-order constraints).

Justification:

- This standard form allows **general-purpose** algorithms that work for any CSP: backtracking search, forward checking, arc consistency (AC-3), min-conflicts.

- It allows **domain-independent heuristics**, such as MRV, degree and least-constraining-value, which use only the variable/constraint structure.

- The constraint graph's structure (e.g. a tree) can be exploited to solve problems faster.

- Many real problems (scheduling, timetabling, map colouring, Sudoku, $n$-queens, cryptarithmetic, circuit layout) fit this representation directly.
