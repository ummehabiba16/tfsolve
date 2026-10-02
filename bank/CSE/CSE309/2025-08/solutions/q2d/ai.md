---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Order S, B, C. S -> B b S' | c S';  S' -> a S' | eps;  B -> c S' e B' | C f B' | g B';  B' -> d B' | b S' e B' | eps;  C -> c S' e B' h C' | g B' h C' | c S' e B' b S' c C' | g B' b S' c C' | c S' c C' | d C';  C' -> a C' | f B' h C' | f B' b S' c C' | eps."
sources: ["MMA syntax analysis slides 27-60 (Elimination of Left Recursion, Algorithm 4.19)", "Dragon book 2e sec. 4.3.3"]
---
The grammar has immediate left recursion ($S \to Sa$, $B \to Bd$, $C \to Ca$) and indirect left recursion ($S \to Bb$, $B \to Se$, ...). Use the textbook algorithm (Algorithm 4.19) with the order $A_1 = S$, $A_2 = B$, $A_3 = C$. The grammar has no $\epsilon$-productions and no cycles, so the algorithm applies.

Rule for immediate left recursion: $A \to A\alpha_1 \mid \ldots \mid A\alpha_m \mid \beta_1 \mid \ldots \mid \beta_n$ becomes

$$A \to \beta_1 A' \mid \ldots \mid \beta_n A'$$

$$A' \to \alpha_1 A' \mid \ldots \mid \alpha_m A' \mid \epsilon$$

**Step 1: $i = 1$ ($S$).** Remove the immediate left recursion in $S \to Sa \mid Bb \mid c$:

$$S \to BbS' \mid cS'$$

$$S' \to aS' \mid \epsilon$$

**Step 2: $i = 2$ ($B$).** Substitute $S$ in $B \to Se$:

$$B \to Bd \mid BbS'e \mid cS'e \mid Cf \mid g$$

Remove the immediate left recursion ($\alpha$'s: $d$, $bS'e$):

$$B \to cS'eB' \mid CfB' \mid gB'$$

$$B' \to dB' \mid bS'eB' \mid \epsilon$$

**Step 3: $i = 3$ ($C$).** Substitute $S$ in $C \to Sc$:

$$C \to Ca \mid Bh \mid BbS'c \mid cS'c \mid d$$

Substitute $B$ in $C \to Bh$ and $C \to BbS'c$:

$$C \to Ca \mid cS'eB'h \mid CfB'h \mid gB'h \mid cS'eB'bS'c \mid CfB'bS'c \mid gB'bS'c \mid cS'c \mid d$$

Remove the immediate left recursion ($\alpha$'s: $a$, $fB'h$, $fB'bS'c$):

$$C \to cS'eB'hC' \mid gB'hC' \mid cS'eB'bS'cC'$$

$$\qquad \mid gB'bS'cC' \mid cS'cC' \mid dC'$$

$$C' \to aC' \mid fB'hC' \mid fB'bS'cC' \mid \epsilon$$

**Final grammar (no left recursion):**

$$S \to BbS' \mid cS'$$

$$S' \to aS' \mid \epsilon$$

$$B \to cS'eB' \mid CfB' \mid gB'$$

$$B' \to dB' \mid bS'eB' \mid \epsilon$$

$$C \to cS'eB'hC' \mid gB'hC' \mid cS'eB'bS'cC'$$

$$\qquad \mid gB'bS'cC' \mid cS'cC' \mid dC'$$

$$C' \to aC' \mid fB'hC' \mid fB'bS'cC' \mid \epsilon$$

Check: every body of $S$ starts with $B$ or a terminal; every body of $B$ starts with $C$ or a terminal; every body of $C$ starts with a terminal. So no derivation $A \overset{+}{\Rightarrow} A\alpha$ remains.
