---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Per process: address space, global variables, open files, signals; per thread: program counter, stack, registers, local variables; none of the listed items is neither."
sources: ["Tanenbaum MOS 4e, sec. 2.2.1 (fig. 2-12: per-process and per-thread items)"]
---
Threads of one process share the process's resources, but each thread has its own execution state:

| Item | Per process | Per thread | Neither |
|:--|:-:|:-:|:-:|
| Program counter | | **yes** | |
| Stack | | **yes** | |
| Address space | **yes** | | |
| Global variables | **yes** | | |
| Registers | | **yes** | |
| Open files | **yes** | | |
| Signals (handlers) | **yes** | | |
| Local variables | | **yes** (they live on the thread's stack) | |

**Per-process items:** address space, global variables, open files, signal handlers. **Per-thread items:** program counter, registers, stack (and so the local variables) and the thread's state. **No item of the list is "neither"**: every one of them belongs to either the process or the thread. (Pending signals can also be per thread in some systems, but the handlers are per process.)
