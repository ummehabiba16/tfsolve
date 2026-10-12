---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Fast PWM, TOP = OCR1A = 0xFFF = 4095, N = 64, inverting OC1B (set on match, clear at BOTTOM): f = 1 MHz/(64 x 4096) = 3.81 Hz, duty = (4095 - 255)/4096 = 93.75%."
sources: ["EHP Timer_Part_2 slides 31-38 (fast PWM, inverting mode, frequency and duty cycle formulas)"]
changes:
  - "2026-10-12: replaced the ASCII sketch by a TikZ timing diagram drawn to scale (answer unchanged)"
---
Assumption: system clock = 1 MHz (default, as in the slides; it is not given).

**Frequency** (slide 37):

$$F_{generated} = \frac{F_{oscillator}}{(TOP+1)\times N} = \frac{10^{6}}{(4095+1)\times64} = \frac{10^{6}}{262144} = \mathbf{3.81\ Hz}$$

(period = 262.1 ms)

**Duty cycle.** OC1B is *set on compare match and cleared at BOTTOM*: inverting mode, COM1B1:0 = 11. It is low from BOTTOM (0) to OCR1B and high from OCR1B to TOP. From slide 38:

$$\text{Duty} = \frac{TOP - OCR1B}{TOP+1}\times100 = \frac{4095-255}{4096}\times100 = \frac{3840}{4096}\times100 = \mathbf{93.75\%}$$

![Fast PWM, TOP = OCR1A = 4095, OCR1B = 255, inverting OC1B (1 MHz / 64)](figures/pwm.png)

One tick is 64 $\mu$s. OC1B is low for the 256 ticks (16.384 ms) from BOTTOM to the OCR1B match and high for the remaining 3840 ticks (245.76 ms) up to TOP.

(For a 4 MHz clock the frequency would be 15.26 Hz; the duty cycle stays 93.75%.)
