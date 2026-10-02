---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Motivation: separate the source-language-dependent analysis (front end: lexical, syntax, semantic analysis, intermediate code) from the machine-dependent synthesis (back end: optimisation, code generation) via an IR, so front and back ends can be reused/combined (m+n instead of m x n) and each is simpler. Symbol table: the front end creates entries (lexer inserts identifiers, parser/semantic analyser add type, scope, storage size, offset), and the back end reads them (addresses, sizes, types) to generate code."
sources: ["MMA introduction slides 40-98 (The Structure of a Compiler, Symbol-Table Management, Grouping of Phases)", "Dragon book 2e sec. 1.2, 1.2.8"]
---
**The two groups**

- **Front end (analysis):** lexical analysis, syntax analysis, semantic analysis, intermediate-code generation. It depends on the **source language** only. It checks the program, reports errors, and produces an **intermediate representation (IR)** plus the symbol table.
- **Back end (synthesis):** machine-independent and machine-dependent code optimisation, code generation. It depends on the **target machine** only. It reads the IR and the symbol table and produces target code.

**Motivation for the division**

1. **Retargeting and reuse.** With a common IR, one front end can be combined with different back ends (one language on many machines), and different front ends with one back end (many languages on one machine). For $m$ languages and $n$ machines, we need $m + n$ components instead of $m \times n$ compilers (as in GCC and LLVM).
2. **Separation of concerns.** Language issues (syntax, types, scope) and machine issues (registers, instruction selection) are handled separately, so each part is simpler to write, test and maintain.
3. **Machine-independent optimisation** can be done once on the IR, for all targets.
4. **Passes.** Phases within a group can be grouped into a single pass (e.g. the whole front end in one pass), since they are tightly coupled, while the IR is the clean interface between passes.

**Interaction with the symbol table** (a data structure with one record per identifier, accessible to all phases):

```text
   FRONT END                          BACK END
   lexical analyzer   --+        +--  code optimizer
   syntax analyzer    --+        |
   semantic analyzer  --+--------+--  code generator
   IR generator       --+   |
                            v
                       SYMBOL TABLE
```

- **Lexical analyser:** when it finds an identifier, it enters the lexeme in the symbol table (if not already there) and returns `<id, pointer to entry>`.
- **Syntax analyser:** may record the kind of name (variable, function, type) and its scope; declarations are processed in the parser's semantic actions.
- **Semantic analyser:** stores and uses **type** information (type checking, coercions), number and types of procedure arguments, and scope.
- **Intermediate-code generator:** uses types and widths to compute storage layout (relative addresses/offsets) and records them; creates temporaries.
- **Back end (optimiser and code generator):** *reads* the symbol table: types, sizes, offsets and storage class decide addressing modes, register allocation and the instructions emitted (e.g. `LD R1, x` needs `x`'s address).

So the front end mainly **fills** the symbol table and the back end mainly **uses** it. Together with the IR, it is the shared information that connects the two groups.
