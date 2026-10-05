---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Step = 5/8 = 0.625 V. SAR: try 100 (2.5 V <= 3.22, keep 1); try 110 (3.75 V > 3.22, clear); try 101 (3.125 V <= 3.22, keep). Output = 101 (5 x 0.625 = 3.125 V)."
sources: ["EHP 6. AVR ADC slides 9-12 (quantizing with step size)", "Mazidi, AVR Microcontroller and Embedded Systems, Ch. 13 (successive approximation ADC)"]
---
For a 3-bit ADC with $V_{ref}$ = 5 V and $V_{gnd}$ = 0 V:

$$\Delta = \frac{5 - 0}{2^3} = 0.625\ \text{V}$$

**Successive approximation:** starting from the MSB, set each bit to 1, convert the trial code to a voltage (code $\times \Delta$) with the internal DAC, and keep the bit only if that voltage does not exceed $V_{in}$ = 3.22 V.

| Step | Bit tested | Trial code | DAC voltage | Compare with 3.22 V | Decision |
|:-:|:-:|:-:|:-:|:--|:--|
| 1 | b2 | 100 | 2.500 V | 2.5 $\le$ 3.22 | keep b2 = 1 |
| 2 | b1 | 110 | 3.750 V | 3.75 > 3.22 | clear b1 = 0 |
| 3 | b0 | 101 | 3.125 V | 3.125 $\le$ 3.22 | keep b0 = 1 |

$$V_{out} = \mathbf{101_2}\ (= 5,\ 5 \times 0.625 = 3.125\ \text{V})$$

Check: $\lfloor 3.22/0.625 \rfloor = \lfloor 5.15 \rfloor = 5 = 101_2$.
