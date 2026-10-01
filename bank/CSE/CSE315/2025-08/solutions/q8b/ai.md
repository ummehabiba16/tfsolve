---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "JMP [BX] is a near indirect jump: new IP = word at DS:BX = 300FEH = 2143H, so the next instruction is at 20000H + 2143H = 22143H."
sources: ["MHE IF slides 18-20 (addressing program codes: indirect JMP)", "MHE 8086-Memory_Organization slides 12-13 (default segments)"]
---
`JMP [BX]` is an **indirect (near) jump**: the new IP is not BX itself but the **word stored in memory at the offset in BX**. A memory operand addressed by BX uses the default segment **DS**.

**Read the new IP**

$$PA = DS\times10H + BX = 30000H + 00FEH = 300FEH$$

- [300FEH] = 43H (low byte)
- [300FFH] = 21H (high byte)

$$\text{new } IP = 2143H$$

CS is unchanged, because this is a near (intra-segment) jump.

**Next instruction's physical address**

$$PA = CS\times10H + IP = 20000H + 2143H = \mathbf{22143H}$$

(The bytes at 200FEH, in CS, are a distractor: [BX] defaults to DS, not CS. The current IP = 0954H is overwritten by the jump.)
