---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Data 1 0001 0100 sent LSB first: start 0 | 0 0 1 0 1 0 0 0 1 | odd parity 0 (three 1s) | stop 1 1."
sources: ["EHP Serial Communication slides 17-19 (frame, parity), 56 (9-bit data)"]
---
Frame format (from Q.12): 1 start bit, **9 data bits** sent LSB first, **odd parity**, **2 stop bits**.

Data $1\,0001\,0100_2$: D8 = 1, D7-D0 = 0001 0100. LSB first: D0 = 0, D1 = 0, D2 = 1, D3 = 0, D4 = 1, D5 = 0, D6 = 0, D7 = 0, D8 = 1.

Odd parity: the data has **three** 1s (D2, D4, D8), already odd, so **P = 0**.

| Field | Start | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | P | Stop | Stop |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Bit | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 |

```text
      St  D0  D1  D2  D3  D4  D5  D6  D7  D8  P   Sp  Sp
 ----+           +---+   +---+           +---+   +-----------
     |___________|   |___|   |___________|   |___|
       0   0   0   1   0   1   0   0   0   1   0   1   1
```
