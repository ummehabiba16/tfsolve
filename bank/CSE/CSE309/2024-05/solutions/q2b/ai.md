---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Both use the same LR(0) item sets, so states, shift and GOTO entries are identical; they differ only in reduce entries: SLR(0) (= LR(0)) puts reduce A->alpha in every column of a state containing A->alpha., while SLR(1) puts it only under terminals in FOLLOW(A), so SLR(1) has fewer conflicts."
sources: ["MMA syntax analysis slides 239-306 (LR(0) Automaton), 354-387 (Constructing SLR-Parsing Tables)", "Dragon book 2e sec. 4.6.2-4.6.4"]
---
Both tables are built from the **same canonical collection of LR(0) items**, so:

- the **number of states** is the same;
- the **shift** entries ($[A \to \alpha \cdot a\beta] \in I_i$ and GOTO$(I_i, a) = I_j$ gives `shift j`) are the same;
- the **GOTO** entries for nonterminals and the **accept** entry are the same.

The only difference is **where reduce entries are placed**:

| | SLR(0) (LR(0)) | SLR(1) |
|:--|:--|:--|
| Item $A \to \alpha \cdot$ in $I_i$ | reduce in **every** terminal column (and \$) of row $i$ | reduce only for $a \in$ FOLLOW($A$) |
| Lookahead used | none | one symbol |
| Conflicts | any state with a complete item plus another complete or shift item conflicts | only if the shift symbol or the other reduce lookaheads overlap FOLLOW($A$) |

**Example:** $E \to E + T \mid T$, $T \to \textbf{id}$. The state $\{E' \to E\cdot,\ E \to E \cdot + T\}$ in LR(0) must both reduce (accept) and shift on $+$: a conflict. In SLR(1), accept is only on \$ and shift on $+$: no conflict.

So an SLR(1) table has blank cells where an SLR(0) table has reduce actions, which makes SLR(1) handle more grammars.
