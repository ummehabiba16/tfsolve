---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "With the fall-through technique (S.next = L3, B.true = fall, B.false = L1): ifFalse x > 20 goto L1; if x < 10 goto L2; ifFalse x != y goto L1; L2: x = 0; goto L3; L1: x = 1; L3:."
sources: ["KMS Chapter 6 slides 98-101 (Avoiding Redundant Gotos)", "Dragon book 2e sec. 6.6.5 (Figs. 6.39, 6.40)"]
---
**Assumptions.** The fall-through technique of the text is used (the special label `fall` means "no jump"). The statement's next label is `L3`. New labels are numbered in the order they are created.

The condition is $B = B_1\ \&\&\ B_2$ with $B_1$: `x > 20` and $B_2 = B_3 \Vert B_4$ ($B_3$: `x < 10`, $B_4$: `x != y`), because of the parentheses.

**Inherited labels:**

1. $S \to \textbf{if}\ (B)\ S_1\ \textbf{else}\ S_2$: $B.true = fall$ (fall into $S_1$), $B.false = L1$ (start of $S_2$). $S.code = B.code \,\Vert\, S_1.code \,\Vert\, gen(\text{goto } S.next) \,\Vert\, label(L1) \,\Vert\, S_2.code$.
2. $B \to B_1\ \&\&\ B_2$: $B.false = L1 \ne fall$, so $B_1.true = fall$, $B_1.false = L1$, $B_2.true = fall$, $B_2.false = L1$.
3. $B_2 \to B_3 \Vert B_4$: $B_2.true = fall$, so $B_3.true = newLabel() = L2$, $B_3.false = fall$, $B_4.true = fall$, $B_4.false = L1$. $B_2.code = B_3.code \,\Vert\, B_4.code \,\Vert\, label(L2)$.
4. Relational expressions:
- $B_1$ (true = fall, false = L1) gives `ifFalse x > 20 goto L1`.
- $B_3$ (true = L2, false = fall) gives `if x < 10 goto L2`.
- $B_4$ (true = fall, false = L1) gives `ifFalse x != y goto L1`.

**Code:**

```text
        ifFalse x > 20 goto L1
        if x < 10 goto L2
        ifFalse x != y goto L1
L2:     x = 0
        goto L3
L1:     x = 1
L3:
```

Every conditional jump is needed; there is no `goto` to the very next instruction. (The only unconditional jump, `goto L3`, skips the else part. Note that `x > 20 && x < 10` can never be true, but the compiler does not reason about this.)
