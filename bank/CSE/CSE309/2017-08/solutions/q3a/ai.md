---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "FIRST(T)={hree,virus}, FIRST(F)={farhanT,rajuT,eps}, FIRST(I)={rancho}; FOLLOW(T)=FOLLOW(F)={\\$,farhanT,rajuT}, FOLLOW(I)={diots}. M[F,farhanT] and M[F,rajuT] each hold two productions (F -> farhanT / F -> eps, F -> rajuT / F -> eps), so the grammar is not LL(1) and is not suitable for predictive parsing."
sources: ["MMA syntax analysis slides 76-123 (FIRST and FOLLOW, LL(1) table)", "Dragon book 2e sec. 4.4.2-4.4.3, Algorithm 4.31"]
---
**Reading the grammar.** Bold letters in the paper are nonterminals, everything else is a terminal. So the productions are

```text
T -> hree I diots T F | virus
F -> farhanT | rajuT | eps
I -> rancho
```

where `hree`, `diots`, `virus`, `farhanT`, `rajuT`, `rancho` are terminals. (In the paper the final `T` of `farhanT` and `rajuT` is not bold. If it were the nonterminal $T$, the FIRST sets and FOLLOW sets change in letter only, and the conclusion in (iii) is the same.) Start symbol: $T$.

**(i) FIRST and FOLLOW.**

| Nonterminal | FIRST | FOLLOW |
|:-:|:--|:--|
| $T$ | $\{hree,\ virus\}$ | $\{\$,\ farhanT,\ rajuT\}$ |
| $F$ | $\{farhanT,\ rajuT,\ \epsilon\}$ | $\{\$,\ farhanT,\ rajuT\}$ |
| $I$ | $\{rancho\}$ | $\{diots\}$ |

Steps: $\text{FOLLOW}(T)$ contains \$ (start symbol), $\text{FIRST}(F)\setminus\{\epsilon\} = \{farhanT, rajuT\}$ from $T \to hree\,I\,diots\,T\,F$, and, because $F$ is nullable, $\text{FOLLOW}(T) \supseteq \text{FOLLOW}(T)$ (no new symbols). $\text{FOLLOW}(F)$ gets $\text{FOLLOW}(T)$ from $T \to \ldots T F$. $\text{FOLLOW}(I) = \{diots\}$ from $T \to hree\,I\,diots\ldots$.

**(ii) LL(1) parsing table** (Algorithm 4.31). For $A \to \alpha$: put it in $M[A, a]$ for each $a \in \text{FIRST}(\alpha)$; if $\epsilon \in \text{FIRST}(\alpha)$ also for each $b \in \text{FOLLOW}(A)$.

| | $hree$ | $virus$ | $farhanT$ | $rajuT$ | $rancho$ | $diots$ | \$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $T$ | $T \to hree\,I\,diots\,T\,F$ | $T \to virus$ | | | | | |
| $F$ | | | $F \to farhanT$ ; $F \to \epsilon$ | $F \to rajuT$ ; $F \to \epsilon$ | | | $F \to \epsilon$ |
| $I$ | | | | | $I \to rancho$ | | |

**(iii) Suitability for predictive parsing.** $M[F, farhanT]$ and $M[F, rajuT]$ each contain **two** productions: $F \to farhanT$ (because $farhanT \in \text{FIRST}$) and $F \to \epsilon$ (because $farhanT \in \text{FOLLOW}(F)$). A predictive parser could not decide whether to expand $F$ or to erase it when the next input is $farhanT$ (or $rajuT$). A grammar whose table has multiply-defined entries is **not LL(1)**, so it is **not suitable** for predictive parsing without transformation. The cause is that $\text{FIRST}(F)$ and $\text{FOLLOW}(F)$ intersect while $F$ is nullable.

*Check:* FIRST/FOLLOW and the table were computed by a script; the conflicts found are exactly the two entries above.
