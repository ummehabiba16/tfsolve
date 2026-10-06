---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) A Java compiler (javac) translates source into bytecode (compilation) and the JVM then interprets the bytecode, with a JIT compiler turning hot code into machine code: a hybrid. (ii) The front end analyses the source and produces IR; the IR is language and machine independent; the back end turns IR into target code and knows only the machine."
sources: ["MMA introduction slides 4-13 and 40-98", "Dragon book 2e sec. 1.1, 1.2"]
---
**(i) "Java language processors combine compilation and interpretation."**

A Java source program is first **compiled** by `javac` into **bytecode** (an intermediate, machine-independent form stored in `.class` files). The bytecode is then **interpreted** by the Java Virtual Machine, which executes it instruction by instruction on the actual machine (Dragon book sec. 1.1, hybrid compiler). To make execution fast, a **just-in-time (JIT) compiler** translates the bytecode of frequently executed methods into machine code just before it is run.

So translation is done in two steps: compilation (source $\to$ bytecode) and interpretation or JIT compilation (bytecode $\to$ results). Advantages: bytecode can be carried to and run on any machine that has a JVM (portability), and the compile step catches many errors early; the price is slower execution than native code.

**(ii) Front end, intermediate representation and back end.**

A compiler has a **front end** (analysis) and a **back end** (synthesis) with an intermediate representation between them (Dragon book sec. 1.2):

- The **front end** (lexical, syntax, semantic analysis, intermediate-code generation) depends on the **source language**: it knows its tokens, grammar and type rules, and produces the intermediate representation. It is independent of the target machine.
- The **back end** (code optimization and code generation) depends on the **target machine**: it knows registers, instructions, addressing modes, and turns the IR into target code. It is independent of the source language.
- The **intermediate representation** (IR), for example three-address code, is neither about the source language (no source syntax, only operations, temporaries and jumps) nor about the target machine (no registers or machine instructions). Therefore $n$ front ends and $m$ back ends give $n \times m$ compilers, and machine-independent optimization is written once, on the IR.
