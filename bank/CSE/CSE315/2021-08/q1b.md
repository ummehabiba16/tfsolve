---
marks: 20
topics: [clock-generator]
kind: analysis
source: {page: 42}
---
Consider the following internal block diagram of a clock generator (Figure 1(b) - 1).

![Figure 1(b) - 1: internal block diagram of the 8284A clock generator (RES, X1/X2 crystal oscillator, F/C, EFI, CSYNC, divide-by-3 and divide-by-2 sync counters, RDY1/AEN1, RDY2/AEN2, ASYNC, FF1/FF2; outputs RESET, OSC, PCLK, CLK, READY)](figures/q1b-1.png)

The above clock generator is used in the following design (Figure 1(b) - 2).

![Figure 1(b) - 2: 30 MHz crystal on X1/X2, F/C tied to +5V, CSYNC, RES with 10K/10uF/diode reset circuit; CLK and RESET to the 8086 or 8088, RESET also to system reset](figures/q1b-2.png)

Now, you need to pinpoint in case you find any flaw in the above design. If so, then you need to elaborate and justify how that flaw(s) can be fixed. In case you think that the above design is flawless, you need to explicitly mention that. Unless you mention anything, your answer will be treated as a blank answer.

You need to justify your answer.
