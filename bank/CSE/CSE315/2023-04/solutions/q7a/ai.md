---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Pre-fetching: fetching the next instruction bytes before they are needed; pipelining: overlapping the fetch/decode/execute of different instructions. In the 8086 the BIU fetches code from CS:IP into a 6-byte queue whenever 2 bytes are free and the bus is idle, while the EU executes from the queue; jumps flush the queue."
sources: ["MHE 8086-Architecture slides 3-10 (instruction cycle, EU/BIU, 6-byte pre-fetch)", "Brey, The Intel Microprocessors, Sec. 2-1; Hall, Microprocessors and Interfacing, Ch. 2 (BIU queue)"]
---
**Pre-fetching** means reading the next instruction bytes from memory **before** they are needed and keeping them in an on-chip **queue**. When the current instruction finishes, the next one is already inside the processor, so the CPU does not wait for memory.

**Pipelining** means splitting instruction processing into stages (fetch, decode, execute) handled by separate hardware, so that **different instructions are in different stages at the same time**. While one instruction executes, the next is being fetched. Each instruction still takes the same time, but more instructions finish per unit time (higher throughput).

```text
Without pipelining:  F1 E1 F2 E2 F3 E3
With pipelining:     F1 F2 F3 F4          (BIU)
                        E1 E2 E3 E4       (EU)
```

**Pre-fetching in the 8086**

The 8086 is split into two units that work in parallel:

- **BIU (Bus Interface Unit):** does all bus operations. It computes the code address $CS \times 10H + IP$, fetches instruction bytes (a word at a time on the 16-bit bus) and puts them into a **6-byte FIFO instruction queue**. It fetches whenever **at least 2 bytes of the queue are empty** and the EU does not need the bus.
- **EU (Execution Unit):** takes bytes from the front of the queue, decodes and executes them. It uses the BIU only when an instruction needs a memory or I/O operand.

So fetching by the BIU overlaps execution by the EU: a simple 2-stage pipeline. Most of the time the EU finds the next instruction already in the queue.

When a **jump, call, return or interrupt** changes CS:IP, the bytes in the queue are the wrong ones. The queue is **flushed** and the BIU starts fetching from the new address, so the EU waits briefly.
