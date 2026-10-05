---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "0580H, 0582H, 0588H, 058AH differ only in A3 and A1 (00, 01, 10, 11), so CPU A1 -> 8255 A0 and CPU A3 -> 8255 A1; A0 = 0 and A2 = 0 (even addresses, low data bus D7-D0). CS' = NAND of A15'...A11', A10, A9', A8, A7, A6', A5', A4', A2', A0' and M/IO' inverted (A15-A0 = 0000 0101 1000 x0x0). RD' and WR' (I/O cycle) to RD', WR'; system RESET to RESET; 8255 D7-D0 to 8086 D7-D0."
sources: ["Brey, The Intel Microprocessors, Sec. 11-2 and 11-3 (I/O decoding, 82C55 on the 8086 low bank)"]
---
**Find the address bits used by the 8255**

| Port | Address | A15-A12 | A11-A8 | A7-A4 | A3 | A2 | A1 | A0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Port A | 0580H | 0000 | 0101 | 1000 | 0 | 0 | 0 | 0 |
| Port B | 0582H | 0000 | 0101 | 1000 | 0 | 0 | **1** | 0 |
| Port C | 0588H | 0000 | 0101 | 1000 | **1** | 0 | 0 | 0 |
| Control | 058AH | 0000 | 0101 | 1000 | **1** | 0 | **1** | 0 |

Only **A3 and A1** change, in the order 00, 01, 10, 11. So:

- CPU **A3 $\to$ 8255 A1**, CPU **A1 $\to$ 8255 A0**.
- **A0 = 0** for all four addresses: the 8255 is on the **low (even) data bus D7-D0**.
- A2 = 0 and A15-A4 = 0000 0101 1000 are decoded for $\overline{CS}$. (I/O addresses use only A15-A0 of the 20-bit bus; A19-A16 are 0 in I/O cycles.)

$$\overline{CS} = \overline{\overline{A15}\,\overline{A14}\,\overline{A13}\,\overline{A12}\,\overline{A11}\,A10\,\overline{A9}\,A8\,A7\,\overline{A6}\,\overline{A5}\,\overline{A4}\,\overline{A2}\,\overline{A0}\cdot\overline{M/\overline{IO}}}$$

**Connection diagram**

```text
 8086 (min mode)                                    8255
 D7-D0  <=========================================> D7-D0
 RD' -------------------------------------------->  RD'
 WR' -------------------------------------------->  WR'
 RESET ------------------------------------------>  RESET
 A3  -------------------------------------------->  A1
 A1  -------------------------------------------->  A0
 A15, A14, A13, A12, A11 --[>o]--+
 A10 ----------------------------+
 A9  ----------------------[>o]--+
 A8, A7 -------------------------+   15-input
 A6, A5, A4 --------------[>o]---+   NAND  o------>  CS'
 A2  ----------------------[>o]--+
 A0  ----------------------[>o]--+
 M/IO' --------------------[>o]--+     ([>o] = inverter on each line)
```

*Notes:* $\overline{RD}$ and $\overline{WR}$ can go directly to the 8255 because M/$\overline{IO}$ is already in the chip select (or use $\overline{IORC}$/$\overline{IOWC}$). The 8255's RESET input is active high and is driven by the system RESET. The unusual Port C address 0588H is what makes A3 (not A2) the second select line.
