---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Frame (in time order): idle 1, start 0, data LSB first 1 0 1 1 1 0 0 1, stop 1, stop 1, idle 1."
sources: ["EHP Serial Communication slides 17-20 (frame: start bit, LSB first, stop bits)"]
---
Data = 1001 1101 (D7 ... D0). Sent **LSB first**, so the order on the line is D0, D1, ..., D7 = 1, 0, 1, 1, 1, 0, 0, 1.

A frame starts with the start bit (always 0), followed by the least significant data bit. There is no parity bit, and there are two stop bits (always 1).

| (Idle) | St | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | Sp1 | Sp2 | (Idle) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |

```text
       St  D0  D1  D2  D3  D4  D5  D6  D7  Sp1 Sp2
 1 ---+   +---+   +-----------+       +-----------------  idle
      |   |   |   |           |       |
 0    +---+   +---+           +-------+
```

The frame is 11 bits long: 1 start + 8 data + 2 stop.
