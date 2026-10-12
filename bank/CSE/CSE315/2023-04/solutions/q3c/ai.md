---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Phase correct PWM, TOP = ICR1 = 2000, tick = 8 us: period = 2 x 2000 x 8 us = 32 ms, f = 31.25 Hz; OC1A is high while TCNT1 < 400, so duty = 400/2000 = 20% (high 6.4 ms)."
sources: ["EHP Timer_Part_2 slides 39-44, 47 (phase correct PWM, TCNT1/OC1x waveforms)", "ATmega32 datasheet, Timer/Counter1, Phase Correct PWM Mode (f = fclk / (2 N TOP))"]
changes:
  - "2026-10-12: replaced the ASCII sketch by a TikZ timing diagram drawn to scale; noted that OC1A is 0 until the first down-count match (answer unchanged)"
---
**Setup.** WGM = 1010 is **phase correct PWM with TOP = ICR1 = 2000**. TCNT1 counts up 0 $\to$ 2000 and then down 2000 $\to$ 0 (dual slope).

Assumption: system clock 1 MHz (paper default). With prescaler 8 the timer ticks every

$$t_{tick} = \frac{8}{1\ \text{MHz}} = 8\ \mu s$$

**Waveform.** OC1A is **cleared** on compare match while counting **up** and **set** on compare match while counting **down**. So OC1A is high while TCNT1 is below OCR1A = 400, around BOTTOM.

![Phase correct PWM, TOP = ICR1 = 2000, OCR1A = 400: TCNT1 triangle and OC1A](figures/pwm.png)

OC1A is 0 after reset, so the first up-count match at 3.2 ms leaves it at 0; the first high pulse starts at the down-count match at 28.8 ms.

OC1A goes **low** at the up-count match with 400 (t = 3.2 ms) and **high** again at the down-count match with 400 (t = 28.8 ms). It stays high through BOTTOM (t = 32 ms) until the next up-count match (t = 35.2 ms). The high pulse is centred on BOTTOM.

**Frequency**

One PWM period is a full up-down cycle of $2 \times TOP$ ticks:

$$T = 2 \times TOP \times t_{tick} = 2 \times 2000 \times 8\ \mu s = 32000\ \mu s = 32\ \text{ms}$$

$$f_{OC1A} = \frac{f_{clk}}{2\,N\,TOP} = \frac{10^6}{2 \times 8 \times 2000} = \mathbf{31.25\ Hz}$$

**Duty cycle**

High time = time TCNT1 spends below 400 = 400 ticks counting down + 400 ticks counting up:

$$t_{high} = 2 \times 400 \times 8\ \mu s = 6400\ \mu s = 6.4\ \text{ms}$$

$$D = \frac{t_{high}}{T} = \frac{6.4}{32} = \frac{OCR1A}{ICR1} = \frac{400}{2000} = \mathbf{20\%}$$
