---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "With int width 4, a: array(5, array(5, integer)) (row width 20): t1 = i \\* 4; t2 = b[t1]; t3 = t2 \\* 20; t4 = j \\* 4; t5 = c[t4]; t6 = t5 \\* 4; t7 = t3 + t6; t8 = a[t7]."
sources: ["KMS Chapter 6 slides 66-71 (Addressing Array Element, Translation of Array References)", "Dragon book 2e sec. 6.4.3-6.4.4 (Fig. 6.22, Example 6.12)"]
---
**Assumptions.** The width of `int` is 4 (as in Q10(a)). So `a` has type array(5, array(5, integer)): an element is 4 bytes and a row is $5 \times 4 = 20$ bytes. `b` and `c` are array(3, integer). The expression is used as a value (reduced to $E \to L$). Temporaries are numbered in the order `new Temp()` is called.

**Parse structure.** `a[b[i]][c[j]]` is $L \to L_1\,[E_2]$, where $L_1 \to \textbf{a}\,[E_1]$, $E_1 \to L$ for `b[i]`, and $E_2 \to L$ for `c[j]`. The actions run bottom-up, left to right.

| Reduction | Attributes / code generated |
|:--|:--|
| $E \to \textbf{i}$ | `E.addr = i` |
| $L \to \textbf{b}\,[E]$ | `L.type = integer`, width 4: **`t1 = i * 4`** |
| $E_1 \to L$ | **`t2 = b [ t1 ]`** |
| $L_1 \to \textbf{a}\,[E_1]$ | `L1.type = array(5, integer)`, width 20: **`t3 = t2 * 20`** |
| $E \to \textbf{j}$ | `E.addr = j` |
| $L \to \textbf{c}\,[E]$ | `L.type = integer`, width 4: **`t4 = j * 4`** |
| $E_2 \to L$ | **`t5 = c [ t4 ]`** |
| $L \to L_1\,[E_2]$ | `L.type = integer`, width 4; `t = t6`, `L.addr = t7`: **`t6 = t5 * 4`**, **`t7 = t3 + t6`** |
| $E \to L$ | **`t8 = a [ t7 ]`** |

**Three-address code:**

```text
t1 = i * 4
t2 = b [ t1 ]
t3 = t2 * 20
t4 = j * 4
t5 = c [ t4 ]
t6 = t5 * 4
t7 = t3 + t6
t8 = a [ t7 ]
```

`t8` holds the value of `a[b[i]][c[j]]`; its address is `a` + $20 \cdot b[i] + 4 \cdot c[j]$, the row-major address.
