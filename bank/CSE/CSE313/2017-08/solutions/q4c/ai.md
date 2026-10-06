---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Yes: interrupts nest; the kernel pushes a new context layer and uses priorities so that a higher-priority interrupt can interrupt a lower one's handler, and the interrupted handler resumes afterwards."
sources: ["Bach, ch. 6 (context layers, interrupts) and ch. 6.5 (interrupt priority levels)"]
---
**Yes, it is possible** (nested interrupts), provided the second interrupt has a **higher priority** than the one being serviced (or the kernel has not blocked it).

**Context of a process.** The *system-level context* of a process is a stack of **context layers**. Each time an interrupt, system call or context switch occurs, the kernel **pushes a layer** (saves the registers and the program counter on the kernel stack) and later **pops it** to resume where it stopped.

- A process running in user mode (the user-level context) receives interrupt A: the kernel pushes layer 1 (the saved user registers) and runs handler A.
- While handler A runs, a **higher-priority interrupt B** arrives: the kernel pushes **layer 2** (the state of handler A) and runs handler B in the same process's kernel stack.
- When B finishes, the layer is popped and handler A **continues**; when A finishes, layer 1 is popped and the user program resumes.

**Control.** The kernel sets the **processor execution level**: while a handler of priority $p$ runs, interrupts of priority $\le p$ are blocked; during critical regions (e.g. manipulating the buffer free list, `wakeup`) the kernel raises the level to block interrupts completely, to avoid corrupting kernel data. Handlers are kept short so that nesting is shallow.
