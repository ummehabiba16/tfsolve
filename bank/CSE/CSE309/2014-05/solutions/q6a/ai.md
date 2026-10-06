---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "S -> T S'; S' -> + S S' | S S' | eps; T -> I T'; T' -> T T' | / T T' | eps; I -> 0 I' | 1 I'; I' -> 0 I' | 1 I' | eps (the grammar stays ambiguous)."
sources: ["MMA syntax analysis slides 27-60 (Elimination of left recursion)", "Dragon book 2e Algorithm 4.19"]
---
Immediate left recursion $A \to A\alpha_1 \mid \dots \mid A\alpha_m \mid \beta_1 \mid \dots \mid \beta_n$ becomes $A \to \beta_1 A' \mid \dots \mid \beta_n A'$, $A' \to \alpha_1 A' \mid \dots \mid \alpha_m A' \mid \epsilon$. No nonterminal is left-recursive through another one, so each can be treated separately.

**$S \to S + S \mid SS \mid T$:** $\alpha_1 = +S$, $\alpha_2 = S$, $\beta = T$:

$$S \to T\,S'$$

$$S' \to +S\,S' \mid S\,S' \mid \epsilon$$

**$T \to TT \mid T/T \mid I$:** $\alpha_1 = T$, $\alpha_2 = /T$, $\beta = I$:

$$T \to I\,T'$$

$$T' \to T\,T' \mid /T\,T' \mid \epsilon$$

**$I \to I0 \mid I1 \mid 0 \mid 1$:** $\alpha_1 = 0$, $\alpha_2 = 1$, $\beta_1 = 0$, $\beta_2 = 1$:

$$I \to 0\,I' \mid 1\,I'$$

$$I' \to 0\,I' \mid 1\,I' \mid \epsilon$$

**Result.**

```text
S  -> T S'
S' -> + S S' | S S' | eps
T  -> I T'
T' -> T T' | / T T' | eps
I  -> 0 I' | 1 I'
I' -> 0 I' | 1 I' | eps
```

(The new grammar has no left recursion, but, as the original, it is still **ambiguous**: for example $SS'$ allows concatenations to be split in many ways; elimination of left recursion does not remove ambiguity.)

*Check:* Algorithm 4.19 was run by a script and printed these productions.
