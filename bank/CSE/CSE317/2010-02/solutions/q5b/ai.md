---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "CNF steps: eliminate <=> and =>, move not inwards, standardize variables, Skolemize, drop the universal quantifiers, distribute or over and. Reading the sentence as forall x exists y [forall z (loves(x,z) => loves(y,z))] and loves(x,y): Skolemize y as F(x), giving the clauses (not loves(x,z) or loves(F(x),z)) and loves(x, F(x))."
sources: ["AIMA 3e sec. 9.5.1 (conversion to CNF)"]
---
**Steps for converting FOL to CNF.**

1. **Eliminate biconditionals and implications:** $\alpha\Leftrightarrow\beta$ becomes $(\alpha\Rightarrow\beta)\land(\beta\Rightarrow\alpha)$, and $\alpha\Rightarrow\beta$ becomes $\neg\alpha\lor\beta$.
2. **Move $\neg$ inwards:** $\neg\forall x\,p$ becomes $\exists x\,\neg p$; $\neg\exists x\,p$ becomes $\forall x\,\neg p$; De Morgan; $\neg\neg p$ becomes $p$.
3. **Standardize variables:** give each quantifier its own variable name.
4. **Skolemize:** remove each $\exists$, replacing its variable by a Skolem function of the enclosing $\forall$ variables (or by a constant if there are none).
5. **Drop the universal quantifiers** (all remaining variables are universal).
6. **Distribute $\lor$ over $\land$**, to get a conjunction of disjunctions (clauses).

**Conversion** of $\forall x\,\exists y\,\big(\forall z\ loves(x,z)\Rightarrow loves(y,z)\big)\land loves(x,y)$, read as "for every $x$ there is a $y$ who loves everyone $x$ loves, and $x$ loves $y$":

$$\forall x\,\exists y\,\Big[\forall z\,\big(loves(x,z)\Rightarrow loves(y,z)\big)\Big]\land loves(x,y)$$

*Step 1* (eliminate $\Rightarrow$):

$$\forall x\,\exists y\,\Big[\forall z\,\big(\neg loves(x,z)\lor loves(y,z)\big)\Big]\land loves(x,y)$$

*Steps 2 and 3:* no negations to move; the variables are already distinct.

*Step 4* (Skolemize $y$, which depends on $x$): $y\mapsto F(x)$:

$$\forall x\,\Big[\forall z\,\big(\neg loves(x,z)\lor loves(F(x),z)\big)\Big]\land loves(x,F(x))$$

*Step 5* (drop $\forall$):

$$\big(\neg loves(x,z)\lor loves(F(x),z)\big)\land loves(x,F(x))$$

*Step 6:* already in CNF. **Two clauses:**

- C1: $\neg loves(x,z)\lor loves(F(x),z)$
- C2: $loves(x,F(x))$

*Note:* if instead $\forall z$ is read as scoping only over $loves(x,z)$, i.e. $(\forall z\ loves(x,z))\Rightarrow loves(y,z)$, then $z$ in $loves(y,z)$ would be free. The reading above, with $\forall z$ over the whole implication, is assumed, since it is the only one that gives a sentence.
