---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "4 = STB_A' falling (data latched); 2 = IBF_A rising (buffer full: no next byte); 1 = end of valid data on PA0-PA7; 5 = INTR rising (after STB_A' rises); 6 = RD' falling (8086 starts reading; INTR then falls); 3 = IBF_A falling after RD' rises (safe to send the next byte)."
sources: ["Brey, The Intel Microprocessors, Sec. 11-3 (82C55 mode 1 strobed input timing: STB, IBF, INTR, RD)"]
---
**Mode 1 strobed input (Port A).** The tape reader puts a byte on PA0-PA7 and pulses $\overline{STB_A}$ low; the 8255 latches the byte and sets IBF_A; when $\overline{STB_A}$ returns high it raises INTR; the 8086's read ($\overline{RD}$) clears INTR (falling edge) and then IBF_A (rising edge).

**Redrawn timing diagram with event IDs** ((n) = circled number)

```text
               (4)
STB_A' ---------+     +--------------------------------------------
                |_____|
                (2)                                  (3)
IBF_A            +------------------------------------+
       __________|                                    |____________
                               (5)
INTR                            +--------+
       _________________________|        |_________________________
                                       (6)
RD'    ---------------------------------+           +--------------
                                        |___________|
PA0-7  .....<===============>......................................
                            (1)
```

| ID | Event | Point on the diagram |
|:-:|:--|:--|
| 4 | 8255 loads the byte into the Port A input latch | falling edge of $\overline{STB_A}$ |
| 2 | 8255 forbids the tape reader to send the next byte | IBF_A goes high (caused by $\overline{STB_A}$ low) |
| 1 | Data byte from the tape reader is no longer valid | end of the valid data on PA0-PA7 (after $\overline{STB_A}$ rises) |
| 5 | 8255 informs the 8086 by an interrupt | INTR goes high (caused by $\overline{STB_A}$ rising, INTE_A = 1) |
| 6 | 8086 starts reading the data | falling edge of $\overline{RD}$ (which also clears INTR) |
| 3 | 8255 signals that it is safe to send the next byte | IBF_A goes low (caused by $\overline{RD}$ rising) |
