---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Timer clock = 1 MHz / 8 = 125 kHz (8 us). 1 kHz needs 125 ticks: TOP = 124 (e.g. ICR1, mode 14). 40% of 125 = 50 ticks high: OCR1A = 49 with non-inverting output (set at BOTTOM, clear on match)."
sources: ["EHP Timer_Part_2 slides 31-38, 49-52, 57 (fast PWM frequency and duty cycle, ICR1 = period - 1, OCR1A = high_time - 1)"]
---
**Timer clock:** $f_{T} = 1\ \text{MHz}/8 = 125$ kHz, so one tick = 8 µs.

**TOP (frequency).** In fast PWM, $f = \dfrac{f_{clk}}{N(1 + TOP)}$:

$$1 + TOP = \frac{10^6}{8 \times 1000} = 125 \ \Rightarrow\ \mathbf{TOP = 124}$$

(period = 125 ticks = 1 ms). Use mode 14 (WGM13:10 = 1110) with ICR1 = 124, so that OCR1A is free for the duty cycle.

**OCR1 (duty cycle).** Non-inverting mode (COM1A1:0 = 10): OC1A is set at BOTTOM and cleared at the compare match, so it is high for OCR1A + 1 ticks:

$$OCR1A + 1 = 0.4 \times 125 = 50 \ \Rightarrow\ \mathbf{OCR1A = 49}$$

High time = 50 $\times$ 8 µs = 400 µs of the 1000 µs period = 40%.

*Note:* with the slide shortcut (ICR1 = period, OCR1A = high time) the values would be TOP = 125 and OCR1A = 50, which gives 992 Hz. In inverting mode (COM1A1:0 = 11) the compare value would be 124 - 50 = 74.
