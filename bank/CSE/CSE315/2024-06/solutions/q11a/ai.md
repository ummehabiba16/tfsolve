---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Normal: UBRR = 10.57, so 11: UBRRH = 0x00, UBRRL = 0x0B (5208 bps, -3.5% error). Double speed: UBRR = 22.15, so 22: UBRRH = 0x00, UBRRL = 0x16 (5435 bps, +0.64%). Double speed is better here."
sources: ["EHP Serial Communication slides 25-26, 52-53 (UBRR formula, double speed example)", "EHP Serial Communication slide 69 (double speed disadvantage)"]
---
**Normal mode (U2X = 0)**

$$UBRR = \frac{10^{6}}{16\times5400}-1 = 11.574-1 = 10.57 \approx 11$$

UBRRH = **0x00**, UBRRL = **0x0B**.

$$\text{Actual baud} = \frac{10^{6}}{16\times(11+1)} = 5208\text{ bps},\ \text{error} = -3.55\%$$

(With UBRR = 10: 5682 bps, an error of +5.2%, which is worse.)

**Double speed mode (U2X = 1)**

$$UBRR = \frac{10^{6}}{8\times5400}-1 = 23.148-1 = 22.15 \approx 22$$

UBRRH = **0x00**, UBRRL = **0x16**.

$$\text{Actual baud} = \frac{10^{6}}{8\times(22+1)} = 5435\text{ bps},\ \text{error} = +0.64\%$$

**Which is better?** **Double speed mode.** In normal mode the fractional part (10.57) is lost in rounding and the baud rate is off by about 3.5%, which is too large for reliable asynchronous reception (the 8 to 10 bits of a frame drift out of their sampling window). Double speed halves the divisor, so UBRR can be set more precisely (0.64% error), as in the slides' 9600 bps example. The drawback is that the receiver uses only 8 samples per bit instead of 16, so it needs an accurate clock and baud rate. With 0.64% error this is acceptable. The transmitter has no downside.
