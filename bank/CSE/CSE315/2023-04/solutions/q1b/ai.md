---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Sampling error: information lost between sampling instants (and aliasing if fs < 2 fmax). Quantization error: difference between a sample and its discrete level, at most one step (floor) or half a step (rounding); 4.88 mV step for the 10-bit ATmega32 ADC at 5 V."
sources: ["EHP 6. AVR ADC slides 7-12 (sampling, quantizing, step size = Vref/2^n)", "EHP 6. AVR ADC slide 16 (10-bit, 4.88 mV step)", "Mazidi, AVR Microcontroller and Embedded Systems, Ch. 13 (ADC)"]
---
A-to-D conversion has two steps: **sampling** approximates the time axis and **quantization** approximates the voltage axis. Each step adds its own error.

**(i) Sampling error**

The analog signal is read only at regularly spaced instants $t = 0, T_s, 2T_s, \dots$ (sampling period $T_s = 1/f_s$). Whatever the signal does **between** two samples is lost. If we rebuild the signal from the samples (holding each value until the next sample), the result is a staircase that differs from the true signal. That difference is the sampling error.

```text
 V       true signal (smooth curve)  vs  held samples (flat steps)
 |               ____
 |          ____|    |____           the gap between the curve and
 |     ____|              |____      the steps is the sampling error
 |____|                        |__
 +----+----+----+----+----+----+--> t
      Ts  2Ts  3Ts  4Ts  5Ts  6Ts    (one sample every Ts)
```

- The error grows when the signal changes fast compared with $f_s$.
- If $f_s < 2 f_{max}$ (Nyquist rate), a fast signal is seen as a slower, wrong one (**aliasing**) and cannot be recovered at all. Example: a 9 Hz sine sampled at 10 Hz gives samples that look like a 1 Hz sine.
- It is reduced by sampling faster ($f_s \ge 2 f_{max}$, in practice much higher). The ATmega32's sample-and-hold keeps the input constant during the conversion, so the value converted is the value at the sampling instant.

**(ii) Quantization error**

Each sample is a real value, but an $n$-bit ADC has only $2^n$ levels with step size

$$\Delta = \frac{V_{ref}}{2^n}$$

The sample is replaced by the level just below it, $D = \lfloor V_{in}/\Delta \rfloor$ (slide convention). The quantization error is the difference between the true sample and the voltage of its code:

$$e_q = V_{in} - D\,\Delta, \qquad 0 \le e_q < \Delta \ (\text{1 LSB})$$

(With rounding to the nearest level the error is at most $\pm\frac{1}{2}\Delta$.)

```text
 code                                  (2-bit ADC, Vref = 5 V)
  11 |                    ________
  10 |             ______|           staircase = ADC output
  01 |      ______|                  ramp      = true input
  00 |_____|
     +-----+------+------+------+--> Vin
     0   1.25    2.5   3.75     5 V

 e_q
 1.25 |    /|    /|    /|    /|      error = input - level of its code:
      |   / |   / |   / |   / |      a sawtooth between 0 and 1 step
    0 |  /  |  /  |  /  |  /  |
      +-----+-----+-----+-----+--> Vin
```

*Example:* a 2-bit ADC with $V_{ref} = 5$ V has $\Delta = 1.25$ V; an input of 3.0 V gives code 10 (2.5 V), so $e_q = 0.5$ V. The ATmega32's 10-bit ADC with $V_{ref} = 5$ V has $\Delta = 5/1024 = 4.88$ mV, so its quantization error is below 4.88 mV. Using more bits (smaller $\Delta$) reduces it.
