---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Single precision: 1 sign, 8 exponent (bias 127), 23 fraction bits. Smallest positive normalized: 0 00000001 000...0 (0x00800000) = 1.0 x 2^-126 = 1.1755 x 10^-38. Smallest positive denormal: 0 00000000 000...01 (0x00000001) = 2^-23 x 2^-126 = 2^-149 = 1.4013 x 10^-45."
sources: ["Brey, The Intel Microprocessors, Ch. 14 (80x87 data formats: single-precision real, biased exponent, special values)"]
---
**80x87 single-precision (32-bit) format**

| Bit 31 | Bits 30-23 | Bits 22-0 |
|:-:|:-:|:-:|
| sign S | biased exponent E (bias 127) | fraction F (implied leading 1) |

Normal numbers: $(-1)^S \times 1.F \times 2^{E-127}$ with $E$ = 1 to 254. $E$ = 0 is used for zero and **denormals** ($0.F \times 2^{-126}$); $E$ = 255 for infinity/NaN.

**Smallest positive normalized number**

S = 0, E = 0000 0001 (smallest allowed), F = 0:

$$0\ 00000001\ 00000000000000000000000_2 = 0080\,0000H$$

$$1.0 \times 2^{1-127} = 2^{-126} \approx \mathbf{1.1755 \times 10^{-38}}$$

**Smallest positive value at all (denormal)**

The 80x87 also supports denormals: S = 0, E = 0, F = 000...001:

$$0\ 00000000\ 00000000000000000000001_2 = 0000\,0001H$$

$$2^{-23} \times 2^{-126} = 2^{-149} \approx \mathbf{1.4013 \times 10^{-45}}$$

So the smallest positive **normal** single-precision number is $2^{-126} \approx 1.18 \times 10^{-38}$; if denormals are counted, the smallest positive representable value is $2^{-149} \approx 1.4 \times 10^{-45}$ (with reduced precision). Both values were checked by decoding the bit patterns with a script.
