---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Regression from the goal G0 = {On(B,C), On(C,A), OnTable(A)}: through stack(B,C) gives {Holding(B), Clear(C), On(C,A), OnTable(A)}; through pickup(B) gives {OnTable(B), Clear(B), HandEmpty, Clear(C), On(C,A), OnTable(A)}; through stack(C,A) gives {Holding(C), Clear(A), OnTable(B), Clear(B), OnTable(A)}; through unstack(C,B) gives {On(C,B), Clear(C), HandEmpty, Clear(A), OnTable(B), OnTable(A)}, which the initial state satisfies. Plan: unstack(C,B), stack(C,A), pickup(B), stack(B,C)."
sources: ["AIMA 3e sec. 10.2.2 (backward / regression search)"]
---
**Regression planning.** Start from the goal. Repeatedly choose a **relevant** action (one that achieves some goal literal and deletes none) and regress the goal through it:

$$g'=(g\setminus\text{ADD}(a))\cup\text{PRECOND}(a).$$

Stop when the initial state satisfies the current goal. The actions found, read in reverse, form the plan.

| Step | Action regressed through | Literals removed from the goal | Literals added to the goal | Resulting goal |
|:-:|:--|:--|:--|:--|
| 0 | | | | $On(B,C)$, $On(C,A)$, $OnTable(A)$ |
| 1 | $stack(B,C)$ | $On(B,C)$ | $Holding(B)$, $Clear(C)$ | $Holding(B)$, $Clear(C)$, $On(C,A)$, $OnTable(A)$ |
| 2 | $pickup(B)$ | $Holding(B)$ | $OnTable(B)$, $Clear(B)$, $HandEmpty$ | $OnTable(B)$, $Clear(B)$, $HandEmpty$, $Clear(C)$, $On(C,A)$, $OnTable(A)$ |
| 3 | $stack(C,A)$ | $On(C,A)$, $Clear(C)$, $HandEmpty$ | $Holding(C)$, $Clear(A)$ | $Holding(C)$, $Clear(A)$, $OnTable(B)$, $Clear(B)$, $OnTable(A)$ |
| 4 | $unstack(C,B)$ | $Holding(C)$, $Clear(B)$ | $On(C,B)$, $Clear(C)$, $HandEmpty$ | $On(C,B)$, $Clear(C)$, $HandEmpty$, $Clear(A)$, $OnTable(B)$, $OnTable(A)$ |

The goal at step 4 is **satisfied by the initial state**: $On(C,B)$, $Clear(C)$, $HandEmpty$, $Clear(A)$, $OnTable(A)$ and $OnTable(B)$ all hold. Stop.

(At step 3, $stack(C,A)$ is chosen because it achieves $On(C,A)$ and also supplies $Clear(C)$ and $HandEmpty$, which it adds. At step 4, $unstack(C,B)$ achieves $Holding(C)$ and $Clear(B)$.)

**Plan** (the regressed actions in reverse order): **unstack(C, B), stack(C, A), pickup(B), stack(B, C)**.
