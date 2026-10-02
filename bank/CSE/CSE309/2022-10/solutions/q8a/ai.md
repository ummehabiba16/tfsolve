---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Treating the dollar sign in T -> S END as the end marker (written END): FIRST(T) = FIRST(S) = {a, b, c}, FIRST(D) = {a, c, eps}, FIRST(V) = {a, c}, FIRST(E) = {c, eps}. FOLLOW(T) = {END}, FOLLOW(S) = {END}, FOLLOW(D) = {b}, FOLLOW(V) = {a, b, c}, FOLLOW(E) = {a, b, c, END}."
sources: ["MMA syntax analysis slides 76-102 (FIRST and FOLLOW)", "Dragon book 2e sec. 4.4.2"]
---
**Assumptions.** The `$` in $T \to S$ \$ is the end-marker terminal. $T$ is the start symbol, so by the FOLLOW rules \$ is also in FOLLOW($T$).

**FIRST (5 marks)**

$$\text{FIRST}(E) = \{c, \epsilon\}$$

$$\text{FIRST}(V) = \{c\} \cup \{a\} = \{a, c\}$$

$$\text{FIRST}(D) = \text{FIRST}(V) \cup \{\epsilon\} = \{a, c, \epsilon\}$$

$$\text{FIRST}(S) = \text{FIRST}(DbE)$$

Since $D \overset{*}{\Rightarrow} \epsilon$, this is $(\text{FIRST}(D) - \{\epsilon\}) \cup \{b\} = \{a, b, c\}$.

$$\text{FIRST}(T) = \text{FIRST}(S) = \{a, b, c\}$$

**FOLLOW (10 marks)**

| Production | Contribution |
|:--|:--|
| start symbol | \$ $\in$ FOLLOW($T$) |
| $T \to S$ \$ | FOLLOW($S$) $\supseteq$ {\$} |
| $S \to D\,b\,E$ | FOLLOW($D$) $\supseteq$ {b}; FOLLOW($E$) $\supseteq$ FOLLOW($S$) = {\$} |
| $D \to V\,D$ | FOLLOW($V$) $\supseteq$ FIRST($D$) $-\ \epsilon$ = {a, c}; $D \overset{*}{\Rightarrow} \epsilon$, so FOLLOW($V$) $\supseteq$ FOLLOW($D$) = {b} |
| $V \to c\,d\,E$, $V \to a\,c\,d\,E$ | FOLLOW($E$) $\supseteq$ FOLLOW($V$) = {a, b, c} |

**Result:**

| Nonterminal | FIRST | FOLLOW |
|:-:|:--|:--|
| $T$ | a, b, c | \$ |
| $S$ | a, b, c | \$ |
| $D$ | a, c, $\epsilon$ | b |
| $V$ | a, c | a, b, c |
| $E$ | c, $\epsilon$ | a, b, c, \$ |

(Remark: $c \in$ FIRST($c$) and $c \in$ FOLLOW($E$), so $E \to c \mid \epsilon$ gives a conflict in $M[E, c]$; the grammar is not LL(1).)
