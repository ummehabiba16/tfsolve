---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Order S, T, U. S -> T b S' | U c S' | a S';  S' -> a S' | eps;  T -> U c S' c T' | a S' c T' | U b T' | b T';  T' -> b S' c T' | a T' | eps;  U -> a S' c T' b S' b U' | b T' b S' b U' | a S' b U' | a S' c T' c U' | b T' c U' | c U';  U' -> c S' c T' b S' b U' | b T' b S' b U' | c S' b U' | c S' c T' c U' | b T' c U' | a U' | eps."
sources: ["MMA syntax analysis slides 27-60 (Elimination of Left Recursion, Algorithm)", "Dragon book 2e sec. 4.3.3 (Algorithm 4.19)"]
---
The grammar has immediate left recursion ($S \to Sa$, $T \to Ta$, $U \to Ua$) and indirect left recursion ($S \to Tb$, $T \to Sc$, $S \to Uc$, $U \to Sb$, $T \to Ub$, $U \to Tc$). It has no $\epsilon$-productions or cycles, so apply Algorithm 4.19 with the order $A_1 = S$, $A_2 = T$, $A_3 = U$.

**Step 1 ($S$).** $S \to Sa \mid Tb \mid Uc \mid a$, with $\alpha = a$ and $\beta$'s $= Tb$, $Uc$, $a$:

$$S \to TbS' \mid UcS' \mid aS'$$

$$S' \to aS' \mid \epsilon$$

**Step 2 ($T$).** Substitute $S$ in $T \to Sc$:

$$T \to TbS'c \mid UcS'c \mid aS'c \mid Ta \mid Ub \mid b$$

Remove the immediate left recursion, with $\alpha$'s $= bS'c$, $a$ and $\beta$'s $= UcS'c$, $aS'c$, $Ub$, $b$:

$$T \to UcS'cT' \mid aS'cT' \mid UbT' \mid bT'$$

$$T' \to bS'cT' \mid aT' \mid \epsilon$$

**Step 3 ($U$).** Substitute $S$ in $U \to Sb$ ($Sb \to TbS'b \mid UcS'b \mid aS'b$):

$$U \to TbS'b \mid UcS'b \mid aS'b \mid Tc \mid Ua \mid c$$

Substitute $T$ in $U \to TbS'b$ and $U \to Tc$:

$$U \to UcS'cT'bS'b \mid aS'cT'bS'b \mid UbT'bS'b \mid bT'bS'b$$

$$\qquad \mid UcS'b \mid aS'b \mid UcS'cT'c \mid aS'cT'c \mid UbT'c \mid bT'c \mid Ua \mid c$$

Remove the immediate left recursion. The $\alpha$'s (the bodies starting with $U$, without the $U$) are $cS'cT'bS'b$, $bT'bS'b$, $cS'b$, $cS'cT'c$, $bT'c$, $a$. The $\beta$'s are the rest:

$$U \to aS'cT'bS'bU' \mid bT'bS'bU' \mid aS'bU'$$

$$\qquad \mid aS'cT'cU' \mid bT'cU' \mid cU'$$

$$U' \to cS'cT'bS'bU' \mid bT'bS'bU' \mid cS'bU'$$

$$\qquad \mid cS'cT'cU' \mid bT'cU' \mid aU' \mid \epsilon$$

**Final grammar (no left recursion):**

$$S \to TbS' \mid UcS' \mid aS'$$

$$S' \to aS' \mid \epsilon$$

$$T \to UcS'cT' \mid aS'cT' \mid UbT' \mid bT'$$

$$T' \to bS'cT' \mid aT' \mid \epsilon$$

$$U \to aS'cT'bS'bU' \mid bT'bS'bU' \mid aS'bU'$$

$$\qquad \mid aS'cT'cU' \mid bT'cU' \mid cU'$$

$$U' \to cS'cT'bS'bU' \mid bT'bS'bU' \mid cS'bU'$$

$$\qquad \mid cS'cT'cU' \mid bT'cU' \mid aU' \mid \epsilon$$

Check: every $U$-body starts with a terminal; every $T$-body starts with $U$ or a terminal; every $S$-body starts with $T$, $U$ or a terminal; the primed nonterminals start with terminals. So no derivation $A \overset{+}{\Rightarrow} A\alpha$ remains.
