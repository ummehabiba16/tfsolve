---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Mode 1: CPOL = 0 (SCK idles low), CPHA = 1: MOSI/MISO change on each rising (leading) edge and both devices sample on each falling (trailing) edge; 8 pulses per byte while SS' is low."
sources: ["EHP Serial Communication slides 94-95, 110-115 (CPOL, CPHA, Table 59 and Figure 68)"]
---
**SPI mode 1** (CPOL = 0, CPHA = 1): SCK is **low when idle**; the **leading (rising) edge is the setup edge** and the **trailing (falling) edge is the sample edge**.

```text
SS'    --+                                                  +--
         |__________________________________________________|
SCK        +--+  +--+  +--+  +--+  +--+  +--+  +--+  +--+  +
       ____|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|___
MOSI   ----Xb7===Xb6===Xb5===Xb4===Xb3===Xb2===Xb1===Xb0===X---
MISO   ----Xb7===Xb6===Xb5===Xb4===Xb3===Xb2===Xb1===Xb0===X---
           s  v  s  v  s  v  s  v  s  v  s  v  s  v  s  v
       s = setup (rising, leading edge): MOSI/MISO change
       v = sample (falling, trailing edge): bits are read
```

**Sequence**

1. The master pulls SS' low; SCK is low (idle).
2. **Rising edge** of each pulse: master and slave shift the next bit onto MOSI and MISO (setup). The first bit (b7, MSB first) appears at the first rising edge.
3. **Falling edge**: the master samples MISO and the slave samples MOSI, in the middle of the bit's valid time.
4. After 8 pulses SCK stays low, the bytes are exchanged and SPIF is set; the master raises SS'.
