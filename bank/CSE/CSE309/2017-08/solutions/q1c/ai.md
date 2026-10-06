---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "In semantic analysis (type checking): the type checker must be changed to accept a float as an array index and insert a float-to-int conversion; the lexer and parser already accept such expressions."
sources: ["MMA compiler phases slides 40-98", "Dragon book 2e sec. 1.2.3 (Semantic Analysis, coercions), 6.5.1"]
---
**Answer: the semantic analysis step (type checking).**

Reason, phase by phase:

- **Lexical analysis:** floating-point constants and variables are already tokens (`float`, `id`); nothing changes.
- **Syntax analysis:** the grammar for an array reference is $\textbf{id}\,[\,E\,]$ for any expression $E$, so `a[x]` with a float $x$ is already *syntactically* correct. A parser does not know types.
- **Semantic analysis:** this is the phase that checks that each operator has operands of the right types (Dragon book sec. 1.2.3). The standard rule for array indexing says that the index expression must be of type **integer**, so `a[2.5]` is rejected here. To allow it, Kishor must change the type-checking rule: accept type `float` in the index position and decide how it is turned into an integer (truncate, round, floor) by inserting a **coercion** (type conversion) node, for example $t_1 = \text{float-to-int}\ x$, so that the tree for `a[x]` becomes `a[float-to-int(x)]`.
- **Intermediate and target code generation** then only have to emit the conversion instruction before the address calculation $\text{base} + t_1 \times w$; they need no new rules for indexing.

So the decision "float index allowed, converted this way" belongs in the semantic analyzer (type checker), and the code generators merely carry it out.
