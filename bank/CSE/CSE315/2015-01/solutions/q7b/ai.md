---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Connect 8255 D7-D0 to the 8086 low data bus D7-D0 (even addresses), CPU A2 -> 8255 A1 and CPU A1 -> 8255 A0, and decode CS' = NAND(A7, A6', A5, A4', A3, A0', M/IO' inverted) (A7-A3 = 10101, A0 = 0, I/O cycle). The 8255 then occupies A8H (Port A), AAH (Port B), ACH (Port C), AEH (control), so it responds at AAH."
sources: ["Brey, The Intel Microprocessors, Sec. 11-2 and 11-3 (I/O port decoding, 8-bit I/O devices on the 8086 low bank, 82C55 interface)"]
---
**Design choices**

- The 8255 has an 8-bit data bus. On the 8086 an 8-bit I/O device is placed on the **low (even) bank**: 8255 D7-D0 to 8086 **D7-D0**, and it is used only at **even** addresses (A0 = 0).
- The 8255's register select inputs A1, A0 are therefore driven by the CPU's **A2 and A1**.
- The remaining lines are fully decoded for the 8-bit port address **AAH = 1010 1010**:

| A7 | A6 | A5 | A4 | A3 | A2 | A1 | A0 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | 0 | 1 | 0 | 1 | to 8255 A1 | to 8255 A0 | 0 |

$$\overline{CS} = \overline{A7 \cdot \overline{A6} \cdot A5 \cdot \overline{A4} \cdot A3 \cdot \overline{A0} \cdot \overline{M/\overline{IO}}}$$

**Connection diagram**

```text
 8086                                     8255
 D7-D0  <===============================> D7-D0
 A2 ------------------------------------> A1
 A1 ------------------------------------> A0
 A7 ----------------+
 A6 ---[>o]---------+
 A5 ----------------+
 A4 ---[>o]---------+  NAND o-----------> CS'
 A3 ----------------+
 A0 ---[>o]---------+
 M/IO' -[>o]--------+         ([>o] = inverter)
```

**Resulting addresses**

| A2 A1 | 8255 register | Port address |
|:-:|:--|:-:|
| 00 | Port A | A8H |
| 01 | Port B | **AAH** |
| 10 | Port C | ACH |
| 11 | Control register | AEH |

*Note:* "an address of AAH" is read as the 8255 being selected at AAH (its block A8H-AEH, even addresses on the low data bus). If an 8-bit bus (8088-style) were assumed, the CPU's A1, A0 would go directly to the 8255 and CS' would decode A7-A2 = 101010, giving A8H-ABH.
