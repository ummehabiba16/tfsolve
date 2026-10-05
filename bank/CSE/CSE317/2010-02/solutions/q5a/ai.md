---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Axioms: Boy(x) or Girl(x) => Child(x); Child(x) => GetsDoll(x) or GetsTrain(x) or GetsBicycle(x); Boy(x) => not GetsDoll(x); Child(x) and Good(x) => not GetsBicycle(x); Boy(Jack). Negating the goal 'not GetsTrain(Jack) => not (Good(Jack) and Boy(Jack))' adds not GetsTrain(Jack) and Good(Jack); resolution derives Child(Jack), GetsDoll or GetsBicycle, not GetsDoll(Jack), GetsBicycle(Jack), not GetsBicycle(Jack), then the empty clause."
sources: ["AIMA 3e sec. 8.3 and 9.5 (FOL representation, resolution refutation)", "Nilsson / Genesereth (toy problem)"]
---
**First-order logic** (predicates $Boy$, $Girl$, $Child$, $Good$, $GetsDoll$, $GetsTrain$, $GetsBicycle$):

1. $\forall x\ (Boy(x)\lor Girl(x))\Rightarrow Child(x)$
2. $\forall x\ Child(x)\Rightarrow GetsDoll(x)\lor GetsTrain(x)\lor GetsBicycle(x)$
3. $\forall x\ Boy(x)\Rightarrow\neg GetsDoll(x)$
4. $\forall x\ Child(x)\land Good(x)\Rightarrow\neg GetsBicycle(x)$
5. $Boy(Jack)$

Goal: $\neg GetsTrain(Jack)\Rightarrow\neg(Good(Jack)\land Boy(Jack))$.

**Clauses.**

- C1a: $\neg Boy(x)\lor Child(x)$; C1b: $\neg Girl(x)\lor Child(x)$
- C2: $\neg Child(x)\lor GetsDoll(x)\lor GetsTrain(x)\lor GetsBicycle(x)$
- C3: $\neg Boy(x)\lor\neg GetsDoll(x)$
- C4: $\neg Child(x)\lor\neg Good(x)\lor\neg GetsBicycle(x)$
- C5: $Boy(Jack)$

Negated goal: $\neg GetsTrain(Jack)\land Good(Jack)\land Boy(Jack)$, giving

- N1: $\neg GetsTrain(Jack)$
- N2: $Good(Jack)$
- (N3: $Boy(Jack)$, the same as C5)

**Resolution proof.**

| # | Resolvent | From (unifier) |
|:-:|:--|:--|
| 6 | $Child(Jack)$ | C1a, C5 $\{x/Jack\}$ |
| 7 | $GetsDoll(Jack)\lor GetsTrain(Jack)\lor GetsBicycle(Jack)$ | C2, 6 |
| 8 | $GetsDoll(Jack)\lor GetsBicycle(Jack)$ | 7, N1 |
| 9 | $\neg GetsDoll(Jack)$ | C3, C5 $\{x/Jack\}$ |
| 10 | $GetsBicycle(Jack)$ | 8, 9 |
| 11 | $\neg Good(Jack)\lor\neg GetsBicycle(Jack)$ | C4, 6 $\{x/Jack\}$ |
| 12 | $\neg GetsBicycle(Jack)$ | 11, N2 |
| 13 | $\square$ | 10, 12 |

The empty clause is derived, so **"If Jack does not get a train, then Jack is not a good boy"** is proved. (Jack is a boy, so he gets no doll; if he gets no train, he gets a bicycle; good children do not get bicycles; so he is not good.)
