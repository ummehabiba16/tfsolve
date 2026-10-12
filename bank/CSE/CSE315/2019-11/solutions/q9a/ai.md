---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Hyper-Threading (Pentium 4): one physical core keeps two architectural states (registers, IP, APIC), so the OS sees two logical processors; both threads share the caches, decoders and execution units, and when one thread stalls the other uses the idle units, raising throughput (~15-30%)."
sources: ["Brey, The Intel Microprocessors, Ch. 19 (Pentium 4 hyper-threading technology)"]
changes:
  - "2026-10-12: replaced the ASCII sketch by a TikZ figure, with a strip showing how thread B fills A's stall cycles (answer unchanged)"
---
**Hyper-Threading (HT)**, introduced with the Pentium 4, makes **one physical processor core appear as two logical processors** to the operating system.

- The core holds **two copies of the architectural state**: general registers, segment and control registers, instruction pointer, flags and local APIC. Each copy runs one thread.
- Both threads **share** the expensive parts: caches, instruction decoders, out-of-order engine and **execution units** (ALUs, FPU, load/store).
- In one clock, micro-operations from **both** threads can be issued to the shared execution units. When one thread stalls (cache miss, branch misprediction, dependency), the other thread keeps the units busy.

![One core without and with Hyper-Threading](figures/ht.png)

Benefit: better use of the execution resources and higher throughput for multithreaded programs (about 15-30%) for only about 5% more chip area. It is not as fast as two real cores, because the threads compete for the same units.
