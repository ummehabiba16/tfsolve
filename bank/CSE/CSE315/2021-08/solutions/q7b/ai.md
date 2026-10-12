---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Not compatible. In Figure 7(b) each register sends from its MSB end and receives at its LSB end (shift left), which is MSB-first (DORD = 0). For LSB first (DORD = 1), MOSI must come from the master's LSB end into the slave's MSB end, and MISO from the slave's LSB end into the master's MSB end (shift right)."
sources: ["EHP Serial Communication slides 82-85, 93 (SPI master-slave interconnection, byte exchange, DORD)"]
changes:
  - "2026-10-12: replaced the ASCII drawing by a TikZ figure (answer unchanged)"
---
**Not compatible.**

In Figure 7(b), MOSI leaves the **master's MSB end** and enters the **slave's LSB end**, and MISO leaves the **slave's MSB end** and enters the **master's LSB end**. Each register shifts **left**: the MSB goes out first and the incoming bit fills the LSB. That is the **MSB-first** arrangement (DORD = 0), the same as the data-sheet figure.

With **DORD = 1 (LSB first)** the LSB must leave first, so the registers must shift **right**: the bit leaves from the **LSB end** and the received bit enters at the **MSB end**.

**Correct connection for LSB first**

![LSB-first SPI: both registers shift right; master LSB to slave MSB on MOSI, slave LSB to master MSB on MISO](figures/lsbfirst.png)

- **MOSI:** master **LSB** out $\to$ slave **MSB** in.
- **MISO:** slave **LSB** out $\to$ master **MSB** in.

After 8 clocks the bytes are exchanged as before, but bit 0 travels first. (In the real ATmega32 the DORD bit changes the internal shift direction; the pins MOSI/MISO/SCK are wired the same way.)
