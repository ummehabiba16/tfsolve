---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Facts: Father(Fred,Harry), Father(Fred,Bill), Father(Harry,Tom), Father(Harry,John). Rules: Father(x,y) and Father(y,z) => Grandfather(x,z); Father(p,x) and Father(p,y) and x != y => Brother(x,y); Brother(x,y) and Father(y,z) => Uncle(x,z). Forward chaining: Grandfather(Fred,Tom) from {x/Fred, y/Harry, z/Tom}; Brother(Bill,Harry) from {p/Fred}; Uncle(Bill,Tom) from {x/Bill, y/Harry, z/Tom}."
sources: ["AIMA 3e sec. 9.3 (forward chaining, Datalog)"]
---
**Datalog knowledge base** (function-free definite clauses).

Facts:

1. $Father(Fred,Harry)$
2. $Father(Fred,Bill)$
3. $Father(Harry,Tom)$
4. $Father(Harry,John)$

Rules:

5. $Father(x,y)\land Father(y,z)\Rightarrow Grandfather(x,z)$
6. $Father(p,x)\land Father(p,y)\land x\neq y\Rightarrow Brother(x,y)$
7. $Brother(x,y)\land Father(y,z)\Rightarrow Uncle(x,z)$

($\neq$ is a built-in test on constants under the unique-names assumption of Datalog. The people are taken to be male, as the question implies.)

**Forward chaining.** In each iteration, apply every rule whose premises unify with known facts, and add new conclusions until no new fact appears.

*Iteration 1*:

- Rule 5 with facts 1 and 3, $\theta=\{x/Fred,\ y/Harry,\ z/Tom\}$, gives **$Grandfather(Fred,Tom)$** (8). (With facts 1 and 4 it also gives $Grandfather(Fred,John)$.)
- Rule 6 with facts 1 and 2, $\theta=\{p/Fred,\ x/Harry,\ y/Bill\}$, gives $Brother(Harry,Bill)$ (9); with $\{p/Fred,\ x/Bill,\ y/Harry\}$ it gives **$Brother(Bill,Harry)$** (10). (Also $Brother(Tom,John)$ and $Brother(John,Tom)$ from facts 3 and 4.)

*Iteration 2*:

- Rule 7 with facts 10 and 3, $\theta=\{x/Bill,\ y/Harry,\ z/Tom\}$, gives **$Uncle(Bill,Tom)$** (11). (Also $Uncle(Bill,John)$.)

*Iteration 3*: no new facts, so a fixed point is reached.

**Proved:** (i) $Grandfather(Fred,Tom)$ (8) and (ii) $Uncle(Bill,Tom)$ (11). Forward chaining is sound and complete for Datalog, and terminates in polynomially many steps.
