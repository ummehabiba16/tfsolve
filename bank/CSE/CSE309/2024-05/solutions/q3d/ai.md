---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "LL(1): FIRST(AaAb) = {a}, FIRST(BbBa) = {b}, disjoint (and A, B only derive eps), so the table has no conflict. Not SLR(1): I0 contains A -> . and B -> . with FOLLOW(A) = FOLLOW(B) = {a, b}, so ACTION[0,a] and ACTION[0,b] both get reduce A->eps and reduce B->eps (reduce/reduce conflict)."
sources: ["MMA syntax analysis slides 103-123 (LL(1) Grammars), 354-387 (Constructing SLR-Parsing Tables)", "Dragon book 2e sec. 4.4.3, 4.6.4, Exercise 4.6.6"]
---
Grammar: $(1)\ S \to AaAb$, $(2)\ S \to BbBa$, $(3)\ A \to \epsilon$, $(4)\ B \to \epsilon$.

**FIRST and FOLLOW**

$$\text{FIRST}(A) = \text{FIRST}(B) = \{\epsilon\}$$

$$\text{FIRST}(AaAb) = \{a\}, \quad \text{FIRST}(BbBa) = \{b\}$$

$$\text{FOLLOW}(S) = \{\$\}$$

$$\text{FOLLOW}(A) = \{a, b\}, \quad \text{FOLLOW}(B) = \{a, b\}$$

($A$ is followed by $a$ in $AaAb$ and by $b$ in $\ldots Ab$; similarly for $B$.)

**Part 1: LL(1).** LL(1) table:

| | a | b | \$ |
|:-:|:-:|:-:|:-:|
| $S$ | $S \to AaAb$ | $S \to BbBa$ | |
| $A$ | $A \to \epsilon$ | $A \to \epsilon$ | |
| $B$ | $B \to \epsilon$ | $B \to \epsilon$ | |

- For $S$: FIRST($AaAb$) $\cap$ FIRST($BbBa$) = $\{a\} \cap \{b\} = \emptyset$, and neither derives $\epsilon$.
- $A$ and $B$ each have only one production.

Every cell has at most one entry, so the grammar is **LL(1)**. In top-down parsing, the parser first decides on $S$ by looking at $a$ or $b$, and only then expands $A$ or $B$.

**Part 2: not SLR(1).** The initial LR(0) state:

$$I_0:\ S' \to \cdot S, \quad S \to \cdot AaAb, \quad S \to \cdot BbBa$$

$$A \to \cdot, \quad B \to \cdot$$

$I_0$ contains **two complete items**, $A \to \cdot$ and $B \to \cdot$. SLR puts

- reduce by $A \to \epsilon$ under FOLLOW($A$) = {a, b}, and
- reduce by $B \to \epsilon$ under FOLLOW($B$) = {a, b}.

So ACTION[0, a] = {r3, r4} and ACTION[0, b] = {r3, r4}: a **reduce/reduce conflict**. The grammar is **not SLR(1)**.

**Reason:** a bottom-up parser must decide to reduce $\epsilon$ to $A$ or to $B$ *before* reading any input. SLR uses FOLLOW sets, which mix both contexts. (An LR(1) parser has lookaheads $[A \to \cdot, a]$ and $[B \to \cdot, b]$ in $I_0$, so the grammar is LR(1).)
