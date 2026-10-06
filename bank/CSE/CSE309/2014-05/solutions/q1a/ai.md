---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A compiler translates the whole source program into a target program (compilation only) which is then run on the input; an interpreter executes the source directly, statement by statement, with no translation to a target program (interpretation only); a hybrid compiler (Java) first compiles the source to bytecode and then interprets the bytecode with a virtual machine, so it involves both."
sources: ["MMA introduction slides 4-13 (compilers, interpreters, hybrid)", "Dragon book 2e sec. 1.1, Fig. 1.3-1.5"]
---
**Compiler.** A compiler reads the *whole* source program and translates it into an equivalent **target program** (machine code). Only **compilation** takes place; the translation stops before the program runs. The target program is then run separately, directly on the machine, on the input to produce the output (Dragon book sec. 1.1). Example: a C program compiled by `gcc` into `a.out`.

**Interpreter.** An interpreter does **not produce a target program**. It takes the source program and the input together, and *directly executes* the operations given in the source, statement by statement. Only **interpretation** takes place, no compilation. Example: a simple BASIC or shell interpreter.

**Hybrid compiler.** It uses **both**: the source program is first **compiled** into an intermediate program (for Java, **bytecode**), and the intermediate program is then **interpreted** by a virtual machine (which may use a just-in-time compiler). Example: Java, with `javac` and the JVM.

![Compiler, interpreter and hybrid compiler](figures/modes.png)

| | Compilation? | Interpretation? | Result of translation |
|:--|:-:|:-:|:--|
| Compiler | yes | no | target program (machine code) |
| Interpreter | no | yes | none; output directly |
| Hybrid compiler | yes (to bytecode) | yes (of bytecode) | intermediate program (bytecode) |

This shows why the statement is true: the compiler *only* translates, the interpreter *only* interprets, and the hybrid does both in sequence.
