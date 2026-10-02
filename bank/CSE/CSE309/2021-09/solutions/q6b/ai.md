---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Grammar 1 is LL(1): the two a-bodies belong to different nonterminals (A -> aA vs bd, B -> aB vs cc), and an LL(1) parser chooses only among the alternatives of one nonterminal, whose FIRST sets {a},{b} and {a},{c} are disjoint. Grammar 2 is not: A -> aA | ad both have FIRST {a}, so M[A,a] has two entries (left factoring A -> aA', A' -> A | d fixes it)."
sources: ["MMA syntax analysis slides 103-123 (LL(1) Grammars, Predictive Parsing Table)", "Dragon book 2e sec. 4.4.3"]
---
**LL(1) condition:** for every nonterminal, the alternatives of **that nonterminal** must have disjoint FIRST sets (plus the FOLLOW condition for $\epsilon$-bodies; neither grammar has $\epsilon$-productions). Bodies of *different* nonterminals may start with the same terminal, because the parser never chooses between two different nonterminals: the nonterminal to expand is given by the stack/procedure.

**Grammar 1:** $A \to aA \mid bd$, $B \to aB \mid cc$

- $A$: FIRST($aA$) = {a}, FIRST($bd$) = {b}: disjoint.
- $B$: FIRST($aB$) = {a}, FIRST($cc$) = {c}: disjoint.

| | a | b | c |
|:-:|:-:|:-:|:-:|
| $A$ | $A \to aA$ | $A \to bd$ | |
| $B$ | $B \to aB$ | | $B \to cc$ |

Each cell has at most one production, so Grammar 1 is **LL(1)**. The two bodies starting with $a$ ($aA$ and $aB$) belong to different nonterminals, so they never compete.

**Grammar 2:** $A \to aA \mid ad$, $B \to bB \mid cc$

- $A$: FIRST($aA$) = FIRST($ad$) = {a}: **not disjoint**.
- $B$: FIRST($bB$) = {b}, FIRST($cc$) = {c}: disjoint.

$M[A, a] = \{A \to aA,\ A \to ad\}$, a multiply-defined entry. On input $a$ the parser cannot decide whether this $a$ is the last one (followed by $d$) or not. Grammar 2 is **not LL(1)**. (It is LL(2): the second symbol, $a$ or $d$, decides.)

**Fix:** left factor $A \to aA'$, $A' \to A \mid d$. Now FIRST($A$) = {a} and FIRST($d$) = {d}, so the grammar becomes LL(1).
