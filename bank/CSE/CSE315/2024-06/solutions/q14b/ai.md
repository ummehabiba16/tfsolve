---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Frame: start 0, data LSB first 1 0 1 0 1 1 0 1 1, odd parity 1 (six 1s), stop 1. With the receive buffer and shift register full, the new start bit causes a Data OverRun (DOR) only; no FE (stop bit = 1) and no PE (parity correct)."
sources: ["EHP Serial Communication slides 17-19 (parity, frame format)", "EHP Serial Communication slides 57, 62-63 (FE, DOR, PE)"]
---
**i. Data framing.** Character = 1 1011 0101 (D8 ... D0), so D0 = 1, D1 = 0, D2 = 1, D3 = 0, D4 = 1, D5 = 1, D6 = 0, D7 = 1, D8 = 1.

Number of 1s in the data = 6 (even). For **odd parity** the parity bit must make the total odd, so **P = 1**.

| (Idle) | St | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | P | Sp | (Idle) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 |

```text
     St D0 D1 D2 D3 D4 D5 D6 D7 D8 P  Sp
1 --+  +--+  +--+  +-----+  +--------------- idle
    |  |  |  |  |  |     |  |
0   +--+  +--+  +--+     +--+
```

**ii. Errors at the receiver (Y).**

- **DOR = 1 (Data OverRun).** Y's receive buffer (2 characters) and its shift register are already full when X's new **start bit is detected**, which is exactly the overrun condition. The new frame cannot be received and data is lost.
- **FE = 0.** The stop bit sent is 1, so no frame error.
- **PE = 0.** The parity bit is correct for odd parity (6 ones + parity 1 = 7, odd), so no parity error, assuming no noise on the line.

**Only the Data OverRun error occurs.**
