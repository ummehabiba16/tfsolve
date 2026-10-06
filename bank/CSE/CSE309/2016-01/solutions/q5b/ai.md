---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "i := i + j*k gives t1 := j * k; t2 := i + t1; i := t2. while i do i := 2*n + k gives L1: if i = 0 goto L2; t1 := 2; t2 := t1 * n; t3 := t2 + k; i := t3; goto L1; L2:."
sources: ["KMS Chapter 6 slides 52-62, 72-103", "Dragon book 2e sec. 6.4, 6.6.3"]
---
**Assumptions.** The three printed lines are two strings: `i := i + j*k`, and `while i do i := 2*n + k`. Each is translated on its own, with `newtemp()` starting at $t_1$ and `newlabel()` at $L_1$ each time. In `E.code := E1.code || E2.code || gen(...)` the code of the operands is emitted first.

**String 1: `i := i + j*k`.** $S \to \textbf{id} := E$, $E \to E_1 + E_2$, $E_1 \to \textbf{id}_i$, $E_2 \to E_3 * E_4$, $E_3 \to \textbf{id}_j$, $E_4 \to \textbf{id}_k$ (since $*$ has higher precedence).

| Node | Rule | $place$ | $code$ |
|:--|:--|:-:|:--|
| $E_1$ (`i`), $E_3$ (`j`), $E_4$ (`k`) | $E \to \textbf{id}$ | `i`, `j`, `k` | empty |
| $E_2$ (`j*k`) | $E \to E_1 * E_2$ | `t1` | `t1 := j * k` |
| $E$ (`i + j*k`) | $E \to E_1 + E_2$ | `t2` | `t1 := j * k`, `t2 := i + t1` |
| $S$ | $S \to \textbf{id} := E$ | | `t1 := j * k`, `t2 := i + t1`, `i := t2` |

```text
t1 := j * k
t2 := i + t1
i := t2
```

**String 2: `while i do i := 2*n + k`.** $S \to \textbf{while}\ E\ \textbf{do}\ S_1$ with $E \to \textbf{id}_i$ (so $E.place$ = `i`, $E.code$ empty), and $S_1$ is `i := 2*n + k` with $E \to E_1 + E_2$, $E_1 \to E_3 * E_4$, $E_3 \to \textbf{num}$ (2), $E_4 \to \textbf{id}_n$, $E_2 \to \textbf{id}_k$.

- $S.begin$ = `L1`, $S.after$ = `L2` (both created when the production is reduced, before the code is concatenated).
- $E_3 \to \textbf{num}$: `t1 := 2`. $E_1 \to E_3 * E_4$: `t2 := t1 * n`. $E \to E_1 + E_2$: `t3 := t2 + k`. $S_1.code$ = these three, then `i := t3`.
- $S.code$ = `L1:` $\parallel$ $E.code$ (empty) $\parallel$ `if i = 0 goto L2` $\parallel$ $S_1.code$ $\parallel$ `goto L1` $\parallel$ `L2:`.

```text
L1:
if i = 0 goto L2
t1 := 2
t2 := t1 * n
t3 := t2 + k
i := t3
goto L1
L2:
```

*Check:* the semantic rules of the table were simulated by a script; it printed exactly the code above.
