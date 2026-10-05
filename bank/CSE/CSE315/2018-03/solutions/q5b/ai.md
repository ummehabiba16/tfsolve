---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) 1 01 1 0 0 0 0 = B0H (Port A mode 1 input, Port B mode 0 output, free port C lines output). (ii) 1 00 0 0 0 1 0 = 82H (Port A mode 0 output, Port B mode 0 input, port C output)."
sources: ["Brey, The Intel Microprocessors, Sec. 11-3 (8255 command byte A: mode set control word)", "Hall, Microprocessors and Interfacing, Ch. 9 (8255 control word)"]
---
**Mode-set control word format**

| D7 | D6 D5 | D4 | D3 | D2 | D1 | D0 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 = mode set | Group A mode (00 = 0, 01 = 1, 1x = 2) | Port A (1 = in, 0 = out) | Port C upper PC7-PC4 (1 = in) | Group B mode (0 = mode 0, 1 = mode 1) | Port B (1 = in) | Port C lower PC3-PC0 (1 = in) |

**(i) Port A input in mode 1, Port B output in mode 0**

| Bit | Value | Reason |
|:--|:-:|:--|
| D7 | 1 | mode-set word |
| D6 D5 | 01 | group A in mode 1 |
| D4 | 1 | Port A input |
| D3 | 0 | PC6, PC7 are free in mode 1 input (PC3-PC5 are INTR_A, STB_A, IBF_A); taken as outputs |
| D2 | 0 | group B mode 0 |
| D1 | 0 | Port B output |
| D0 | 0 | PC0-PC2 free; taken as outputs |

$$\text{Control word} = 1011\ 0000_2 = \mathbf{B0H}$$

**(ii) Port A output in mode 0, Port B input in mode 0**

| Bit | Value | Reason |
|:--|:-:|:--|
| D7 | 1 | mode-set word |
| D6 D5 | 00 | group A mode 0 |
| D4 | 0 | Port A output |
| D3 | 0 | PC7-PC4 output (assumed) |
| D2 | 0 | group B mode 0 |
| D1 | 1 | Port B input |
| D0 | 0 | PC3-PC0 output (assumed) |

$$\text{Control word} = 1000\ 0010_2 = \mathbf{82H}$$

*Note:* the port C bits (D3, D0) are not specified by the question; they are set to output (0). Making them inputs would give B9H in (i) and 8BH in (ii).
