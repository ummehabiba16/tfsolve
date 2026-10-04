---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Bytes 00111H-00114H need 3 bus cycles = 12 clocks (no wait states): 00111H odd byte (BHE' = 0, A0 = 1), 00112H-00113H aligned word (BHE' = 0, A0 = 0), 00114H even byte (BHE' = 1, A0 = 0)."
sources: ["MHE 8086-Memory_Organization slides 3-7 (odd/even banks, BHE and A0, odd-address word needs two cycles)", "Brey, The Intel Microprocessors, Sec. 10-3 (8086 memory interface)"]
---
**Minimum number of clocks**

Locations 00111H, 00112H, 00113H, 00114H (4 bytes). Two bytes move together only as an **aligned word** (even address + next odd address).

| Bus cycle | Address | Bytes | $\overline{BHE}$ | A0 | Bank(s) | Data lines |
|:-:|:-:|:--|:-:|:-:|:--|:-:|
| 1 | 00111H | 00111H (odd) | 0 | 1 | odd only | D8-D15 |
| 2 | 00112H | 00112H, 00113H (aligned word) | 0 | 0 | both | D0-D15 |
| 3 | 00114H | 00114H (even) | 1 | 0 | even only | D0-D7 |

The first byte is odd and the last is even, so neither can pair inside the range: **3 bus cycles** minimum. Each bus cycle is 4 clocks (T1-T4), so with no wait states:

$$3 \times 4 = \mathbf{12\ clock\ cycles}$$

**$\overline{BHE}$ and A0 timing** (both are output in T1 of each bus cycle and latched by ALE)

```text
         | cycle 1: 00111H | cycle 2: 00112H | cycle 3: 00114H |
CLK      | T1  T2  T3  T4  | T1  T2  T3  T4  | T1  T2  T3  T4  |
BHE'     |____             |____             |-----            |
(in T1)  |  0              |  0              |  1              |
A0       |----             |____             |____             |
(in T1)  |  1              |  0              |  0              |
Banks    |  odd only       |  both (word)    |  even only      |
```

*Note:* "clock" is read as clock period (T-state); the answer in bus cycles is 3.
