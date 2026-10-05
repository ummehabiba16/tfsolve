---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Sampling: reading the analog signal at regular instants (fs >= 2 fmax to avoid aliasing). Quantization: mapping each sample to one of 2^n levels (error up to one step). Resolution: smallest input change that changes the code = step size Vref/2^n (ATmega32: 10 bits, 4.88 mV at 5 V). Conversion time: time for one conversion (ATmega32: 13 ADC clocks, 25 for the first; 65-260 us)."
sources: ["EHP 6. AVR ADC slides 7-16 (sampling, quantizing, step size, 10-bit ADC, 13 ADC cycles per conversion)"]
---
**Sampling.** The continuous analog signal is measured at **regularly spaced time instants** ($T_s = 1/f_s$); each measurement is a sample with a real value. To keep all the information the sampling frequency must be at least twice the highest signal frequency ($f_s \ge 2 f_{max}$, Nyquist), otherwise aliasing occurs. A sample-and-hold keeps the input constant during the conversion.

**Quantization.** Each sample is approximated by one of the $2^n$ discrete levels of an $n$-bit ADC and represented by a binary code: $D = \lfloor V_{in}/\Delta \rfloor$. The difference between the true value and the level (up to one step, or half a step with rounding) is the **quantization error**.

**Resolution.** The smallest change of input voltage that changes the output code, i.e. the **step size**:

$$\Delta = \frac{V_{ref}}{2^n}$$

More bits give finer resolution. ATmega32: 10-bit ADC, with $V_{ref}$ = 5 V the resolution is $5/1024 = 4.88$ mV (with 2.56 V: 2.5 mV).

**Conversion time.** The time the ADC needs to turn one sample into a digital value. For the ATmega32 successive-approximation ADC it is **13 ADC clock cycles** (25 for the first conversion after enabling, 13.5 when auto-triggered). With the recommended ADC clock of 50-200 kHz this is about 65-260 µs, which limits the maximum sampling rate (about 15 kSPS).
