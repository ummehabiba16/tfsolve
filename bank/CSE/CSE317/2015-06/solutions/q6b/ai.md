---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(i) Yes: not B12 and (not P22 or B12) resolve to not P22. (ii) Yes: B21 with (not B21 or P11 or P31 or P22), then not P11 and not P22, gives P31. (iii) Cannot be proved: S13 gives W12 or W23 or W14, and not W12 (the agent survived [1,2]) leaves W23 or W14, but no percept rules out [2,3]; e.g. Wumpus at [2,3] with pits at [3,1], [1,4] and 2 others is consistent with every percept, so W14 is not entailed."
sources: ["AIMA 3e sec. 7.2 and 7.5.2 (Wumpus world, resolution)"]
---
**Notation.** $P_{x,y}$ = pit in $[x,y]$; $W_{x,y}$ = Wumpus in $[x,y]$; $B_{x,y}$ = breeze and $S_{x,y}$ = stench perceived in $[x,y]$. $[x,y]$ is column $x$, row $y$.

**Percepts** (facts): $\neg B_{1,1}$, $\neg S_{1,1}$; $B_{2,1}$, $\neg S_{2,1}$; $\neg B_{1,2}$, $\neg S_{1,2}$; $B_{1,3}$, $S_{1,3}$.

The agent visited $[1,1]$, $[2,1]$, $[1,2]$ and $[1,3]$ and is alive, so none of them has a pit or the Wumpus: $\neg P_{1,1}$, $\neg W_{1,2}$, and so on.

**Rules used** (from the biconditionals, in CNF):

- R1: $B_{1,2}\Leftrightarrow(P_{1,1}\lor P_{2,2}\lor P_{1,3})$ contains the clause $\neg P_{2,2}\lor B_{1,2}$.
- R2: $B_{2,1}\Leftrightarrow(P_{1,1}\lor P_{3,1}\lor P_{2,2})$ contains the clause $\neg B_{2,1}\lor P_{1,1}\lor P_{3,1}\lor P_{2,2}$.
- R3: $S_{1,3}\Leftrightarrow(W_{1,2}\lor W_{2,3}\lor W_{1,4})$ contains the clause $\neg S_{1,3}\lor W_{1,2}\lor W_{2,3}\lor W_{1,4}$.

**(i) $[2,2]$ contains no pit: $\neg P_{2,2}$. Proved.** Add the negated goal $P_{2,2}$.

1. $P_{2,2}$ with $\neg P_{2,2}\lor B_{1,2}$ (R1) gives $B_{1,2}$.
2. $B_{1,2}$ with $\neg B_{1,2}$ (percept) gives the empty clause $\square$.

**(ii) $[3,1]$ contains a pit: $P_{3,1}$. Proved.** Add the negated goal $\neg P_{3,1}$.

1. $\neg B_{2,1}\lor P_{1,1}\lor P_{3,1}\lor P_{2,2}$ (R2) with $B_{2,1}$ gives $P_{1,1}\lor P_{3,1}\lor P_{2,2}$.
2. With $\neg P_{1,1}$ (the start square has no pit): $P_{3,1}\lor P_{2,2}$.
3. With $\neg P_{2,2}$ (from (i)): $P_{3,1}$.
4. With $\neg P_{3,1}$: $\square$.

**(iii) $[1,4]$ contains the Wumpus: $W_{1,4}$. Cannot be proved.** Add $\neg W_{1,4}$.

1. R3 with $S_{1,3}$ gives $W_{1,2}\lor W_{2,3}\lor W_{1,4}$.
2. With $\neg W_{1,2}$ (the agent was in $[1,2]$ and survived; also $\neg S_{1,1}$ rules it out): $W_{2,3}\lor W_{1,4}$.
3. With $\neg W_{1,4}$: $W_{2,3}$.

Nothing in the KB contradicts $W_{2,3}$. The only percepts near $[2,3]$ come from $[1,3]$, which has a stench, while $[2,2]$, $[3,3]$ and $[2,4]$ have not been visited. Resolution saturates without $\square$.

Indeed, there is a model of the KB with the Wumpus in $[2,3]$: pits in $[3,1]$, $[1,4]$ (explaining the breeze in $[1,3]$) and two other squares, e.g. $[4,3]$ and $[4,4]$. It agrees with every percept. A second model has the Wumpus in $[1,4]$ and pits in $[3,1]$ and $[2,3]$ (plus two others).

So $KB\not\models W_{1,4}$: the Wumpus is in **$[1,4]$ or $[2,3]$**, but which one is undetermined.

*Note:* we checked this by enumerating all placements of 4 pits and 1 Wumpus consistent with the percepts (56 models). $\neg P_{2,2}$ and $P_{3,1}$ hold in all of them, while the Wumpus is in $[1,4]$ in some and in $[2,3]$ in others.
