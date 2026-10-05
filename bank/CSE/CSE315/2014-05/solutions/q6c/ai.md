---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "75H = 0111 0101: D7 = 0, so it is a bit set/reset (BSR) word, not a mode word: D3-D1 = 010 selects PC2 and D0 = 1 sets it. Result: PC2 is set to 1; the port modes are not changed (D6-D4 are don't care)."
sources: ["Brey, The Intel Microprocessors, Sec. 11-3 (82C55 command byte B: bit set/reset)"]
---
$$75H = 0111\ 0101_2$$

**D7 = 0**, so this is **not** a mode-definition word but a **bit set/reset (BSR) control word** for Port C:

| Bit(s) | Value | Meaning |
|:--|:-:|:--|
| D7 | 0 | BSR mode |
| D6 D5 D4 | 111 | don't care |
| D3 D2 D1 | 010 | selects **PC2** |
| D0 | 1 | **set** the bit (0 would reset it) |

**Configuration:** writing 75H to the control register **sets PC2 = 1**. The modes and directions of ports A, B and C stay as previously programmed (BSR does not change them). It is typically used to drive a single Port C line or to set an INTE flip-flop in mode 1/2 (PC2 is INTE_B in mode 1 input/output of port B).
