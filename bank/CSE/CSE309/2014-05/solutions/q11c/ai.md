---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Jumping-code SDD with inherited labels: B -> B1 || B2: B1.true = B.true, B1.false = newlabel(), B2.true = B.true, B2.false = B.false, B.code = B1.code || label(B1.false) || B2.code. B -> true: B.code = gen('goto' B.true). B -> E1 rel E2: B.code = E1.code || E2.code || gen('if' E1.addr rel.op E2.addr 'goto' B.true) || gen('goto' B.false)."
sources: ["KMS Chapter 6 slides 72-103 (boolean expressions, short-circuit code)", "Dragon book 2e sec. 6.6.1-6.6.4, Fig. 6.37"]
---
Boolean expressions are translated into **jumping code** (short-circuit): $B.code$ jumps to $B.true$ if the expression is true and to $B.false$ if it is false, and does not fall through. $B.true$ and $B.false$ are **inherited** labels; $E.addr$ and $E.code$ are the usual attributes of arithmetic expressions (Dragon book sec. 6.6.4, Fig. 6.37).

| Production | Semantic rules |
|:--|:--|
| $B \to B_1\ \vert\vert\ B_2$ | $B_1.true = B.true$ |
| | $B_1.false = newlabel()$ |
| | $B_2.true = B.true$ |
| | $B_2.false = B.false$ |
| | $B.code = B_1.code\ /\!/\ label(B_1.false)\ /\!/\ B_2.code$ |
| $B \to \textbf{true}$ | $B.code = gen(\text{'goto'}\ B.true)$ |
| $B \to E_1\ \textbf{rel}\ E_2$ | $B.code = E_1.code\ /\!/\ E_2.code$ |
| | $\quad /\!/\ gen(\text{'if'}\ E_1.addr\ \textbf{rel}.op\ E_2.addr\ \text{'goto'}\ B.true)$ |
| | $\quad /\!/\ gen(\text{'goto'}\ B.false)$ |

($/\!/$ is concatenation; $\textbf{rel}.op$ is the relational operator.)

**Explanation.**

- **$B_1 \,\vert\vert\, B_2$.** If $B_1$ is true, the whole expression is true, so $B_1.true = B.true$ (jump out immediately: short circuit). If $B_1$ is false, we must evaluate $B_2$, so $B_1.false$ is a **new label** placed at the start of $B_2.code$. The true and false exits of $B_2$ are those of $B$.
- **`true`.** Always jumps to $B.true$ (no test).
- **$E_1\ \textbf{rel}\ E_2$.** Evaluate both operands, then a conditional jump to $B.true$ when the relation holds, otherwise an unconditional `goto` $B.false$.

**Example.** `x < 100 || y > 5` with $B.true = L_1$, $B.false = L_2$ gives

```text
        if x < 100 goto L1
        goto L3
L3:     if y > 5 goto L1
        goto L2
```
