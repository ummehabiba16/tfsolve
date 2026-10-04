---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Bytes 00223h-00226h need 3 bus cycles = 12 clock cycles (no wait states): 00223h odd byte (BHE' = 0, A0 = 1), 00224h-00225h aligned word (BHE' = 0, A0 = 0), 00226h even byte (BHE' = 1, A0 = 0)."
sources: ["MHE 8086-Memory_Organization slides 3-7 (odd/even banks, BHE and A0 table, odd-address word needs two cycles)", "Brey, The Intel Microprocessors, Sec. 10-3 (8086 memory interface, BHE)"]
---
*Note:* the table printed with the question swaps two rows. The correct table (slides, Intel data sheet) is: $\overline{BHE}$ = 0, A0 = 1: **odd (high) bank**, D8-D15; $\overline{BHE}$ = 1, A0 = 0: **even (low) bank**, D0-D7. The answer uses the correct table.

**i. Minimum number of cycles**

Locations 00223h, 00224h, 00225h, 00226h are 4 bytes. The 8086 can move 2 bytes in one bus cycle only if they form an **aligned word** (even address and the next odd address).

| Bus cycle | Address on bus | Bytes moved | $\overline{BHE}$ | A0 | Bank(s) | Data lines |
|:-:|:-:|:--|:-:|:-:|:--|:-:|
| 1 | 00223h | 00223h (odd) | 0 | 1 | odd bank only | D8-D15 |
| 2 | 00224h | 00224h and 00225h (aligned word) | 0 | 0 | both banks | D0-D15 |
| 3 | 00226h | 00226h (even) | 1 | 0 | even bank only | D0-D7 |

The first byte (odd) and the last byte (even) cannot pair with a neighbour inside the range, so **3 bus cycles** is the minimum. Each 8086 bus cycle has 4 clock periods (T1-T4), so with no wait states:

$$3 \times 4 = \mathbf{12\ clock\ cycles}$$

**ii. $\overline{BHE}$ and A0 timing**

$\overline{BHE}$ (pin 34) and A0 (multiplexed on AD0) are put out in **T1** of each bus cycle together with the address and latched by ALE. (In T2-T4 the pins carry status S7 and data.)

```text
         | cycle 1: 00223h | cycle 2: 00224h | cycle 3: 00226h |
CLK      | T1  T2  T3  T4  | T1  T2  T3  T4  | T1  T2  T3  T4  |
         |                 |                 |                 |
BHE'     |____             |____             |_____            |
(valid   |    0            |    0            |  1              |
 in T1)  |                 |                 |                 |
A0       |----             |____             |____             |
(valid   |    1            |    0            |    0            |
 in T1)  |                 |                 |                 |
Banks    |  odd only       |  both (word)    |  even only      |
```

As levels: cycle 1: $\overline{BHE}$ = 0, A0 = 1; cycle 2: $\overline{BHE}$ = 0, A0 = 0; cycle 3: $\overline{BHE}$ = 1, A0 = 0.

*Note:* "clock cycles" is read as T-states; if the question means bus (memory) cycles, the answer is 3.
