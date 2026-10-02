---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Machine language is the binary instruction set of a specific CPU, executed directly by hardware and not portable; bytecode is a compact, machine-independent instruction set for a virtual machine (e.g. JVM), executed by an interpreter or JIT compiler, portable but needing the VM and slower unless JIT-compiled."
sources: ["MMA introduction slides 4-13 (Language Processors, hybrid compiler)", "Dragon book 2e sec. 1.1 (Fig. 1.4)"]
---
| | Bytecode | Machine language |
|:--|:--|:--|
| Target | A virtual machine (e.g. JVM, .NET CLR, Python VM) | A real CPU (x86, ARM, ...) |
| Executed by | An interpreter or JIT compiler inside the VM | The hardware directly |
| Portability | Machine-independent: "compile once, run anywhere" | Tied to one instruction set and OS |
| Level | Higher: stack-based instructions, typed operations, symbolic references to classes and methods | Lowest: registers, memory addresses, binary opcodes |
| Speed | Slower if interpreted; close to native after JIT | Fastest: no translation at run time |
| Safety | Can be verified by the VM before execution | No such checks |

Java's hybrid compiler (textbook Fig. 1.4) shows the role of bytecode: `javac` compiles source to bytecode, which the JVM interprets or JIT-compiles to machine language on the target computer.
