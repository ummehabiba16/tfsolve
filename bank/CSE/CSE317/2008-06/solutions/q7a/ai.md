---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "From the stenches: W in [3,1] or [2,2] and W in [1,3] or [2,2], with one Wumpus, so W22: (i) yes, the Wumpus is in [2,2]. The Wumpus is not in a pit, so not P22; the breeze in [2,1] then gives P31 and the breeze in [1,2] gives P13: (ii) pits in [1,3] and [3,1], not in [2,2]."
sources: ["AIMA 3e sec. 7.2-7.5 (Wumpus world, propositional inference)"]
---
**Notation.** $W_{x,y}$, $P_{x,y}$, $S_{x,y}$, $B_{x,y}$ for Wumpus, pit, stench and breeze in $[x,y]$ ($x$ = column, $y$ = row).

**Knowledge base.**

- Rules: $S_{x,y}\Leftrightarrow$ (a Wumpus in an adjacent square); $B_{x,y}\Leftrightarrow$ (a pit in an adjacent square); exactly one Wumpus; no pit or Wumpus in $[1,1]$; $W_{x,y}\Rightarrow\neg P_{x,y}$.
- Percepts: $\neg S_{1,1}$, $\neg B_{1,1}$; $S_{2,1}$, $B_{2,1}$; $S_{1,2}$, $B_{1,2}$.

Neighbours: $[2,1]$ is next to $[1,1]$, $[3,1]$, $[2,2]$; $[1,2]$ is next to $[1,1]$, $[1,3]$, $[2,2]$.

**(i) Is the Wumpus in $[2,2]$? Yes.**

1. $S_{2,1}$ gives $W_{1,1}\lor W_{3,1}\lor W_{2,2}$; with $\neg W_{1,1}$: $W_{3,1}\lor W_{2,2}$.
2. $S_{1,2}$ gives $W_{1,1}\lor W_{1,3}\lor W_{2,2}$; so $W_{1,3}\lor W_{2,2}$.
3. There is only one Wumpus: $\neg W_{3,1}\lor\neg W_{1,3}$.
4. Resolving (1) with (3) gives $W_{2,2}\lor\neg W_{1,3}$; with (2) this gives $W_{2,2}$.

So **the Wumpus is in $[2,2]$**.

**(ii) Pits in $[1,3]$, $[2,2]$, $[3,1]$?**

1. $W_{2,2}\Rightarrow\neg P_{2,2}$ gives **no pit in $[2,2]$**.
2. $B_{2,1}\Leftrightarrow P_{1,1}\lor P_{3,1}\lor P_{2,2}$, with $\neg P_{1,1}$ and $\neg P_{2,2}$, gives **$P_{3,1}$: a pit in $[3,1]$**.
3. $B_{1,2}\Leftrightarrow P_{1,1}\lor P_{1,3}\lor P_{2,2}$ gives **$P_{1,3}$: a pit in $[1,3]$**.

The third pit's location is not determined. (The same percepts appear in the 2013 paper; enumerating all consistent models confirms these conclusions.)
