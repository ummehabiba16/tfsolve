---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A program is a passive file; a process is a running instance of a program with its own state; the loader creates the process (PCB, address space, PC at entry point) and makes it ready."
sources: ["Tanenbaum MOS 4e, sec. 2.1.1 (the process model)"]
---
**Difference.**

| Program | Process |
|:--|:--|
| a **passive** entity: an executable file (code + initial data) on disk | an **active** entity: a program in execution |
| no state | has a program counter, registers, stack, heap, open files, state (ready/running/blocked), a PCB |
| one copy on disk | one program can give rise to **several processes** (e.g. two users running the editor) |

(The "baking a cake" analogy: the recipe is the program, the activity of baking is the process.)

**How a program becomes a process.** When the user starts it (`fork` + `exec`, or a double click), the OS: (1) allocates a **PCB** and a process id; (2) creates an **address space** and loads the code and initialised data from the executable file (usually lazily by paging), allocating the stack and heap; (3) sets the **program counter** to the entry point and initialises the registers and the stack pointer; (4) opens the standard files; (5) puts the process in the **ready queue**; the scheduler then dispatches it.
