---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Harvard pros: separate program and data memories/buses allow fetching the next instruction while accessing data (no von Neumann bottleneck), different word widths (16-bit instructions, 8-bit data) and code protected from data writes. Cons: more buses/pins and hardware, fixed split of memory, harder to treat code as data. ATmega32 is Harvard: the single-level pipeline fetches from Flash while executing, giving ~1 instruction per clock (1 MIPS/MHz)."
sources: ["EHP ATMega32_Core slides 10-15 (Harvard architecture, single-level pipelining, register file, single-cycle ALU)"]
---
**Advantages of Harvard over von Neumann**

1. **Simultaneous instruction fetch and data access.** Program and data have separate memories and buses, so there is no "von Neumann bottleneck": the CPU can fetch the next instruction while the current one reads or writes data. This makes pipelining easy.
2. **Different widths and sizes.** Instruction memory and data memory can have different word sizes (ATmega32: 16-bit instructions in Flash, 8-bit data in SRAM), each chosen for its job.
3. **Program safety.** A data write (e.g. a bad pointer) cannot overwrite the program, which suits embedded systems running from Flash.

**Disadvantages**

1. **More hardware:** two sets of buses and memory interfaces (more pins/area, higher cost if memories are external).
2. **Fixed split of memory:** unused program memory cannot hold data and vice versa.
3. **Constants and self-modifying code are awkward:** tables stored in Flash need special instructions (`LPM`, `PROGMEM` in C) to be read as data.

**ATmega32 uses the Harvard architecture** (32 KB Flash for code, 2 KB SRAM + registers + I/O for data, separate buses).

**How it helps performance.** Because of the separate buses the AVR uses a **single-level pipeline**: while one instruction is executed, the next is fetched from Flash. Most instructions are 16 bits wide (fetched in one access) and execute in one cycle using the 32-register file and single-cycle ALU. So the ATmega32 completes about **one instruction per clock cycle (about 1 MIPS per MHz)**, much faster than a von Neumann CPU at the same clock, which must share one bus between fetch and data.
