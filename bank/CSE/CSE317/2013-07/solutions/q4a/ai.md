---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "FOL: Member(Tony), Member(Michael), Member(Ellen); forall x Member(x) => Skier(x) or Climber(x); forall x Climber(x) => not Likes(x, Rain); forall x Skier(x) => Likes(x, Snow); forall y Likes(Tony, y) => not Likes(Ellen, y); forall y not Likes(Tony, y) => Likes(Ellen, y); Likes(Tony, Rain); Likes(Tony, Snow). Query exists x Member(x) and Climber(x) and not Skier(x): resolution with an answer literal gives x = Ellen (Ellen dislikes snow, so she is not a skier, so she is a climber)."
sources: ["AIMA 3e sec. 9.5 (resolution, answer extraction)", "Nilsson / Rich & Knight Hoofers Club example"]
---
**(i) First-order logic.**

1. $Member(Tony)$, $Member(Michael)$, $Member(Ellen)$
2. $\forall x\ Member(x)\Rightarrow Skier(x)\lor Climber(x)$
3. $\forall x\ Climber(x)\Rightarrow\neg Likes(x,Rain)$
4. $\forall x\ Skier(x)\Rightarrow Likes(x,Snow)$
5. $\forall y\ Likes(Tony,y)\Rightarrow\neg Likes(Ellen,y)$
6. $\forall y\ \neg Likes(Tony,y)\Rightarrow Likes(Ellen,y)$
7. $Likes(Tony,Rain)$
8. $Likes(Tony,Snow)$

Query: $\exists x\ Member(x)\land Climber(x)\land\neg Skier(x)$.

**(ii) CNF.**

- C1a: $Member(Tony)$; C1b: $Member(Michael)$; C1c: $Member(Ellen)$
- C2: $\neg Member(x)\lor Skier(x)\lor Climber(x)$
- C3: $\neg Climber(x)\lor\neg Likes(x,Rain)$
- C4: $\neg Skier(x)\lor Likes(x,Snow)$
- C5: $\neg Likes(Tony,y)\lor\neg Likes(Ellen,y)$
- C6: $Likes(Tony,y)\lor Likes(Ellen,y)$
- C7: $Likes(Tony,Rain)$
- C8: $Likes(Tony,Snow)$

Negated query, with an answer literal to extract $x$:

- C9: $\neg Member(x)\lor\neg Climber(x)\lor Skier(x)\lor Answer(x)$

**(iii) Resolution (answer extraction).**

| # | Resolvent | From (unifier) |
|:-:|:--|:--|
| 10 | $\neg Likes(Ellen,Snow)$ | C5, C8 $\{y/Snow\}$ |
| 11 | $\neg Skier(Ellen)$ | C4, 10 $\{x/Ellen\}$ |
| 12 | $\neg Member(Ellen)\lor Climber(Ellen)$ | C2, 11 $\{x/Ellen\}$ |
| 13 | $Climber(Ellen)$ | 12, C1c |
| 14 | $\neg Member(Ellen)\lor Skier(Ellen)\lor Answer(Ellen)$ | C9, 13 $\{x/Ellen\}$ |
| 15 | $Skier(Ellen)\lor Answer(Ellen)$ | 14, C1c |
| 16 | $Answer(Ellen)$ | 15, 11 |

Only the answer literal remains, which counts as the empty clause. **The member who is a mountain climber but not a skier is Ellen.**

*Reasoning in words:* Tony likes snow, so Ellen dislikes snow (5). Skiers like snow (4), so Ellen is not a skier. Every member is a skier or a climber (2), so Ellen is a climber.
