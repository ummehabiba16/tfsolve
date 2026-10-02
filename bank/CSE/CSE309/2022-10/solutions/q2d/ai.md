---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Fall-through translation with B.false = L1 and S.next = L2: if x != y goto L3; ifFalse x > 20 goto L1; L3: ifFalse x < 10 goto L1; flag = 0; goto L2; L1: flag = 1; L2:."
sources: ["KMS Chapter 6 slides 98-101 (Avoiding Redundant Gotos)", "Dragon book 2e sec. 6.6.5 (Figs. 6.39, 6.40)"]
---
**Assumptions.** The fall-through technique of the text is used (the special label `fall` means "no jump"). The statement's next label is L2. The else-part gets the label L1, and labels created inside the condition are numbered from L3.

Structure: $B = B_1\ \&\&\ B_2$ with $B_1 = B_3 \Vert B_4$ ($B_3$: `x != y`, $B_4$: `x > 20`) and $B_2$: `x < 10`.

**Inherited labels:**

1. If-else: $B.true = fall$ (fall into the then-part), $B.false = L1$.
2. $B \to B_1\ \&\&\ B_2$: $B.false = L1 \ne fall$, so $B_1.true = fall$, $B_1.false = L1$, $B_2.true = fall$, $B_2.false = L1$.
3. $B_1 \to B_3 \Vert B_4$: $B_1.true = fall$, so $B_3.true = newLabel() = L3$, $B_3.false = fall$, $B_4.true = fall$, $B_4.false = L1$. Code: $B_3.code \,\Vert\, B_4.code \,\Vert\, label(L3)$.
4. Relational expressions:
- $B_3$ (true = L3, false = fall) gives `if x != y goto L3`.
- $B_4$ (true = fall, false = L1) gives `ifFalse x > 20 goto L1`.
- $B_2$ (true = fall, false = L1) gives `ifFalse x < 10 goto L1`.

**Three-address code:**

```text
        if x != y goto L3
        ifFalse x > 20 goto L1
L3:     ifFalse x < 10 goto L1
        flag = 0
        goto L2
L1:     flag = 1
L2:
```

Check: if `x != y`, skip the `x > 20` test and go straight to `x < 10`. Otherwise `x > 20` must hold. Then `x < 10` decides between `flag = 0` and `flag = 1`. No jump goes to the very next instruction.
