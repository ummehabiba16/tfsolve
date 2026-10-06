---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Semantic errors: (1) use of an undeclared identifier; (2) multiple declaration of a name in the same scope; (3) type mismatch of operands or in an assignment; (4) wrong number or types of arguments in a function call; (5) non-integer array index, return type mismatch, or break/continue outside a loop."
sources: ["MMA introduction slides 40-98 (semantic analysis)", "Dragon book 2e sec. 1.2.3, 4.1.1, 6.5.1"]
---
The semantic analyzer checks the program against the language definition, using the symbol table and the types of the expressions (Dragon book sec. 1.2.3). Five semantic errors it is expected to recognise:

1. **Undeclared identifier:** a variable or function is used without a declaration (`x = y + 1;` where `y` was never declared).
2. **Multiple declaration:** the same name declared twice in the same scope (`int a; float a;`).
3. **Type mismatch:** an operator applied to operands of incompatible types, or an assignment with incompatible types (adding an integer and a string; assigning a `float` array to an `int` variable); also a non-boolean condition in `if`/`while`.
4. **Wrong function call:** the number or types of the actual arguments do not match the declaration (`f(1, 2)` for `int f(int)`), or a non-function is called.
5. **Misuse of other constructs:** an array index that is not an integer, a `return` whose type does not match the function's, a missing `return` in a non-void function, a `break` or `continue` outside a loop, assignment to a constant, or use of a variable before it is initialised (flow-based check).
