---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "In SSA every variable is assigned exactly once; where control-flow paths with different definitions of a variable meet, a phi-function x3 = phi(x1, x2) selects the value of the argument corresponding to the path by which control arrived, so the single-assignment property is kept. Example: if (flag) x = -1; else x = 1; y = x \\* a; becomes if (flag) x1 = -1; else x2 = 1; x3 = phi(x1, x2); y = x3 \\* a."
sources: ["KMS Chapter 6 slides 35-36 (Static Single Assignment Form)", "Dragon book 2e sec. 6.2.4"]
---
**SSA form** has two properties: (1) every assignment is to a variable with a **distinct name** (each variable is defined exactly once in the program text), and (2) when the same variable is defined on different control-flow paths, the definitions are combined with a **$\varphi$-function**.

**Use of the $\varphi$-function.** At a join point in the flow graph, a variable may have been given different SSA names on the different incoming paths. A later use must refer to *one* name. So a new name is defined at the join point:

$$x_3 = \varphi(x_1, x_2)$$

$\varphi$ returns the value of its argument that corresponds to the path by which control reached the join: $x_1$ if control came along the first path, $x_2$ along the second. This keeps the single-assignment property, and every use has exactly one reaching definition, which simplifies data-flow analysis and optimisation (constant propagation, dead-code elimination, register allocation).

**Example** (textbook):

```c
if (flag) x = -1; else x = 1;
y = x * a;
```

In SSA form:

```text
    if (flag) x1 = -1; else x2 = 1;
    x3 = phi(x1, x2);
    y  = x3 * a;
```

If `flag` is true, $x_3 = x_1 = -1$; otherwise $x_3 = x_2 = 1$.

$\varphi$ also appears at loop headers, e.g. `i2 = phi(i1, i3)` merges the initial value with the value from the previous iteration. It is not a real machine instruction. Before code generation, it is removed by inserting copies (`x3 = x1` at the end of one predecessor, `x3 = x2` in the other).
