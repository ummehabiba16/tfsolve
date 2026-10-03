---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Linear planning solves goals one at a time on a single stack (totally ordered, e.g. STRIPS / goal-stack), so it fails on interacting goals (Sussman anomaly); non-linear planning keeps a set of goals and a partial order of steps, interleaving subgoals (e.g. NOAH, TWEAK, partial-order planning). Modal truth criterion: a proposition p is necessarily true at step s iff some step t necessarily before s necessarily asserts p, and no step possibly between t and s possibly denies p (unless a white-knight step re-asserts p)."
sources: ["Rich & Knight, Artificial Intelligence, sec. 13.5 (non-linear planning, TWEAK)", "Chapman 1987 (TWEAK, modal truth criterion)"]
---
**Linear versus non-linear planning** (5).

| Linear planning | Non-linear planning |
|:--|:--|
| Works on **one goal at a time**, on a single goal stack. Each subgoal is completely solved before the next one is started. | Works on **several goals at once**, with a set of goals (not a stack). |
| Produces a **totally ordered** sequence of actions. | Keeps steps **partially ordered**: commits to an order only when needed (least commitment). |
| Fails or gives non-optimal plans for **interacting subgoals** (Sussman anomaly: solving $ON(A,B)$ first must be undone to achieve $ON(B,C)$). | Subgoals can be **interleaved**, so it handles interacting goals (e.g. NOAH, TWEAK, POP). |
| Simple, with a small search space. | More complex: it must detect and resolve threats (conflicts) between steps. |

**Modal truth criterion** (Chapman's TWEAK) (2). A proposition $p$ is **necessarily true** in the situation before step $s$ if and only if:

1. there is a step $t$, **necessarily before** $s$ (or the initial state), that **necessarily asserts** $p$; and
2. there is **no step $c$ possibly between $t$ and $s$ that possibly denies** $p$ (a clobberer), unless for every such $c$ there is a "**white knight**" step $w$, necessarily between $c$ and $s$, that re-asserts $p$.

TWEAK uses this criterion to decide whether a precondition holds in a partial plan, and to find the modifications needed to make it hold.
