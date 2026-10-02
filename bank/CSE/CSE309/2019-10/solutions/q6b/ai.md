---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Assuming S.next = L1 from P -> S and labels created in the order L1 (S.next), L2/L3 (B.true/B.false), L4 (|| : B1.false), L5 (&& : B3.true): if x > 20 goto L5; goto L4; L5: if x < 10 goto L2; goto L4; L4: if x != y goto L2; goto L3; L2: x = 0; goto L1; L3: x = 1; L1:."
sources: ["KMS Chapter 6 slides 84-94 (Translation of Boolean Expression, SDD for Flow-of-Control)", "Dragon book 2e sec. 6.6.4 (Example 6.22)"]
---
**Assumptions.**

- The completed SDD of 6(a) is used, with $P \to S$ supplying $S.next$.
- Assignments use the usual rule $S \to \textbf{id} = E\ ;\ \{S.code = E.code \,\Vert\, gen(top.get(\textbf{id}.lexeme)\ '='\ E.addr)\}$ together with (v) for the constants.
- `newlabel()` returns L1, L2, ... in the order of the calls. The calls happen top-down: $S.next$ first, then $B.true$, $B.false$, then the labels created inside $B$.

`&&` has higher precedence, so the condition is $B = B_1 \Vert B_2$ with $B_1 = B_3\ \&\&\ B_4$ ($B_3$: `x > 20`, $B_4$: `x < 10`) and $B_2$: `x != y`.

**Labels:**

| Node | Rule | Labels |
|:--|:--|:--|
| $P \to S$ | $S.next = newlabel()$ | L1 |
| $S \to$ if $(B)\ S_1$ else $S_2$ | $B.true$, $B.false$ | L2, L3 |
| $B \to B_1 \Vert B_2$ | $B_1.true = L2$, $B_1.false = newlabel()$ = L4; $B_2.true = L2$, $B_2.false = L3$ | L4 |
| $B_1 \to B_3\ \&\&\ B_4$ | $B_3.true = newlabel()$ = L5, $B_3.false = L4$; $B_4.true = L2$, $B_4.false = L4$ | L5 |

Each relational expression $E_1\ \textbf{rel}\ E_2$ generates `if E1 rel E2 goto B.true` followed by `goto B.false`.

**Three-address code:**

```text
        if x > 20 goto L5
        goto L4
L5:     if x < 10 goto L2
        goto L4
L4:     if x != y goto L2
        goto L3
L2:     x = 0
        goto L1
L3:     x = 1
L1:
```

This SDD does not avoid redundant jumps: for example, `goto L4` just before `L4:` is unnecessary. The fall-through technique would remove such jumps.
