---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "ADMUX = 11010000: Vref = 2.56 V, right adjusted, differential ADC0 - ADC1 with gain 1: ADC = (2 - 1) x 1 x 512 / 2.56 = 200 = 0x0C8, so ADCH = 0x00, ADCL = 0xC8. (Handwritten 11001001: ADC1 - ADC0, gain 10 gives -2000, clipped to -512 = 0x200: ADCH = 0x02, ADCL = 0x00.)"
sources: ["EHP 6. AVR ADC slides 20-27 (ADMUX, REFS, ADLAR, MUX4:0 table, differential result formula, two's complement 0x200-0x1FF)"]
---
**Decode ADMUX = 1101 0000**

| Bits | Value | Meaning |
|:--|:-:|:--|
| REFS1:0 (7-6) | 11 | Internal **2.56 V** reference |
| ADLAR (5) | 0 | Result **right adjusted** (ADCH holds bits 9-8, ADCL bits 7-0) |
| MUX4:0 (4-0) | 10000 | **Differential**: positive = ADC0, negative = ADC1, **gain 1x** |

**Conversion.** For differential channels

$$ADC = \frac{(V_{POS} - V_{NEG}) \times GAIN \times 512}{V_{REF}} = \frac{(2 - 1) \times 1 \times 512}{2.56} = 200$$

The result is a 10-bit two's complement number; +200 = 00 1100 1000 = 0x0C8. Right adjusted:

| Register | Bits | Value |
|:--|:--|:-:|
| ADCH | 0000 00**00** | **0x00** |
| ADCL | 1100 1000 | **0xC8** |

*Note:* the scan has "11001001" handwritten above the printed value. If that is the intended ADMUX: REFS = 11 (2.56 V), ADLAR = 0, MUX = 01001 means positive = ADC1, negative = ADC0, gain 10x. Then $ADC = (1-2)\times10\times512/2.56 = -2000$, which is outside the range $-512$ to $+511$, so the result saturates at $-512$ = 0x200: **ADCH = 0x02, ADCL = 0x00**.
