---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Skolemization removes existential quantifiers by replacing each existentially quantified variable with a new constant (if it is not inside any universal quantifier) or a new function of the enclosing universally quantified variables. Example: exists x P(x) becomes P(A); forall y exists x Loves(x, y) becomes forall y Loves(F(y), y). It preserves satisfiability, not logical equivalence."
sources: ["AIMA 3e sec. 9.5.1 (conversion to CNF, Skolemization)"]
---
**Skolemization** removes **existential quantifiers** during conversion to CNF, by replacing each existentially quantified variable with a new term:

- If $\exists x$ is **not** inside any universal quantifier, replace $x$ by a **new constant** (a Skolem constant):

$$\exists x\ P(x)\land Q(x)\quad\leadsto\quad P(A)\land Q(A).$$

- If $\exists x$ is inside $\forall y_1,\dots,y_k$, the value of $x$ may depend on them, so replace $x$ by a **new function** of them (a Skolem function):

$$\forall y\ \exists x\ Loves(x,y)\quad\leadsto\quad\forall y\ Loves(F(y),y),$$

where $F(y)$ is "the one who loves $y$". Using a constant here would wrongly say that one person loves everyone.

**Example** (AIMA): "Everyone who loves all animals is loved by someone."

$$\forall x\ [\exists y\ Animal(y)\land\neg Loves(x,y)]\lor[\exists z\ Loves(z,x)]$$

becomes

$$\forall x\ [Animal(F(x))\land\neg Loves(x,F(x))]\lor Loves(G(x),x).$$

Skolem function names must be **new** (not already used in the KB). The Skolemized sentence is **satisfiable iff the original is** (it is not logically equivalent), which is all that resolution refutation needs.
