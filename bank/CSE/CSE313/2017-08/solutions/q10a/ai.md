---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Exposing physical memory gives no protection, no relocation, no more processes than fit, fragmentation and hardware-dependent programs."
sources: ["Tanenbaum MOS 4e, sec. 3.1 (no memory abstraction; address spaces)"]
---
If processes use **physical addresses directly** (no memory abstraction):

1. **No protection:** any process can read or overwrite the memory of **other processes or the operating system** (a bug can crash the whole machine), and one process can steal data of another.
2. **No relocation:** a program must be linked for specific physical addresses; two programs compiled for the same addresses cannot be loaded together (they clash), and a program cannot be moved.
3. **Limited multiprogramming:** all programs must fit in physical memory at once; a program cannot be larger than the installed RAM.
4. **Fragmentation and management:** memory is allocated in contiguous chunks, so holes appear; there is no way to extend a process's memory transparently.
5. **Hardware dependence:** programs are tied to the memory size and layout of the machine, which makes them non-portable.

The solution is an **address-space abstraction** (virtual addresses translated by an MMU).
