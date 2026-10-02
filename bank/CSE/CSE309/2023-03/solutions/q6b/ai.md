---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "B -> B1 && B2: B1.true = fall; B1.false = if B.false != fall then B.false else newLabel(); B2.true = B.true; B2.false = B.false; B.code = if B.false != fall then B1.code || B2.code else B1.code || B2.code || label(B1.false).  B -> E1 rel E2: test = E1.addr rel.op E2.addr; s = if both true/false != fall: gen(if test goto B.true) || gen(goto B.false); else if B.true != fall: gen(if test goto B.true); else if B.false != fall: gen(ifFalse test goto B.false); else ''; B.code = E1.code || E2.code || s."
sources: ["KMS Chapter 6 slides 98-101 (Avoiding Redundant Gotos)", "Dragon book 2e sec. 6.6.5 (Figs. 6.39, 6.40)"]
---
The special label `fall` means "do not jump; fall through to the next instruction". The rules mirror those given for `||`, with the roles of *true* and *false* exchanged.

**(i) $B \to B_1\ \&\&\ B_2$**

If $B_1$ is false, the whole $B$ is false, so $B_1$ must jump to $B.false$. If $B_1$ is true, control simply falls into $B_2$.

| Semantic rules |
|:--|
| $B_1.true = fall$ |
| $B_1.false =$ **if** $B.false \ne fall$ **then** $B.false$ **else** $newLabel()$ |
| $B_2.true = B.true$ |
| $B_2.false = B.false$ |
| $B.code =$ **if** $B.false \ne fall$ **then** $B_1.code \,\Vert\, B_2.code$ |
| $\qquad$ **else** $B_1.code \,\Vert\, B_2.code \,\Vert\, label(B_1.false)$ |

If $B.false$ is itself `fall`, $B_1$ cannot fall through on false, because falling through means "go into $B_2$". So it gets a new label, which is placed right after $B_2$'s code, where $B$'s false exit falls through.

**(ii) $B \to E_1\ \textbf{rel}\ E_2$**

Generate as few jumps as possible, depending on which exits are `fall`:

| Semantic rules |
|:--|
| $test = E_1.addr\ \textbf{rel}.op\ E_2.addr$ |
| $s =$ **if** $B.true \ne fall$ **and** $B.false \ne fall$ **then** $gen('\text{if}'\ test\ '\text{goto}'\ B.true) \,\Vert\, gen('\text{goto}'\ B.false)$ |
| $\quad$ **else if** $B.true \ne fall$ **then** $gen('\text{if}'\ test\ '\text{goto}'\ B.true)$ |
| $\quad$ **else if** $B.false \ne fall$ **then** $gen('\text{ifFalse}'\ test\ '\text{goto}'\ B.false)$ |
| $\quad$ **else** $''$ |
| $B.code = E_1.code \,\Vert\, E_2.code \,\Vert\, s$ |

- Both exits are real labels: a conditional jump to *true* and an unconditional jump to *false*.
- Only *true* is a label (false falls through): a single `if ... goto`.
- Only *false* is a label (true falls through): a single `ifFalse ... goto`.
- Both fall through: no jump needed (this cannot happen in a correct program, but the rule is complete).
