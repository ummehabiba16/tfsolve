---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Yes. The substitution binds X1 to Senator(X1, Illinois), a term that contains X1 itself; the occurs check fails (X1 would be an infinite term Senator(Senator(...), Illinois)), so the two atoms do not unify. A correct unifier exists only if the variable did not occur in the term."
sources: ["AIMA 3e sec. 9.2.2 (unification, occurs check)"]
---
**The terms.**

1. $President(Obama,\ 2014,\ X1)$
2. $President(X2,\ T1,\ Senator(X1,\ Illinois))$

Unify argument by argument:

- $Obama$ with $X2$ gives $\{Obama/X2\}$. Fine.
- $2014$ with $T1$ gives $\{2014/T1\}$. Fine.
- $X1$ with $Senator(X1,Illinois)$ gives $\{Senator(X1,Illinois)/X1\}$. **Problem.**

**The problem: occurs check.** A variable cannot be bound to a term that **contains the same variable**. Applying $\{Senator(X1,Illinois)/X1\}$ never terminates:

$$X1=Senator(X1,Illinois)=Senator(Senator(X1,Illinois),Illinois)=\dots$$

This would need an **infinite term**, which does not exist in first-order logic. The **occurs check** in the UNIFY algorithm detects that $X1$ occurs inside $Senator(X1,Illinois)$ and returns **failure**.

So **the two expressions are not unifiable**, and the given substitution is invalid. If the variables were standardized apart first (e.g. the second sentence used $Y1$ instead of $X1$), the unifier $\{Obama/X2,\ 2014/T1,\ Senator(Y1,Illinois)/X1\}$ would be fine.
