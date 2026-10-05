---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Data: immediate (MOV BL, 44H), direct (MOV BX, [437AH]), register (MOV AX, BX), register indirect (MOV CX, [BX]), base-plus-index (MOV DX, [BX+DI]), register relative (MOV AX, [BX+1000H]), base-relative-plus-index (MOV AX, [BX+DI+10H]). Program memory: direct (JMP 1000H:0000H), relative (JMP SHORT NEXT), indirect (JMP AX / JMP [BX]). Stack (PUSH AX / POP BX), I/O (IN AL, 05H / OUT DX, AL), implied (CLC, HLT)."
sources: ["MHE IF slides 12-23 (addressing modes of 8086 with examples)", "Brey, The Intel Microprocessors, Ch. 3 (addressing modes)"]
---
**1. Data addressing modes**

| Mode | Where the operand is | Example |
|:--|:--|:--|
| Immediate | in the instruction itself | `MOV BL, 44H` |
| Direct | at a memory address given in the instruction | `MOV BX, [437AH]` |
| Register | in a register | `MOV AX, BX` |
| Register indirect | at the memory address held in BX, BP, SI or DI | `MOV CX, [BX]` |
| Base-plus-index | address = base (BX/BP) + index (SI/DI) | `MOV DX, [BX+DI]` |
| Register relative | address = base or index register + displacement | `MOV AX, [BX+1000H]` |
| Base-relative-plus-index | address = base + index + displacement | `MOV AX, [BX+DI+10H]` |

**2. Program memory addressing** (JMP, CALL)

| Mode | Example |
|:--|:--|
| Direct (far, address in the instruction) | `JMP 1000H:0000H` |
| Relative (displacement from IP) | `JMP SHORT NEXT`, `JNZ AGAIN` |
| Indirect (address in a register or memory) | `JMP AX`, `CALL BX`, `JMP [DI]` |

**3. Stack addressing:** PUSH and POP use SS:SP implicitly: `PUSH AX`, `POP BX` (CALL/RET also use the stack).

**4. I/O port addressing:** fixed port in the instruction, `IN AL, 05H`; or variable port in DX, `OUT DX, AL`.

**5. Implied addressing:** the operand is implied by the instruction: `CLC`, `HLT`, `CBW`.

(Segment defaults: BP-based addresses use SS, the others DS; the 80386 adds scaled-index addressing such as `MOV AX, [EBX+2*ECX]`.)
