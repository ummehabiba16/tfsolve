---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Intellectual(x) => OnHitList(x); OnHitList(x) and not Hiding(x) => Captured(x); Captured(x) => Murdered(x, Dec14_1971); Intellectual(Selina); not Hiding(Selina). Query exists t Murdered(Selina, t): resolving not Murdered(Selina, t) or Answer(t) step by step gives Answer(Dec14_1971): she was murdered on December 14, 1971."
sources: ["AIMA 3e sec. 9.5 (resolution with answer extraction)"]
---
**Predicate form.** $Intellectual(x)$; $OnHitList(x)$ (in the hit-list created by the traitors); $Hiding(x)$ (went into hiding); $Captured(x)$ (captured by the traitors); $Murdered(x,t)$ (murdered by the traitors on date $t$). Constants: $Selina$, $D$ = 14 December 1971.

1. $\forall x\ Intellectual(x)\Rightarrow OnHitList(x)$
2. $\forall x\ OnHitList(x)\land\neg Hiding(x)\Rightarrow Captured(x)$
3. $\forall x\ Captured(x)\Rightarrow Murdered(x,D)$
4. $Intellectual(Selina)$
5. $\neg Hiding(Selina)$

**Clause form.**

- C1: $\neg Intellectual(x)\lor OnHitList(x)$
- C2: $\neg OnHitList(x)\lor Hiding(x)\lor Captured(x)$
- C3: $\neg Captured(x)\lor Murdered(x,D)$
- C4: $Intellectual(Selina)$
- C5: $\neg Hiding(Selina)$

**Query** "When was Selina Parvin murdered?", i.e. $\exists t\ Murdered(Selina,t)$. Negate it and add an answer literal:

- Q: $\neg Murdered(Selina,t)\lor Answer(t)$

| # | Resolvent | From (unifier) |
|:-:|:--|:--|
| 6 | $\neg Captured(Selina)\lor Answer(D)$ | Q, C3 $\{x/Selina,\ t/D\}$ |
| 7 | $\neg OnHitList(Selina)\lor Hiding(Selina)\lor Answer(D)$ | 6, C2 $\{x/Selina\}$ |
| 8 | $\neg OnHitList(Selina)\lor Answer(D)$ | 7, C5 |
| 9 | $\neg Intellectual(Selina)\lor Answer(D)$ | 8, C1 $\{x/Selina\}$ |
| 10 | $Answer(D)$ | 9, C4 |

**Answer:** Selina Parvin was murdered on **14 December 1971**.
