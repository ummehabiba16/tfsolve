---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "8087 = Control Unit (bus tracking and instruction queue that mirrors the 8086's, control and status words, tag word, exception pointers, data buffer, operand queue) + Numeric Execution Unit (eight 80-bit register stack ST(0)-ST(7), exponent module, fraction/mantissa module with programmable shifter and arithmetic unit, temporary registers, microcode control) connected by 16-bit and 68/84-bit internal buses."
sources: ["Brey, The Intel Microprocessors, Ch. 14 (8087/80x87 internal structure: control unit and numeric execution unit)"]
---
```text
   AD15-AD0, A19-A16, BHE, S2-S0, QS1-QS0, READY, RQ/GT, BUSY, INT, CLK
                                   |
 +---------------------- Control Unit (CU) ----------------------+
 |  bus interface: address/status, data buffer                   |
 |  instruction queue (tracks the 8086 queue using QS0/QS1)      |
 |  control word | status word | tag word | exception pointers   |
 |  operand queue                                                |
 +-------------------------------+-------------------------------+
                                 |  internal data and control buses
 +----------------- Numeric Execution Unit (NEU) ----------------+
 |  microcode control unit                                       |
 |  exponent module          fraction module: programmable       |
 |  (16-bit)                 shifter + arithmetic unit (64-bit)  |
 |  temporary registers                                          |
 |  register stack: 8 x 80-bit  ST(0) ... ST(7)                  |
 +---------------------------------------------------------------+
```

**Control Unit (CU):** connects the 8087 to the 8086's buses. It monitors the instruction stream (keeping a queue identical to the 8086's using QS0/QS1), recognizes ESC (floating-point) instructions, fetches memory operands through the data buffer and operand queue, and holds the **control word** (rounding, precision, exception masks), **status word** (condition codes, stack top pointer, exception flags), **tag word** (state of each stack register) and **exception pointers**. It signals BUSY (to the 8086's TEST pin) and INT on unmasked exceptions.

**Numeric Execution Unit (NEU):** performs all arithmetic in the 80-bit extended format, using the **8 $\times$ 80-bit register stack** (ST(0) top of stack), an **exponent module**, a **fraction module** with a **programmable shifter** and **arithmetic module**, and temporary registers, under **microcode** control.
