---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "LL(1) table: M[S,x] = M[S,y] = M[S,[] = S -> T;S, M[S,]] = M[S,\\$] = S -> eps, M[T,x|y|[] = T -> UR, M[R,*] = R -> *T, M[R,;] = R -> eps, M[U,x] = U -> x, M[U,y] = U -> y, M[U,[] = U -> [S]. On [x;y]*[; the parser matches [ x ; y and then fails at ] with R on top (M[R,]] is empty): the string is not in the language (after y a ; is required)."
sources: ["MMA syntax analysis slides 103-151 (LL(1) table, predictive parsing)", "Dragon book 2e sec. 4.4.3-4.4.4, Algorithm 4.31, 4.34"]
---
Grammar of Question 5: $S \to T;S \mid \epsilon$, $T \to UR$, $R \to *T \mid \epsilon$, $U \to x \mid y \mid [S]$, with the FIRST and FOLLOW sets of Question 5.

**LL(1) parsing table** (Algorithm 4.31; blank = error):

| | $x$ | $y$ | $[$ | $]$ | $*$ | $;$ | \$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $S$ | $S \to T;S$ | $S \to T;S$ | $S \to T;S$ | $S \to \epsilon$ | | | $S \to \epsilon$ |
| $T$ | $T \to UR$ | $T \to UR$ | $T \to UR$ | | | | |
| $R$ | | | | | $R \to *T$ | $R \to \epsilon$ | |
| $U$ | $U \to x$ | $U \to y$ | $U \to [S]$ | | | | |

($S \to T;S$ goes under $\text{FIRST}(T) = \{x, y, [\}$; $S \to \epsilon$ under $\text{FOLLOW}(S) = \{], \$\}$; $R \to \epsilon$ under $\text{FOLLOW}(R) = \{;\}$.) There is at most one production in each cell, so the grammar is LL(1).

**Parsing `[x;y]*[;`** (stack top at the left):

| Step | Stack | Input | Move |
|:-:|:--|:--|:--|
| 1 | `S $` | `[x;y]*[;$` | $S \to T;S$ |
| 2 | `T ; S $` | `[x;y]*[;$` | $T \to UR$ |
| 3 | `U R ; S $` | `[x;y]*[;$` | $U \to [S]$ |
| 4 | `[ S ] R ; S $` | `[x;y]*[;$` | match `[` |
| 5 | `S ] R ; S $` | `x;y]*[;$` | $S \to T;S$ |
| 6 | `T ; S ] R ; S $` | `x;y]*[;$` | $T \to UR$ |
| 7 | `U R ; S ] R ; S $` | `x;y]*[;$` | $U \to x$ |
| 8 | `x R ; S ] R ; S $` | `x;y]*[;$` | match `x` |
| 9 | `R ; S ] R ; S $` | `;y]*[;$` | $R \to \epsilon$ |
| 10 | `; S ] R ; S $` | `;y]*[;$` | match `;` |
| 11 | `S ] R ; S $` | `y]*[;$` | $S \to T;S$ |
| 12 | `T ; S ] R ; S $` | `y]*[;$` | $T \to UR$ |
| 13 | `U R ; S ] R ; S $` | `y]*[;$` | $U \to y$ |
| 14 | `y R ; S ] R ; S $` | `y]*[;$` | match `y` |
| 15 | `R ; S ] R ; S $` | `]*[;$` | **error**: $M[R, ]]$ is empty |

**What happens.** The parser accepts `[x;` and then `y`, but in $S \to T;S$ every `T` must be **followed by `;`**: after `y` the parser has `R ; ...` on the stack, yet the next symbol is `]` (which is not in $\text{FOLLOW}(R) = \{;\}$). The parse stops with a **syntax error at the `]`** after `y`, so `[x;y]*[;` is **not** a sentence of the grammar. (`[x;y;]*[;` would also fail later: after `*` a `T` is needed, but `[;` is $[$ followed by a `;`, and $S$ cannot start with `;`.) A panic-mode recovery would skip input to a synchronizing symbol (such as `;` or `]` from FOLLOW sets) and continue.

*Check:* the table and the parse (error at `]` with `R` on top) were computed by a script.
