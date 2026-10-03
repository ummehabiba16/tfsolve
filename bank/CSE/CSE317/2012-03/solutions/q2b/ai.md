---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "The substitution binds X1 to President(X1, Since(T2)), a term that contains X1 itself; the occurs check fails (it would need an infinite term), so the two atoms do not unify as given. (After standardizing apart, with X1 renamed in one sentence, they would unify.)"
sources: ["AIMA 3e sec. 9.2.2 (unification, occurs check, standardizing apart)"]
---
**Terms.**

(i) $SpringRevolution(2011,\ egypt,\ X1)$

(ii) $SpringRevolution(T1,\ C1,\ President(X1,\ Since(T2)))$

Argument by argument:

- $2011$ with $T1$ gives $\{2011/T1\}$: fine.
- $egypt$ with $C1$ gives $\{egypt/C1\}$: fine.
- $X1$ with $President(X1,Since(T2))$ gives $\{President(X1,Since(T2))/X1\}$: **invalid**.

**The problem: occurs check.** The variable $X1$ is bound to a term that **contains $X1$ itself**. Substituting gives

$$X1=President(President(President(\dots),Since(T2)),Since(T2)),Since(T2)),$$

an infinite term, which is not allowed in first-order logic. The **occurs check** of UNIFY detects that $X1$ occurs in $President(X1,Since(T2))$ and returns **failure**. So the substitution is not a unifier, and the two atoms **cannot be unified as written**.

**Underlying cause:** the two sentences share the variable name $X1$. Variables in different clauses are independent and should be **standardized apart** (e.g. rename $X1$ in (ii) to $X2$). Then

$$\{2011/T1,\ egypt/C1,\ President(X2,Since(T2))/X1\}$$

is a valid unifier.
