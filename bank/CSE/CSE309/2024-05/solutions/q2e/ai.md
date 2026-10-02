---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "FOLLOW(S) = {end}, FOLLOW(A) = {b, c, d}, FOLLOW(B) = {b, c, d, e}, FOLLOW(C) = {d}, FOLLOW(D) = empty (D is unreachable)."
sources: ["MMA syntax analysis slides 76-102 (FIRST and FOLLOW)", "Dragon book 2e sec. 4.4.2"]
---
**FIRST sets** (needed for FOLLOW):

$$\text{FIRST}(C) = \{c, \epsilon\}, \quad \text{FIRST}(D) = \{d, \epsilon\}$$

$$\text{FIRST}(B) = \{b\} \cup \text{FIRST}(Cd) = \{b, c, d\}$$

$$\text{FIRST}(A) = \text{FIRST}(B) \cup \{\epsilon\} = \{b, c, d, \epsilon\}$$

$$\text{FIRST}(S) = \{a\}$$

**FOLLOW rules:** put \$ in FOLLOW(start); for $X \to \alpha B \beta$ add FIRST($\beta$) $- \{\epsilon\}$ to FOLLOW($B$); if $\beta$ is empty or derives $\epsilon$, add FOLLOW($X$) to FOLLOW($B$).

| Production | Contribution |
|:--|:--|
| start symbol | \$ $\in$ FOLLOW($S$) |
| $S \to aABe$ | FOLLOW($A$) $\supseteq$ FIRST($Be$) = {b, c, d} ($B$ does not derive $\epsilon$) |
| $S \to aABe$ | FOLLOW($B$) $\supseteq$ {e} |
| $A \to B$ | FOLLOW($B$) $\supseteq$ FOLLOW($A$) |
| $B \to bB$ | FOLLOW($B$) $\supseteq$ FOLLOW($B$) (nothing new) |
| $B \to Cd$ | FOLLOW($C$) $\supseteq$ {d} |
| $C \to cC$ | FOLLOW($C$) $\supseteq$ FOLLOW($C$) |
| $D \to dD$ | FOLLOW($D$) $\supseteq$ FOLLOW($D$) |

**Result:**

| Nonterminal | FOLLOW |
|:--|:--|
| $S$ | { \$ } |
| $A$ | { b, c, d } |
| $B$ | { b, c, d, e } |
| $C$ | { d } |
| $D$ | $\emptyset$ |

$D$ does not appear in the body of any production reachable from $S$ (it is unreachable), so nothing can follow it: FOLLOW($D$) is empty.
