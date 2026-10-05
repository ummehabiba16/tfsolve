---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "RxD is sampled 16 times per bit (normal) or 8 times (double speed). After a high-to-low edge, the start bit is accepted if the majority of samples 8, 9, 10 (4, 5, 6 in double speed) are low, otherwise rejected as a spike; each data, parity and stop bit is the majority of its three centre samples. Double speed uses half the samples, so it tolerates less baud-rate error and noise."
sources: ["EHP Serial Communication slides 69, 71-77 (clock recovery, start-bit detection, data recovery, double speed disadvantage)"]
---
**Start bit (clock recovery)**

1. The receiver samples RxD at **16 $\times$ baud rate** in normal mode (**8 $\times$** in double-speed mode, U2X = 1). While the line is idle (high) it waits for a **high-to-low** transition.
2. On that edge the start-bit detection begins. In normal mode the receiver checks samples **8, 9 and 10** (the middle of the bit); in double-speed mode samples **4, 5 and 6**.
3. If at least two of the three are **low** (majority), the start bit is valid and the receiver's bit timing is synchronized to it. If two or more are high, the low pulse was noise and the receiver waits for the next falling edge.

**Data bits (data recovery)**

Each following bit (data, parity, stop) is also sampled 16 (or 8) times, and its value is the **majority vote of the three centre samples** (8, 9, 10 in normal, 4, 5, 6 in double speed). A 0 stop bit sets FE.

```text
          | start bit                    | D0 ...
 normal:  1 2 3 4 5 6 7 [8 9 10] ... 16  | 1 ... [8 9 10] ... 16
 2x:      1 2 3 [4 5 6] 7 8              | 1 2 3 [4 5 6] 7 8
```

**Key difference.** Double-speed mode takes **half as many samples per bit (8 instead of 16)**. Each sample covers twice as much of the bit, so the start edge is located less precisely and the majority vote is taken over a wider part of the bit; the receiver therefore tolerates **less baud-rate mismatch and noise**: a more accurate baud rate and clock are needed. (For the transmitter there is no disadvantage.)
