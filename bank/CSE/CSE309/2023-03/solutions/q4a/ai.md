---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Order S, B, C: S -> a S';  S' -> B r S' | eps;  B -> C s | b;  C -> a S' t | c (only S had immediate left recursion; substituting S into C -> S t removes the indirect recursion)."
sources: ["MMA syntax analysis slides 27-60 (Elimination of Left Recursion)", "Dragon book 2e sec. 4.3.3 (Algorithm 4.19)"]
---
The grammar has no $\epsilon$-productions and no cycles, so apply Algorithm 4.19 with the order $A_1 = S$, $A_2 = B$, $A_3 = C$.

**$i = 1$ ($S$).** $S \to SBr \mid a$ is immediately left recursive ($\alpha = Br$, $\beta = a$):

$$S \to aS'$$

$$S' \to BrS' \mid \epsilon$$

**$i = 2$ ($B$).** $B \to Cs \mid b$: no body starts with $S$ (the only earlier nonterminal), so nothing to substitute; there is no immediate left recursion.

$$B \to Cs \mid b$$

**$i = 3$ ($C$).** $C \to St \mid c$: substitute $S \to aS'$ in $C \to St$:

$$C \to aS't \mid c$$

No body of $C$ starts with $B$, and there is no immediate left recursion.

**Result:**

$$S \to aS'$$

$$S' \to BrS' \mid \epsilon$$

$$B \to Cs \mid b$$

$$C \to aS't \mid c$$

Check: $S$ and $C$ start with a terminal, and $B$ starts with $C$ (hence a terminal) or $b$, so no derivation $A \overset{+}{\Rightarrow} A\alpha$ is possible. In the original grammar the only left recursion was the immediate one, $S \to SBr$. $B \Rightarrow Cs \Rightarrow Sts$ and $C \Rightarrow St$ lead to $S$, not back to $B$ or $C$. Still, the algorithm substitutes $S$ into $C$ so that every body starts with a terminal or a later nonterminal.
