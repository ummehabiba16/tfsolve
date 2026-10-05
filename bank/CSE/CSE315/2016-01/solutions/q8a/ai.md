---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Timer clock 4 MHz / 8 = 500 kHz (2 us). (i) 1 kHz: 500 ticks, TOP = 499; 30% = 150 ticks high, OCR1 = 149 (non-inverting). (ii) Fast PWM needs TOP >= 3 (2-bit minimum). 25%: TOP = 3, OCR1 = 0 gives 500 kHz/4 = 125 kHz. 50%: also limited by TOP >= 3: TOP = 3, OCR1 = 1, so still 125 kHz (TOP = 1 would give 250 kHz but is below the minimum resolution)."
sources: ["EHP Timer_Part_2 slides 31-38, 57 (fast PWM frequency f = fclk/(N(1+TOP)), duty cycle, ICR1 = period - 1)", "ATmega32 datasheet, Timer/Counter1 Fast PWM (minimum resolution 2 bits, TOP = 3)"]
---
Timer clock: $f_T = 4\ \text{MHz}/8 = 500$ kHz, one tick = 2 µs. In fast PWM (non-inverting), the period is TOP + 1 ticks and OC1x is high for OCR1x + 1 ticks:

$$f = \frac{f_T}{1 + TOP}, \qquad D = \frac{OCR1 + 1}{TOP + 1}$$

**(i) 1 kHz, 30% duty**

$$1 + TOP = \frac{500\ \text{kHz}}{1\ \text{kHz}} = 500 \ \Rightarrow\ \mathbf{TOP = 499}\ (\text{e.g. ICR1, WGM = 1110})$$

$$OCR1 + 1 = 0.3 \times 500 = 150 \ \Rightarrow\ \mathbf{OCR1 = 149}$$

(High time 300 µs of a 1000 µs period.)

**(ii) Highest frequency**

The highest frequency needs the smallest TOP that still gives the required duty cycle exactly. Fast PWM has a **minimum resolution of 2 bits: TOP $\ge$ 3**.

- **25% duty:** $(OCR1 + 1)/(TOP + 1) = 1/4$. Smallest choice: **TOP = 3, OCR1 = 0** (high for 1 of 4 ticks).

$$f_{max} = \frac{500\ \text{kHz}}{4} = \mathbf{125\ kHz}$$

- **50% duty:** $(OCR1 + 1)/(TOP + 1) = 1/2$ would allow TOP = 1, OCR1 = 0 (250 kHz), but TOP = 1 is below the minimum. With TOP = 3, OCR1 = 1 gives 50%:

$$f_{max} = \frac{500\ \text{kHz}}{4} = \mathbf{125\ kHz}$$

So increasing the duty to 50% does **not** raise the maximum frequency; it stays at 125 kHz.

*Note:* if the 2-bit minimum is ignored, the 50% case could reach 250 kHz (TOP = 1, OCR1 = 0).
