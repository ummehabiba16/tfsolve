---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Eliminate the left recursion and carry the value computed so far in an inherited attribute: B -> 1 { R.i = 1 } R { B.val = R.s };  R -> 0 { R1.i = 2 \\* R.i } R1 { R.s = R1.s };  R -> 1 { R1.i = 2 \\* R.i + 1 } R1 { R.s = R1.s };  R -> eps { R.s = R.i }. For 101: R.i takes 1, 2, 5 and B.val = 5."
sources: ["KMS Chapter 5 slides 62-69 (Eliminating Left Recursion from SDTs)", "Dragon book 2e sec. 5.4.4"]
changes:
  - "2026-10-06: added TikZ figure (figures/annotated.png) for the inherited and synthesized values; the answer itself is unchanged."
---
**Idea.** The left-recursive grammar $B \to B\,0 \mid B\,1 \mid 1$ generates a leading `1` followed by any string of 0s and 1s. In the right-recursive form

$$B \to 1\,R, \qquad R \to 0\,R \mid 1\,R \mid \epsilon$$

the value can no longer be synthesized from the left part. Instead, pass the **value of the prefix read so far** down as an inherited attribute `R.i`, and pass the final value back up in a synthesized attribute `R.s` (KMS slides / Dragon 5.4.4: "a value computed by the left-recursive rules is handed down through an inherited attribute").

**SDT:**

$$B \to 1\ \{R.i = 1;\}\ R\ \{B.val = R.s;\}$$

$$R \to 0\ \{R_1.i = 2 \times R.i;\}\ R_1\ \{R.s = R_1.s;\}$$

$$R \to 1\ \{R_1.i = 2 \times R.i + 1;\}\ R_1\ \{R.s = R_1.s;\}$$

$$R \to \epsilon\ \{R.s = R.i;\}$$

Each action that computes an inherited attribute of $R_1$ is placed just before $R_1$, and each synthesized-attribute action at the end of its body, so the SDT is L-attributed and works in a top-down parse.

![Annotated parse tree for 1011](figures/annotated.png)

**Check with `1011` (= 11):**

| Expansion | Inherited `R.i` |
|:--|:--|
| $B \to 1\,R$ | $R.i = 1$ |
| $R \to 0\,R_1$ | $R_1.i = 2 \times 1 = 2$ |
| $R_1 \to 1\,R_2$ | $R_2.i = 2 \times 2 + 1 = 5$ |
| $R_2 \to 1\,R_3$ | $R_3.i = 2 \times 5 + 1 = 11$ |
| $R_3 \to \epsilon$ | $R_3.s = 11$, copied up: $B.val = 11$ |

The original SDT gives the same value: $((1 \times 2 + 0) \times 2 + 1) \times 2 + 1 = 11$.
