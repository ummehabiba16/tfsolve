---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A type checker checks that operands of operators have compatible types, that assignments, function calls (argument number and types) and array indexes (integer) are type correct, and inserts coercions. Errors recognised: type mismatch, incompatible operands, wrong argument count or types, non-integer index, illegal use of a non-function or a non-pointer, undeclared names, return type mismatch."
sources: ["KMS Chapter 6 slides 37-51", "Dragon book 2e sec. 6.5.1-6.5.3"]
---
**Tasks of a type checker** (Dragon book sec. 6.5.1-6.5.3). Three typical examples:

1. **Checking the operands of operators and expressions.** Each operator has types of operands it accepts: `+`, `*` take numbers, `&&` takes booleans, `*p` needs a pointer. The checker computes the type of every sub-expression and checks that it fits, e.g. `a + b` with `a` an `int` and `b` a `float` has type `float`.
2. **Checking assignments and statements.** The type of the right side must be compatible with the type of the variable on the left; the condition of an `if` or `while` must be boolean; a `return` expression must match the declared return type.
3. **Type conversion (coercion) and function calls.** Where the language allows it, the checker inserts an implicit conversion (e.g. int-to-float) into the tree. For a call $f(e_1, \ldots, e_n)$ it checks that $f$ is a function, that the number of arguments is $n$, and that each $e_i$ has the type of the $i$-th parameter. For an array reference $a[i]$ it checks that $a$ is an array and $i$ is an integer.

**Types of errors recognised by a type checker:**

- **Type mismatch:** incompatible operand types (adding a string and an integer), incompatible assignment.
- **Wrong argument list:** wrong number or types of arguments in a call; calling something that is not a function.
- **Illegal operation:** a non-integer array index, dereferencing a non-pointer, using a non-boolean as a condition.
- **Return type mismatch** and missing return value.
- **Undeclared or redeclared names** (found with the help of the symbol table).
