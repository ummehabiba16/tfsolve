---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "(1) In SSA every variable is assigned exactly once (each definition creates a new name, e.g. p1, p2, p3), unlike three-address code where a name can be assigned many times. (2) Where different definitions of a variable reach a join point, SSA uses a phi-function, e.g. x3 = phi(x1, x2) after if (flag) x1 = -1; else x2 = 1."
sources: ["KMS Chapter 6 slides 35-36 (Static Single Assignment Form)", "Dragon book 2e sec. 6.2.4 (Fig. 6.13)"]
---
**Aspect 1: every assignment is to a distinct name.** In three-address code a variable may be assigned many times. In SSA each assignment gives the variable a new subscripted name, so every name is defined exactly once.

| Three-address code | SSA form |
|:--|:--|
| `p = a + b` | `p1 = a + b` |
| `q = p - c` | `q1 = p1 - c` |
| `p = q * d` | `p2 = q1 * d` |
| `p = e - p` | `p3 = e - p2` |
| `q = p + q` | `q2 = p3 + q1` |

Each use refers to exactly one definition (e.g. the `p` in `e - p` is `p2`).

**Aspect 2: $\varphi$-functions combine definitions at join points.** When the same variable is defined on different control-flow paths, a use after the paths join would not know which name to use. SSA inserts a $\varphi$-function:

```text
if (flag) x = -1; else x = 1;        if (flag) x1 = -1; else x2 = 1;
y = x * a;                    =>     x3 = phi(x1, x2);
                                     y1 = x3 * a;
```

$\varphi(x_1, x_2)$ has the value $x_1$ if control arrived through the then-branch and $x_2$ if it came through the else-branch.

These two properties make the definition-use relationships explicit, which simplifies optimisations such as constant propagation and dead-code elimination.
