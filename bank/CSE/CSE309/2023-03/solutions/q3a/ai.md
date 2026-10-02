---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "For X -> Y1 Y2 ... Yk, add FIRST(Y1) - {eps}; if Y1 =>\\* eps also add FIRST(Y2) - {eps}, and so on; eps is in FIRST(X) only if every Yi derives eps (all of FIRST(Y1..Yk) contain eps), or X -> eps is a production. E.g. X -> AB, A -> a | eps, B -> b | eps gives FIRST(X) = {a, b, eps}; with B -> b only, eps is not in FIRST(X)."
sources: ["MMA syntax analysis slides 76-102 (FIRST and FOLLOW)", "Dragon book 2e sec. 4.4.2"]
---
**Rule for FIRST($X$) with $X \to Y_1 Y_2 \ldots Y_k$:**

1. Add everything in FIRST($Y_1$) except $\epsilon$.
2. If $\epsilon \in$ FIRST($Y_1$) (i.e. $Y_1 \overset{*}{\Rightarrow} \epsilon$), also add FIRST($Y_2$) $- \{\epsilon\}$. In general, add FIRST($Y_i$) $- \{\epsilon\}$ if $\epsilon$ is in all of FIRST($Y_1$), ..., FIRST($Y_{i-1}$).
3. **Add $\epsilon$ to FIRST($X$) only if $\epsilon$ is in FIRST($Y_j$) for every $j = 1, \ldots, k$**, i.e. the whole body can vanish: $Y_1 Y_2 \ldots Y_k \overset{*}{\Rightarrow} \epsilon$. (Also, if $X \to \epsilon$ is a production, $\epsilon \in$ FIRST($X$).)

The idea: $\epsilon \in$ FIRST($X$) means $X$ can derive the empty string, which requires every symbol of the body to derive $\epsilon$. One terminal, or one nonterminal that cannot vanish, stops it.

**Example 1** ($\epsilon$ included):

$$X \to AB, \qquad A \to a \mid \epsilon, \qquad B \to b \mid \epsilon$$

FIRST($A$) = {a, $\epsilon$} and FIRST($B$) = {b, $\epsilon$}.

$$\text{FIRST}(X) = \{a\} \cup \{b\} \cup \{\epsilon\} = \{a, b, \epsilon\}$$

$\epsilon$ is included because both $A$ and $B$ derive $\epsilon$: $X \Rightarrow AB \Rightarrow B \Rightarrow \epsilon$.

**Example 2** ($\epsilon$ not included): if instead $B \to b$, then

$$\text{FIRST}(X) = \{a\} \cup \{b\} = \{a, b\}$$

We still add FIRST($B$) because $A$ can vanish, but $B$ cannot, so $\epsilon \notin$ FIRST($X$).

**Example 3** (textbook expression grammar): $E \to TE'$, $T \to FT'$. FIRST($T$) = FIRST($F$) = { (, id }. $F$ cannot vanish, so FIRST($E$) = { (, id } without $\epsilon$; but $E' \to +TE' \mid \epsilon$ gives FIRST($E'$) = { +, $\epsilon$ }.
