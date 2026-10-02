---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Order S, T, U. S -> T a S' | b S';  S' -> c S' | eps;  T -> b S' d T' | U b T' | d T';  T' -> c T' | a S' d T' | eps;  U -> b S' d T' d U' | d T' d U' | b S' d T' a S' b U' | d T' a S' b U' | b S' b U' | b U';  U' -> a U' | b T' d U' | b T' a S' b U' | eps."
sources: ["MMA syntax analysis slides 27-60 (Elimination of Left Recursion)", "Dragon book 2e sec. 4.3.3 (Algorithm 4.19)"]
---
Immediate left recursion: $S \to Sc$, $T \to Tc$, $U \to Ua$. Indirect: $S \to Ta$, $T \to Sd$, $T \to Ub$, $U \to Td$, $U \to Sb$. No $\epsilon$-productions or cycles, so apply Algorithm 4.19 with the order $S, T, U$.

**Step 1 ($S$).** $S \to Sc \mid Ta \mid b$, with $\alpha = c$ and $\beta$'s $= Ta$, $b$:

$$S \to TaS' \mid bS'$$

$$S' \to cS' \mid \epsilon$$

**Step 2 ($T$).** Substitute $S$ into $T \to Sd$:

$$T \to Tc \mid TaS'd \mid bS'd \mid Ub \mid d$$

Remove the immediate recursion, with $\alpha$'s $= c$, $aS'd$ and $\beta$'s $= bS'd$, $Ub$, $d$:

$$T \to bS'dT' \mid UbT' \mid dT'$$

$$T' \to cT' \mid aS'dT' \mid \epsilon$$

**Step 3 ($U$).** Substitute $S$ into $U \to Sb$ ($Sb \to TaS'b \mid bS'b$):

$$U \to Ua \mid Td \mid TaS'b \mid bS'b \mid b$$

Substitute $T$ into $U \to Td$ and $U \to TaS'b$:

$$U \to Ua \mid UbT'd \mid UbT'aS'b \mid bS'dT'd \mid dT'd$$

$$\qquad \mid bS'dT'aS'b \mid dT'aS'b \mid bS'b \mid b$$

Remove the immediate recursion, with $\alpha$'s $= a$, $bT'd$, $bT'aS'b$:

$$U \to bS'dT'dU' \mid dT'dU' \mid bS'dT'aS'bU'$$

$$\qquad \mid dT'aS'bU' \mid bS'bU' \mid bU'$$

$$U' \to aU' \mid bT'dU' \mid bT'aS'bU' \mid \epsilon$$

**Final grammar:**

$$S \to TaS' \mid bS'$$

$$S' \to cS' \mid \epsilon$$

$$T \to bS'dT' \mid UbT' \mid dT'$$

$$T' \to cT' \mid aS'dT' \mid \epsilon$$

$$U \to bS'dT'dU' \mid dT'dU' \mid bS'dT'aS'bU'$$

$$\qquad \mid dT'aS'bU' \mid bS'bU' \mid bU'$$

$$U' \to aU' \mid bT'dU' \mid bT'aS'bU' \mid \epsilon$$

Every $U$-body now starts with a terminal, every $T$-body with a terminal or $U$, and every $S$-body with $T$ or a terminal. So no left recursion remains.
