---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Frame (LSB first): start 0 | 1 0 1 0 0 0 0 0 1 | parity 0 (three 1s, already odd) | stop 1. Only a data overrun (DOR) occurs: Y's two-character receive buffer and its shift register are full when the new start bit arrives, so a frame is lost. No FE (stop bit = 1) and no PE (parity correct)."
sources: ["EHP Serial Communication slides 17-19 (frame, parity), 56-58 (9-bit data), 62-63 (FE, DOR)"]
---
**i. Data framing**

Character $1\,0000\,0101_2$: bit 8 = 1, bits 7-0 = 0000 0101. It is sent **LSB first**:

| Field | Start | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | Parity | Stop |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Bit | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | **0** | 1 |

Odd parity: the data contains **three** 1s (D0, D2, D8), already odd, so the parity bit is **0**.

```text
      St  D0  D1  D2  D3  D4  D5  D6  D7  D8  P   Sp
 ----+   +---+   +---+                   +---+   +-------
     |___|   |___|   |___________________|   |___|
       0   1   0   1   0   0   0   0   0   1   0   1
```

**ii. Errors at the receiver Y**

- **DOR (Data OverRun): yes.** The ATmega32 receive buffer (UDR) holds two characters, and a third waits in the receive shift register. Y's buffer and shift register are **both full**. When the start bit of X's new frame is detected, there is nowhere to put it, so the **DOR flag is set** and a frame is lost (the data between the last frame read from UDR and the next one read is incomplete). The cause is that Y's program did not read UDR fast enough.
- **FE (Frame Error): no.** FE is set only if the first stop bit is read as 0. X sends a correct stop bit (1), and both sides use the same baud rate and frame format.
- **PE (Parity Error): no.** X computed the odd-parity bit correctly (0), and Y is set to odd parity too, so the parity check passes.

So only **DOR** is reported. It is not a transmission error but a receiver-side buffer overflow.
