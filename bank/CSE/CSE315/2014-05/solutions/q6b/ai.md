---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Non-pipelined read: T1: ADS' low, valid A31-A3, BE7'-BE0', M/IO' and W/R' = 0; T2: the Pentium samples BRDY' at the end of each T2 (extra T2s are wait states); when BRDY' is low the 64-bit data on D63-D0 is latched and the cycle ends. Minimum 2 clocks."
sources: ["Brey, The Intel Microprocessors, Ch. 18 (Pentium memory read cycle, ADS, BRDY, NA)"]
---
```text
         T1      T2      T2      T1 (next cycle)
CLK     +---+   +---+   +---+   +---+   +---+
        |   |___|   |___|   |___|   |___|   |___
ADS'    +       +-------------------------------
        |_______|
A31-A3  X=======================X---------------  also BE7-BE0, M/IO, W/R = 0
BRDY'   ------------------+     +---------------
                          |_____|
D63-D0  ..................<====>
                               ^ data latched (end of T2, BRDY' low)
```

1. **T1:** the Pentium drives the address **A31-A3** and byte enables **$\overline{BE7}$-$\overline{BE0}$**, M/$\overline{IO}$ = 1 (memory) and **W/$\overline{R}$ = 0** (read), and pulses **$\overline{ADS}$** (address status) low for one clock to say a new valid bus cycle has started.
2. **T2:** the memory system works; the Pentium samples **$\overline{BRDY}$** (burst ready) at the **end of each T2**. If $\overline{BRDY}$ is high, another T2 (a wait state) follows.
3. When $\overline{BRDY}$ is low at the end of T2, the Pentium **latches the data from D63-D0** and the cycle ends. The next cycle can start with a new T1.

A non-pipelined read takes at least **2 clocks** (T1 + T2); the figure shows one wait state. (In pipelined mode, $\overline{NA}$ lets the next address be sent before the current data arrives.)
