---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "RDY1 gated by AEN1' and RDY2 gated by AEN2' are ORed and synchronized to CLK by one (ASYNC' = 1) or two (ASYNC' = 0) flip-flops; the output READY goes to the 8086, which inserts wait states (Tw) while READY = 0 at the end of T2/T3."
sources: ["MHE 8086 Hardware Specifications slides 11, 16-17 (8284A, READY)", "Brey, The Intel Microprocessors, Sec. 9-3 and 9-5 (8284A clock generator, READY and wait states)"]
---
**Part of the 8284A block diagram used for READY**

```text
 RDY1 ---------+
               AND --+
 AEN1' --o-----+     |
                     OR ---+--> [FF1  D Q] ---> [FF2  D Q] ---> READY
 RDY2 ---------+     |     |     clock:          clock:          (to 8086
               AND --+     |     CLK rising      CLK falling      pin 22)
 AEN2' --o-----+           |                       ^
                           +-----------------------+
                           ASYNC' = 1: FF1 bypassed (one stage)
                           ASYNC' = 0: FF1 and FF2 (two stages)

 Crystal X1/X2 -> oscillator -> divide by 3 -> CLK (33% duty, 8086 pin 19)
                                               (also clocks FF1, FF2)
```

**How READY is generated**

1. **Inputs from the system.** A slow memory or I/O device (through its wait-state logic) drives **RDY1** or **RDY2** high when it is ready. Each RDY input is valid only when its **address enable** ($\overline{AEN1}$ or $\overline{AEN2}$) is **low**, so two bus masters can each have their own ready line. The two gated signals are ORed.
2. **Synchronization.** The 8086 requires READY to meet set-up and hold times relative to CLK, but RDY from a device can change at any time. The 8284A therefore passes the ORed signal through flip-flops clocked by its own CLK:
   - $\overline{ASYNC}$ = **0**: **two stages** of synchronization (FF1 on the rising edge, FF2 on the falling edge of CLK). Used when RDY is **asynchronous** to CLK.
   - $\overline{ASYNC}$ = **1**: **one stage** (FF2 only). Used when RDY is already synchronous with CLK.
3. **Output.** The synchronized signal is the **READY** output to the 8086.
4. **Effect on the bus cycle.** The 8086 samples READY at the end of T2 (start of T3). If READY = 0, it inserts **wait states (Tw)** after T3 and keeps the address/control signals active. When READY returns to 1, the cycle continues with T4. This lets fast processors work with slow memory and I/O.

The same chip also generates the CLK (crystal oscillator divided by 3, 33% duty cycle) and a synchronized RESET from $\overline{RES}$ through a Schmitt trigger and flip-flop, which is why it is drawn as one block with READY.
