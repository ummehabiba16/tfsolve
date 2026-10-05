---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "10-bit step = 5/1024 = 4.88 mV. (i) Left adjusted: ADCH = bits 9-2, the 2 LSBs are lost, max error = 3 LSB = 14.65 mV (< one 8-bit step of 19.53 mV). (ii) Right adjusted: ADCH = bits 9-8 only, the 8 LSBs are lost, max error = 255 LSB = 1.245 V (< one 2-bit step of 1.25 V)."
sources: ["EHP 6. AVR ADC slides 16, 26-28 (10-bit result, ADCH/ADCL, ADLAR, maximum error when reading only ADCH)"]
---
The 10-bit ADC with $V_{ref}$ = 5 V has a step (1 LSB) of

$$\Delta = \frac{5}{1024} = 4.883\ \text{mV}$$

Reading only ADCH throws away the bits that are in ADCL. The largest error is when all the discarded bits are 1.

**(i) Left adjusted (ADLAR = 1):** ADCH = bits 9-2, ADCL holds bits 1-0. Two bits are lost, worth at most $11_2 = 3$ LSB:

$$e_{max} = 3 \times 4.883\ \text{mV} = \mathbf{14.65\ mV}$$

(Equivalently, ADCH alone is an 8-bit result with step $5/256 = 19.53$ mV; the error is always less than one such step.)

**(ii) Right adjusted (ADLAR = 0):** ADCH holds only bits 9-8, ADCL holds bits 7-0. Eight bits are lost, worth at most $1111\,1111_2 = 255$ LSB:

$$e_{max} = 255 \times 4.883\ \text{mV} = \mathbf{1.245\ V}$$

(ADCH alone is then a 2-bit result with step 1.25 V, which is almost useless.)

*Note:* these are the errors caused by not reading ADCL. The ADC's own quantization error (less than 1 LSB = 4.88 mV) comes on top: totals are below 19.53 mV and 1.25 V respectively.
