---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Shift-reduce trace for kwwrgz: END | kwwrgz -> shift k, shift w (handle w on top) reduce X->w, shift w, shift r (handle Xwr on top) reduce X->Xwr, shift g (handle g on top) reduce Y->g, shift z (handle kXYz on top) reduce A->kXYz, accept: every handle is on top when reduced, because a rightmost derivation expands the rightmost nonterminal, so in reverse the next handle is always at or right of the stack top."
sources: ["MMA syntax analysis slides 179-200 (Shift-Reduce Parsing)", "Dragon book 2e sec. 4.5.3 (Fig. 4.29)"]
---
**Shift-reduce parse of `kwwrgz`:**

| Stack | Input | Action |
|:--|--:|:--|
| \$ | kwwrgz\$ | shift |
| \$k | wwrgz\$ | shift |
| \$kw | wrgz\$ | handle `w` on top: reduce $X \to w$ |
| \$kX | wrgz\$ | shift |
| \$kXw | rgz\$ | shift |
| \$kXwr | gz\$ | handle `Xwr` on top: reduce $X \to Xwr$ |
| \$kX | gz\$ | shift |
| \$kXg | z\$ | handle `g` on top: reduce $Y \to g$ |
| \$kXY | z\$ | shift |
| \$kXYz | \$ | handle `kXYz` on top: reduce $A \to kXYz$ |
| \$A | \$ | accept |

In every reduction, the handle occupies the **top** of the stack; the parser never needs to look inside.

**Why it always happens.** In a rightmost derivation, each step replaces the **rightmost** nonterminal. Reading backwards: after a handle is reduced to a nonterminal (e.g. `w` to $X$), that nonterminal is the rightmost nonterminal of the new sentential form. Everything to its right is unread input (terminals). So the next handle cannot lie to the left of the stack top:

- **Case 1:** it ends at the stack top (`g` after `kX` needs one shift first; `kXYz` after `z` is shifted).
- **Case 2:** it includes the stack top and some input symbols to the right (`X` then `w r`: the parser shifts `w`, `r` until `Xwr` is on top).

In both cases the parser shifts zero or more input symbols until the handle's right end reaches the top, then reduces. The handle is never buried inside the stack, as seen above for (d).
