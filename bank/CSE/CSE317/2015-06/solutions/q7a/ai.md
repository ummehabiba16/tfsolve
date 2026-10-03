---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Symbols: Swim, NotSunny, NotFriday, Friday, NotSwim, Library, StudyAI, Headache, ConsultBarry, KillMary, IceCream, NotHome. Definite clauses: NotSunny and NotFriday => NotSwim; NotSwim => Library; Library => StudyAI; StudyAI => Headache; NotSwim and Headache => ConsultBarry; ConsultBarry and Friday => KillMary; ConsultBarry and NotFriday => IceCream; Library => NotHome; facts NotSunny, NotFriday. Forward chaining derives NotSwim, Library, StudyAI, Headache, ConsultBarry, IceCream."
sources: ["AIMA 3e sec. 7.5.3-7.5.4 (Horn and definite clauses, forward chaining)"]
---
**(i) Symbols.**

| Definition | Symbol |
|:--|:--|
| Mary goes swimming | $Swim$ |
| Mary does not go swimming | $NotSwim$ |
| It is sunny | $Sunny$ |
| It is not sunny | $NotSunny$ |
| It is Friday | $Friday$ |
| It is not Friday | $NotFriday$ |
| Mary goes to the library | $Library$ |
| Mary studies AI | $StudyAI$ |
| Mary has a headache | $Headache$ |
| Mary consults Dr. Barry | $ConsultBarry$ |
| Dr. Barry kills Mary | $KillMary$ |
| Dr. Barry gives Mary ice cream | $IceCream$ |
| Mary does not return home by sunset | $NotHome$ |

**(ii) Definite clauses.** A **definite clause** is a disjunction of literals with **exactly one positive** literal. Equivalently it is a rule $p_1\land\dots\land p_n\Rightarrow q$ (all premises positive) or a single fact $q$. Negated conditions such as "not sunny" are made positive by introducing new symbols ($NotSunny$, $NotSwim$, $NotFriday$).

Knowledge base:

1. $Sunny\Rightarrow Swim$ and $Friday\Rightarrow Swim$ (the "if" half of the "iff")
2. $NotSunny\land NotFriday\Rightarrow NotSwim$ (the "only if" half, with the new symbols)
3. $NotSwim\Rightarrow Library$
4. $Library\Rightarrow StudyAI$
5. $StudyAI\Rightarrow Headache$
6. $NotSwim\land Headache\Rightarrow ConsultBarry$
7. $ConsultBarry\land Friday\Rightarrow KillMary$
8. $ConsultBarry\land NotFriday\Rightarrow IceCream$
9. $Library\Rightarrow NotHome$
10. $NotSunny$ (fact)
11. $NotFriday$ (fact)

**(iii) Forward chaining to prove $IceCream$.** Agenda = [NotSunny, NotFriday]. Rules fire when all their premises are known.

| Step | Pop | Rule that fires | New fact added |
|:-:|:--|:--|:--|
| 1 | $NotSunny$ | (rule 2 still needs $NotFriday$) | |
| 2 | $NotFriday$ | 2: $NotSunny\land NotFriday\Rightarrow NotSwim$ | $NotSwim$ |
| 3 | $NotSwim$ | 3: $NotSwim\Rightarrow Library$ | $Library$ |
| 4 | $Library$ | 4 and 9 | $StudyAI$, $NotHome$ |
| 5 | $StudyAI$ | 5: $StudyAI\Rightarrow Headache$ | $Headache$ |
| 6 | $NotHome$ | none | |
| 7 | $Headache$ | 6: $NotSwim\land Headache\Rightarrow ConsultBarry$ | $ConsultBarry$ |
| 8 | $ConsultBarry$ | 8: $ConsultBarry\land NotFriday\Rightarrow IceCream$ | $IceCream$ |
| 9 | $IceCream$ | the query is reached | |

(Rule 7 never fires: $Friday$ is never derived.)

So **"Dr. Barry gives Mary ice cream"** is entailed.
