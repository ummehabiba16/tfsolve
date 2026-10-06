---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Using the SDD of 5(a): T for 2 gives T.val = 2, so E'.inh = 2; the term 3 \\* 4 gives T'.inh = 3, T1'.inh = 12, T.val = 12, so the next E1'.inh = 14; the term 5 gives T.val = 5, E2'.inh = 19; at E3' -> eps, syn = 19 is copied up, so E.val = 19."
sources: ["KMS Chapter 5 slides 18-22 (Evaluating Inherited Attributes)", "Dragon book 2e sec. 5.1.2 (Fig. 5.5), 5.2.1"]
changes:
  - "2026-10-06: replaced the ASCII tree by a TikZ annotated parse tree (values unchanged)"
---
Using the SDD of 5(a). Attribute values are shown at each node (`inh` = inherited, `syn` = synthesized, `val` = value).

![Annotated parse tree of 2+3*4+5 with inherited and synthesized values](figures/annotated.png)

**Order of evaluation** (a topological order of the dependency graph):

1. Leftmost term: $F.val = 2$, $T'.inh = 2$, $T'.syn = 2$, $T.val = 2$. Then $E'.inh = T.val = 2$.
2. Second term: $F.val = 3$, $T'.inh = 3$; $F.val = 4$, $T_1'.inh = 3 \times 4 = 12$, $T_1'.syn = 12$, $T'.syn = 12$, $T.val = 12$. Then $E_1'.inh = 2 + 12 = 14$.
3. Third term: $T.val = 5$. Then $E_2'.inh = 14 + 5 = 19$.
4. $E_2' \to \epsilon$: $E_2'.syn = 19$, copied up: $E_1'.syn = 19$, $E'.syn = 19$, $E.val = 19$.

**Result: 19**, which is $2 + (3 \times 4) + 5$.
