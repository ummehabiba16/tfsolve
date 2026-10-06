---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The grammar is already left-factored (no nonterminal has two alternatives with a common prefix; T -> UR with R -> *T | eps is the factored form of T -> U*T | U). FIRST(S) = {x, y, [, eps}, FIRST(T) = FIRST(U) = {x, y, [}, FIRST(R) = {*, eps}; FOLLOW(S) = {\\$, ]}, FOLLOW(T) = FOLLOW(R) = {;}, FOLLOW(U) = {*, ;}."
sources: ["MMA syntax analysis slides 61-102 (left factoring, FIRST/FOLLOW)", "Dragon book 2e sec. 4.3.4, 4.4.2"]
---
The question prints $R \to \bullet T \mid \epsilon$; the bullet is the multiplication sign `*` (it is the `*` in the input string `[x;y]*[;` of Question 6, and $T \to UR$ with $R \to *T \mid \epsilon$ is the left-factored form of $T \to U*T \mid U$). So the grammar is

$$S \to T\ ;\ S \mid \epsilon$$

$$T \to U\,R$$

$$R \to *\,T \mid \epsilon$$

$$U \to x \mid y \mid [\,S\,]$$

**Left factoring.** Left factoring is needed when two alternatives of a nonterminal begin with the same prefix. Here the alternatives are: of $S$, $T;S$ and $\epsilon$; of $R$, $*T$ and $\epsilon$; of $U$, $x$, $y$, $[S]$; $T$ has one alternative. No two alternatives of the same nonterminal share a first symbol, so **the grammar is already left-factored** and nothing needs to change (the common prefix $U$ of the original $T \to U*T \mid U$ has already been factored out into $T \to UR$).

**FIRST sets.**

- $\text{FIRST}(U) = \{x, y, [\}$; $\text{FIRST}(T) = \text{FIRST}(U) = \{x, y, [\}$ (since $T \to UR$ and $U$ is not nullable);
- $\text{FIRST}(R) = \{*, \epsilon\}$;
- $\text{FIRST}(S) = \text{FIRST}(T) \cup \{\epsilon\} = \{x, y, [, \epsilon\}$.

**FOLLOW sets.**

- $\text{FOLLOW}(S)$: \$ (start symbol); from $U \to [S]$ add `]`: $\{\$, ]\}$.
- $\text{FOLLOW}(T)$: from $S \to T;S$ add `;`; from $R \to *T$ add $\text{FOLLOW}(R)$ (which is $\{;\}$ below): $\{;\}$.
- $\text{FOLLOW}(R)$: from $T \to UR$ it is $\text{FOLLOW}(T) = \{;\}$.
- $\text{FOLLOW}(U)$: from $T \to UR$ add $\text{FIRST}(R) \setminus \{\epsilon\} = \{*\}$ and, as $R$ is nullable, $\text{FOLLOW}(T) = \{;\}$: $\{*, ;\}$.

| Nonterminal | FIRST | FOLLOW |
|:-:|:--|:--|
| $S$ | $\{x, y, [, \epsilon\}$ | $\{\$, ]\}$ |
| $T$ | $\{x, y, [\}$ | $\{;\}$ |
| $R$ | $\{*, \epsilon\}$ | $\{;\}$ |
| $U$ | $\{x, y, [\}$ | $\{*, ;\}$ |

*Check:* the FIRST and FOLLOW sets were computed by a script; the grammar is LL(1).
