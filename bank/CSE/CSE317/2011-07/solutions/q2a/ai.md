---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "CNF uses the Skolem function F(x) (the lottery loved by x) and the Skolem constant K (a Baptist who does not both vote and oppose). Negated goal: not Baptist(x) or Votes(x); Wins(LP); not Baptist(x) or Faithful(x). Resolution: Baptist(K); not Votes(K) or not Opposes(K,LP); Votes(K); not Opposes(K,LP); Favors(K,LP); Lottery(F(K)); Loves(K,F(K)); Gambler(K); Faithful(K); not Gambler(K); empty clause."
sources: ["AIMA 3e sec. 9.5 (CNF, Skolemization, resolution refutation)"]
---
**Predicate form.** Predicates: $Lottery(y)$, $Loves(x,y)$, $Gambler(x)$, $Favors(x,LP)$, $Opposes(x,LP)$, $Baptist(x)$, $Votes(x)$, $Wins(LP)$, $Faithful(x)$. $LP$ is the lottery proposition.

1. $\forall x\ [\exists y\ Lottery(y)\land Loves(x,y)]\Rightarrow Gambler(x)$
2. $\forall x\ Favors(x,LP)\Rightarrow\exists y\ Lottery(y)\land Loves(x,y)$
3. $\forall x\ Favors(x,LP)\lor Opposes(x,LP)$
4. $[\forall x\ Baptist(x)\Rightarrow Votes(x)\land Opposes(x,LP)]\Rightarrow\neg Wins(LP)$
5. $\forall x\ Baptist(x)\land Faithful(x)\Rightarrow\neg Gambler(x)$

**Clause form.**

- C1: $\neg Lottery(y)\lor\neg Loves(x,y)\lor Gambler(x)$
- C2a: $\neg Favors(x,LP)\lor Lottery(F(x))$ and C2b: $\neg Favors(x,LP)\lor Loves(x,F(x))$ ($F$ is a Skolem function)
- C3: $Favors(x,LP)\lor Opposes(x,LP)$
- Sentence 4 is $\neg\forall x[\dots]\lor\neg Wins(LP)$, i.e. $[\exists x\ Baptist(x)\land(\neg Votes(x)\lor\neg Opposes(x,LP))]\lor\neg Wins(LP)$. With the Skolem constant $K$:

- C4a: $Baptist(K)\lor\neg Wins(LP)$ and C4b: $\neg Votes(K)\lor\neg Opposes(K,LP)\lor\neg Wins(LP)$.
- C5: $\neg Baptist(x)\lor\neg Faithful(x)\lor\neg Gambler(x)$

**Goal:** $[\forall x\ Baptist(x)\Rightarrow Votes(x)]\land Wins(LP)\Rightarrow\exists x\ Baptist(x)\land\neg Faithful(x)$.

Negated goal: N1: $\neg Baptist(x)\lor Votes(x)$; N2: $Wins(LP)$; N3: $\neg Baptist(x)\lor Faithful(x)$.

**Resolution proof.**

| # | Resolvent | From (unifier) |
|:-:|:--|:--|
| 6 | $Baptist(K)$ | C4a, N2 |
| 7 | $\neg Votes(K)\lor\neg Opposes(K,LP)$ | C4b, N2 |
| 8 | $Votes(K)$ | N1, 6 $\{x/K\}$ |
| 9 | $\neg Opposes(K,LP)$ | 7, 8 |
| 10 | $Favors(K,LP)$ | C3, 9 $\{x/K\}$ |
| 11 | $Lottery(F(K))$ | C2a, 10 $\{x/K\}$ |
| 12 | $Loves(K,F(K))$ | C2b, 10 $\{x/K\}$ |
| 13 | $\neg Loves(x,F(K))\lor Gambler(x)$ | C1, 11 $\{y/F(K)\}$ |
| 14 | $Gambler(K)$ | 13, 12 $\{x/K\}$ |
| 15 | $Faithful(K)$ | N3, 6 $\{x/K\}$ |
| 16 | $\neg Faithful(K)\lor\neg Gambler(K)$ | C5, 6 $\{x/K\}$ |
| 17 | $\neg Gambler(K)$ | 16, 15 |
| 18 | $\square$ | 17, 14 |

The empty clause is derived, so the conclusion is proved.

In words: the proposition wins, so not every Baptist votes against it. Some Baptist $K$ votes but does not oppose it, so $K$ favours it, loves some lottery, and is a gambler. A faithful Baptist is not a gambler, so $K$ is not faithful.
