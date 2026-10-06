---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The Java compiler (javac) translates the program to platform-independent bytecode; the Java virtual machine then interprets the bytecode, and a just-in-time (JIT) compiler translates frequently executed bytecode to native machine code at run time, just before it is executed, to speed up execution."
sources: ["MMA introduction slides 4-13 (hybrid compilers, bytecode)", "Dragon book 2e sec. 1.1 (Fig. 1.4)"]
---
**How the Java language processor works** (a *hybrid* compiler, Dragon book sec. 1.1):

1. The source program (`.java`) is translated by the compiler `javac` into **bytecode** (`.class` files), a compact, platform-independent intermediate language. This step does lexical, syntax and semantic analysis, so most errors are found here.
2. The bytecode is loaded by the **Java virtual machine** (JVM), which can run on any machine (portability: "write once, run anywhere"). The loader brings in the classes needed, the verifier checks the bytecode for safety.
3. The JVM executes the bytecode: it **interprets** it, one bytecode instruction at a time, and with the help of a JIT compiler, executes hot code as machine code.
4. The input of the program is processed during this execution, and the output is produced.

```text
source (.java) --javac--> bytecode (.class) --JVM (interpreter + JIT)--> output
                                               ^ input
```

**Just-in-time (JIT) compiler.** A JIT compiler translates the bytecode into **native machine code at run time**, just before the code is executed for the first time (or when a method has been executed many times: *hot spots*). The native code is kept in memory and reused for later calls, so frequently executed code runs at the speed of compiled code, while the rest of the program is simply interpreted; this removes much of the penalty of interpretation, and the JIT can optimise using run-time information.
