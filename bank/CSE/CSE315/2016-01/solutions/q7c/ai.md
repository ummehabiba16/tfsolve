---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Harvard: separate program and data memories with separate address/data buses (and possibly different word widths). Advantages over von Neumann: instruction fetch and data access at the same time (no bottleneck, easy pipelining, ~1 instruction per clock), widths optimized separately, and the program cannot be overwritten by data writes."
sources: ["EHP ATMega32_Core slides 10-13 (Harvard architecture, separate memories and buses, pipelining)"]
---
**Key characteristics of the Harvard architecture**

1. **Separate memories** for program (instructions) and data. In the ATmega32: 32 KB Flash for the program and 2 KB SRAM (plus registers and I/O) for data.
2. **Separate buses** (address and data) for each memory, so they can be accessed **at the same time**.
3. The two memories can have **different word widths and address spaces** (ATmega32: 16-bit wide program memory, 8-bit data memory), and often different technologies (non-volatile Flash for code, RAM for data).

**Advantages over von Neumann**

1. **No von Neumann bottleneck:** the next instruction can be fetched while the current one reads or writes data; with one shared bus they must take turns.
2. **Simple, efficient pipelining:** fetch and execute overlap, so most instructions complete in one clock (about 1 MIPS per MHz on the AVR).
3. **Widths chosen independently:** instructions can be wide (one fetch per instruction) while data stays 8-bit.
4. **Safety:** data writes (e.g. a bad pointer or stack overflow) cannot overwrite the program, and the program can stay in non-volatile memory.

(Disadvantages: more buses and hardware, a fixed split between code and data space, and special instructions such as `LPM` to read constants stored in program memory.)
