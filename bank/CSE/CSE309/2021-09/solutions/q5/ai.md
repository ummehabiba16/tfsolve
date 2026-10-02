---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Order X, S. X -> S a X' | b X';  X' -> S b X' | eps;  then S -> S b | S a X' a | b X' a | a becomes S -> b X' a S' | a S';  S' -> b S' | a X' a S' | eps."
sources: ["MMA syntax analysis slides 27-60 (Elimination of Left Recursion)", "Dragon book 2e sec. 4.3.3 (Algorithm 4.19)"]
---
Left recursion: $X \to XSb$ and $S \to Sb$ are immediate; $X \to Sa$, $S \to Xa$ is indirect. There are no $\epsilon$-productions or cycles, so apply Algorithm 4.19 with the order $A_1 = X$, $A_2 = S$.

**Step 1 ($X$).** $X \to XSb \mid Sa \mid b$ with $\alpha = Sb$ and $\beta$'s $= Sa$, $b$:

$$X \to SaX' \mid bX'$$

$$X' \to SbX' \mid \epsilon$$

**Step 2 ($S$).** Substitute $X$ in $S \to Xa$:

$$S \to Sb \mid SaX'a \mid bX'a \mid a$$

Now remove the immediate left recursion, with $\alpha$'s $= b$, $aX'a$ and $\beta$'s $= bX'a$, $a$:

$$S \to bX'aS' \mid aS'$$

$$S' \to bS' \mid aX'aS' \mid \epsilon$$

**Final grammar:**

$$X \to SaX' \mid bX'$$

$$X' \to SbX' \mid \epsilon$$

$$S \to bX'aS' \mid aS'$$

$$S' \to bS' \mid aX'aS' \mid \epsilon$$

Check: every $S$-body starts with a terminal, $X$ starts with $S$ or $b$, $X'$ starts with $S$, and $S'$ starts with a terminal. So no nonterminal can derive a string beginning with itself.
