---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Quantization error is the difference between the real sample value and the voltage of the digital level it is mapped to. With step size Vref/2^n and floor truncation it lies between 0 and 1 LSB (+-1/2 LSB with rounding); for the ATmega32 (10-bit, 5 V) the step is 4.88 mV."
sources: ["EHP 6. AVR ADC slides 7-12, 16 (quantizing, step size, floor rule, 4.88 mV)"]
---
An $n$-bit ADC can produce only $2^n$ output codes, but the analog input can take any value. Each sample is therefore replaced by one of the discrete levels, separated by the **step size**

$$\Delta = \frac{V_{ref}}{2^n}, \qquad D = \left\lfloor \frac{V_{in}}{\Delta} \right\rfloor$$

The **quantization error** is the difference between the true sample and the voltage of the level it is converted to:

$$e_q = V_{in} - D\,\Delta, \qquad 0 \le e_q < \Delta\ (1\ \text{LSB})$$

(If the ADC rounds to the nearest level, $|e_q| \le \frac{1}{2}\Delta$.)

```text
 code                                  (2-bit ADC, Vref = 5 V)
  11 |                    ________
  10 |             ______|           staircase = ADC output
  01 |      ______|                  ramp      = true input
  00 |_____|
     +-----+------+------+------+--> Vin
     0   1.25    2.5   3.75     5 V
```

*Example:* 2-bit ADC, $V_{ref}$ = 5 V: $\Delta = 1.25$ V. An input of 3.0 V gives code 10 (2.5 V), so $e_q$ = 0.5 V. The error cannot be removed, only reduced by using more bits: the ATmega32's 10-bit ADC at 5 V has $\Delta = 5/1024 = 4.88$ mV, so its quantization error is less than 4.88 mV.
