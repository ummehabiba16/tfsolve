---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "The 6-byte queue lets the BIU prefetch the next instruction bytes while the EU executes the current instruction, so fetch and execution overlap (2-stage pipeline): the EU rarely waits for memory, the bus is used when otherwise idle, and throughput rises. It is flushed on jumps, calls and interrupts."
sources: ["MHE 8086-Architecture slides (pre-fetches up to 6 bytes, EU/BIU)"]
---
The 8086 BIU has a **6-byte FIFO instruction queue**. Whenever at least 2 bytes are free and the EU does not need the bus, the BIU **prefetches** the next instruction bytes into it.

**Advantages**

1. **Overlap of fetch and execute (pipelining):** while the EU executes one instruction, the BIU is already fetching the following ones. The EU usually finds the next instruction waiting in the queue, so it does not wait for memory.
2. **Better bus use:** the bus is used during clocks when the EU is busy with internal work (e.g. MUL, DIV), instead of staying idle.
3. **Higher speed:** more instructions are completed per unit time without a faster clock or memory.

The queue is emptied (flushed) when a jump, call, return or interrupt changes CS:IP, because the prefetched bytes are then not needed.
