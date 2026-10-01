---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Normal mode, 1 MHz: baud = f/(16(UBRR+1)); UBRR = 0 gives max 62500 bps; UBRR = 4095 (12 bits) gives min = about 15.26 bps."
sources: ["EHP Serial Communication slides 23-26 (UBRRH/UBRRL, baud rate formula)"]
---
In normal (U2X = 0) asynchronous mode:

$$\text{baud rate} = \frac{f_{osc}}{16\,(UBRR+1)}$$

UBRR is a **12-bit** value (UBRRH[3:0] : UBRRL), so $0\le UBRR\le 4095$.

**Maximum** (UBRR = 0):

$$\frac{10^{6}}{16\times1} = \mathbf{62500\ bps}$$

**Minimum** (UBRR = 4095 = 0x0FFF):

$$\frac{10^{6}}{16\times4096} = \mathbf{15.26\ bps}$$

(In practice the slides quote about 960 bps to 57.6 kbps as typical rates. The values above are the limits the registers allow.)
