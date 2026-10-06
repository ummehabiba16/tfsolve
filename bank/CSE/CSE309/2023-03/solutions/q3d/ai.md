---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Parse tree: A -> k X Y z with X -> X w r, inner X -> w, Y -> g. Rightmost derivation A => kXYz => kXgz => kXwrgz => kwwrgz; handles in order: w (first w, X -> w), Xwr (X -> Xwr), g (Y -> g), kXYz (A -> kXYz)."
sources: ["MMA syntax analysis slides 152-200 (Reductions, Handle Pruning)", "Dragon book 2e sec. 4.5.1-4.5.2"]
changes:
  - "2026-10-06: replaced the ASCII drawing by a TikZ figure (figures/tree.png); the answer itself is unchanged."
---
**Parse tree for `kwwrgz`:**

![Parse tree for kwwrgz](figures/tree.png)

**Rightmost derivation:**

$$A \underset{rm}{\Rightarrow} kXYz \underset{rm}{\Rightarrow} kXgz \underset{rm}{\Rightarrow} kXwrgz \underset{rm}{\Rightarrow} kwwrgz$$

**Handles** (the right-sentential forms read backwards, i.e. handle pruning):

| Right-sentential form | Handle | Reduce by |
|:--|:--|:--|
| k w w r g z | the first w (position 2) | $X \to w$ |
| k X w r g z | X w r (positions 2-4) | $X \to Xwr$ |
| k X g z | g | $Y \to g$ |
| k X Y z | k X Y z | $A \to kXYz$ |
| A | | (start symbol: done) |

Note: the second `w` in `kwwrgz` is **not** a handle even though it matches $X \to w$. Reducing it would give `kwXrgz`, which is not a right-sentential form, so the parse would fail. The handle is the first `w`.
