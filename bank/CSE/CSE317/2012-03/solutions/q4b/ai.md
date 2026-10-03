---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Goal ON(D,B) and ON(B,A) and ONTABLE(A) and ONTABLE(C). ON(D,B) is already true but must be undone to place B on A. Goal stack: solve ON(B,A) by STACK(B,A), which needs HOLDING(B) (PICKUP(B), which needs CLEAR(B), so UNSTACK(D,B) and PUTDOWN(D)); then ON(D,B) is re-achieved by PICKUP(D) and STACK(D,B). Plan: UNSTACK(D,B), PUTDOWN(D), PICKUP(B), STACK(B,A), PICKUP(D), STACK(D,B)."
sources: ["Rich & Knight, Artificial Intelligence, sec. 13.4 (goal stack planning)"]
---
**Initial state:** $ON(D,B)\land ONTABLE(A)\land ONTABLE(B)\land ONTABLE(C)\land CLEAR(D)\land CLEAR(A)\land CLEAR(C)\land ARMEMPTY$.

**Goal:** $ON(D,B)\land ON(B,A)\land ONTABLE(A)\land ONTABLE(C)$.

**Goal stack planning.** Push the conjunctive goal, then its unsatisfied components. Here $ON(D,B)$, $ONTABLE(A)$ and $ONTABLE(C)$ already hold, so only $ON(B,A)$ needs work. (If $ON(D,B)$ were pushed first, it would be popped as already true and later found undone when the whole conjunction is rechecked.)

| # | Top of the stack | Action | State after |
|:-:|:--|:--|:--|
| 1 | $ON(B,A)$ (false) | push STACK(B,A) and its preconditions $CLEAR(A)$, $HOLDING(B)$ | |
| 2 | $HOLDING(B)$ (false) | push PICKUP(B) and its preconditions $CLEAR(B)$, $ONTABLE(B)$, $ARMEMPTY$ | |
| 3 | $CLEAR(B)$ (false: D is on B) | push UNSTACK(D,B) and its preconditions $ON(D,B)$, $CLEAR(D)$, $ARMEMPTY$ (all true) | |
| 4 | UNSTACK(D,B) | **execute** | $HOLDING(D)$, $CLEAR(B)$, $\neg ON(D,B)$, $\neg ARMEMPTY$ |
| 5 | $ARMEMPTY$ (false: holding D) | push PUTDOWN(D) (its precondition $HOLDING(D)$ is true) | |
| 6 | PUTDOWN(D) | **execute** | $ONTABLE(D)$, $ARMEMPTY$ |
| 7 | $ONTABLE(B)$ true; PICKUP(B) | **execute** | $HOLDING(B)$ |
| 8 | $CLEAR(A)$ true; STACK(B,A) | **execute** | $ON(B,A)$, $ARMEMPTY$ |
| 9 | Recheck the conjunctive goal: $ON(D,B)$ is now **false** | push $ON(D,B)$, then STACK(D,B), $CLEAR(B)$, $HOLDING(D)$ | |
| 10 | $HOLDING(D)$ (false) | push PICKUP(D) ($CLEAR(D)$, $ONTABLE(D)$, $ARMEMPTY$ all true) | |
| 11 | PICKUP(D) | **execute** | $HOLDING(D)$ |
| 12 | STACK(D,B) ($CLEAR(B)$ true) | **execute** | $ON(D,B)$, $ARMEMPTY$ |
| 13 | The conjunctive goal is true | pop. **Done** | |

**Plan:** UNSTACK(D, B), PUTDOWN(D), PICKUP(B), STACK(B, A), PICKUP(D), STACK(D, B).

```text
initial:  [D]                goal:   [D]
          [A] [B] [C]                [B]
                                     [A] [C]
```
