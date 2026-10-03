---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Stench in [2,1] gives W in [3,1] or [2,2]; stench in [1,2] gives W in [1,3] or [2,2] ([1,1] is excluded); one Wumpus, so W22. Breeze in [2,1] gives P31 or P22; breeze in [1,2] gives P13 or P22; the Wumpus never shares a square with a pit, so not P22, hence P31 and P13. So (i) [2,2] has the Wumpus; (ii) [1,3] and [3,1] contain pits, [2,2] does not."
sources: ["AIMA 3e sec. 7.2-7.4 (Wumpus world, propositional inference)"]
---
**Notation.** $W_{x,y}$ = Wumpus, $P_{x,y}$ = pit, $S_{x,y}$ = stench, $B_{x,y}$ = breeze in $[x,y]$ (column $x$, row $y$). Neighbours: $[2,1]$ is next to $[1,1]$, $[3,1]$, $[2,2]$; $[1,2]$ is next to $[1,1]$, $[1,3]$, $[2,2]$.

**Initial knowledge base.**

- Rules: $S_{x,y}\Leftrightarrow\bigvee_{\text{neighbours}}W$; $B_{x,y}\Leftrightarrow\bigvee_{\text{neighbours}}P$; exactly one Wumpus; no pit or Wumpus in $[1,1]$; the Wumpus is not in a pit square ($W_{x,y}\Rightarrow\neg P_{x,y}$).
- Percepts: $\neg S_{1,1}$, $\neg B_{1,1}$; $S_{2,1}$, $B_{2,1}$; $S_{1,2}$, $B_{1,2}$.

**(i) Does $[2,2]$ contain the Wumpus? Yes.**

1. $S_{2,1}\Leftrightarrow W_{1,1}\lor W_{3,1}\lor W_{2,2}$ with $S_{2,1}$ gives $W_{1,1}\lor W_{3,1}\lor W_{2,2}$.
2. $\neg W_{1,1}$ (start square) gives $W_{3,1}\lor W_{2,2}$.
3. Likewise, $S_{1,2}$ gives $W_{1,3}\lor W_{2,2}$.
4. There is exactly one Wumpus: $\neg W_{3,1}\lor\neg W_{1,3}$ (it cannot be in both).
5. Resolving (2) with (4) gives $W_{2,2}\lor\neg W_{1,3}$; with (3) this gives $W_{2,2}\lor W_{2,2}=W_{2,2}$.

So **the Wumpus is in $[2,2]$**. (Also, $\neg S_{1,1}$ rules out $W_{2,1}$ and $W_{1,2}$, consistent with the agent having survived there.)

**(ii) Pits in $[1,3]$, $[2,2]$, $[3,1]$?**

1. $W_{2,2}\Rightarrow\neg P_{2,2}$ gives **$\neg P_{2,2}$: no pit in $[2,2]$**.
2. $B_{2,1}\Leftrightarrow P_{1,1}\lor P_{3,1}\lor P_{2,2}$ with $B_{2,1}$, $\neg P_{1,1}$ and $\neg P_{2,2}$ gives **$P_{3,1}$: a pit in $[3,1]$**.
3. $B_{1,2}\Leftrightarrow P_{1,1}\lor P_{1,3}\lor P_{2,2}$ with $B_{1,2}$, $\neg P_{1,1}$ and $\neg P_{2,2}$ gives **$P_{1,3}$: a pit in $[1,3]$**.

| Square | Wumpus? | Pit? |
|:-:|:-:|:-:|
| [2,2] | **yes** | **no** |
| [1,3] | no | **yes** |
| [3,1] | no | **yes** |

The third pit is somewhere else, undetermined. (Checked by enumerating all placements of 1 Wumpus and 3 pits consistent with the percepts: in all 10 models the Wumpus is in $[2,2]$, and pits are in $[1,3]$ and $[3,1]$.)
