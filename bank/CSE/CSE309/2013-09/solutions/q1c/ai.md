---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A compiler translates the whole program into a target program before execution, an interpreter executes the source statement by statement without producing a target program. The compiler is suitable for performance: translation is done once and the machine code runs directly, while an interpreter re-analyses each statement every time it executes it."
sources: ["MMA introduction slides 4-13 (compilers, interpreters)", "Dragon book 2e sec. 1.1"]
---
**Difference** (Dragon book sec. 1.1):

| | Compiler | Interpreter |
|:--|:--|:--|
| Translation | translates the **whole** source program into a target program (machine code) **before** execution | executes the source **statement by statement**; **no** target program is produced |
| Output of translation | an executable file, which can be run many times without the source | none: the source (and the interpreter) is needed at every run |
| Error reporting | reports many syntax/semantic errors for the whole program before it runs | reports an error when the offending statement is reached, with the exact source position |
| Memory | extra memory for the target program | the interpreter and source stay in memory |
| Examples | C, C++ (gcc) | early BASIC, shell, Python (in its simple form) |

**Which one is suitable for performance? The compiler.** Reasons:

1. The translation (lexical, syntax and semantic analysis) is performed **once**; running the target program does not repeat it. An interpreter has to analyse a statement again each time it is executed, for example every iteration of a loop.
2. The target program is **machine code that runs directly on the hardware**, whereas an interpreter adds a layer of software between the program and the machine.
3. The compiler can apply **optimizations** (common-subexpression elimination, register allocation, loop optimizations) using knowledge of the whole program.

An interpreter is typically an order of magnitude slower; its advantages are quick start (no compile step), easier debugging and portability.
