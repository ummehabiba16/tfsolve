---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A type system is the set of rules that assign types to the constructs of a program and check their consistent use. A strongly typed language is one whose compiler guarantees that the accepted programs run without type errors."
sources: ["KMS Chapter 6 slides 37-51", "Dragon book 2e sec. 6.3, 6.5"]
---
**Type system.** A type system is a collection of **rules that assign types to the parts of a program** (variables, expressions, functions, statements) and the rules for checking that they are used consistently: type expressions to describe types (basic types, arrays, records, pointers, functions), rules for **type checking** (for example, `+` requires operands of numeric types, an array index must be an integer, a function call must pass arguments of the declared types), type conversion (coercion) rules, and often type inference (Dragon book sec. 6.5). Its purposes are to catch errors early, to let the compiler choose operations, sizes and representations, and to document the program. Checking can be **static** (at compile time: C, Java, ML) or **dynamic** (at run time: Lisp, Python).

**Strongly typed language.** A language is *strongly typed* if its compiler can **guarantee that the programs it accepts will run without type errors**: every operation is applied only to operands of the type it expects, and there are no unchecked unsafe conversions (Dragon book sec. 6.5). Examples: Java, ML, Ada. Some checks (array bounds, down-casts) may still be done at run time. A language such as C, which allows unchecked casts between pointers and integers, unions and implicit conversions, is **weakly typed**.
