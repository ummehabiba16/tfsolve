---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "(i) S -> if (B) S1 else S2: B.true = newlabel(); B.false = newlabel(); S1.next = S2.next = S.next; S.code = B.code || label(B.true) || S1.code || gen(goto S.next) || label(B.false) || S2.code. (ii) B -> B1 && B2: B1.true = newlabel(); B1.false = B.false; B2.true = B.true; B2.false = B.false; B.code = B1.code || label(B1.true) || B2.code."
sources: ["KMS Chapter 6 slides 75-94 (Short Circuit Code, Flow of Control Statements, Translation of Boolean Expression)", "Dragon book 2e sec. 6.6.3-6.6.4 (Figs. 6.36, 6.37)"]
---
**(i) $S \to \textit{if}\ (B)\ S_1\ \textit{else}\ S_2$**

| Semantic rules |
|:--|
| $B.true = newlabel()$ |
| $B.false = newlabel()$ |
| $S_1.next = S_2.next = S.next$ |
| $S.code = B.code \,\Vert\, label(B.true) \,\Vert\, S_1.code$ |
| $\qquad \Vert\ gen('\text{goto}'\ S.next) \,\Vert\, label(B.false) \,\Vert\, S_2.code$ |

The code for $B$ jumps to $B.true$ (start of $S_1$) or $B.false$ (start of $S_2$). After $S_1$, a jump skips $S_2$. Both branches continue at $S.next$.

```text
        B.code          (jumps to B.true / B.false)
B.true: S1.code
        goto S.next
B.false:S2.code
```

**(ii) $B \to B_1\ \&\&\ B_2$** (short circuit: if $B_1$ is false, $B$ is false without evaluating $B_2$)

| Semantic rules |
|:--|
| $B_1.true = newlabel()$ |
| $B_1.false = B.false$ |
| $B_2.true = B.true$ |
| $B_2.false = B.false$ |
| $B.code = B_1.code \,\Vert\, label(B_1.true) \,\Vert\, B_2.code$ |

```text
          B1.code       (false -> B.false, true -> B1.true)
B1.true:  B2.code       (true -> B.true, false -> B.false)
```

`newlabel()` creates a fresh label and `label(L)` attaches $L$ to the next instruction. The jumping labels are inherited, as stated in the question.
