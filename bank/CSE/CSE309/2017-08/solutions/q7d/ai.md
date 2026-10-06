---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A -> X {R.i = f(X.x)} R {A.a = R.s}; R -> Y {R1.i = g(R.i, Y.y)} R1 {R.s = R1.s} | eps {R.s = R.i}, using the inherited attribute R.i to carry the value computed so far and the synthesized R.s to return the final value."
sources: ["KMS Chapter 5 slides 48-69 (sdt-left-recursion)", "Dragon book 2e sec. 5.4.4"]
---
Eliminating left recursion from an SDT (Dragon book sec. 5.4.4): the grammar part $A \to A_1 Y \mid X$ becomes $A \to X R$, $R \to Y R \mid \epsilon$. The semantic actions are moved so that the same values are computed:

- the *value computed so far* is passed to $R$ as an **inherited** attribute $R.i$;
- the *final value* is returned as a **synthesized** attribute $R.s$.

Original:

$$A \to A_1 Y\ \{A.a = g(A_1.a, Y.y)\}$$

$$A \to X\ \{A.a = f(X.x)\}$$

Transformed:

$$A \to X\ \{R.i = f(X.x)\}\ R\ \{A.a = R.s\}$$

$$R \to Y\ \{R_1.i = g(R.i, Y.y)\}\ R_1\ \{R.s = R_1.s\}$$

$$R \to \epsilon\ \{R.s = R.i\}$$

**Check on `X Y1 Y2`.** Original: $A.a = g(g(f(X.x), Y_1.y), Y_2.y)$. Transformed: $R.i = f(X.x)$; the first $R$ passes $R_1.i = g(f(X.x), Y_1.y)$ to the second $R$, which passes $R_2.i = g(R_1.i, Y_2.y)$ to the third $R \to \epsilon$; the last gives $R.s = R.i = g(g(f(X.x), Y_1.y), Y_2.y)$, which returns up the chain as $R.s$, and $A.a = R.s$. The result is the same.
