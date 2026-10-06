---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Left-factored grammar: S -> T ; S | eps; T -> U T'; T' -> * T | eps; U -> x | y | [ S ]. FIRST(S) = {x, y, [, eps}, FIRST(T) = FIRST(U) = {x, y, [}, FIRST(T') = {*, eps}; FOLLOW(S) = {\\$, ]}, FOLLOW(T) = FOLLOW(T') = {;}, FOLLOW(U) = {*, ;}."
sources: ["MMA syntax analysis slides 61-102 (left factoring, FIRST/FOLLOW)", "Dragon book 2e sec. 4.3.4, 4.4.2"]
---
Grammar: $S \to T;\,S \mid \epsilon$, $T \to U*T \mid U$, $U \to x \mid y \mid [S]$.

**Left factoring.** Only $T$ has two alternatives with a common prefix, $U$: $T \to U * T \mid U$. Write $T \to U\,T'$, $T' \to *T \mid \epsilon$:

$$S \to T\ ;\ S \mid \epsilon$$

$$T \to U\,T'$$

$$T' \to *\,T \mid \epsilon$$

$$U \to x \mid y \mid [\,S\,]$$

**FIRST sets.**

- $\text{FIRST}(U) = \{x, y, [\}$.
- $\text{FIRST}(T) = \text{FIRST}(U) = \{x, y, [\}$ (since $T \to U\,T'$ and $U$ is not nullable).
- $\text{FIRST}(T') = \{*, \epsilon\}$.
- $\text{FIRST}(S) = \text{FIRST}(T) \cup \{\epsilon\} = \{x, y, [, \epsilon\}$.

**FOLLOW sets.**

- $\text{FOLLOW}(S)$: \$ (start symbol); from $U \to [S]$ add `]`. So $\{\$, ]\}$.
- $\text{FOLLOW}(T)$: from $S \to T\,;\,S$ add `;`; from $T' \to *T$, $\text{FOLLOW}(T) \supseteq \text{FOLLOW}(T')$. So $\text{FOLLOW}(T) = \{;\}$ together with $\text{FOLLOW}(T')$.
- $\text{FOLLOW}(T')$: from $T \to U\,T'$ it equals $\text{FOLLOW}(T) = \{;\}$.
- $\text{FOLLOW}(U)$: from $T \to U\,T'$ add $\text{FIRST}(T') \setminus \{\epsilon\} = \{*\}$; since $T'$ is nullable also $\text{FOLLOW}(T) = \{;\}$. So $\{*, ;\}$.

| Nonterminal | FIRST | FOLLOW |
|:-:|:--|:--|
| $S$ | $\{x, y, [, \epsilon\}$ | $\{\$, ]\}$ |
| $T$ | $\{x, y, [\}$ | $\{;\}$ |
| $T'$ | $\{*, \epsilon\}$ | $\{;\}$ |
| $U$ | $\{x, y, [\}$ | $\{*, ;\}$ |

*Check:* the left factoring, FIRST and FOLLOW sets were computed by a script and agree; the resulting grammar is LL(1).
