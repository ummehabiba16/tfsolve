---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Take the data segment base as 01000H (so DS:SI points to 1020H): MOV CX, [SI+0AH] loads CL = 'D' (102AH) and CH = 'E' (102BH). Machine code 8B 4C 0A."
sources: ["MHE IF slides 5-11 (MOV coding; MOD/REG/R/M; Examples 1-3)", "MHE IF slides 14-17 (register relative addressing)"]
---
**Locate 'ED'.** 'D' is at 102AH and 'E' is at 102BH. A word is stored low byte first, so the word at 102AH gives low byte = 'D' and high byte = 'E'. Loaded into CX, this puts **CH = 'E'** and **CL = 'D'**, so CX reads "ED" (CX = 4544H in ASCII).

**Effective address.** The table's physical addresses are 4-digit, so the data segment is taken to start at **01000H**. The printed DS = 1000H is used directly as the base, which by the $\times 10H$ rule would mean DS = 0100H. Then:

$$DS:SI = 01000H + 0020H = 01020H$$

$$102AH - 1020H = 0AH \Rightarrow EA = SI + 0AH$$

**Assembly code**

```text
MOV CX, [SI+0AH]     ; CL <- [102AH] = 'D', CH <- [102BH] = 'E'
```

**Machine code** (MOV = 100010):

- D = 1: the destination is the REG field. W = 1: word.
- REG = 001: CX.
- Memory operand [SI] + d8 (displacement 0AH < 256): MOD = 01, R/M = 100.

| Byte | Bits | Hex |
|:--|:--|:-:|
| 1 | 100010 1 1 (OPCODE D W) | 8B |
| 2 | 01 001 100 (MOD REG R/M) | 4C |
| 3 | 0000 1010 (8-bit displacement) | 0A |

$$\textbf{MOV CX, [SI+0AH]} = \mathbf{8B\ 4C\ 0A}$$

*Byte-by-byte alternative:* `MOV CL, [SI+0AH]` = 8A 4C 0A, then `MOV CH, [SI+0BH]` = 8A 6C 0B (W = 0, REG = 101 for CH).
