---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "PL-FC-ENTAILS with agenda [A, B] and a count of unproven premises per rule: popping A, B fires A and B => C; C fires B and C => E and A and C => P; E fires C and E => D; P gives no firing; D fires A and D => C, D => E and D and P => Q; Q fires P and Q => R; R fires A and D and R => S; S is popped, so the KB entails S."
sources: ["AIMA 3e sec. 7.5.4 (forward chaining, PL-FC-ENTAILS?, Fig. 7.15)"]
---
**Data structures.** `count[c]` = the number of premises of rule $c$ not yet known; `inferred[s]` = whether symbol $s$ has been processed; `agenda` = a FIFO queue of symbols known true but not yet processed. A symbol is checked against the query when it is popped.

**Rules and initial counts.**

| Rule | 1: $A\land B\Rightarrow C$ | 2: $A\land D\Rightarrow C$ | 3: $B\land C\Rightarrow E$ | 4: $C\land E\Rightarrow D$ | 5: $A\land C\Rightarrow P$ | 6: $D\Rightarrow E$ | 7: $D\land P\Rightarrow Q$ | 8: $P\land Q\Rightarrow R$ | 9: $A\land D\land R\Rightarrow S$ |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| count | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 |

Initially the agenda is $[A, B]$ (the facts) and nothing is inferred.

**Trace.** Counts are listed for rules 1-9.

| Step | Pop | Counts after decrementing | Rules that fire (count reaches 0) | Agenda after | Inferred |
|:-:|:-:|:--|:--|:--|:--|
| 1 | A | 1,1,2,2,1,1,2,2,2 | none | [B] | A |
| 2 | B | 0,1,1,2,1,1,2,2,2 | 1, so add C | [C] | A, B |
| 3 | C | 0,1,0,1,0,1,2,2,2 | 3 (add E), 5 (add P) | [E, P] | A, B, C |
| 4 | E | 0,1,0,0,0,1,2,2,2 | 4, so add D | [P, D] | +E |
| 5 | P | 0,1,0,0,0,1,1,1,2 | none | [D] | +P |
| 6 | D | 0,0,0,0,0,0,0,1,1 | 2 (add C), 6 (add E), 7 (add Q) | [C, E, Q] | +D |
| 7 | C | already inferred, skip | | [E, Q] | |
| 8 | E | already inferred, skip | | [Q] | |
| 9 | Q | 0,0,0,0,0,0,0,0,1 | 8, so add R | [R] | +Q |
| 10 | R | 0,0,0,0,0,0,0,0,0 | 9, so add S | [S] | +R |
| 11 | **S** | S is the query | | | |

**Result:** $S$ is popped from the agenda, so PL-FC-ENTAILS returns **true**: $KB\models S$. (Derivation: $C$ from $A,B$; then $E$ and $P$; $D$ from $C,E$; $Q$ from $D,P$; $R$ from $P,Q$; $S$ from $A,D,R$.)
