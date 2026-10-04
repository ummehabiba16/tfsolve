---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Leading edge falling = setup and trailing edge rising = sample is SPI mode 3 (CPOL = 1, CPHA = 1): SCK idles high; MOSI/MISO change on every falling edge and both devices sample on every rising edge."
sources: ["EHP Serial Communication slides 94-95, 110-115 (CPOL, CPHA, data modes, Table 59, Figure 68)"]
---
**Which mode?** The *leading* edge of each SCK pulse is **falling**, so SCK idles **high**: **CPOL = 1**. Data is **set up on the leading edge** and **sampled on the trailing edge**: **CPHA = 1**. This is **SPI mode 3**.

| | Leading edge | Trailing edge |
|:--|:--|:--|
| CPOL = 1, CPHA = 1 (mode 3) | Setup (falling) | Sample (rising) |

**Timing diagram** (8-bit transfer, MSB first, DORD = 0)

```text
SS'    --+                                                  +--
         |__________________________________________________|  
SCK    ----+  +--+  +--+  +--+  +--+  +--+  +--+  +--+  +--+---
           |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|      
MOSI   ----Xb7===Xb6===Xb5===Xb4===Xb3===Xb2===Xb1===Xb0===X---
MISO   ----Xb7===Xb6===Xb5===Xb4===Xb3===Xb2===Xb1===Xb0===X---
           s  ^  s  ^  s  ^  s  ^  s  ^  s  ^  s  ^  s  ^      
       s = setup (falling edge): MOSI/MISO change to the next bit
       ^ = sample (rising edge): master reads MISO, slave reads MOSI
```

**Sequence**

1. The master pulls **SS' low** to select the slave. SCK is still high (idle, CPOL = 1).
2. **First falling (leading) edge:** master and slave both put their first bit (b7) on MOSI and MISO (**setup**).
3. **First rising (trailing) edge:** the master **samples** MISO and the slave **samples** MOSI. The bit is in the middle of its valid window, so it is stable.
4. Steps 2-3 repeat for b6, ..., b0: change on every falling edge, sample on every rising edge.
5. After 8 clock pulses SCK stays high, the bytes have been exchanged, SPIF is set, and the master raises **SS'** to end the transfer.

(With LSB first, DORD = 1, the bit order is b0 ... b7; the edges are the same.)
