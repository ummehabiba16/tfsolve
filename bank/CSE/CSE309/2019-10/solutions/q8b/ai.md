---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "DAG: leaves b0, c0, a0, i0, j0; node n1 = \\* (b0, c0) with labels d and g (b \\* c is a common subexpression); n2 = =[] (a0, i0) labelled e; n3 = + (n2, n1) labelled f; n4 = []= (a0, j0, n3) for a[j] = f, which kills n2 for later reuse. Reassembled: d = b \\* c; e = a[i]; f = e + d; g = d; a[j] = f."
sources: ["KMS Chapter 8 slides 40-50 (DAG representation of Basic Blocks, Representation of Array References)", "Dragon book 2e sec. 8.5.1-8.5.5"]
---
**Assumptions.** All of `d`, `e`, `f`, `g` may be live on exit (the question does not say otherwise), so every label is kept.

**Construction** (one node per distinct value, reusing a node when the same operator and children appear again):

| Statement | Action |
|:--|:--|
| `d = b * c` | leaves $b_0$, $c_0$; node $n_1 = {*}(b_0, c_0)$, label **d** |
| `e = a [ i ]` | leaves $a_0$, $i_0$; node $n_2 = {=}[\,](a_0, i_0)$, label **e** |
| `f = e + d` | node $n_3 = {+}(n_2, n_1)$, label **f** |
| `g = b * c` | ${*}(b_0, c_0)$ already exists as $n_1$ (neither b nor c changed), so attach label **g** to $n_1$ |
| `a [ j ] = f` | leaf $j_0$; node $n_4 = [\,]{=}(a_0, j_0, n_3)$. An array assignment **kills** all nodes depending on `a` (here $n_2$), so a later `a[i]` would need a new node |

**DAG:**

```text
            n4 ( []= )
           /    |    \
         a0     j0    n3 ( + )  f
                     /     \
             e  n2 (=[])    n1 ( * )  d, g
                /    \       /   \
              a0      i0   b0     c0
```

(The leaf $a_0$ is shared by $n_2$ and $n_4$.)

**Code reassembled from the DAG** (the common subexpression `b * c` is computed once):

```text
d = b * c
e = a [ i ]
f = e + d
g = d
a [ j ] = f
```

If `g` were the only live label of $n_1$, $n_1$ would be computed directly into `g`. If `d` were dead, `d = b * c` would become `g = b * c` and `f = e + g`.
