---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "80386 = CPU (execution unit: control, data unit with ALU/registers/barrel shifter, protection test unit; instruction unit: prefetcher with 16-byte code queue and decoder with 3-instruction decoded queue), MMU (segmentation unit: descriptor caches, limit/rights checks, linear address; paging unit: page directory/tables, 32-entry TLB, physical address), and BIU (address drivers, pipelined bus control, BE0-BE3, data transceivers, request prioritizer)."
sources: ["MHE 80386-updated slides 5-7 (architecture: CPU with EU and IU, MMU with SU and PU, BIU; 15/16-byte queue, 3 decoded instructions)", "Brey, The Intel Microprocessors, Ch. 17 (80386 internal architecture)"]
---
**Block diagram**

```text
 +---------------------- CPU -----------------------+
 |  Instruction unit                                |
 |   prefetcher (16-byte code queue) -> decoder     |
 |   (3 decoded instructions)                       |
 |  Execution unit                                  |
 |   control unit | data unit (ALU, 32-bit regs,    |
 |   barrel shifter) | protection test unit         |
 +----------+----------------------------+----------+
            | effective address          ^ code / data
            v                            |
 +---------------- MMU ---------------+  |
 | segmentation unit -> linear addr   |  |
 | paging unit (TLB) -> physical addr |  |
 +-----------------+------------------+  |
                   v                     |
 +---------------- Bus Interface Unit ---+----------+
 | request prioritizer, address drivers, pipelined  |
 | bus control, data transceivers                   |
 +--------------------------------------------------+
     A31-A2, BE3'-BE0'   D31-D0   control signals
```

**Units**

1. **Bus Interface Unit (BIU).** The only unit connected to the outside: 32-bit address (A31-A2 with byte enables $\overline{BE0}$-$\overline{BE3}$) and 32-bit data bus. It accepts requests from the prefetcher and from the execution unit (data), prioritizes them, and runs the bus cycles (with address pipelining and dynamic bus sizing).
2. **Instruction unit:**
   - **Prefetch unit:** while the bus is free, fetches code ahead into a **16-byte (15 B used) instruction queue**.
   - **Decode unit:** decodes instructions from the queue into micro-instructions and keeps up to **3 decoded instructions** ready for the execution unit.
3. **Execution unit (CPU proper):**
   - **Control unit:** microcode that sequences the execution of each instruction.
   - **Data unit:** the 32-bit **ALU**, the 8 general-purpose 32-bit registers, a 64-bit barrel shifter and multiply/divide hardware.
   - **Protection test unit:** checks segment limits and access rights during execution.
4. **Memory Management Unit (MMU):**
   - **Segmentation unit:** turns logical addresses (selector:offset) into **linear addresses** using the descriptor caches, with limit and privilege checks.
   - **Paging unit:** if paging is on, translates linear to **physical** addresses through the page directory and page tables (CR3), using the **TLB** (32 recent page translations) to avoid table reads.

These units work in parallel (a 6-stage pipeline: bus, prefetch, decode, execute, segmentation, paging), so the 80386 executes most instructions in about 2 clocks.
