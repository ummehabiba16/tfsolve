---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "8255 at 010000xxb: Port A = 40H, Port B = 41H, Port C = 42H, control = 43H. Control word 1 01 1 0 0 0 0 = B0H (Port A mode 1 strobed input, Port B mode 0 output, free port C lines output). Flowchart: write B0H to 43H; loop: read Port C, test IBF_A (PC5); when 1, IN AL from 40H (clears IBF), OUT AL to 41H; repeat."
sources: ["Brey, The Intel Microprocessors, Sec. 11-3 (82C55 mode 1 strobed input: STB_A = PC4, IBF_A = PC5, INTR_A = PC3)", "Hall, Microprocessors and Interfacing, Ch. 9 (8255 with the 8088, polled strobed input)"]
---
**Port addresses.** The 8255's A1 A0 select the port, and the chip is selected for 010000xx b:

| Address | A1 A0 | Register |
|:-:|:-:|:--|
| 40H (0100 0000) | 00 | Port A (tape recorder) |
| 41H (0100 0001) | 01 | Port B (output device) |
| 42H (0100 0010) | 10 | Port C (handshake/status) |
| 43H (0100 0011) | 11 | Control register |

**Control word**

| D7 | D6 D5 | D4 | D3 | D2 | D1 | D0 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 (mode set) | 01 (group A mode 1) | 1 (Port A input) | 0 (PC7, PC6 free: output) | 0 (group B mode 0) | 0 (Port B output) | 0 (PC2-PC0 output) |

$$\text{Control word} = 1011\ 0000_2 = \mathbf{B0H}$$

In mode 1 input, PC4 = $\overline{STB_A}$ (from the tape recorder), **PC5 = IBF_A** (input buffer full) and PC3 = INTR_A.

**Flowchart (polled)**

```text
        +-----------------------------+
        | START                       |
        +--------------+--------------+
                       v
        +-----------------------------+
        | AL <- B0H ; OUT 43H, AL      |   initialise 8255
        +--------------+--------------+
                       v
        +-----------------------------+
   +--->| IN AL, 42H  (read Port C)   |<----------+
   |    +--------------+--------------+           |
   |                   v                          |
   |          /-----------------\    no           |
   |          | IBF_A (PC5) = 1 ?|-----------------+
   |          \--------+--------/   (no byte yet)
   |                   | yes
   |                   v
   |    +-----------------------------+
   |    | IN AL, 40H  (read byte from |   reading clears IBF_A,
   |    | tape via Port A)            |   tape may strobe next byte
   |    +--------------+--------------+
   |                   v
   |    +-----------------------------+
   |    | OUT 41H, AL (Port B output) |
   |    +--------------+--------------+
   +-------------------+
```

*Note:* port C lines not used by mode 1 are set as outputs (another choice of D3/D0 gives B8H, B1H or B9H).
