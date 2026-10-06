---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "S -> T a S' | b S'; S' -> c S' | eps; T -> b S' d T' | d T'; T' -> c T' | a S' d T' | eps; U -> b S' d T' d U' | d T' d U' | b S' d T' a S' b U' | d T' a S' b U' | b S' b U' | b U'; U' -> a U' | eps."
sources: ["MMA syntax analysis slides 27-60 (Elimination of left recursion)", "Dragon book 2e Algorithm 4.19"]
---
Use Algorithm 4.19 with the order $S, T, U$. Immediate recursion $A \to A\alpha_1 \mid \dots \mid \beta_1 \mid \dots$ becomes $A \to \beta_1 A' \mid \dots$, $A' \to \alpha_1 A' \mid \dots \mid \epsilon$.

**$S \to Sc \mid Ta \mid b$.** $\alpha = c$, $\beta \in \{Ta, b\}$:

$$S \to Ta\,S' \mid b\,S'$$

$$S' \to c\,S' \mid \epsilon$$

**$T \to Tc \mid Sd \mid d$.** Substitute $S$ in $T \to Sd$:

$$T \to Tc \mid Ta\,S'd \mid b\,S'd \mid d$$

Immediate recursion with $\alpha_1 = c$, $\alpha_2 = a\,S'd$, $\beta_1 = b\,S'd$, $\beta_2 = d$:

$$T \to b\,S'd\,T' \mid d\,T'$$

$$T' \to c\,T' \mid a\,S'd\,T' \mid \epsilon$$

**$U \to Ua \mid Td \mid Sb \mid b$.** Substitute $T$ in $Td$ and $S$ in $Sb$ (the new $Ta\,S'b$ again begins with $T$, so substitute $T$ once more):

$$U \to Ua \mid b\,S'd\,T'd \mid d\,T'd \mid b\,S'd\,T'a\,S'b \mid d\,T'a\,S'b \mid b\,S'b \mid b$$

Immediate recursion with $\alpha = a$:

$$U \to b\,S'd\,T'd\,U' \mid d\,T'd\,U' \mid b\,S'd\,T'a\,S'b\,U' \mid d\,T'a\,S'b\,U' \mid b\,S'b\,U' \mid b\,U'$$

$$U' \to a\,U' \mid \epsilon$$

**Result.**

```text
S  -> T a S' | b S'
S' -> c S' | eps
T  -> b S' d T' | d T'
T' -> c T' | a S' d T' | eps
U  -> b S' d T' d U' | d T' d U' | b S' d T' a S' b U' | d T' a S' b U' | b S' b U' | b U'
U' -> a U' | eps
```

None of the productions starts with its own nonterminal or with a nonterminal that leads back to it, so the grammar is free of left recursion.

*Check:* Algorithm 4.19 was run by a script on the grammar and printed exactly this grammar.
