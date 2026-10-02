---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "(i) Compile-time (static/lexical) scope: Function1 always uses the global x = 137 and y = 42, so the three calls print 179, 179, 179. (ii) Run-time (dynamic) scope: a name refers to the most recent active declaration: Function1() prints 137 + 42 = 179; Function2() (local x = 0) calls Function1, which prints 0 + 42 = 42; Function3() (local y = 0) calls Function2 (local x = 0), then Function1 prints 0 + 0 = 0. Output 179, 42, 0."
sources: ["KMS Chapter 7 slides 9-16 (Stack Allocation, Control Stack)", "Dragon book 2e sec. 1.6.3, 1.6.5 (Dynamic Scope), 7.3"]
---
**Assumptions.** `Print` prints its argument followed by a newline. The three calls at the bottom are executed in order, from the global (main) level.

**(i) Names handled at compile time: static (lexical) scope.** A use of a name refers to the declaration found by looking at the program **text**: the innermost enclosing block that declares it. `Function1` declares neither `x` nor `y`, so its `x` and `y` are always the **global** ones, whoever calls it.

| Call | Inside Function1 | Printed |
|:--|:--|:-:|
| `Function1()` | global x = 137, global y = 42 | **179** |
| `Function2()` $\to$ `Function1()` | Function2's local `x = 0` is not visible in Function1 | **179** |
| `Function3()` $\to$ `Function2()` $\to$ `Function1()` | locals of Function3 and Function2 not visible | **179** |

Output: **179, 179, 179**.

**(ii) Names handled at run time: dynamic scope.** A use of a name refers to the **most recent active** declaration of that name, found by searching the activations on the control stack from the top (most recent call) downward.

| Call | Control stack (top first) | x | y | Printed |
|:--|:--|:-:|:-:|:-:|
| `Function1()` | Function1, main (x = 137, y = 42) | 137 | 42 | **179** |
| `Function2()` | Function1, Function2 (x = 0), main | 0 | 42 | **42** |
| `Function3()` | Function1, Function2 (x = 0), Function3 (y = 0), main | 0 | 0 | **0** |

Output: **179, 42, 0**.

The same code gives different results because static scope binds names when the program is compiled, using its structure, while dynamic scope binds them during execution, using the calling sequence.
