---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Order A, B, C, D. After substitution C -> C | b | a | CBD | c; dropping C -> C and eliminating C -> CBD: A -> B | a | CBD; B -> C | b; C -> bC' | aC' | cC'; C' -> BDC' | eps; D -> d."
sources: ["MMA syntax analysis slides 27-60 (indirect left recursion)", "Dragon book 2e Algorithm 4.19"]
---
Grammar: $A \to B \mid a \mid CBD$, $B \to C \mid b$, $C \to A \mid c$, $D \to d$. The left recursion is **indirect**: $A \Rightarrow B \Rightarrow C \Rightarrow A$. Use Algorithm 4.19 with the order $A, B, C, D$.

- **$A$ ($i = 1$):** no earlier nonterminal; no immediate recursion ($A$'s alternatives start with $B$, $a$, $C$).
- **$B$ ($i = 2$):** $B \to C \mid b$; $A$ does not start any alternative of $B$. No immediate recursion. Unchanged.
- **$C$ ($i = 3$):** $C \to A \mid c$. Substitute $A$ in $C \to A$ (production of $A$: $B \mid a \mid CBD$):

$$C \to B \mid a \mid CBD \mid c$$

  Now $C \to B$ starts with $B$ (earlier in the order); substitute $B \to C \mid b$:

$$C \to C \mid b \mid a \mid CBD \mid c$$

  $C \to C$ is a useless production ($X \to X$) and, as the question says, is **dropped** since it does not change the language:

$$C \to b \mid a \mid CBD \mid c$$

  Eliminate the immediate left recursion $C \to CBD$ ($\alpha = BD$; $\beta \in \{b, a, c\}$):

$$C \to b\,C' \mid a\,C' \mid c\,C'$$

$$C' \to B\,D\,C' \mid \epsilon$$

- **$D$ ($i = 4$):** $D \to d$, no recursion.

**Result.**

```text
A  -> B | a | C B D
B  -> C | b
C  -> b C' | a C' | c C'
C' -> B D C' | eps
D  -> d
```

No nonterminal can derive a string that starts with itself: $A \to B \to C \to$ (terminal)..., so the left recursion is gone.

*Check:* Algorithm 4.19 (with the removal of $C \to C$) was run by a script and gave this grammar.
