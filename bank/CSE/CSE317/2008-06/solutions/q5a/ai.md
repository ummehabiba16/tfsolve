---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "FOL: Member(Tony), Member(Michael), Member(Ellen); Member(x) => Skier(x) or Climber(x); Climber(x) => not Likes(x,Rain); Skier(x) => Likes(x,Snow); Likes(Tony,y) <=> not Likes(Ellen,y); Likes(Tony,Rain), Likes(Tony,Snow). CNF clauses as listed. Resolution refutation with an answer literal proves yes: Ellen is a mountain climber but not a skier."
sources: ["AIMA 3e sec. 9.5 (resolution, answer extraction)"]
---
**(i) First-order logic** (10).

1. $Member(Tony)\land Member(Michael)\land Member(Ellen)$
2. $\forall x\ Member(x)\Rightarrow Skier(x)\lor Climber(x)$
3. $\forall x\ Climber(x)\Rightarrow\neg Likes(x,Rain)$
4. $\forall x\ Skier(x)\Rightarrow Likes(x,Snow)$
5. $\forall y\ Likes(Tony,y)\Leftrightarrow\neg Likes(Ellen,y)$
6. $Likes(Tony,Rain)\land Likes(Tony,Snow)$

Query: $\exists x\ Member(x)\land Climber(x)\land\neg Skier(x)$.

**(ii) CNF** (5).

- C1: $Member(Tony)$; C2: $Member(Michael)$; C3: $Member(Ellen)$
- C4: $\neg Member(x)\lor Skier(x)\lor Climber(x)$
- C5: $\neg Climber(x)\lor\neg Likes(x,Rain)$
- C6: $\neg Skier(x)\lor Likes(x,Snow)$
- C7: $\neg Likes(Tony,y)\lor\neg Likes(Ellen,y)$
- C8: $Likes(Tony,y)\lor Likes(Ellen,y)$
- C9: $Likes(Tony,Rain)$; C10: $Likes(Tony,Snow)$

**(iii) Resolution refutation** (10). Negate the query and add an answer literal:

- Q: $\neg Member(x)\lor\neg Climber(x)\lor Skier(x)\lor Answer(x)$

| # | Resolvent | From (unifier) |
|:-:|:--|:--|
| 11 | $\neg Likes(Ellen,Snow)$ | C7, C10 $\{y/Snow\}$ |
| 12 | $\neg Skier(Ellen)$ | C6, 11 $\{x/Ellen\}$ |
| 13 | $\neg Member(Ellen)\lor Climber(Ellen)$ | C4, 12 $\{x/Ellen\}$ |
| 14 | $Climber(Ellen)$ | 13, C3 |
| 15 | $\neg Member(Ellen)\lor Skier(Ellen)\lor Answer(Ellen)$ | Q, 14 $\{x/Ellen\}$ |
| 16 | $Skier(Ellen)\lor Answer(Ellen)$ | 15, C3 |
| 17 | $Answer(Ellen)$ | 16, 12 |

**Yes**: there is such a member, namely **Ellen**. Tony likes snow, so Ellen does not; hence she is not a skier; every member is a skier or a climber, so she is a climber.
