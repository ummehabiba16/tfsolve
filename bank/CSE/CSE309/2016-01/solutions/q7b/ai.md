---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Name equivalence: two types are equal only if they have the same name; structural equivalence: they are equal if they have the same structure (same constructors applied to equivalent components). type A = array[10] of int and type B = array[10] of int are structurally but not name equivalent."
sources: ["KMS Chapter 6 slides 37-51 (type expressions, type equivalence)", "Dragon book 2e sec. 6.3.2, 6.5.1"]
---
Type checking has to decide when two type expressions are *the same type* (Dragon book sec. 6.3.2, 6.5.1).

**Structural equivalence.** Two types are equivalent if they have the **same structure**: they are built from the same basic types by the same type constructors, recursively (the same array size, the same element types, the same fields in the same order, ...), irrespective of the names given to them.

**Name equivalence.** Names are treated as distinct types: two types are equivalent only if they have the **same name** (or are the same type expression written once). Two separately named types with identical structure are *different*.

**Example (Pascal-like).**

```text
type A = array [1..10] of integer;
type B = array [1..10] of integer;
var  x : A;
var  y : B;
```

- **Structural equivalence:** `A` and `B` have the same structure, so `x := y` is allowed.
- **Name equivalence:** `A` and `B` are different names, so `x := y` is a type error.

**Example (C-like).**

```c
struct P { int a; int b; };
struct Q { int a; int b; };
struct P p;  struct Q q;
p = q;       /* error in C: P and Q are distinct types although they have the same structure */
```

C uses name equivalence for `struct`s (and `typedef` only introduces another name for the same type), but structural equivalence for arrays and pointers (`int a[10]` and `int b[10]` have equivalent types).

| | Structural | Name |
|:--|:--|:--|
| Basis | structure of the type expression | the names |
| Recursive types | needs a test that avoids infinite loops (cyclic graphs) | trivial |
| Flexibility | more permissive | stricter, safer |
| Cost | tree/graph comparison | name comparison |

For recursive types (e.g. a list node pointing to itself) structural equivalence is tested on the **cyclic type graph**, assuming equal while the same pair of nodes is being compared, which is why it is harder to implement than name equivalence.
