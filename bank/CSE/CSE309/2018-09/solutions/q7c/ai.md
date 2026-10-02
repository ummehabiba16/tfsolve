---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Assuming doSomething() is called on a Derived object (and the classes are in their own files), the output is 4, 2, 3, 6: inside Derived, publicBaseInt finds Derived's own field (4), which hides Base's (1); baseInt is found in the superclass Base (2); derivedInt is Derived's field (3); after the local declaration int publicBaseInt = 6, the local hides the field, giving 6. Justified with chained symbol tables: method scope -> Derived class table -> Base class table, searched innermost first."
sources: ["MMA introduction slides 87-89 (Symbol-Table Management)", "Dragon book 2e sec. 1.6.3, 2.7.1 (Symbol Table Per Scope), 6.3.6"]
---
**Assumptions.** `doSomething()` is called on an object of class `Derived` (e.g. `new Derived().doSomething();`). The two public classes are in separate files, as Java requires.

**Output:**

```text
4
2
3
6
```

**Justification with chained symbol tables (one table per scope).** Each scope has its own symbol table, linked to the table of the enclosing scope. A name is looked up in the **innermost** table first; if it is not found, the search continues outward along the chain. For a class, the enclosing table is that of its superclass.

```text
 method doSomething (local scope)      { publicBaseInt -> local, value 6 }   (only after its declaration)
          |
          v
 class Derived                          { derivedInt -> 3, publicBaseInt -> 4 }
          |
          v
 class Base (superclass)                { publicBaseInt -> 1, baseInt -> 2 }
```

| Statement | Lookup | Found in | Printed |
|:--|:--|:--|:-:|
| `println(publicBaseInt)` | the local scope has no such name yet | `Derived`'s table: its own field **hides** `Base.publicBaseInt` | **4** |
| `println(baseInt)` | not local, not in `Derived` | `Base`'s table (inherited, `protected` is accessible in a subclass) | **2** |
| `println(derivedInt)` | not local | `Derived`'s table | **3** |
| `int publicBaseInt = 6;` | enters `publicBaseInt` in the method's local table | | |
| `println(publicBaseInt)` | now found in the **local** table, which shadows the field | local scope | **6** |

The base-class field `Base.publicBaseInt = 1` is never printed. It is hidden first by `Derived`'s field and then also by the local variable. (It could be reached with `super.publicBaseInt`.)
