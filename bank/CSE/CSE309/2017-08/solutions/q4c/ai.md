---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) First kind of manager = compiler (whole plan translated into instructions first, then executed); second kind = interpreter (execute step by step). (ii) C is compiled to native code; Python is compiled to bytecode and interpreted; Java is compiled to bytecode and run by the JVM (interpretation plus JIT). (iii) Compiled code is faster; an interpreter gives better, statement-level error diagnostics."
sources: ["MMA introduction slides 4-13 (Compilers, interpreters, hybrid)", "Dragon book 2e sec. 1.1, Fig. 1.1-1.4"]
---
**(i) Similarities.**

| Event company | Language processor |
|:--|:--|
| The client's plan | Source program |
| The manager (translates the plan into things employees can do) | The translator: compiler or interpreter |
| The employees who do the job | The machine (CPU) that executes the instructions |
| **First kind:** hears the *whole* plan, discusses, gives *all* instructions, then assures the event happens | **Compiler:** reads the *whole* source program, translates it to a target program (machine code); the target program is then run, producing the output |
| **Second kind:** takes the plan *step by step*, checks if the step is possible and gets it done before the next step | **Interpreter:** reads one statement at a time and executes it immediately; no target program is produced |

Both kinds of manager (translator) must understand the client's wish and check that it is possible; a compiler checks the whole program for feasibility (syntax, semantic errors) before running, an interpreter checks and runs each step. In both cases the employees (machine) finally do the work.

**(ii) Compilation and running of C, Python and Java** (Dragon book sec. 1.1):

| | Translation | Execution |
|:--|:--|:--|
| **C** | Preprocessor, then the compiler translates the whole program to assembly, assembler to relocatable machine code, linker/loader build the executable. A pure **compiler**. | The native executable runs directly on the CPU (fast, platform specific). |
| **Python** | The source is compiled implicitly to **bytecode** (`.pyc`) when run; there is no separate user-visible compile step. | The bytecode is executed by the Python virtual machine, i.e. **interpreted**. |
| **Java** | `javac` compiles the source to platform-independent **bytecode** (`.class`). | The **JVM** interprets the bytecode and a just-in-time compiler turns frequently used code into native code at run time: a **hybrid** compiler. |

**(iii) Compiler versus interpreter.**

| | Compiler | Interpreter |
|:--|:--|:--|
| **Performance** | Translation is done once; the target program runs directly on the machine and can be optimized, so execution is **much faster**. | Every statement is analysed again each time it is executed (e.g. in loops), so execution is **slower**. |
| **Error diagnostics** | Reports many syntax/semantic errors together before any run, but run-time errors refer to machine code unless debug information is kept. | Executes statement by statement, so it points to the **exact source statement** where the error occurred and stops there, which is easier to debug. |
