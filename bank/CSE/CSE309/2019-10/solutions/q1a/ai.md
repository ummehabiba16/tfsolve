---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A compiler translates the whole program into the target machine language of a real CPU, so the result runs directly on the hardware; code in a language for a virtual machine (e.g. Java bytecode, Python byte code) or source code given to an interpreter is not native machine code and needs an interpreter (VM) to execute it statement by statement."
sources: ["MMA introduction slides 4-13 (Language Processors)", "Dragon book 2e sec. 1.1"]
changes:
  - "2026-10-06: added TikZ figure (figures/modes.png) comparing a compiler, an interpreter and a hybrid translator; the answer itself is unchanged."
---
- A **compiler** translates the whole source program into an equivalent **target program**. When the target is the **machine language** of the computer, the CPU can execute it directly: the user just runs the target program on its input.
- An **interpreter** does not produce a target program. It executes the operations of the source program (or an intermediate code) directly on the input, statement by statement.
- Some compilers produce code for a **virtual machine** rather than a real one. Java's `javac` produces bytecode, which no CPU executes natively. It needs an interpreter (the JVM, possibly with a JIT compiler) to run it. Scripting languages (Python, shell scripts) are likewise executed by an interpreter.

So whether code runs directly depends on whether it is the machine language of the real processor (direct execution) or a source/intermediate form that only an interpreter or virtual machine understands. Machine code is faster; interpreted code is more portable and gives better error diagnostics.

![Compiler, interpreter and hybrid translator](figures/modes.png)
