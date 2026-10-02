---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "No. Merging same-core CLR states gives exactly the SLR number of states (the LR(0) cores), but each reduce item keeps a lookahead set that is a subset of FOLLOW, so LALR is strictly more powerful than SLR; e.g. S -> L = R | R, L -> \\*R | id, R -> L has an SLR conflict on = but none in LALR."
sources: ["MMA syntax analysis slides 380-387, 490-564", "Dragon book 2e sec. 4.6.5 (Example 4.48), 4.7.4"]
---
**No.** After merging, the LALR parser has the *same states* (same cores = the LR(0) item sets) as the SLR parser, but **not the same lookaheads**, so the tables can differ.

- **SLR** reduces by $A \to \alpha$ in a state on **every** terminal in FOLLOW($A$). FOLLOW is a global property of the grammar.
- **LALR** reduces on the *union of the LR(1) lookaheads* of the merged states, i.e. only on terminals that can actually follow $A$ in **that** context. This set is always a subset of FOLLOW($A$), and is often a proper subset.

So every SLR(1) grammar is LALR(1), but not conversely.

**Example.** The textbook grammar

$$S \to L = R \mid R$$

$$L \to *R \mid \textbf{id}$$

$$R \to L$$

- LR(0) state $I_2 = \{S \to L \cdot = R,\ R \to L \cdot\}$. FOLLOW($R$) contains `=` (from $S \Rightarrow L = R \Rightarrow *R = R$). On `=`, SLR has both **shift** and **reduce $R \to L$**, which is a **conflict**: the grammar is not SLR(1).
- In the LR(1) automaton the same state is $\{[S \to L \cdot = R, \$],\ [R \to L \cdot, \$]\}$: reduce only on `$`, shift on `=`. No other state has this core, so merging does not change it, and the **LALR table has no conflict**.

Thus the LALR parser has the SLR's size but uses more precise lookahead information, which is closer to CLR in power. It does not revert to SLR.
