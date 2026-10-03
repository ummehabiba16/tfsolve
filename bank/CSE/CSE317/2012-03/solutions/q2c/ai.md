---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "KB in FOL and clauses (Cat5, Within5km, Submerged, KnockedDown, LivesIn, GoesToShelter, Drowns, Crushed, Dies); the query 'exists t Dies(Hamidur, t)' with the answer literal not Dies(Hamidur, t) or Answer(t) resolves through Drowns, Submerged, LivesIn(Hamidur, Patenga, Apr29_1991), not GoesToShelter, Cat5(Bangladesh, Apr29_1991) and Within5km(Patenga, Bangladesh) to Answer(Apr29_1991): he died on April 29, 1991 (by drowning)."
sources: ["AIMA 3e sec. 9.5 (resolution, answer extraction)"]
---
**Predicates.** $Cat5Hits(c,t)$: a category-5 cyclone hits country $c$'s coastline at time $t$. $Within5(a,c)$: area $a$ is within 5 km of $c$'s coastline. $Submerged(a,t)$; $House(h)$; $In(h,a)$; $KnockedDown(h,t)$; $LivesIn(p,x,t)$ (person $p$ lives in area or house $x$ at $t$); $GoesToShelter(p,t)$; $Drowns(p,t)$; $Crushed(p,t)$; $Dies(p,t)$. Constants: $Bangladesh$, $Patenga$, $Hamidur$, $D$ (= April 29, 1991).

**Predicate form.**

1. $\forall c,t\ Cat5Hits(c,t)\Rightarrow[\forall a\ Within5(a,c)\Rightarrow Submerged(a,t)]\land[\forall h,a\ House(h)\land In(h,a)\land Within5(a,c)\Rightarrow KnockedDown(h,t)]$
2. $\forall a,t\ Submerged(a,t)\Rightarrow\forall p\ [LivesIn(p,a,t)\land\neg GoesToShelter(p,t)\Rightarrow Drowns(p,t)]$
3. $\forall h,t\ KnockedDown(h,t)\Rightarrow\forall p\ [LivesIn(p,h,t)\Rightarrow Crushed(p,t)]$
4. $\forall p,t\ Drowns(p,t)\lor Crushed(p,t)\Rightarrow Dies(p,t)$
5. $Cat5Hits(Bangladesh,D)$
6. $LivesIn(Hamidur,Patenga,D)$
7. $Within5(Patenga,Bangladesh)$
8. $\neg GoesToShelter(Hamidur,D)$

**Clause form.**

- C1a: $\neg Cat5Hits(c,t)\lor\neg Within5(a,c)\lor Submerged(a,t)$
- C1b: $\neg Cat5Hits(c,t)\lor\neg House(h)\lor\neg In(h,a)\lor\neg Within5(a,c)\lor KnockedDown(h,t)$
- C2: $\neg Submerged(a,t)\lor\neg LivesIn(p,a,t)\lor GoesToShelter(p,t)\lor Drowns(p,t)$
- C3: $\neg KnockedDown(h,t)\lor\neg LivesIn(p,h,t)\lor Crushed(p,t)$
- C4a: $\neg Drowns(p,t)\lor Dies(p,t)$
- C4b: $\neg Crushed(p,t)\lor Dies(p,t)$
- C5-C8 as above (unit clauses).

**Query** "When did Hamidur Rahman die?" is $\exists t\ Dies(Hamidur,t)$. Negate it and add an answer literal:

- Q: $\neg Dies(Hamidur,t)\lor Answer(t)$

**Resolution.**

| # | Resolvent | From (unifier) |
|:-:|:--|:--|
| 9 | $\neg Drowns(Hamidur,t)\lor Answer(t)$ | Q, C4a $\{p/Hamidur\}$ |
| 10 | $\neg Submerged(a,t)\lor\neg LivesIn(Hamidur,a,t)\lor GoesToShelter(Hamidur,t)\lor Answer(t)$ | 9, C2 $\{p/Hamidur\}$ |
| 11 | $\neg Submerged(Patenga,D)\lor GoesToShelter(Hamidur,D)\lor Answer(D)$ | 10, C6 $\{a/Patenga,\ t/D\}$ |
| 12 | $\neg Submerged(Patenga,D)\lor Answer(D)$ | 11, C8 |
| 13 | $\neg Cat5Hits(c,D)\lor\neg Within5(Patenga,c)\lor Answer(D)$ | 12, C1a $\{a/Patenga,\ t/D\}$ |
| 14 | $\neg Within5(Patenga,Bangladesh)\lor Answer(D)$ | 13, C5 $\{c/Bangladesh\}$ |
| 15 | $Answer(D)$ | 14, C7 |

Only the answer literal is left, so **Hamidur Rahman died on April 29, 1991** (by drowning: Patenga was submerged and he did not go to the shelter).

*Note:* "cyclone center" in (viii) is taken to mean the cyclone shelter of (ii). Without information about his house, the crushing branch (C1b, C3) is not needed.
