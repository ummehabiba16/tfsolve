---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "ADMUX = 11001011: internal 2.56 V ref, right-adjusted, ADC1(+) - ADC0(-) x200. ADC = 0.0064 x 200 x 512 / 2.56 = 256 = 0x100, so ADCH = 00000001 and ADCL = 00000000."
sources: ["EHP 6. AVR ADC slides 20-26 (ADMUX, reference selection, input source table, ADCH/ADCL)", "EHP 6. AVR ADC slide 25 (differential output in two's complement)"]
---
**Decode ADMUX = 1100 1011**

| REFS1 | REFS0 | ADLAR | MUX4..0 |
|:-:|:-:|:-:|:-:|
| 1 | 1 | 0 | 01011 |

- REFS1:0 = 11: **internal 2.56 V** reference, with an external capacitor at AREF. The capacitor at AREF matches this; the 5 V on AVCC only powers the ADC.
- ADLAR = 0: **right adjusted**.
- MUX4:0 = 01011: positive input **ADC1**, negative input **ADC0**, **gain 200x**.

**Input**

$$V_{ADC1}-V_{ADC0} = 4.0064-4.0000 = 0.0064\text{ V}$$

**Conversion** (differential, 10-bit two's complement):

$$ADC = \frac{(V_{POS}-V_{NEG})\times GAIN\times512}{V_{REF}} = \frac{0.0064\times200\times512}{2.56} = 256$$

$$256 = 01\,0000\,0000_2 = 0x100$$

256 is within the range $-512$ to $+511$ and positive, so the sign bit D9 = 0.

**Right adjusted (ADLAR = 0)**: ADCH holds D9-D8, and ADCL holds D7-D0.

| Register | Content |
|:--|:-:|
| ADCH | **0000 0001** |
| ADCL | **0000 0000** |
