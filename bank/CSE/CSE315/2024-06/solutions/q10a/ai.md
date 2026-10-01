---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "With ADLAR = 1, reading only ADCH drops D1-D0, so up to 3 LSB are lost: max error = 3 x Vref/1024 (about 14.6 mV at Vref = 5 V, about 0.29% of Vref)."
sources: ["EHP 6. AVR ADC slides 16, 26 (step size, ADCH/ADCL, max error reading only ADCH)"]
---
With ADLAR = 1 (left justified): ADCH = D9 ... D2 and ADCL = D1 D0 followed by 6 unused bits.

Reading **only ADCH** ignores D1 and D0. The ignored part can be anything from $00_2$ to $11_2$, so the reading can be too low by at most

$$11_2 = 3\text{ steps}$$

One step (resolution) $= V_{ref}/1024$. With the default $V_{ref} = 5$ V:

$$\text{step} = \frac{5}{1024} = 4.88\text{ mV}$$

$$\text{Max error} = 3\times\frac{V_{ref}}{1024} = 3\times4.88\text{ mV} = \mathbf{14.65\ mV}$$

As a fraction of full scale this is $3/1024 \approx 0.29\%$ of $V_{ref}$. In effect the ADC becomes 8-bit: one 8-bit step is $4\times 4.88$ mV, and the truncation error is just under one such step.
