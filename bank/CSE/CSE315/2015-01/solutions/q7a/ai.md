---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "FFH = 1 11 1 1 1 1 1: mode-set word; group A in mode 2 (Port A bidirectional strobed; the D4 input bit is ignored), group B in mode 1 with Port B as strobed input; Port C is used for handshaking (PC3-PC7 for Port A, PC0-PC2 for Port B), the D3/D0 'input' bits only affect unused lines (none left)."
sources: ["Brey, The Intel Microprocessors, Sec. 11-3 (82C55 command byte A, modes 1 and 2, port C handshake pins)"]
---
$$FFH = 1\ 11\ 1\ 1\ 1\ 1\ 1$$

| Bit(s) | Value | Meaning |
|:--|:-:|:--|
| D7 | 1 | **Mode-set** command (not bit set/reset) |
| D6 D5 | 11 | **Group A in mode 2** (1x = mode 2) |
| D4 | 1 | Port A input: ignored in mode 2, because Port A is **bidirectional** |
| D3 | 1 | Port C upper (PC7-PC4) input: these lines are taken by the mode 2 handshake |
| D2 | 1 | **Group B in mode 1** (strobed) |
| D1 | 1 | **Port B input** |
| D0 | 1 | Port C lower (PC3-PC0) input: taken by handshakes |

**Resulting configuration**

- **Port A: mode 2, bidirectional strobed I/O.** Handshake lines: PC7 = $\overline{OBF_A}$, PC6 = $\overline{ACK_A}$, PC5 = IBF_A, PC4 = $\overline{STB_A}$, PC3 = INTR_A.
- **Port B: mode 1, strobed input.** Handshake lines: PC2 = $\overline{STB_B}$, PC1 = IBF_B, PC0 = INTR_B.
- **Port C:** all 8 lines are used as handshake/status signals for ports A and B, so none is left for general I/O (reading Port C returns the status).
