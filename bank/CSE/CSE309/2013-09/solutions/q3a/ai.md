---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Predictive parsing is top-down parsing without backtracking: the next input symbol alone selects the production. The given grammar is not LL(1) (common prefixes in E -> T+E | T and T -> int | int*T); after left factoring (E -> T E'; E' -> + E | eps; T -> ( E ) | int T'; T' -> * T | eps) the table is: M[E,int] = M[E,(] = E -> T E'; M[E',+] = E' -> + E; M[E',)] = M[E',\\$] = E' -> eps; M[T,int] = T -> int T'; M[T,(] = T -> ( E ); M[T',*] = T' -> * T; M[T',+] = M[T',)] = M[T',\\$] = T' -> eps."
sources: ["MMA syntax analysis slides 103-151 (LL(1) table, predictive parsing)", "Dragon book 2e sec. 4.4.2-4.4.3, 4.3.4"]
---
**Predictive parsing.** A top-down parsing method that **never backtracks**: the parser, while expanding the current nonterminal, looks at the next input symbol (the *lookahead*) and from it alone decides which production to use. It is implemented by recursive procedures or by a stack and a table $M[A, a]$ (Dragon book sec. 4.4). It works for LL(1) grammars.

**The grammar.** $E \to T + E \mid T$, $T \to \textbf{int} \mid \textbf{int} * T \mid (E)$.

It is **not LL(1)** as it stands: both alternatives of $E$ start with $T$, and the first two alternatives of $T$ start with $\textbf{int}$, so $M[E, \textbf{int}]$, $M[E, (]$ and $M[T, \textbf{int}]$ would each have two entries. **Left factoring** (sec. 4.3.4) gives

$$E \to T\,E'$$

$$E' \to +\,E \mid \epsilon$$

$$T \to (\,E\,) \mid \textbf{int}\,T'$$

$$T' \to *\,T \mid \epsilon$$

**FIRST and FOLLOW.**

| | FIRST | FOLLOW |
|:-:|:--|:--|
| $E$ | $\{(,\ \textbf{int}\}$ | $\{\$,\ )\}$ |
| $E'$ | $\{+,\ \epsilon\}$ | $\{\$,\ )\}$ |
| $T$ | $\{(,\ \textbf{int}\}$ | $\{\$,\ ),\ +\}$ |
| $T'$ | $\{*,\ \epsilon\}$ | $\{\$,\ ),\ +\}$ |

**Parsing table** (Algorithm 4.31):

| | $\textbf{int}$ | $+$ | $*$ | $($ | $)$ | \$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $E$ | $E \to TE'$ | | | $E \to TE'$ | | |
| $E'$ | | $E' \to +E$ | | | $E' \to \epsilon$ | $E' \to \epsilon$ |
| $T$ | $T \to \textbf{int}\,T'$ | | | $T \to (E)$ | | |
| $T'$ | | $T' \to \epsilon$ | $T' \to *T$ | | $T' \to \epsilon$ | $T' \to \epsilon$ |

No entry has two productions, so the factored grammar is **LL(1)** and is suitable for predictive parsing.

*Check:* the table and the conflicts of the original grammar (three multiply-defined entries) were computed by a script.
