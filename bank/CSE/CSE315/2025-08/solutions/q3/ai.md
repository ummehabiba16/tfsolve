---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Next instruction at 23F14H is 8B 0E 7A 43 = MOV CX, [437AH]; it reads 5837AH-5837BH, so CX = 7856H (IP becomes 0A18H)."
sources: ["MHE IF slides 5-11 (MOV coding: opcode 100010, D, W, MOD, REG, R/M; Example 3)", "MHE 8086-Memory_Organization slide 12 (physical address)"]
---
**Address of the next instruction**

$$PA = CS\times10H + IP = 23500H + 0A14H = 23F14H$$

The bytes from 23F14H are: 8B, 0E, 7A, 43, (88 ...).

**Decode byte 1: 8BH = 1000 1011**

| OPCODE | D | W |
|:-:|:-:|:-:|
| 100010 | 1 | 1 |

- 100010 is **MOV** (hint)
- D = 1: data goes **to** the REG register
- W = 1: word (16-bit) operation

**Decode byte 2: 0EH = 0000 1110**

| MOD | REG | R/M |
|:-:|:-:|:-:|
| 00 | 001 | 110 |

- REG = 001 with W = 1 gives **CX**
- MOD = 00 with R/M = 110 gives **d16, a direct address**, so the next two bytes are the address: low byte 7AH, high byte 43H, giving **437AH**

The instruction is 4 bytes long: 8B 0E 7A 43.

$$\textbf{MOV CX, [437AH]}$$

(This is the same as Example 3 in the slides.)

**Execute.** The memory operand is in the data segment:

$$PA = DS\times10H + 437AH = 54000H + 437AH = 5837AH$$

- [5837AH] = 56H, goes to CL (low byte)
- [5837BH] = 78H, goes to CH (high byte)

**The register that changes is CX: CX = 7856H.** IP also moves past the 4-byte instruction to 0A14H + 4 = 0A18H.
