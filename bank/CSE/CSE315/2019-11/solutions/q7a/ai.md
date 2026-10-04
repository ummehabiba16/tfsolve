---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Clock count = 4 + n(4 + 4 + 17(n-1) + 5 + 4) + 17(n-1) + 5 = 17n^2 + 17n - 8. Need >= 10^7 clocks (1 s at 10 MHz): n = 767 (02FFH), giving 10,013,944 clocks = 1.0014 s."
sources: ["Brey, The Intel Microprocessors, Ch. 6 (LOOP, nested delay loops)", "MHE IF slides (8086 instructions)"]
---
**Counting clocks** (MOV = 4; LOOP = 17 when it jumps, 5 when it falls through)

| Instruction | Executed | Clocks |
|:--|:--|:--|
| `MOV CX, n` | once | 4 |
| `MOV m, CX` | $n$ times | $4n$ |
| `MOV CX, n` | $n$ times | $4n$ |
| `LOOP DELAY_2` | $n$ times per outer pass: jumps $n-1$ times, falls through once | $n[17(n-1) + 5]$ |
| `MOV CX, m` | $n$ times | $4n$ |
| `LOOP DELAY` | jumps $n-1$ times, falls through once | $17(n-1) + 5$ |

One pass of the outer loop body (without its LOOP) is $4 + 4 + 17(n-1) + 5 + 4 = 17n$ clocks. Total:

$$C(n) = 4 + n(17n) + 17(n-1) + 5 = 17n^2 + 17n - 8$$

**Required clocks.** At 10 MHz one clock is 0.1 µs, so 1 s = $10^7$ clocks:

$$17n^2 + 17n - 8 \ge 10^7 \ \Rightarrow\ n^2 + n \ge 588235.8 \ \Rightarrow\ n \ge 766.47$$

So **n = 767** (02FFH). (n = 766 gives 9,987,866 clocks = 0.9988 s, which is less than 1 s.)

**Actual delay**

$$C(767) = 17 \times 767^2 + 17 \times 767 - 8 = 10\,013\,944\ \text{clocks}$$

$$t = 10\,013\,944 \times 0.1\ \mu s = \mathbf{1.0014\ s}$$

*Note:* the formula was checked by simulating the loop's clock count with a script (e.g. $n = 3$ gives 196 clocks both ways).
