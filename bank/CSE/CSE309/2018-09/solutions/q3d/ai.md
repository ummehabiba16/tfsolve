---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Left factored: S -> a b S';  S' -> A | c S;  A -> a A | eps. The original grammar needs k = 3 (abA and abcS agree on ab and differ in the 3rd symbol: a or end vs c); after left factoring it is LL(1)."
sources: ["MMA syntax analysis slides 61-69 (Left Factoring), 103-111 (LL(1) Grammars)", "Dragon book 2e sec. 4.3.4, 4.4.3"]
---
**Left factoring (3 marks).** Both alternatives of $S$ begin with $ab$. Factor it out with a new nonterminal $S'$:

$$S \to abS'$$

$$S' \to A \mid cS$$

$$A \to aA \mid \epsilon$$

**Value of $k$ (3 marks).**

- **Original grammar:** $S \to abA$ derives $ab$ followed by $a^n$, so its first 3 symbols are $aba$, or $ab$ followed by \$. $S \to abcS$ derives strings beginning $abc$. With $k = 1$ (both `a`) or $k = 2$ (both `ab`) the alternatives cannot be distinguished. With $k = 3$ they differ in the third symbol ($a$ or \$ vs $c$). So the original grammar is **LL(3)** ($k = 3$). ($A$ itself is LL(1): FIRST($aA$) = {a} and FOLLOW($A$) = {\$}.)
- **After left factoring:** FIRST($A$) = {a, $\epsilon$} and FOLLOW($S'$) = FOLLOW($S$) = {\$}. So $S' \to A$ is chosen on `a` or \$, and $S' \to cS$ on `c`; these are disjoint. The left-factored grammar is **LL(1)**.
