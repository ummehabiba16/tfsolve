---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "FIRST(S) = FIRST(T) = {(, a}; FIRST(A) = {+, \\*, (, a}; FIRST(B) = {+, \\*, (, a, eps}. FOLLOW(S) = FOLLOW(T) = FOLLOW(A) = FOLLOW(B) = {+, \\*, (, a, ), end}."
sources: ["MMA syntax analysis slides 76-102 (FIRST and FOLLOW)", "Dragon book 2e sec. 4.4.2"]
---
**FIRST sets**

$$\text{FIRST}(T) = \{(,\ a\}$$

$$\text{FIRST}(S) = \text{FIRST}(TB) = \text{FIRST}(T) = \{(,\ a\}$$

($T$ does not derive $\epsilon$.)

$$\text{FIRST}(A) = \{+\} \cup \text{FIRST}(TB) \cup \{*\} = \{+,\ *,\ (,\ a\}$$

$$\text{FIRST}(B) = \text{FIRST}(AB) \cup \{\epsilon\} = \{+,\ *,\ (,\ a,\ \epsilon\}$$

**FOLLOW sets.** Constraints from each production:

| Production | Constraint |
|:--|:--|
| start | \$ $\in$ FOLLOW($S$) |
| $S \to TB$ | FOLLOW($T$) $\supseteq$ FIRST($B$) $- \epsilon$ = {+, \*, (, a}; $B \Rightarrow \epsilon$, so FOLLOW($T$) $\supseteq$ FOLLOW($S$); FOLLOW($B$) $\supseteq$ FOLLOW($S$) |
| $T \to (S)$ | FOLLOW($S$) $\supseteq$ { ) } |
| $A \to +S$ | FOLLOW($S$) $\supseteq$ FOLLOW($A$) |
| $A \to TB$ | FOLLOW($T$) $\supseteq$ {+, \*, (, a} $\cup$ FOLLOW($A$); FOLLOW($B$) $\supseteq$ FOLLOW($A$) |
| $B \to AB$ | FOLLOW($A$) $\supseteq$ FIRST($B$) $- \epsilon$ = {+, \*, (, a}; $B \Rightarrow \epsilon$, so FOLLOW($A$) $\supseteq$ FOLLOW($B$) |

Solving: FOLLOW($A$) $\supseteq$ {+, \*, (, a}; FOLLOW($S$) $\supseteq$ {\$, )} $\cup$ FOLLOW($A$); FOLLOW($B$) $\supseteq$ FOLLOW($S$) $\cup$ FOLLOW($A$); FOLLOW($A$) $\supseteq$ FOLLOW($B$). These form a cycle $S \to B \to A \to S$, so all three are equal, and FOLLOW($T$) contains them too.

| Nonterminal | FIRST | FOLLOW |
|:-:|:--|:--|
| $S$ | ( , a | + , \* , ( , a , ) , \$ |
| $T$ | ( , a | + , \* , ( , a , ) , \$ |
| $A$ | + , \* , ( , a | + , \* , ( , a , ) , \$ |
| $B$ | + , \* , ( , a , $\epsilon$ | + , \* , ( , a , ) , \$ |

(Note: FIRST($AB$) $\cap$ FOLLOW($B$) $\ne \emptyset$, so the grammar is not LL(1). It is ambiguous: $B \to AB \mid \epsilon$ together with $A \to TB$.)
