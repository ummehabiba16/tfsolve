---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Row width = 15*8 = 120, element width 8: t1 = k * 4; t2 = a[t1]; t3 = (float) t2; t4 = t3 * b; param 3; param d; param 2.5; t5 = call c, 3; t6 = t4 + t5; t7 = i * 120; t8 = j * 8; t9 = t7 + t8; y[t9] = t6."
sources: ["KMS Chapter 6 slides 52-71 (expressions and array references)", "Dragon book 2e sec. 6.4.3, 6.2.1, 6.5.2"]
---
**Types and widths.** $y : array(10, array(15, float))$: a row $y[i]$ is $array(15, float)$ with width $15 \times 8 = 120$; an element $y[i][j]$ has width 8. $a : array(10, integer)$: element width 4. $c : integer \times float \times float \to float$, so $c(3, d, 2.5)$ is a $float$; thus the arguments are the integer 3, and $d$ and 2.5 are $float$. Assumption: $b$ is a $float$ (the product is added to a $float$, and the result is stored in a $float$ array).

**Addresses** (Dragon book sec. 6.4.3):

- $a[k]$ is at $base(a) + k \times 4$;
- $y[i][j]$ is at $base(y) + i \times 120 + j \times 8$.

**Translation.** The right side is evaluated first: `a[k] * b` (with the coercion of the integer `a[k]` to float before multiplying by the float `b`), then the function call, then the sum; last the address of the left-hand element:

```text
t1 = k * 4
t2 = a [ t1 ]
t3 = (float) t2          // a[k] is an integer: widened to float
t4 = t3 * b
param 3
param d
param 2.5
t5 = call c, 3
t6 = t4 + t5
t7 = i * 120
t8 = j * 8
t9 = t7 + t8
y [ t9 ] = t6
```

(`t9 = i*120 + j*8` is the offset of `y[i][j]` from the start of `y`.)
