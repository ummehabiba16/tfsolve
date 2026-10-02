---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "CLR table: 0: a s2, b s3, GOTO S 1; 1: end acc; 2: c s6, A 4, B 5; 3: c s9, A 7, B 8; 4: d s10; 5: e s11; 6: d r5 (A->c), e r6 (B->c); 7: e s12; 8: d s13; 9: d r6, e r5; 10-13: end r1, r3, r4, r2. No conflicts, so the grammar is LR(1)."
sources: ["MMA syntax analysis slides 479-489 (Canonical LR(1) Parsing Tables)", "Dragon book 2e sec. 4.7.3 (Algorithm 4.56)"]
---
Productions: (1) $S \to aAd$, (2) $S \to bBd$, (3) $S \to aBe$, (4) $S \to bAe$, (5) $A \to c$, (6) $B \to c$.

Rules (Algorithm 4.56): $[A \to \alpha \cdot a\beta, b]$ in $I_i$ with GOTO($I_i, a$) = $I_j$ gives ACTION$[i, a]$ = shift $j$; $[A \to \alpha \cdot, a]$ gives ACTION$[i, a]$ = reduce $A \to \alpha$ (only on the lookahead $a$); $[S' \to S \cdot, \$]$ gives accept.

| State | a | b | c | d | e | \$ | S | A | B |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | s2 | s3 | | | | | 1 | | |
| 1 | | | | | | acc | | | |
| 2 | | | s6 | | | | | 4 | 5 |
| 3 | | | s9 | | | | | 7 | 8 |
| 4 | | | | s10 | | | | | |
| 5 | | | | | s11 | | | | |
| 6 | | | | r5 | r6 | | | | |
| 7 | | | | | s12 | | | | |
| 8 | | | | s13 | | | | | |
| 9 | | | | r6 | r5 | | | | |
| 10 | | | | | | r1 | | | |
| 11 | | | | | | r3 | | | |
| 12 | | | | | | r4 | | | |
| 13 | | | | | | r2 | | | |

There are no multiply-defined entries, so the grammar is **LR(1)**.

Look at states 6 and 9: after `ac`, reduce to $A$ if `d` follows and to $B$ if `e` follows; after `bc`, the opposite. In an LALR table these two states would be merged, giving r5/r6 in both columns d and e: a reduce/reduce conflict.
