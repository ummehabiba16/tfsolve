---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "CPU A1, A0 -> 8255 A1, A0, so A004h = Port A (mouse), A005h = Port B (keyboard), A006h = Port C (none), A007h = control register. CS' = NAND of A15, A14', A13, A12', A11'-A3', A2 and IO (M/IO' = 0); RD'/WR' from IORC'/IOWC'; control word 92h (mode 0, ports A and B input)."
sources: ["Brey, The Intel Microprocessors, Sec. 11-3 (82C55 interface, port addresses, control word)", "Rafiquzzaman, Microprocessors and Microcomputer-Based System Design, Ch. 5 (8255 control word, I/O decoding)"]
---
**Port assignment**

The 8255 selects its registers with its A1, A0 pins. Connect them to the CPU's **A1 and A0**:

| Address | A15 ... A2 | A1 A0 | 8255 register | Device |
|:-:|:-:|:-:|:--|:--|
| A004h | 1010 0000 0000 01 | 0 0 | Port A | **Mouse** |
| A005h | 1010 0000 0000 01 | 0 1 | Port B | **Keyboard** |
| A006h | 1010 0000 0000 01 | 1 0 | Port C | **None** |
| A007h | 1010 0000 0000 01 | 1 1 | Control register | - |

**Chip select ($\overline{CS}$)**

A15-A2 must be **1010 0000 0000 01**, and the cycle must be an I/O cycle (M/$\overline{IO}$ = 0, since `IN`/`OUT` are used). The NAND output is 0 only when all its inputs are 1, so the lines that must be 0 go through inverters:

$$\overline{CS} = \overline{A_{15}\cdot \overline{A_{14}} \cdot A_{13} \cdot \overline{A_{12}} \cdot \overline{A_{11}} \cdots \overline{A_{3}} \cdot A_{2} \cdot \overline{M/\overline{IO}}}$$

**Completed connection diagram**

```text
 8086 side                                 8255
 D7-D0   <=========================>  D7-D0
 IORC' (RD' with M/IO' = 0) ------->  RD'
 IOWC' (WR' with M/IO' = 0) ------->  WR'
 RESET  --------------------------->  RESET
 A1 ------------------------------->  A1                Port A <==> Mouse
 A0 ------------------------------->  A0                Port B <==> Keyboard
                                                        Port C      None
 A15 ------------------+
 A14 ---[>o]-----------+
 A13 ------------------+
 A12 ---[>o]-----------+
 A11 ---[>o]-----------+
 A10 ---[>o]-----------+
 A9  ---[>o]-----------+
 A8  ---[>o]-----------+  NAND
 A7  ---[>o]-----------+ (15 inputs) o------->  CS'
 A6  ---[>o]-----------+
 A5  ---[>o]-----------+
 A4  ---[>o]-----------+
 A3  ---[>o]-----------+
 A2  ------------------+
 M/IO' -[>o]-----------+     ([>o] = inverter)
```

**Programming.** The mouse and the keyboard both send data to the CPU, so ports A and B are **inputs** in mode 0:

| D7 | D6 D5 | D4 | D3 | D2 | D1 | D0 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 (mode set) | 00 (group A mode 0) | 1 (Port A in) | 0 (PC upper out) | 0 (group B mode 0) | 1 (Port B in) | 0 (PC lower out) |

Control word = 1001 0010 = **92h**:

```text
MOV DX, 0A007h   ; control register
MOV AL, 92h
OUT DX, AL
MOV DX, 0A004h   ; read mouse
IN  AL, DX
MOV DX, 0A005h   ; read keyboard
IN  AL, DX
```

*Notes:*

- Assumption: isolated I/O (port addresses used with `IN`/`OUT`), and mode 0 because no handshake is required. Mode 1 strobed input could be used instead if the devices provide a strobe.
- Because A004h and A005h are consecutive, the 8255 sees the CPU's A1, A0 directly, as in an 8-bit (8088-style) data bus. On a 16-bit 8086 bus the odd address A005h is transferred on D8-D15, so the 8255's D7-D0 would have to be connected through a bus that steers both bytes to it.
