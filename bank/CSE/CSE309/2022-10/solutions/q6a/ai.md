---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Both S-alternatives start with ab: S -> a b S';  S' -> A | c S;  A -> a A | eps (A is already left factored)."
sources: ["MMA syntax analysis slides 61-69 (Left Factoring)", "Dragon book 2e sec. 4.3.4 (Algorithm 4.21)"]
---
**Algorithm.** For $A \to \alpha\beta_1 \mid \alpha\beta_2$ with the longest common prefix $\alpha$, introduce a new nonterminal: $A \to \alpha A'$, $A' \to \beta_1 \mid \beta_2$.

For $S \to abA \mid abcS$, the longest common prefix is $\alpha = ab$, with $\beta_1 = A$ and $\beta_2 = cS$:

$$S \to ab\,S'$$

$$S' \to A \mid cS$$

$$A \to aA \mid \epsilon$$

$A$'s alternatives ($aA$ and $\epsilon$) have no common prefix, so nothing more is needed. ($S'$ could also be written $S' \to aA \mid \epsilon \mid cS$ by substituting $A$.)

The factored grammar is LL(1): $S'$ chooses $A$ on `a` or the end of input (FIRST($A$) = {a, $\epsilon$}, FOLLOW($S'$) = {\$}), and $cS$ on `c`.
