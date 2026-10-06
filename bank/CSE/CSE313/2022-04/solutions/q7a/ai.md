---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Precise interrupt: PC saved, all earlier instructions complete, no later instruction complete, state of the PC instruction known; its disadvantage is the complex hardware needed on pipelined/superscalar CPUs."
sources: ["Tanenbaum MOS 4e, sec. 5.1.5 (interrupts revisited)"]
---
**Precise interrupt.** An interrupt that leaves the machine in a **well-defined state** at the moment it is taken, so that the OS can later resume the program exactly where it stopped.

**Four properties.**

1. The **program counter (PC) is saved** in a known place.
2. **All instructions before** the one pointed to by the PC have **completely executed**.
3. **No instruction after** the one pointed to by the PC has executed.
4. The **execution state of the instruction pointed to by the PC is known** (it may or may not have started, but we know which).

**Disadvantages.** In a pipelined or superscalar CPU, instructions are issued and finish out of order, so making the interrupt precise requires a lot of extra hardware: buffers/registers to hold results of instructions that have finished early but must not be committed yet, and logic to undo or delay them (e.g. a reorder buffer). This makes the CPU design **complex and large and uses silicon area** and can slow interrupt entry. Machines with imprecise interrupts avoid this, but then the OS must deal with a large, machine-dependent state dump, which makes the OS code slower and more complicated.
