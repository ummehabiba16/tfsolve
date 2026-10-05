---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "TWEAK's five steps: step addition (add a new step to achieve p), promotion (order a clobberer after the step that needs p), declobbering (insert a white-knight step re-asserting p), simple establishment (use an existing step that asserts p), separation (add non-codesignation constraints so that a clobberer cannot delete p); examples from the blocks world."
sources: ["Rich & Knight, Artificial Intelligence, sec. 13.5", "Chapman 1987 (TWEAK)"]
---
TWEAK repeatedly takes a precondition $p$ of some step $s$ that is not yet *necessarily* true, and applies one of five plan modifications:

1. **Step addition:** add a **new step** whose effect is $p$, ordered before $s$.
*Example:* $STACK(A,B)$ needs $HOLDING(A)$, so add $PICKUP(A)$ before it.

2. **Promotion:** if a step $c$ might delete $p$ before $s$ uses it, order $c$ **after** $s$.
*Example:* $PICKUP(B)$ deletes $ARMEMPTY$, which $PICKUP(A)$ needs; promote it after $STACK(A,\dots)$, which restores $ARMEMPTY$.

3. **Declobbering:** if a clobberer $c$ must stay before $s$, insert a **white knight** step $w$ with $c\prec w\prec s$ that re-asserts $p$.
*Example:* after $PICKUP(C)$ (which clobbers $ARMEMPTY$), insert $PUTDOWN(C)$ to restore $ARMEMPTY$ before another $PICKUP$.

4. **Simple establishment:** use an **existing** step (or the initial state) that already asserts $p$.
*Example:* $STACK(A,B)$ needs $CLEAR(B)$, already made true by an earlier $UNSTACK(C,B)$.

5. **Separation:** add a **non-codesignation** constraint so that a clobberer's deleted literal cannot unify with $p$.
*Example:* $STACK(x,y)$ deletes $CLEAR(y)$; to protect $CLEAR(B)$, add the constraint $y\neq B$.
