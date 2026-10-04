---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "One instruction (mnemonic) has many machine codes: the opcode bits plus D, W, MOD, REG and R/M fields change with direction, operand size, register and one of 24 memory addressing modes. E.g. MOV CX with another operand alone has 64 different codes, so the ~117 instruction types expand to thousands of opcodes/codes."
sources: ["MHE IF slides 3-8 (instruction template, 32 ways to specify MOV CX source, 64 codes, D/W/MOD/REG/R/M fields)", "Hall, Microprocessors and Interfacing, Ch. 3 (8086 instruction coding)"]
---
An 8086 **instruction** (mnemonic, e.g. `MOV`) is one operation, but its binary **code** depends on how the operands are given:

- **D bit:** direction (register is source or destination).
- **W bit:** byte or word operation.
- **REG field:** which of 8 registers.
- **MOD and R/M fields:** another register, or one of **24 memory addressing modes** (with no, 8-bit or 16-bit displacement).
- Special short forms (e.g. `MOV reg, imm` with the register coded in the opcode, `MOV AL/AX, mem`), and segment-override and other prefixes.

*Example (slides):* in `MOV CX, source` the source can be any of 8 registers or 24 memory modes: **32** possibilities. With CX as the source there are 32 more destinations, so there are **64 different codes** just for MOV with CX. Over all registers and modes MOV alone has hundreds of codes.

So the 8086's relatively small set of instruction types (about 117 mnemonics) corresponds to a **far larger number of opcodes/machine codes**. This is why codes are built from instruction templates and MOD/RM tables instead of being listed in one table, as can be done for the 8085.
