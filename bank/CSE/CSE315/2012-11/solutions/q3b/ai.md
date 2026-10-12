---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "AVR core: Flash program memory -> instruction register -> decoder -> control lines; PC; 32 x 8 register file feeding the ALU (with status register), SRAM data memory, I/O modules and interrupt unit on the 8-bit data bus. One instruction per clock comes from the Harvard buses plus single-level pipelining (fetch the next while executing the current) and the register file, which delivers two operands to the single-cycle ALU and stores the result in the same clock."
sources: ["EHP ATMega32_Core slides 8, 10-15 (block diagram, Harvard, single-level pipelining, general purpose register file, single cycle ALU operation)"]
changes:
  - "2026-10-12: replaced the ASCII block diagram by a TikZ block diagram (answer unchanged)"
---
**Block diagram of the AVR CPU and memories**

![AVR CPU and memories: Flash, program counter, instruction register and decoder, register file, ALU, SREG, data bus with SRAM, EEPROM, I/O and interrupt unit](figures/avr.png)

**How it executes an instruction in (almost) every clock cycle**

1. **Harvard architecture:** program memory and data memory have separate buses, so an instruction can be fetched while data is being accessed.
2. **Single-level pipelining:** while one instruction is executing, the **next one is fetched** from Flash into the instruction register. When the current instruction finishes, the next is ready to execute at once.
3. **Register file + single-cycle ALU:** the 32 registers are all directly connected to the ALU. In **one clock** two register operands are read, the ALU performs the operation, and the result is written back to the register file (and SREG updated).
4. **Simple RISC instructions:** most are a single 16-bit word (one fetch) and execute in one cycle; only memory accesses, jumps and a few others take 2 or more cycles.

As a result the ATmega approaches **1 MIPS per MHz**.
