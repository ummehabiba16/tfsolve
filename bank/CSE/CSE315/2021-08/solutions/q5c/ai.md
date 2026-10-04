---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "(i) 2.1 x 1024 / 2.56 = 840 = 1101001000. (ii) 3.5 x 64 / 5 = 44.8 -> 44 = 101100."
sources: ["EHP 6. AVR ADC slides 9-12, 23 (step size, digital value = floor(V / step), ADC = Vin x 1024 / Vref)"]
---
For an $n$-bit ADC: step $= V_{ref}/2^n$ and the digital value is $\lfloor V_{in} / \text{step} \rfloor = \lfloor V_{in} \times 2^n / V_{ref} \rfloor$.

**(i) 10-bit, $V_{ref}$ = 2.56 V, $V_{in}$ = 2.1 V**

Step $= 2.56/1024 = 2.5$ mV.

$$D = \frac{2.1 \times 1024}{2.56} = 840 = \mathbf{11\,0100\,1000_2}\ (348_{16})$$

**(ii) 6-bit, $V_{ref}$ = 5 V, $V_{in}$ = 3.5 V**

Step $= 5/64 = 78.125$ mV.

$$D = \left\lfloor \frac{3.5 \times 64}{5} \right\rfloor = \lfloor 44.8 \rfloor = 44 = \mathbf{101100_2}$$

The remaining $0.8$ step ($0.8 \times 78.125 = 62.5$ mV) is the quantization error.
