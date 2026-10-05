---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Port A mode 1 (single handshake) output to the printer, Port B mode 0 input: control word 1 01 0 0 0 1 0 = A2H. Pseudo code: write A2H to the control register; loop: read Port B; wait until OBF_A' (PC7) = 1 (printer has taken the previous byte); write the byte to Port A; repeat."
sources: ["Brey, The Intel Microprocessors, Sec. 11-3 (82C55 mode 1 strobed output: OBF_A = PC7, ACK_A = PC6, INTR_A = PC3; printer interface)", "Hall, Microprocessors and Interfacing, Ch. 9"]
---
**Control word**

| D7 | D6 D5 | D4 | D3 | D2 | D1 | D0 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 (mode set) | 01 (group A mode 1) | 0 (Port A output) | 0 (PC5, PC4 free: output) | 0 (group B mode 0) | 1 (Port B input) | 0 (PC2-PC0 output) |

$$\text{Control word} = 1010\ 0010_2 = \mathbf{A2H}$$

In mode 1 output, PC7 = $\overline{OBF_A}$ (output buffer full, to the printer), PC6 = $\overline{ACK_A}$ (from the printer), PC3 = INTR_A.

Port addresses are assumed: Port A = PA, Port B = PB, Port C = PC, control register = CR (e.g. 40H-43H).

**Pseudo code (polled)**

```text
OUT CR, A2H                  ; Port A: mode 1 output, Port B: mode 0 input
LOOP:
    AL <- IN PB              ; read the input device (simple I/O)
WAIT:
    STATUS <- IN PC          ; read port C
    if (STATUS bit 7 = 0)    ; OBF_A' = 0: printer has not taken the last byte
        goto WAIT
    OUT PA, AL               ; send the byte; 8255 makes OBF_A' = 0,
                             ; printer reads it and answers with ACK_A'
    goto LOOP
```

Waiting for $\overline{OBF_A}$ = 1 (set again by the printer's $\overline{ACK_A}$) makes sure the previous character was taken before the next is written. (Alternatively INTR_A, PC3, can be polled or used as an interrupt after enabling INTE_A by setting PC6 with the bit set/reset word 0DH.)
