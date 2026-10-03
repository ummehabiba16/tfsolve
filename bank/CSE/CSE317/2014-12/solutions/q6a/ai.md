---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "The stated goal is premise (iii) itself, so it follows at once (its negation resolves with clauses 3a and 3b). Intended conclusion, (forall x Student(x) => Healthy(x)) => forall x [Student(x) and exists y (Chess(y) and Plays(x,y))] => exists z (Tennis(z) and Plays(x,z)): negating gives N1-N5 with Skolem constants A, B and the function F; resolution derives Healthy(A), Plays(A,F(A)), Vigorous(F(A)), not Chess(F(A)), Tennis(F(A)) or Soccer(F(A)), not Tennis(F(A)), Soccer(F(A)), not Plays(A,F(A)), then the empty clause."
sources: ["AIMA 3e sec. 9.5 (conversion to CNF, Skolemization, resolution refutation)"]
---
**Predicate form.**

1. $\forall x,y\ [Student(y)\land Plays(y,x)]\Rightarrow Tennis(x)\lor Soccer(x)\lor Chess(x)$
2. $\forall x\ Chess(x)\Rightarrow\neg Vigorous(x)$
3. $\forall x\ Healthy(x)\Rightarrow\exists y\ [Plays(x,y)\land Vigorous(y)]$
4. $\forall x\ [\exists y\ (Chess(y)\land Plays(x,y))]\Rightarrow\neg\exists z\ (Soccer(z)\land Plays(x,z))$

Conclusion (Q):

$$[\forall x\ Student(x)\Rightarrow Healthy(x)]\Rightarrow\forall x\ [Student(x)\land\exists y\,(Chess(y)\land Plays(x,y))]\Rightarrow\exists z\,(Tennis(z)\land Plays(x,z))$$

**Clause form** (eliminate $\Rightarrow$, move $\neg$ in, Skolemize, drop $\forall$, distribute). $F$ is a Skolem function: in 3, $y$ depends on $x$.

- C1: $\neg Student(y)\lor\neg Plays(y,x)\lor Tennis(x)\lor Soccer(x)\lor Chess(x)$
- C2: $\neg Chess(x)\lor\neg Vigorous(x)$
- C3a: $\neg Healthy(x)\lor Plays(x,F(x))$
- C3b: $\neg Healthy(x)\lor Vigorous(F(x))$
- C4: $\neg Chess(y)\lor\neg Plays(x,y)\lor\neg Soccer(z)\lor\neg Plays(x,z)$

**The goal as printed.** "Anyone who is healthy plays something that is vigorous" is premise 3 itself. Its negation, $\exists x\ Healthy(x)\land\forall y\ \neg(Plays(x,y)\land Vigorous(y))$, gives the clauses $Healthy(K)$ and $\neg Plays(K,y)\lor\neg Vigorous(y)$. Then:

- $Healthy(K)$ with C3a gives $Plays(K,F(K))$, and with C3b gives $Vigorous(F(K))$;
- $\neg Plays(K,y)\lor\neg Vigorous(y)$ with $\{y/F(K)\}$ gives $\neg Vigorous(F(K))$;
- that resolves with $Vigorous(F(K))$ to the empty clause $\square$.

So the goal is proved trivially. The question very likely intends the **Conclusion**, which is proved next.

**Proof of the Conclusion by resolution.** Negate Q: $\forall x\,(Student(x)\Rightarrow Healthy(x))$, and some student $A$ plays some chess game $B$ and plays no tennis. With the Skolem constants $A$ and $B$:

- N1: $\neg Student(x)\lor Healthy(x)$
- N2: $Student(A)$
- N3: $Chess(B)$
- N4: $Plays(A,B)$
- N5: $\neg Tennis(z)\lor\neg Plays(A,z)$

| # | Resolvent | From (unifier) |
|:-:|:--|:--|
| 6 | $Healthy(A)$ | N1, N2 $\{x/A\}$ |
| 7 | $Plays(A,F(A))$ | C3a, 6 $\{x/A\}$ |
| 8 | $Vigorous(F(A))$ | C3b, 6 $\{x/A\}$ |
| 9 | $\neg Chess(F(A))$ | C2, 8 $\{x/F(A)\}$ |
| 10 | $\neg Plays(A,x)\lor Tennis(x)\lor Soccer(x)\lor Chess(x)$ | C1, N2 $\{y/A\}$ |
| 11 | $Tennis(F(A))\lor Soccer(F(A))\lor Chess(F(A))$ | 10, 7 $\{x/F(A)\}$ |
| 12 | $Tennis(F(A))\lor Soccer(F(A))$ | 11, 9 |
| 13 | $\neg Tennis(F(A))$ | N5, 7 $\{z/F(A)\}$ |
| 14 | $Soccer(F(A))$ | 12, 13 |
| 15 | $\neg Plays(x,B)\lor\neg Soccer(z)\lor\neg Plays(x,z)$ | C4, N3 $\{y/B\}$ |
| 16 | $\neg Soccer(z)\lor\neg Plays(A,z)$ | 15, N4 $\{x/A\}$ |
| 17 | $\neg Plays(A,F(A))$ | 16, 14 $\{z/F(A)\}$ |
| 18 | $\square$ | 17, 7 |

The empty clause is derived, so the Conclusion follows from the KB.

In words: a healthy student plays something vigorous, $F(A)$. Being vigorous, it is not chess (2), so it is tennis or soccer (1). A chess player plays no soccer (4), so $F(A)$ is tennis.
