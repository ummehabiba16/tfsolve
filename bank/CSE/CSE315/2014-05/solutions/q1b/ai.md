---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "8086 = BIU (segment registers CS, DS, SS, ES, IP, address adder, 6-byte queue, bus control) + EU (ALU, flags, general registers AX, BX, CX, DX, pointer/index SP, BP, SI, DI, control). Registers: AX accumulator (MUL/DIV, I/O), BX base (address), CX count (LOOP, REP, shifts), DX data (MUL/DIV, I/O port); SP/BP stack pointers; SI/DI string source/destination; CS/DS/SS/ES segments; IP next instruction; FLAGS with 6 status (CF, PF, AF, ZF, SF, OF) and 3 control (TF, IF, DF) flags."
sources: ["MHE 8086-Architecture slides (EU/BIU block diagram, AX, BX, CX, DX, SP, BP, SI, DI, flags, segment registers, IP)"]
---
**Internal architecture**

```text
 +------------------ BIU (Bus Interface Unit) ------------------+
 |  CS  DS  SS  ES   IP          address adder (seg x 10H + off) |---> A19-A0
 |  6-byte instruction queue     bus control logic              |<--> D15-D0
 +---------------------------+----------------------------------+     control
                             | instruction bytes / operands
 +------------------ EU (Execution Unit) -----------------------+
 |  AH AL (AX)   BH BL (BX)   CH CL (CX)   DH DL (DX)            |
 |  SP   BP   SI   DI                                            |
 |  ALU (16-bit)    FLAGS    EU control (decoder)                |
 +--------------------------------------------------------------+
```

- **BIU:** does all bus operations: computes physical addresses (segment $\times$ 10H + offset), **fetches instructions into the 6-byte queue**, reads/writes operands for the EU.
- **EU:** decodes and executes instructions taken from the queue, using the ALU and registers.

**Registers (fourteen 16-bit registers)**

| Group | Register | Use |
|:--|:--|:--|
| General purpose (8- or 16-bit: AH/AL ...) | **AX** (accumulator) | arithmetic, MUL/DIV, IN/OUT |
| | **BX** (base) | general, and holds an offset (base address) in memory |
| | **CX** (count) | count for LOOP, REP string instructions, CL for shifts/rotates |
| | **DX** (data) | general, high word of MUL/DIV results, I/O port address |
| Pointer / index | **SP** (stack pointer) | top of stack (with SS) |
| | **BP** (base pointer) | addresses data in the stack segment |
| | **SI** (source index) | source of string operations (DS:SI) |
| | **DI** (destination index) | destination of string operations (ES:DI) |
| Segment | **CS** | code segment (with IP) |
| | **DS** | data segment |
| | **SS** | stack segment |
| | **ES** | extra segment (string destination) |
| Instruction pointer | **IP** | offset of the next instruction in CS |
| Flags | **FLAGS** | status: CF (carry), PF (parity), AF (auxiliary carry), ZF (zero), SF (sign), OF (overflow); control: TF (trap/single step), IF (interrupt enable), DF (direction for strings) |
