---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "RDY1 gated by AEN1' and RDY2 gated by AEN2' are ORed and synchronized to CLK by one (ASYNC' = 1) or two (ASYNC' = 0) flip-flops; the output READY goes to the 8086, which inserts wait states (Tw) while READY = 0 at the end of T2/T3."
sources: ["MHE 8086 Hardware Specifications slides 11, 16-17 (8284A, READY)", "Brey, The Intel Microprocessors, Sec. 9-3 and 9-5 (8284A clock generator, READY and wait states)"]
changes:
  - "2026-10-12: replaced the ASCII drawing by a TikZ block diagram of the READY and CLK logic (answer unchanged)"
---
**Part of the 8284A block diagram used for READY**

![8284A READY logic: gated RDY inputs, two synchronizing flip-flops selected by ASYNC', and the clock section](figures/ready.png)

**How READY is generated**

1. **Inputs from the system.** A slow memory or I/O device (through its wait-state logic) drives **RDY1** or **RDY2** high when it is ready. Each RDY input is valid only when its **address enable** ($\overline{AEN1}$ or $\overline{AEN2}$) is **low**, so two bus masters can each have their own ready line. The two gated signals are ORed.
2. **Synchronization.** The 8086 requires READY to meet set-up and hold times relative to CLK, but RDY from a device can change at any time. The 8284A therefore passes the ORed signal through flip-flops clocked by its own CLK:
   - $\overline{ASYNC}$ = **0**: **two stages** of synchronization (FF1 on the rising edge, FF2 on the falling edge of CLK). Used when RDY is **asynchronous** to CLK.
   - $\overline{ASYNC}$ = **1**: **one stage** (FF2 only). Used when RDY is already synchronous with CLK.
3. **Output.** The synchronized signal is the **READY** output to the 8086.
4. **Effect on the bus cycle.** The 8086 samples READY at the end of T2 (start of T3). If READY = 0, it inserts **wait states (Tw)** after T3 and keeps the address/control signals active. When READY returns to 1, the cycle continues with T4. This lets fast processors work with slow memory and I/O.

The same chip also generates the CLK (crystal oscillator divided by 3, 33% duty cycle) and a synchronized RESET from $\overline{RES}$ through a Schmitt trigger and flip-flop, which is why it is drawn as one block with READY.
