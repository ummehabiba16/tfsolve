---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Parse: B = B1 || B2 with B2 = B3 && B4 (&& binds tighter). With S.next = L1: B.true = fall, B.false = L1; B1.true = L2 (new), B1.false = fall; B2.true = fall, B2.false = L1; B3.true = fall, B3.false = L1; B4.true = fall, B4.false = L1. Code: if x > 100 goto L2; ifFalse x > 200 goto L1; ifFalse x != y goto L1; L2: x = 0; L1:."
sources: ["KMS Chapter 6 slides 93-101 (SDD for Flow-of-Control and Booleans, Avoiding Redundant Gotos)", "Dragon book 2e sec. 6.6.5"]
---
`&&` has higher precedence than `||`, so the condition parses as

$$x > 100 \ \Vert\ (x > 200\ \&\&\ x \ne y)$$

Let $B$ be the whole condition, $B_1$ = `x > 100`, $B_2$ = `x > 200 && x != y`, $B_3$ = `x > 200`, $B_4$ = `x != y`. Let the statement's next label be $S.next = L1$ (attached after the statement, e.g. by $P \to S$).

**Annotated parse tree** (inherited *true*/*false* attributes shown at each node):

```text
S  [next = L1]
|-- if ( B ) S1
    B   [true = fall, false = L1]                       (B -> B1 || B2)
    |-- B1  [true = L2, false = fall]                   (x > 100)
    |    `-- E1.addr = x   rel.op = >   E2.addr = 100
    |-- ||
    `-- B2  [true = fall, false = L1]                   (B2 -> B3 && B4)
         |-- B3  [true = fall, false = L1]              (x > 200)
         |    `-- E1.addr = x   rel.op = >   E2.addr = 200
         |-- &&
         `-- B4  [true = fall, false = L1]              (x != y)
              `-- E1.addr = x   rel.op = !=  E2.addr = y
    S1  [next = L1]   x = 0
```

**How the attributes are computed:**

1. $S \to \textbf{if}\ (B)\ S_1$: $B.true = fall$, $B.false = S_1.next = S.next = L1$.
2. $B \to B_1 \Vert B_2$: $B.true = fall$, so $B_1.true = newLabel() = L2$, $B_1.false = fall$, $B_2.true = fall$, $B_2.false = L1$. Code: $B_1.code \,\Vert\, B_2.code \,\Vert\, label(L2)$.
3. $B_2 \to B_3\ \&\&\ B_4$: $B_2.false = L1 \ne fall$, so $B_3.true = fall$, $B_3.false = L1$, $B_4.true = fall$, $B_4.false = L1$. Code: $B_3.code \,\Vert\, B_4.code$.
4. Relational nodes:

- $B_1$ has *true* = L2 and *false* = fall, giving `if x > 100 goto L2`.
- $B_3$ has *true* = fall and *false* = L1, giving `ifFalse x > 200 goto L1`.
- $B_4$ is the same, giving `ifFalse x != y goto L1`.

**Generated code:**

```text
        if x > 100 goto L2
        ifFalse x > 200 goto L1
        ifFalse x != y goto L1
L2:     x = 0
L1:
```

Check: if `x > 100`, jump to L2 and assign. Otherwise test `x > 200` and `x != y`; if either fails, skip the assignment; if both hold, fall into `x = 0`. There are no redundant `goto`s.
