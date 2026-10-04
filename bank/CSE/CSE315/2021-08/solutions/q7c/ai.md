---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "In double speed (U2X = 1) RxD is sampled 8 times per bit. After an idle-high to low transition, the receiver takes samples 4, 5 and 6 of the start bit; if at least two are low (majority) the start bit is valid and the clock is synchronized, otherwise it is rejected as a noise spike and the search restarts."
sources: ["EHP Serial Communication slides 69, 71-75 (double speed mode, asynchronous clock recovery, samples 4-5-6 in double speed)"]
---
**Sampling rate.** In double-speed mode (U2X = 1) the receiver samples RxD **8 times per bit** (instead of 16). This is why it is more sensitive to baud-rate errors.

**Start-bit detection (clock recovery)**

1. While the line is idle (high), the clock recovery logic keeps sampling RxD (samples marked 0 below) and looks for a **high-to-low transition**.
2. The first low sample starts the **start-bit detection sequence**; that sample is counted as sample 1 of the start bit.
3. The logic takes **samples 4, 5 and 6** (the centre of the bit) and makes a **majority vote**:
   - at least two of them **low**: a **valid start bit**. The internal clock is now synchronized to the frame, and data recovery starts (each following bit is again judged by samples 4, 5, 6);
   - at least two **high**: the low level was only a **noise spike**. The start bit is **rejected** and the receiver waits for the next high-to-low transition.
4. This is repeated for every frame, so small clock differences do not add up.

```text
RxD    idle ----------+                               +-----
                      |______________ start bit ______| D0 ...
sample (U2X = 1)   0 0 1 2 3 [4 5 6] 7 8
                              ^^^^^ majority of 4, 5, 6
                       low -> valid start bit, sync
                       high -> noise spike, rejected
```

(In normal speed the same procedure uses 16 samples per bit and votes on samples 8, 9, 10.)
