---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) If A => alpha =>* eps and the next input b is in FOLLOW(A), then A must be erased when b is seen, so A -> alpha goes in M[A,b]. (ii) Multiple entries mean the parser cannot choose a production; the grammar is not LL(1) (left recursive, not left factored, or ambiguous). (iii) The stack holds the unmatched part of the left-sentential form, top = leftmost: alpha beta gamma, with top at alpha; w has terminals only. (iv) Pop X and push W, V, U so that U is on top."
sources: ["MMA syntax analysis slides 124-151 (non-recursive predictive parsing)", "Dragon book 2e sec. 4.4.3-4.4.4, Algorithm 4.31"]
---
**(i) Why add $A \to \alpha$ to $M[A, b]$ for each $b \in \text{FOLLOW}(A)$ when $\epsilon \in \text{FIRST}(\alpha)$?**

The table tells the parser which production to use when $A$ is on top of the stack and $b$ is the next input symbol. If $\epsilon \in \text{FIRST}(\alpha)$, then $\alpha \Rightarrow^* \epsilon$, so using $A \to \alpha$ can make $A$ **disappear**. $A$ should disappear exactly when the next input symbol is something that can come *after* $A$ in a sentential form, that is, a symbol $b$ in $\text{FOLLOW}(A)$. Then $A$ is replaced by $\alpha$, which derives $\epsilon$; the stack now exposes the symbol after $A$, which can match $b$ or derive a string starting with $b$. If $b \notin \text{FOLLOW}(A)$ and not in $\text{FIRST}(\alpha)$, no valid parse can erase $A$ before $b$, and the entry is an error entry.

**(ii) Multiple entries in a parsing table.**

An entry $M[A, a]$ with two or more productions means that with $A$ on top and $a$ as the next symbol the parser **cannot decide, with one symbol of lookahead, which production to apply** (it would need backtracking or more lookahead). The grammar is therefore **not LL(1)**. Typical causes: the grammar is ambiguous, left recursive, or not left-factored.

**(iii) Stack contents and the nature of the symbols.**

$w$ is the part of the input matched so far and $S \Rightarrow^* w\alpha\beta\gamma$ is the current **left-sentential form**. The stack holds the **rest** of the left-sentential form, the unmatched part $\alpha\beta\gamma$, with the **leftmost symbol on top** and the end marker `$` at the bottom:

```text
(bottom) $  gamma  beta  alpha  (top)
```

- Every symbol of $w$ is a **terminal**: they were matched with the input, so $w$ is a string of terminals.
- The stack symbols $\alpha\beta\gamma$ can be **terminals and nonterminals**: terminals are waiting to be matched against the input, nonterminals are waiting to be expanded. The parser always looks at the top: if it is a terminal it must equal the next input symbol; if a nonterminal, the table chooses its production.

**(iv) Stack update for $M[X, a] = X \to UVW$.**

$X$ is on top of the stack and the next input symbol is $a$. The parser **pops $X$** and **pushes the body in reverse order**, $W$, then $V$, then $U$, so that **$U$ ends up on top**:

```text
before:  ... X          (top)
after:   ... W V U      (top = U)
```

This is done because the parser builds a *leftmost derivation*: after replacing $X$ by $UVW$ the leftmost symbol, $U$, must be processed next. The input pointer does not move; it moves only when a terminal on top is matched.
