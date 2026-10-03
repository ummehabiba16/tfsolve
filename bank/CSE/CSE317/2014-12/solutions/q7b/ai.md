---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Goal stack on ON(A,C) and ON(C,B) and ONTABLE(B): achieving ONTABLE(B) needs PUTDOWN(B,2), which needs HOLDING(B,2), which needs UNSTACK(B,A,2), which needs CLEAR(B), which needs UNSTACK(C,B,1). Then ON(C,B) by STACK(C,B,1) (agent 1 still holds C), then ON(A,C) by PICKUP(A,2) and STACK(A,C,2). Plan: UNSTACK(C,B,1), UNSTACK(B,A,2), PUTDOWN(B,2), STACK(C,B,1), PICKUP(A,2), STACK(A,C,2)."
sources: ["Rich & Knight, Artificial Intelligence, sec. 13.4 (goal stack planning)"]
---
**Initial state:** $ON(C,B)\land ON(B,A)\land ONTABLE(A)\land CLEAR(C)\land ARMEMPTY(1)\land ARMEMPTY(2)$.

**Goal:** $ON(A,C)\land ON(C,B)\land ONTABLE(B)$.

**Goal stack planning.** Push the compound goal, then its components. Repeatedly look at the top of the stack:

- if it is a goal that is already true, pop it;
- if it is an unsatisfied goal, push an action that achieves it, then the action's preconditions;
- if it is an action whose preconditions now hold, pop it, **execute** it (update the state) and add it to the plan.

The subgoals are ordered $ONTABLE(B)$ first, then $ON(C,B)$, then $ON(A,C)$, building bottom-up. Agents are assigned so that the work is shared: both have equal abilities, and whichever has a free arm takes the step.

| # | Stack (top first, abbreviated) | Action taken | State change |
|:-:|:--|:--|:--|
| 1 | ONTABLE(B); ON(C,B); ON(A,C); [goal] | ONTABLE(B) is false: push PUTDOWN(B,2) and its precondition HOLDING(B,2) | |
| 2 | HOLDING(B,2); PUTDOWN(B,2); ... | false: push UNSTACK(B,A,2) and its preconditions ON(B,A), CLEAR(B), ARMEMPTY(2) | |
| 3 | CLEAR(B); ON(B,A); ARMEMPTY(2); UNSTACK(B,A,2); ... | CLEAR(B) is false (C is on B): push UNSTACK(C,B,1) and ON(C,B), CLEAR(C), ARMEMPTY(1) | |
| 4 | ON(C,B), CLEAR(C), ARMEMPTY(1) all true; pop. UNSTACK(C,B,1) | **execute UNSTACK(C,B,1)** | agent 1 holds C; CLEAR(B) true |
| 5 | ON(B,A), ARMEMPTY(2) true; UNSTACK(B,A,2) | **execute UNSTACK(B,A,2)** | agent 2 holds B; CLEAR(A) true |
| 6 | PUTDOWN(B,2) (HOLDING(B,2) true) | **execute PUTDOWN(B,2)** | ONTABLE(B), CLEAR(B) |
| 7 | ONTABLE(B) true: pop. ON(C,B) is false: push STACK(C,B,1) and CLEAR(B), HOLDING(C,1) | both true | |
| 8 | STACK(C,B,1) | **execute STACK(C,B,1)** | ON(C,B); CLEAR(C); ARMEMPTY(1) |
| 9 | ON(A,C) is false: push STACK(A,C,2) and CLEAR(C), HOLDING(A,2) | HOLDING(A,2) is false: push PICKUP(A,2) and ONTABLE(A), CLEAR(A), ARMEMPTY(2), all true | |
| 10 | PICKUP(A,2) | **execute PICKUP(A,2)** | agent 2 holds A |
| 11 | STACK(A,C,2) (CLEAR(C) and HOLDING(A,2) true) | **execute STACK(A,C,2)** | ON(A,C) |
| 12 | compound goal $ON(A,C)\land ON(C,B)\land ONTABLE(B)$ | all true: pop. **Done** | |

**Plan:**

1. UNSTACK(C, B, 1)
2. UNSTACK(B, A, 2)
3. PUTDOWN(B, 2)
4. STACK(C, B, 1)
5. PICKUP(A, 2)
6. STACK(A, C, 2)

With two arms, agent 1 can keep holding C while agent 2 frees B, so C never has to be put on the table. A one-arm robot would need 8 steps. Steps 4 and 5 can be done at the same time.

*Note:* if both agents must do exactly the same number of actions, use the 8-step plan instead: agent 1 does UNSTACK(C,B), PUTDOWN(C), PICKUP(C), STACK(C,B), and agent 2 does UNSTACK(B,A), PUTDOWN(B), PICKUP(A), STACK(A,C).
