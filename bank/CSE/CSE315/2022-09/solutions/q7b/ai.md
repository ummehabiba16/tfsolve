---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Port A: mode 1 (single handshake) output to the printer; Port B: mode 0 input from the switches. Control word = 1 01 0 x 0 1 x = 1010 0010 = A2h (PC4, PC5 and PC0-PC2 taken as outputs); INTE_A is enabled with the BSR word 0Dh (set PC6) if interrupts are used."
sources: ["Brey, The Intel Microprocessors, Sec. 11-3 (82C55 command byte A, mode 1 strobed output, INTE via PC6)", "Hall, Microprocessors and Interfacing, Ch. 9 (simple I/O, single and double handshake)"]
---
**Configuration**

- **Port A:** printer, **single handshake = mode 1 (strobed) output**. Port C lines used for its handshake: PC7 = $\overline{OBF_A}$, PC6 = $\overline{ACK_A}$, PC3 = INTR_A.
- **Port B:** array of switches, **simple I/O = mode 0 input**.
- Remaining port C lines (PC5, PC4 and PC2-PC0) are free; they are assumed to be outputs.

**Mode-set control word**

| D7 | D6 D5 | D4 | D3 | D2 | D1 | D0 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | 0 1 | 0 | 0 | 0 | 1 | 0 |
| mode set | group A mode 1 | Port A output | PC7-PC4 (free PC5, PC4) output | group B mode 0 | Port B input | PC3-PC0 (free PC2-PC0) output |

$$\text{Control word} = 1010\ 0010_2 = \mathbf{A2h}$$

```text
MOV AL, 0A2h        ; Port A mode 1 output, Port B mode 0 input
OUT CTRL, AL        ; CTRL = address of the 8255 control register
MOV AL, 0Dh         ; BSR: 0 xxx 110 1 -> set PC6 = INTE_A (only if INTR_A is used)
OUT CTRL, AL
```

*Notes:* bits D3 and D0 only set the direction of the port C lines not used for handshaking, so A2h assumes they are outputs (AAh or A3h would also be valid choices). In mode 1 output, the interrupt enable for port A (INTE_A) is the internal flip-flop set through PC6 with the bit set/reset word.
