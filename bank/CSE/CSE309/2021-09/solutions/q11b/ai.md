---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "CSE and copy propagation shrink B5 to temp = a[t3]; t10 = a[t9]; a[t3] = t10; a[t9] = temp (t3 = 16i + 4j, t9 = 16j + 4i); d = 4 is propagated as a constant and removed; t1 = 16i and t8 = 4i move out of the inner loop; strength reduction gives t3 = t3 + 4, t9 = t9 + 16 (inner) and t1 = t1 + 16, t8 = t8 + 4 (outer); i and j are eliminated by testing t1 < 64 and t3 < t1 + 16. Checked by running both versions on a sample array."
sources: ["KMS Chapter 9 slides 9-35 (Semantic-Preserving Transformations)", "Dragon book 2e sec. 9.1"]
---
**Assumptions.** `a` is a 4 $\times$ 4 array of 4-byte elements (row width 16). After the code, only the array `a` is needed: `d`, `i`, `j` and the temporaries are dead on exit. The code swaps `a[i][j]` with `a[j][i]` (a transpose).

**(i) Common-subexpression elimination.** In B5, `i` and `j` do not change before line 22:

- `t4 = i*16` and `t5 = j*4` equal `t1` and `t2`, so `t6 = t4 + t5` equals `t3`;
- `t11 = j*16` and `t12 = i*4` equal `t7` and `t8`, so `t13` equals `t9`.

**(ii) Copy propagation.** Replace `t6` by `t3` and `t13` by `t9`: `a[t3] = t10`, `a[t9] = temp`. Also `d = 4` is a constant copy, so the tests become `i < 4` and `j < 4`.

**(iii) Dead-code elimination.** `t4`, `t5`, `t6`, `t11`, `t12`, `t13` and `d` are no longer used, so their assignments are removed. B5 becomes:

```text
t1 = i * 16      t7 = j * 16      temp = a[t3]     a[t3] = t10
t2 = j * 4       t8 = i * 4       t10 = a[t9]      a[t9] = temp
t3 = t1 + t2     t9 = t7 + t8     j = j + 1        goto B4
```

**(iv) Reduction in strength on induction variables.**

- *Inner loop (B4, B5):* `j` is a basic induction variable (+1). `t2 = 4j` and `t7 = 16j` are derived induction variables, and so are `t3 = t1 + 4j` and `t9 = 16j + t8`, since `t1 = 16i` and `t8 = 4i` are invariant in the inner loop. Replace them by `t3 = t3 + 4` and `t9 = t9 + 16` after `j` is incremented.
- Initialise in B3, using `j = i + 1`: `t3 = 16i + 4(i+1) = t1 + t8 + 4` and `t9 = 16(i+1) + 4i = t1 + t8 + 16`.
- *Outer loop:* `i` is a basic induction variable. `t1 = 16i` and `t8 = 4i` (now computed only in B3, a form of code motion out of the inner loop) become `t1 = t1 + 16` and `t8 = t8 + 4` in B6, initialised to 0 in B1.

**(v) Elimination of induction variables.**

- Inner test: `j < 4` holds exactly when `16i + 4j < 16i + 16`, i.e. `t3 < t14` with `t14 = t1 + 16` computed in B3.
- Outer test: `i < 4` holds exactly when `t1 < 64`.
- Now `i` and `j` are unused, so `i = 0`, `j = i + 1`, `j = j + 1` and `i = i + 1` are removed.

**Optimised code:**

```text
B1:  t1 = 0
     t8 = 0
B2:  iffalse t1 < 64 goto B7
B3:  t15 = t1 + t8
     t3 = t15 + 4
     t9 = t15 + 16
     t14 = t1 + 16
B4:  iffalse t3 < t14 goto B6
B5:  temp = a [ t3 ]
     t10 = a [ t9 ]
     a [ t3 ] = t10
     a [ t9 ] = temp
     t3 = t3 + 4
     t9 = t9 + 16
     goto B4
B6:  t1 = t1 + 16
     t8 = t8 + 4
     goto B2
B7:
```

The inner loop went from 19 instructions with 8 multiplications to 8 instructions with none. (Both versions were run on a sample array and leave identical contents.)
