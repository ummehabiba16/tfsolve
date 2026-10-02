---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Order A, B. A -> B a A' | c A';  A' -> a A' | eps;  substitute A in B -> A b: B -> B b | B a A' b | c A' b | d;  then B -> c A' b B' | d B';  B' -> b B' | a A' b B' | eps."
sources: ["MMA syntax analysis slides 27-60 (Elimination of Left Recursion)", "Dragon book 2e sec. 4.3.3 (Algorithm 4.19)"]
---
There is immediate left recursion ($A \to Aa$, $B \to Bb$) and indirect left recursion ($A \to Ba$, $B \to Ab$). Apply Algorithm 4.19 with the order $A_1 = A$, $A_2 = B$.

**Step 1 ($A$).** $A \to Aa \mid Ba \mid c$, with $\alpha = a$ and $\beta$'s $= Ba, c$:

$$A \to BaA' \mid cA'$$

$$A' \to aA' \mid \epsilon$$

**Step 2 ($B$).** Replace $A$ in $B \to Ab$ with the bodies of $A$:

$$B \to Bb \mid BaA'b \mid cA'b \mid d$$

Remove the immediate left recursion ($\alpha$'s $= b$, $aA'b$; $\beta$'s $= cA'b$, $d$):

$$B \to cA'bB' \mid dB'$$

$$B' \to bB' \mid aA'bB' \mid \epsilon$$

**Result:**

$$A \to BaA' \mid cA'$$

$$A' \to aA' \mid \epsilon$$

$$B \to cA'bB' \mid dB'$$

$$B' \to bB' \mid aA'bB' \mid \epsilon$$

$A$ starts with $B$ or $c$, and $B$ starts with a terminal, so no left recursion remains.
