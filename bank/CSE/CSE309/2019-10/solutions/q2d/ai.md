---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Order S, A, B. S -> A a | B b;  A -> c A' | B b b A';  A' -> a A' | b c A' | a b A' | eps;  B -> d A | b b."
sources: ["MMA syntax analysis slides 27-60 (Elimination of Left Recursion)", "Dragon book 2e sec. 4.3.3 (Algorithm 4.19)"]
---
Left recursion: $A \to Aa \mid Abc$ is immediate, and $A \to Sb$ with $S \to Aa$ is indirect ($A \Rightarrow Sb \Rightarrow Aab$). No $\epsilon$-productions or cycles, so use Algorithm 4.19 with the order $A_1 = S$, $A_2 = A$, $A_3 = B$.

**$i = 1$ ($S$).** $S \to Aa \mid Bb$: no immediate left recursion, and nothing earlier to substitute.

**$i = 2$ ($A$).** Substitute $S \to Aa \mid Bb$ into $A \to Sb$:

$$A \to Aa \mid Abc \mid c \mid Aab \mid Bbb$$

Remove the immediate left recursion, with $\alpha$'s $= a$, $bc$, $ab$ and $\beta$'s $= c$, $Bbb$:

$$A \to cA' \mid BbbA'$$

$$A' \to aA' \mid bcA' \mid abA' \mid \epsilon$$

**$i = 3$ ($B$).** $B \to dA \mid bb$: no body starts with $S$ or $A$, and there is no immediate left recursion, so it is unchanged.

**Result:**

$$S \to Aa \mid Bb$$

$$A \to cA' \mid BbbA'$$

$$A' \to aA' \mid bcA' \mid abA' \mid \epsilon$$

$$B \to dA \mid bb$$

Check: $B$ starts with $d$ or $b$; $A$ starts with $c$ or $B$; $S$ starts with $A$ or $B$; $A'$ starts with a terminal. No nonterminal can derive a string beginning with itself.
