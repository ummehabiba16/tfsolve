---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Initial: ON(D,C), ONTABLE(A), ONTABLE(B), ONTABLE(C), CLEAR(A), CLEAR(B), CLEAR(D), ARMEMPTY. Goal: ON(C,A) and ON(D,B). Goal stack: ON(D,B) needs STACK(D,B), whose precondition HOLDING(D) needs UNSTACK(D,C); then ON(C,A) needs PICKUP(C) and STACK(C,A). Plan: UNSTACK(D,C), STACK(D,B), PICKUP(C), STACK(C,A)."
sources: ["Rich & Knight, Artificial Intelligence, sec. 13.4 (goal stack planning)"]
---
**Initial state:** $ON(D,C)\land ONTABLE(A)\land ONTABLE(B)\land ONTABLE(C)\land CLEAR(A)\land CLEAR(B)\land CLEAR(D)\land ARMEMPTY$.

**Goal:** $ON(C,A)\land ON(D,B)\land ONTABLE(A)\land ONTABLE(B)$.

Push the conjunctive goal, then the unsatisfied subgoals: $ON(C,A)$, and on top of it $ON(D,B)$. Solving $ON(D,B)$ first moves D off C, which also clears C.

| # | Top of the stack | Action | State after |
|:-:|:--|:--|:--|
| 1 | $ON(D,B)$ (false) | push STACK(D,B) and its preconditions $CLEAR(B)$, $HOLDING(D)$ | |
| 2 | $HOLDING(D)$ (false) | push UNSTACK(D,C) and its preconditions $ON(D,C)$, $CLEAR(D)$, $ARMEMPTY$ (all true) | |
| 3 | UNSTACK(D,C) | **execute** | $HOLDING(D)$, $CLEAR(C)$ |
| 4 | $CLEAR(B)$ true; STACK(D,B) | **execute** | $ON(D,B)$, $ARMEMPTY$ |
| 5 | $ON(C,A)$ (false) | push STACK(C,A) and its preconditions $CLEAR(A)$, $HOLDING(C)$ | |
| 6 | $HOLDING(C)$ (false) | push PICKUP(C) and its preconditions $CLEAR(C)$, $ONTABLE(C)$, $ARMEMPTY$ (all true) | |
| 7 | PICKUP(C) | **execute** | $HOLDING(C)$ |
| 8 | STACK(C,A) | **execute** | $ON(C,A)$, $ARMEMPTY$ |
| 9 | Recheck the conjunctive goal | all true: pop. **Done** | |

**Plan:** UNSTACK(D, C), STACK(D, B), PICKUP(C), STACK(C, A).

```text
initial:         [D]          goal:   [C] [D]
             [A] [B] [C]              [A] [B]
```
