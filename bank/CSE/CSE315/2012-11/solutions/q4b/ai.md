---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "RxD is sampled at 16x the baud rate (normal) or 8x (double speed); idle samples are 0-labelled. On a high-to-low transition the start-bit detection starts; the receiver checks samples 8, 9, 10 (normal) or 4, 5, 6 (double speed): if at least two are low the start bit is valid and the internal clock is synchronized to the frame, otherwise the edge is treated as a spike and the search restarts. This repeats for every frame."
sources: ["EHP Serial Communication slides 71-75 (asynchronous clock recovery, start bit sampling, samples 8-9-10 and 4-5-6)"]
changes:
  - "2026-10-12: replaced the ASCII sketch by a TikZ figure of the start-bit samples in both modes (answer unchanged)"
---
The clock recovery logic synchronizes the receiver's internal baud clock to each incoming frame by detecting the **start bit**.

1. **Oversampling.** RxD is sampled **16 times per bit in normal mode** and **8 times per bit in double-speed mode** (U2X = 1).
2. **Idle line.** While the line is idle (high), the samples are counted as "0" (no activity) and the logic waits for a **high-to-low transition**.
3. **Start-bit detection.** The first low sample starts the sequence; that sample is number 1 of the start bit.
4. **Majority vote in the middle of the bit:** normal mode uses **samples 8, 9 and 10**; double-speed mode uses **samples 4, 5 and 6**.
   - At least two of the three **low**: a **valid start bit**. The clock recovery is now synchronized, and data recovery samples each following bit in its centre.
   - Two or more **high**: the low level was a **noise spike**. The start bit is rejected and the receiver waits for the next high-to-low transition.
5. The process is repeated for **every frame**, so small baud-rate differences do not accumulate.

![Start-bit sampling: 16 samples per bit with a vote on samples 8-10 (normal), 8 samples per bit with a vote on samples 4-6 (double speed)](figures/startbit.png)

In double-speed mode there are half as many samples, so the receiver tolerates less baud-rate error and noise.
