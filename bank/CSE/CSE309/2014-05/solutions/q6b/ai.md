---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "S -> T b S' | c S'; S' -> a S' | eps; T -> c S' y T' | z T'; T' -> x T' | b S' y T' | eps."
sources: ["MMA syntax analysis slides 27-60 (Elimination of left recursion)", "Dragon book 2e Algorithm 4.19"]
---
Order $S, T$ (Algorithm 4.19).

**$S \to Sa \mid Tb \mid c$:** $\alpha = a$, $\beta \in \{Tb, c\}$:

$$S \to Tb\,S' \mid c\,S'$$

$$S' \to a\,S' \mid \epsilon$$

**$T \to Tx \mid Sy \mid z$:** $T \to Sy$ starts with $S$, which comes earlier in the order, so substitute the new productions of $S$:

$$T \to Tx \mid Tb\,S'y \mid c\,S'y \mid z$$

Immediate left recursion with $\alpha_1 = x$, $\alpha_2 = b\,S'y$ and $\beta \in \{c\,S'y, z\}$:

$$T \to c\,S'y\,T' \mid z\,T'$$

$$T' \to x\,T' \mid b\,S'y\,T' \mid \epsilon$$

**Result.**

```text
S  -> T b S' | c S'
S' -> a S' | eps
T  -> c S' y T' | z T'
T' -> x T' | b S' y T' | eps
```

*Check:* produced by the algorithm in a script.
