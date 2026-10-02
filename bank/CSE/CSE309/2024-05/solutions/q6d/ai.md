---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Taking the printed i to mean j: t1 = j \\* 2; t2 = c[t1]; t3 = t2 \\* 2; t4 = b[t3]; t5 = t4 \\* 2; t6 = a[t5]; x = t6."
sources: ["KMS Chapter 6 slides 66-71 (Addressing Array Element, Translation of Array References)", "Dragon book 2e sec. 6.4.3-6.4.4 (Fig. 6.22)"]
---
**Assumptions.**

- The paper says "i and x are integers", but the statement uses `j`. Take `j` (the index variable) as an integer.
- Arrays start at index 0, with no bounds checking. `a`, `b`, `c` denote the base addresses of the arrays.
- The translation scheme for array references from the text is used:

```text
L -> id [ E ]   { L.array = top.get(id.lexeme); L.type = L.array.type.elem;
                  L.addr = new Temp(); gen(L.addr '=' E.addr '*' L.type.width); }
E -> L          { E.addr = new Temp(); gen(E.addr '=' L.array.base '[' L.addr ']'); }
S -> id = E ;   { gen(top.get(id.lexeme) '=' E.addr); }
```

For one-dimensional `int` arrays, the element width is 2, so the offset of element $k$ is $k \times 2$.

**Translation, innermost reference first:**

1. `c[j]`: offset `t1 = j * 2`, value `t2 = c[t1]`.
2. `b[c[j]]`: index `t2`, offset `t3 = t2 * 2`, value `t4 = b[t3]`.
3. `a[b[c[j]]]`: index `t4`, offset `t5 = t4 * 2`, value `t6 = a[t5]`.
4. Assignment: `x = t6`.

```text
t1 = j * 2
t2 = c [ t1 ]
t3 = t2 * 2
t4 = b [ t3 ]
t5 = t4 * 2
t6 = a [ t5 ]
x = t6
```

(The last copy can be folded into `x = a [ t5 ]`.) The declared sizes `a[5]`, `b[3]`, `c[3]` matter only for bounds checking: each dimension has one index, so only the width 2 enters the address computation.
