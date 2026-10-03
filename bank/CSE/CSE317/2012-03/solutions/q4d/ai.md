---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Linear planning solves one goal at a time on a stack and produces a totally ordered plan (it can fail on interacting goals, e.g. the Sussman anomaly); non-linear planning works on several goals at once with a partially ordered plan, interleaving subgoals."
sources: ["Rich & Knight, Artificial Intelligence, sec. 13.4-13.5"]
---
**Linear planning** (for example STRIPS or goal stack planning) solves goals **one at a time, in sequence**, each completely before the next, and produces a **totally ordered** plan. It cannot interleave the steps of different subgoals, so with **interacting goals** (the Sussman anomaly) it produces non-optimal plans or fails.

**Non-linear planning** (NOAH, TWEAK, partial-order planning) keeps a **set of goals**, considers them together, and builds a **partially ordered** plan, ordering steps only when necessary (least commitment). Steps for different subgoals can be **interleaved**, which handles interacting goals, at the cost of more complex reasoning (detecting and resolving threats).
