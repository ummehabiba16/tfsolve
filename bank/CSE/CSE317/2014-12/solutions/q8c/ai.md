---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "TWEAK (Chapman) builds a partial-order plan with five plan modifications: step addition (add a new step to achieve a goal), promotion (order a clobbering step after the step it threatens), declobbering (insert a white-knight step that re-asserts p after the clobberer), simple establishment (make an existing step achieve the precondition by binding variables), and separation (add codesignation constraints so that the clobberer's effect cannot unify with p)."
sources: ["Rich & Knight, Artificial Intelligence, sec. 13.5 (non-linear planning using constraint posting, TWEAK)", "Chapman 1987"]
---
TWEAK is a non-linear (partial-order, constraint-posting) planner. For each precondition $p$ of a step $s$ that is not yet necessarily true (by the modal truth criterion), it applies one of five plan modifications:

1. **Step addition:** add a new step $t$ whose effect asserts $p$, ordered before $s$.
*Example:* to achieve $ON(A,B)$, add $STACK(A,B)$ before the step that needs it.

2. **Promotion:** if a step $c$ might clobber (delete) $p$ between its establisher $t$ and $s$, order $c$ **after** $s$ ($s\prec c$), so it cannot interfere.
*Example:* move $UNSTACK(A,B)$ to after the step that needs $ON(A,B)$.

3. **Declobbering:** if a clobberer $c$ cannot be moved, insert a **"white knight"** step $w$ between $c$ and $s$ ($c\prec w\prec s$) that re-asserts $p$.
*Example:* if $PICKUP(C)$ deletes $ARMEMPTY$, add $PUTDOWN(D)$ after it to restore $ARMEMPTY$.

4. **Simple establishment:** use an **existing** step (or the initial state) that asserts $p$ (possibly after binding variables), and order it before $s$.
*Example:* $CLEAR(B)$ needed by $STACK(A,B)$ is already established by an earlier $UNSTACK(C,B)$.

5. **Separation:** prevent a possible clobberer from denying $p$ by adding a **non-codesignation constraint** ($x\neq y$), so that its deleted proposition cannot unify with $p$.
*Example:* if $STACK(x,y)$ deletes $CLEAR(y)$ and $p=CLEAR(B)$, add the constraint $y\neq B$.

TWEAK repeatedly picks an unachieved precondition and applies one of these modifications, backtracking over the choices, until every precondition is necessarily true.
