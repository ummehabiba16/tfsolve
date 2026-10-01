---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Von Neumann: one memory and one bus for program and data (simple, flexible, but has the von Neumann bottleneck). Harvard: separate memories and buses (fetch and data access in parallel, faster, more hardware; ATmega32 uses it)."
sources: ["EHP ATMega32_Core slides 10-13 (Harvard architecture, von Neumann bottleneck, single level pipelining)"]
---
**Von Neumann architecture**

- A **single memory** holds both instructions and data, and the CPU reaches it over **one set of address, data and status buses**.
- An instruction fetch and a data read or write cannot happen at the same time. They take turns on the shared bus: the **von Neumann bottleneck**. The 8086 is an example.

*Advantages:* simpler and cheaper hardware (one memory, one bus); memory is shared flexibly between program and data; programs can be loaded or modified like data.

*Disadvantages:* the bottleneck limits speed; instruction and data widths must match the same bus; code can be overwritten by data by mistake.

**Harvard architecture**

- **Separate memories and buses** for program (instruction memory) and data (data memory). The ATmega32 has 32KB flash for the program and 2KB SRAM (plus EEPROM) for data.
- The next instruction can be **fetched while the current one executes** and accesses data, which gives single-level pipelining and about 1 MIPS per MHz in the ATmega32.

*Advantages:* higher throughput (parallel fetch and data access); instruction and data words can have different widths (16-bit instructions, 8-bit data in AVR); program memory is protected from accidental data writes.

*Disadvantages:* more complex and costly hardware (two memories, two bus sets, more pins); fixed partition, so unused program memory cannot be used for data; constants in program memory need special instructions to read.
