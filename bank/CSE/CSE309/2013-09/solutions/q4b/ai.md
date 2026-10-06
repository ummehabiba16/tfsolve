---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "With the usual precedence (* and / above + and -) and left associativity: E -> E + T | E - T | T; T -> T * F | T / F | F; F -> int. The grammar is unambiguous (SLR(1) with no conflicts)."
sources: ["MMA syntax analysis slides 25-26; KMS ambiguity", "Dragon book 2e sec. 4.3.2, 2.2.5-2.2.6"]
---
The question is printed incomplete ("...left associative and the precedence of the operators?"); the usual precedence is assumed: `*` and `/` bind tighter than `+` and `-`, and all four operators are **left associative**.

**Method** (Dragon book sec. 4.3.2, 2.2.5-2.2.6): introduce one nonterminal for each level of precedence, and make the production **left recursive** for left associativity:

- $E$: the lowest level, sums and differences of terms;
- $T$: the products and quotients of factors;
- $F$: the factors (here only $\textbf{int}$).

**New grammar:**

$$E \to E + T \mid E - T \mid T$$

$$T \to T * F \mid T / F \mid F$$

$$F \to \textbf{int}$$

- **Precedence.** A `*` or `/` can only appear below a `T`; a `+` or `-` only at the `E` level. So in `int + int * int` the product is a sub-tree of the sum, and `*` is evaluated first.
- **Left associativity.** In $E \to E + T$, the left operand is $E$ (the whole expression so far) and the right operand is a $T$ (one term), so $a - b - c$ is $(a - b) - c$; likewise $a / b / c = (a / b) / c$.
- **No ambiguity.** For each string there is exactly one parse tree.

**Example:** `int + int * int / int` has the unique tree $\textbf{int} + ((\textbf{int} * \textbf{int}) / \textbf{int})$: the root is $E \to E + T$, its $T$ derives `int * int / int` through $T \to T / F$ and $T \to T * F$.

(If parentheses are wanted, add $F \to (E)$.)

*Check:* the SLR(1) table of the new grammar has no conflicts (so it is unambiguous).
