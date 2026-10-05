---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Left adjusted: ADCH holds the top 8 bits. (i) ADCH only = 8-bit result: step = 4 V / 2^8 = 15.625 mV. (ii) ADCH and ADCL = full 10 bits: step = 4 V / 2^10 = 3.906 mV."
sources: ["EHP 6. AVR ADC slides 9, 16, 26-28 (step size = Vref / 2^n, ADLAR, reading only ADCH)"]
---
With ADLAR = 1 (left justified) the 10-bit result is stored as ADCH = bits 9-2 and ADCL bits 7-6 = bits 1-0.

**(i) Reading only ADCH** gives the 8 most significant bits, so the converter behaves as an **8-bit** ADC:

$$\text{step} = \frac{V_{ref}}{2^8} = \frac{4\ \text{V}}{256} = \mathbf{0.015625\ V} = 15.625\ \text{mV}$$

**(ii) Reading ADCL and ADCH** gives all **10 bits**:

$$\text{step} = \frac{V_{ref}}{2^{10}} = \frac{4\ \text{V}}{1024} = \mathbf{0.00390625\ V} \approx 3.906\ \text{mV}$$

Reading only ADCH is faster (one register read) but 4 times coarser.
