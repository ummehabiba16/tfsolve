---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "14 LR(1) item sets I0-I13; the key ones are I6 = {[A -> c., d], [B -> c., e]} (after ac) and I9 = {[A -> c., e], [B -> c., d]} (after bc)."
sources: ["MMA syntax analysis slides 407-478 (Canonical LR(1) Items, Constructing LR(1) Sets of Items)", "Dragon book 2e sec. 4.7.2, Example 4.58"]
---
Augment and number the productions:

$$(0)\ S' \to S \quad (1)\ S \to aAd \quad (2)\ S \to bBd$$

$$(3)\ S \to aBe \quad (4)\ S \to bAe \quad (5)\ A \to c \quad (6)\ B \to c$$

Closure: for $[X \to \alpha \cdot Y\beta, x]$ add $[Y \to \cdot\gamma, y]$ for $y \in$ FIRST($\beta x$). For example, in $I_2$, $[S \to a \cdot Ad, \$]$ gives $[A \to \cdot c, d]$, and $[S \to a \cdot Be, \$]$ gives $[B \to \cdot c, e]$.

| State | LR(1) items | GOTO |
|:-:|:--|:--|
| $I_0$ | $[S' \to \cdot S, \$]$, $[S \to \cdot aAd, \$]$, $[S \to \cdot bBd, \$]$, $[S \to \cdot aBe, \$]$, $[S \to \cdot bAe, \$]$ | S: $I_1$, a: $I_2$, b: $I_3$ |
| $I_1$ | $[S' \to S \cdot, \$]$ | |
| $I_2$ | $[S \to a \cdot Ad, \$]$, $[S \to a \cdot Be, \$]$, $[A \to \cdot c, d]$, $[B \to \cdot c, e]$ | A: $I_4$, B: $I_5$, c: $I_6$ |
| $I_3$ | $[S \to b \cdot Bd, \$]$, $[S \to b \cdot Ae, \$]$, $[A \to \cdot c, e]$, $[B \to \cdot c, d]$ | A: $I_7$, B: $I_8$, c: $I_9$ |
| $I_4$ | $[S \to aA \cdot d, \$]$ | d: $I_{10}$ |
| $I_5$ | $[S \to aB \cdot e, \$]$ | e: $I_{11}$ |
| $I_6$ | $[A \to c \cdot, d]$, $[B \to c \cdot, e]$ | |
| $I_7$ | $[S \to bA \cdot e, \$]$ | e: $I_{12}$ |
| $I_8$ | $[S \to bB \cdot d, \$]$ | d: $I_{13}$ |
| $I_9$ | $[A \to c \cdot, e]$, $[B \to c \cdot, d]$ | |
| $I_{10}$ | $[S \to aAd \cdot, \$]$ | |
| $I_{11}$ | $[S \to aBe \cdot, \$]$ | |
| $I_{12}$ | $[S \to bAe \cdot, \$]$ | |
| $I_{13}$ | $[S \to bBd \cdot, \$]$ | |

$I_6$ and $I_9$ have the same core $\{A \to c\cdot, B \to c\cdot\}$ but different lookaheads. This is what makes the grammar LR(1) but not LALR(1) (see part (c)).
