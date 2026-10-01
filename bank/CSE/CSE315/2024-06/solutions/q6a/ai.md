---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Pre-fetching: fetching the next instruction bytes before they are needed; pipelining: overlapping fetch and execute of different instructions. In the 8086 the BIU fills a 6-byte queue while the EU executes."
sources: ["MHE 8086-Architecture slides 3-10 (instruction cycle, EU/BIU, 6-byte pre-fetch)", "MHE 80286 slides 9-11 (prefetcher, 6-byte queue)"]
---
**Pre-fetching** means reading the next instruction bytes from memory **before** they are needed and keeping them in an on-chip **queue**, so that when the current instruction finishes, the next one is already inside the processor.

**Pipelining** means splitting instruction processing into stages (fetch, decode, execute) handled by separate units, so that **different instructions are in different stages at the same time**. While one instruction is executed, the next is being fetched or decoded. Throughput increases even though each instruction still takes the same time.

**Pre-fetching in the 8086.** The 8086 is divided into two independent units:

- **BIU (Bus Interface Unit):** does the fetching. Whenever the bus is free and the queue has room (at least 2 bytes empty), it reads the next bytes of code from $CS\times10H + IP$ and puts them in a **6-byte FIFO instruction queue**.
- **EU (Execution Unit):** takes instruction bytes from the front of the queue, decodes and executes them, and uses the BIU only for memory operands.

So fetching (BIU) overlaps with execution (EU): a 2-stage pipeline. When a jump, call or interrupt changes CS:IP, the queue is **flushed** and filling restarts from the new address.
