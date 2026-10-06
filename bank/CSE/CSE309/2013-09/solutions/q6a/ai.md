---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Short-circuit code evaluates a boolean expression by jumps, skipping the rest as soon as the value is known; the value is represented by the position in the code reached. Example: if (x < 100 || x > 200 && x != y) x = 0; becomes if x < 100 goto L2; ifFalse x > 200 goto L1; ifFalse x != y goto L1; L2: x = 0; L1:."
sources: ["KMS Chapter 6 slides 72-103 (short-circuit code)", "Dragon book 2e sec. 6.6.1-6.6.2"]
---
**Short-circuit (jumping) code.** In the translation of a boolean expression with `&&`, `||`, `!` the operators are not computed as values: the expression is translated into a sequence of **jumps**, and the **position reached in the code** shows the value (true or false). The evaluation stops as soon as the value is determined: in $B_1 \,||\, B_2$ if $B_1$ is true, $B_2$ is not evaluated; in $B_1 \,\&\&\, B_2$ if $B_1$ is false, $B_2$ is not evaluated (Dragon book sec. 6.6.2). This is the semantics of C and Java, and it also makes the code faster.

**Example.** `if (x < 100 || x > 200 && x != y) x = 0;`

Jumping code:

```text
        if x < 100 goto L2
        goto L3
L3:     if x > 200 goto L4
        goto L1
L4:     if x != y goto L2
        goto L1
L2:     x = 0
L1:     ...
```

With the redundant `goto`s removed (fall-through code, sec. 6.6.5):

```text
        if x < 100 goto L2          // true: skip the rest
        ifFalse x > 200 goto L1     // false: && is false, skip x != y
        ifFalse x != y goto L1
L2:     x = 0
L1:     ...
```

If `x < 100` is true the other two comparisons are never evaluated; if it is false, `x > 200 && x != y` is evaluated and `x != y` only when `x > 200`.
