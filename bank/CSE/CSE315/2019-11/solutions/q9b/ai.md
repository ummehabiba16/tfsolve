---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "For cache coherency: during an inquire (snoop) cycle another bus master drives an address into the Pentium's A31-A5 (with EADS') so the Pentium can check whether its internal cache holds that line (HIT/HITM') and write it back if modified."
sources: ["Brey, The Intel Microprocessors, Ch. 18 (Pentium pins: A31-A3, EADS', inquire cycles, HIT/HITM')"]
---
The Pentium has an **internal (write-back) cache**. If another bus master (a second processor or a DMA controller) reads or writes main memory, the Pentium must check whether **its cache** holds a copy of that location, otherwise the data could become inconsistent.

To do this it runs an **inquire (snoop) cycle**:

1. The other bus master places the memory address on the bus and asserts **$\overline{EADS}$** (external address strobe).
2. The Pentium's address lines **A31-A5 act as inputs**: the Pentium reads the address from the bus and looks it up in its cache.
3. It reports the result on **$\overline{HIT}$** (line present) and **$\overline{HITM}$** (line present and modified). A modified line is written back to memory first.

So the address bus is normally an **output** (the Pentium addresses memory) but becomes an **input** during inquire cycles. That is why it is **bidirectional**: to keep the internal cache **coherent** with memory in multiprocessor and DMA systems.
