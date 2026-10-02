---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "FIRST(S) = FIRST(A) = {(, a}, FIRST(B) = {+, eps}; FOLLOW(S) = {+, ), end}, FOLLOW(A) = FOLLOW(B) = {)}. Table: M[S,(] = S -> (A), M[S,a] = S -> a, M[A,(] = M[A,a] = A -> SB, M[B,+] = B -> +SB, M[B,)] = B -> eps; no conflicts (LL(1))."
sources: ["MMA syntax analysis slides 76-123 (FIRST and FOLLOW, Predictive Parsing Table)", "Dragon book 2e sec. 4.4.2-4.4.3 (Algorithm 4.31)"]
---
**FIRST (3 marks)**

$$\text{FIRST}(S) = \{(,\ a\}$$

$$\text{FIRST}(A) = \text{FIRST}(SB) = \text{FIRST}(S) = \{(,\ a\}$$

$$\text{FIRST}(B) = \{+,\ \epsilon\}$$

**FOLLOW (3 marks)**

- \$ $\in$ FOLLOW($S$) (start symbol).
- $S \to (A)$: FOLLOW($A$) $\supseteq$ { ) }.
- $A \to SB$: FOLLOW($S$) $\supseteq$ FIRST($B$) $- \epsilon$ = { + }; since $B \Rightarrow \epsilon$, FOLLOW($S$) $\supseteq$ FOLLOW($A$). Also FOLLOW($B$) $\supseteq$ FOLLOW($A$).
- $B \to +SB$: FOLLOW($S$) $\supseteq$ { + } $\cup$ FOLLOW($B$); FOLLOW($B$) $\supseteq$ FOLLOW($B$).

| Nonterminal | FIRST | FOLLOW |
|:-:|:--|:--|
| $S$ | ( , a | + , ) , \$ |
| $A$ | ( , a | ) |
| $B$ | + , $\epsilon$ | ) |

**Predictive parsing table (4 marks)**

| | ( | ) | a | + | \$ |
|:-:|:-:|:-:|:-:|:-:|:-:|
| $S$ | $S \to (A)$ | | $S \to a$ | | |
| $A$ | $A \to SB$ | | $A \to SB$ | | |
| $B$ | | $B \to \epsilon$ | | $B \to +SB$ | |

($B \to \epsilon$ is entered under FOLLOW($B$) = { ) }.) No cell has more than one entry, so the grammar is LL(1).

Check on `(a+a)`: $S \Rightarrow (A) \Rightarrow (SB) \Rightarrow (aB) \Rightarrow (a+SB) \Rightarrow (a+aB) \Rightarrow (a+a)$, using $M[S,(]$, $M[A,a]$, $M[S,a]$, $M[B,+]$, $M[S,a]$, $M[B,)]$.
