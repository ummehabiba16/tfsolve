---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A type system is the set of rules that assigns types to program constructs and checks their use. A strongly typed language guarantees that accepted programs run without type errors (Java, ML); a weakly typed one allows implicit or unchecked conversions (C, JavaScript). Partial ordering of types: the widening relation char <= int <= long <= float <= double, used to find the type of mixed expressions (least upper bound)."
sources: ["KMS Chapter 6 slides 37-51 (type expressions, type equivalence)", "Dragon book 2e sec. 6.3, 6.5.1-6.5.2"]
---
**Type system.** A type system is a collection of **rules that assign types to the constructs of a program** (variables, expressions, functions) and the rules by which these types are checked and combined. It has *type expressions* (int, array, pointer, function types), rules for **type checking** (every operator gets operands of the right type) and often *type inference* (types deduced from use). Checking can be **static** (compile time: C, Java, ML) or **dynamic** (run time: Lisp, Python). A type system catches errors early, documents code and lets the compiler choose operations, sizes and optimisations (Dragon book sec. 6.5).

```c
int x = 3;   float y = 2.5;   x = y + 1;   /* the checker decides the type of y + 1 and the needed conversion */
```

**Strongly typed system.** A language is strongly typed if the compiler can guarantee that **the programs it accepts will execute without type errors**: operations are applied only to values of the correct types, and there are no unchecked unsafe conversions. Examples: Java, ML, Ada (Pascal is nearly strong). In practice some checks may be delayed to run time (array bounds, casts).

**Weakly typed system.** A language that **does not enforce** the type rules strictly: it allows implicit (and often lossy) conversions or unchecked reinterpretation of data (pointers cast to integers, unions, `int` used as `char *`). Examples: C, C++ (casts), assembly; JavaScript's `"5" + 3` gives `"53"`. Type errors can remain undetected until run time, or be silently turned into wrong results.

**Partial ordering of types.** Types of numbers are related by *widening* (conversion without loss of information): $char \preceq short \preceq int \preceq long \preceq float \preceq double$ (Dragon book sec. 6.5.2). The relation $s \preceq t$ ("$s$ can be widened to $t$") is reflexive, transitive and antisymmetric, but it is only a **partial** order: some pairs are not comparable, for example a pointer type and `float`, or two unrelated classes. It is used (1) in coercions: in $x + y$ with types $s$ and $t$, the result has the **least upper bound** $\max(s, t)$ and the smaller operand is converted (`int + float` $\to$ `float`); (2) in object-oriented languages, where the subclass relation is a partial order and a subtype can be used wherever the supertype is expected.

```text
char  <  short  <  int  <  long  <  float  <  double      (widening order)
```
