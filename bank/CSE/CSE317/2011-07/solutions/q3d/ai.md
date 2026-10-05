---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Linear planning solves goals one at a time on a stack, producing a totally ordered plan (fails on interacting goals); non-linear planning works on all goals together with a partially ordered plan and interleaves subgoals. Modal truth criterion: p is necessarily true before step s iff some step t necessarily before s necessarily asserts p, and every step possibly between t and s that possibly denies p is followed, necessarily before s, by a white knight that necessarily asserts p."
sources: ["Rich & Knight, Artificial Intelligence, sec. 13.4-13.5", "Chapman 1987"]
---
**Linear versus non-linear planning.**

- **Linear planning** (STRIPS, goal stack) works on **one goal at a time**, completing each subgoal before starting the next, and produces a **totally ordered** sequence of actions. It cannot interleave the steps of different subgoals, so with interacting goals (the Sussman anomaly) it gives non-optimal plans or fails.
- **Non-linear planning** (NOAH, TWEAK, partial-order planning) works on **all goals together**, builds a **partially ordered** plan (least commitment) and can interleave subgoal steps. It handles interacting goals, at the price of reasoning about threats among unordered steps.

**Modal truth criterion** (Chapman). A proposition $p$ is **necessarily true** in the situation before step $s$ iff:

1. there is a step $t$, **necessarily before** $s$ (or the initial state), that **necessarily asserts** $p$; and
2. for every step $c$ **possibly before** $s$ that **possibly denies** $p$, there is a step $w$ (a **white knight**), necessarily between $c$ and $s$, that necessarily asserts $p$.
