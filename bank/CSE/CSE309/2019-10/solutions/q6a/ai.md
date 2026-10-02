---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "(i) if-else: B.true = newlabel(); B.false = newlabel(); S1.next = S2.next = S.next; S.code = B.code || label(B.true) || S1.code || gen(goto S.next) || label(B.false) || S2.code. (ii) while: begin = newlabel(); B.true = newlabel(); B.false = S.next; S1.next = begin; S.code = label(begin) || B.code || label(B.true) || S1.code || gen(goto begin). (iii) ||: B1.true = B.true; B1.false = newlabel(); B2.true = B.true; B2.false = B.false; B.code = B1.code || label(B1.false) || B2.code. (iv) &&: B1.true = newlabel(); B1.false = B.false; B2.true = B.true; B2.false = B.false; B.code = B1.code || label(B1.true) || B2.code. (v) E -> num: E.addr = num.val; E.code = ''."
sources: ["KMS Chapter 6 slides 77-94 (Flow of Control Statements, SDD for Flow-of-Control and Booleans)", "Dragon book 2e sec. 6.6.3-6.6.4 (Figs. 6.36, 6.37)"]
---
The added rules follow the same conventions as the given SDD: `newlabel()`, `label(L)`, `gen(...)`, inherited `B.true`, `B.false`, `S.next`, and synthesized `code`.

**(i) $S \to \text{if}\ (B)\ S_1\ \text{else}\ S_2$**

| Semantic rules |
|:--|
| $B.true = newlabel()$ |
| $B.false = newlabel()$ |
| $S_1.next = S_2.next = S.next$ |
| $S.code = B.code \,\Vert\, label(B.true) \,\Vert\, S_1.code$ |
| $\qquad \Vert\ gen('\text{goto}'\ S.next) \,\Vert\, label(B.false) \,\Vert\, S_2.code$ |

**(ii) $S \to \textbf{while}\ (B)\ S_1$**

| Semantic rules |
|:--|
| $begin = newlabel()$ |
| $B.true = newlabel()$ |
| $B.false = S.next$ |
| $S_1.next = begin$ |
| $S.code = label(begin) \,\Vert\, B.code \,\Vert\, label(B.true) \,\Vert\, S_1.code \,\Vert\, gen('\text{goto}'\ begin)$ |

**(iii) $B \to B_1 \Vert B_2$** (if $B_1$ is true, $B$ is true; otherwise test $B_2$)

| Semantic rules |
|:--|
| $B_1.true = B.true$ |
| $B_1.false = newlabel()$ |
| $B_2.true = B.true$ |
| $B_2.false = B.false$ |
| $B.code = B_1.code \,\Vert\, label(B_1.false) \,\Vert\, B_2.code$ |

**(iv) $B \to B_1\ \&\&\ B_2$** (if $B_1$ is false, $B$ is false; otherwise test $B_2$)

| Semantic rules |
|:--|
| $B_1.true = newlabel()$ |
| $B_1.false = B.false$ |
| $B_2.true = B.true$ |
| $B_2.false = B.false$ |
| $B.code = B_1.code \,\Vert\, label(B_1.true) \,\Vert\, B_2.code$ |

**(v) $E \to \textbf{num}$**

| Semantic rules |
|:--|
| $E.addr = \textbf{num}.val$ |
| $E.code = ''$ |

A constant needs no code; its value is used directly as an address operand, like `id` uses its symbol-table entry.
