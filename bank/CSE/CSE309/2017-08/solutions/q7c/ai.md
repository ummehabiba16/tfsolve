---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "001001 is derived from S -> CC (CC = 001 001): shifts and reduces C->1, C->0C, C->0C, C->1, C->0C, C->0C, S->CC, accept. 001011 is not derived: after reducing the first C (001) and shifting 0 1 the parser reduces C->1, C->0C, but the remaining input 1 has no action in state 6, so it is rejected."
sources: ["MMA syntax analysis slides 152-226 (shift-reduce parsing)", "Dragon book 2e sec. 4.5.3, Fig. 4.28"]
---
Grammar: $S \to CC$, $C \to 0C \mid 1$. A handle is reduced as soon as it is on top of the stack. $C$ generates the strings $0^*1$ and $S$ generates two such strings, $0^i10^j1$.

**Input `001001`** (the question prints `'001001;`):

| Step | Stack | Input | Action |
|:-:|:--|:--|:--|
| 1 | `$` | `001001$` | shift |
| 2 | `$0` | `01001$` | shift |
| 3 | `$00` | `1001$` | shift |
| 4 | `$001` | `001$` | reduce $C \to 1$ |
| 5 | `$00C` | `001$` | reduce $C \to 0C$ |
| 6 | `$0C` | `001$` | reduce $C \to 0C$ |
| 7 | `$C` | `001$` | shift |
| 8 | `$C0` | `01$` | shift |
| 9 | `$C00` | `1$` | shift |
| 10 | `$C001` | `$` | reduce $C \to 1$ |
| 11 | `$C00C` | `$` | reduce $C \to 0C$ |
| 12 | `$C0C` | `$` | reduce $C \to 0C$ |
| 13 | `$CC` | `$` | reduce $S \to CC$ |
| 14 | `$S` | `$` | **accept** |

`001001` is derived from the grammar ($S \Rightarrow CC \Rightarrow 0C\,C \Rightarrow \ldots \Rightarrow 001\;001$).

**Input `001011`:**

| Step | Stack | Input | Action |
|:-:|:--|:--|:--|
| 1 | `$` | `001011$` | shift |
| 2 | `$0` | `01011$` | shift |
| 3 | `$00` | `1011$` | shift |
| 4 | `$001` | `011$` | reduce $C \to 1$ |
| 5 | `$00C` | `011$` | reduce $C \to 0C$ |
| 6 | `$0C` | `011$` | reduce $C \to 0C$ |
| 7 | `$C` | `011$` | shift |
| 8 | `$C0` | `11$` | shift |
| 9 | `$C01` | `1$` | reduce $C \to 1$ |
| 10 | `$C0C` | `1$` | reduce $C \to 0C$ |
| 11 | `$CC` | `1$` | **error**: $CC$ could be reduced to $S$ only with $ as lookahead; no shift or reduce action exists on `1` |

After `$CC` the parser has a complete $S$ but input `1` is left over, so the string is **not accepted**: `001011` $= 001\ 011$ and `011` is not of the form $0^*1$. `001011` is **not derived** from the grammar.

*Check:* both strings were run through the SLR(1) parsing table of the grammar by a script; the first is accepted, the second is rejected in state 6 on input `1`.
