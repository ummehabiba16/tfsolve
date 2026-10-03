---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "TWEAK's five plan modifications (operations): step addition, promotion, declobbering (white knight), simple establishment, and separation."
sources: ["Rich & Knight, Artificial Intelligence, sec. 13.5", "Chapman 1987 (TWEAK)"]
---
TWEAK achieves each precondition $p$ of a step $s$ that is not yet necessarily true (by the modal truth criterion) using one of five plan modifications:

1. **Step addition:** create a **new step** whose effect asserts $p$, and order it before $s$. *Example:* add $STACK(A,B)$ to achieve $ON(A,B)$.
2. **Promotion:** if a step $c$ could clobber (delete) $p$, constrain $c$ to come **after** $s$, so it cannot destroy $p$ before $s$ uses it.
3. **Declobbering:** if a clobberer $c$ might come between the establisher and $s$, insert a **"white knight"** step $w$ after $c$ and before $s$ that **re-asserts** $p$.
4. **Simple establishment:** use an **existing** step (or the initial state) that already asserts $p$, possibly binding variables, ordered before $s$.
5. **Separation:** add a **non-codesignation constraint** (e.g. $x\neq B$) so that a possible clobberer's delete effect **cannot unify** with $p$.

Steps 2, 3 and 5 resolve threats; steps 1 and 4 establish preconditions. TWEAK applies them, backtracking over choices, until every precondition of every step is necessarily true.
