---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "(i) step 10 mV, 1.45 V -> 145 = 10010001. (ii) step 4.88 mV, 4.17 V -> floor(854.016) = 854 = 1101010110."
sources: ["EHP 6. AVR ADC slides 9-12, 16 (step size, digital value = floor(V / step))"]
---
Digital value $D = \lfloor (V_{in} - V_{min}) / \text{step} \rfloor$ with step $= (V_{ref} - V_{min}) / 2^n$.

**(i)** 8-bit, $V_{ref}$ = 2.56 V: step $= 2.56/256 = 10$ mV.

$$D = \frac{1.45}{0.01} = 145 = \mathbf{1001\,0001_2}\ (91H)$$

**(ii)** 10-bit, $V_{ref}$ = 5 V: step $= 5/1024 = 4.883$ mV.

$$D = \left\lfloor \frac{4.17 \times 1024}{5} \right\rfloor = \lfloor 854.016 \rfloor = 854 = \mathbf{11\,0101\,0110_2}\ (356H)$$
