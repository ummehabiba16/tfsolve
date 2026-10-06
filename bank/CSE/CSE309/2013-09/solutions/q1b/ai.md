---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The symbol table is the data structure that stores, for every identifier of the program, its attributes (type, scope, storage, etc.). It is created and filled by lexical/syntax/semantic analysis and read by semantic analysis, intermediate-code generation, optimization and code generation, which is why every phase uses it; it is managed with insert and lookup operations, usually a hash table per scope."
sources: ["MMA compiler phases slides 40-98 (symbol table)", "Dragon book 2e sec. 1.2.7, 2.7"]
---
**Symbol table.** The symbol table is a data structure that holds a record for each **identifier** (variable, function, type, constant) of the source program together with its **attributes**: name (lexeme), type, scope/nesting level, storage class, size, offset or address, number and types of parameters (for functions), line of declaration, and so on (Dragon book sec. 1.2.7, 2.7). It must allow the compiler to find the record quickly and to store or retrieve information about an identifier.

**Phases that use it.**

| Phase | Use of the symbol table |
|:--|:--|
| Lexical analysis | enters a new identifier lexeme (and tests whether a lexeme is a keyword); the token's attribute points to the entry |
| Syntax analysis | enters declarations (names and categories); may recover from errors |
| Semantic analysis | looks up types and scopes: checks declaration before use, type checking, argument checking, fills in types |
| Intermediate-code generation | looks up types and widths, assigns offsets and temporaries |
| Code optimization | uses attribute information (e.g. liveness, aliasing) |
| Code generation | reads storage locations, offsets and addresses to produce machine code |

So the symbol table is used by (almost) **all phases**, mainly lexical analysis through code generation.

**Symbol-table management.**

1. **Operations:** `insert(name, attributes)` when a declaration is processed; `lookup(name)` for each use, returning the entry or "not found" (an undeclared identifier error); operations to **open and close scopes** (`enterScope`, `exitScope`).
2. **Data structure:** a **hash table** (average constant time for lookup and insert; separate chaining for collisions) is the usual choice; the names are stored in a separate string area, and an entry holds a pointer to the name and the attributes. Alternatives are linear lists (simple, slow) and binary search trees.
3. **Scopes:** blocks and procedures can redeclare names. Either keep **one table per scope**, with each table linked to the table of the enclosing scope (a chain searched from the innermost scope outwards), or use one table and a stack that records the old entries and removes them when a scope ends, so an inner declaration hides an outer one.
4. **Information is added in stages:** the lexer creates the entry for the lexeme, the declaration processing fills in the type and storage, and later phases add more attributes. The table must be able to grow dynamically.
