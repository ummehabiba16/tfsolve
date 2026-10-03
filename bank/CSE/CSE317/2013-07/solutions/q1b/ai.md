---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Forward (progression) search starts from the initial state, applies applicable actions and searches towards the goal (many irrelevant actions); backward (regression) search starts from the goal, regresses it through relevant, consistent actions to subgoals until the initial state satisfies one (smaller branching factor, but it works with sets of states). Example: forward: unstack(C,B), putdown(C), pickup(A), stack(A,B); backward from on(A,B) and ontable(C): regress through stack(A,B), then pickup(A) ..., reaching a subgoal true in the initial state."
sources: ["AIMA 3e sec. 10.2.1-10.2.2 (forward and backward state-space search)"]
---
**Problem.** Initial: $on(C,B)$, $ontable(A)$, $ontable(B)$, $clear(C)$, $clear(A)$, $armempty$. Goal: $on(A,B)\land ontable(B)\land ontable(C)$.

**Forward (progression) state-space search.**

- Starts at the **initial state** and applies **applicable** actions (whose preconditions hold) to generate successor states, until a state satisfies the goal.
- Sound and simple, with complete states. But it considers **irrelevant actions**, so the branching factor is large: with many blocks, every pickup and unstack applies. It needs a good heuristic.

*Example:* from the initial state, the applicable actions are $unstack(C,B)$ and $pickup(A)$. Choose $unstack(C,B)$, then $putdown(C)$, $pickup(A)$, $stack(A,B)$. The goal is satisfied.

```text
S0 --unstack(C,B)--> S1 --putdown(C)--> S2 --pickup(A)--> S3 --stack(A,B)--> goal
```

**Backward (regression / relevant-states) search.**

- Starts from the **goal** (a set of states described by literals). It chooses **relevant** actions, whose effects achieve a goal literal and do not undo any (consistent). It **regresses** the goal through each action: $g'=(g-\text{ADD}(a))\cup\text{PRECOND}(a)$. It stops when the initial state satisfies the current subgoal.
- Only relevant actions are considered, so the branching factor is usually **smaller**. But it works with partially specified states, which makes heuristics harder.

*Example:*

```text
g0 = on(A,B), ontable(B), ontable(C)
  regress through stack(A,B):   g1 = holding(A), clear(B), ontable(B), ontable(C)
  regress through pickup(A):    g2 = ontable(A), clear(A), armempty, clear(B), ontable(B), ontable(C)
  regress through putdown(C):   g3 = holding(C), ontable(A), clear(A), clear(B), ontable(B)
  regress through unstack(C,B): g4 = on(C,B), clear(C), armempty, ontable(A), clear(A), ontable(B)
  g4 holds in the initial state: stop.
```

The plan, read forwards, is the same: $unstack(C,B), putdown(C), pickup(A), stack(A,B)$.

| | Forward | Backward |
|:--|:--|:--|
| Starts from | initial state | goal |
| Actions considered | applicable | relevant and consistent |
| States | complete states | sets of states (subgoals) |
| Branching factor | often large | usually smaller |
