---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "8-bit fast PWM (TOP = 255, period 256 us at 1 MHz), inverting: OC1A low for counts 0..OCR1A, high for OCR1A+1..255. The ISR swaps d between 31 and 224 at each match, and OCR1A takes the new value at TOP, so the cycles alternate: 0-256 us low 32 us then high 224 us; 256-512 low 225 us then high 31 us; 512-768 like the first; 768-1024 like the second."
sources: ["EHP Timer_Part_2 slides 31-38 (fast PWM, inverting mode, double-buffered OCR1A)"]
---
**Settings**

- TCCR1A = 1100 0001: COM1A1:0 = **11 (inverting)**: OC1A is **set at compare match** and **cleared at BOTTOM**; WGM11:10 = 01.
- TCCR1B = 0000 1001: WGM13:12 = 01, so WGM = 0101: **fast PWM 8-bit, TOP = 0xFF**; no prescaler at 1 MHz, so 1 tick = 1 µs and one PWM period = 256 µs.
- OCR1A is double-buffered: a value written in the ISR is used only from the next TOP (next period).

**Sequence of OCR1A values.** d = 31 at the start. At each compare match the ISR does `d = ~d` (31 = 0001 1111 becomes 1110 0000 = 224 and back) and writes it to OCR1A, effective from the next period. So the periods use OCR1A = 31, 224, 31, 224, ...

In inverting mode OC1A is low for TCNT1 = 0 to OCR1A and high for OCR1A + 1 to 255:

| Period | Time (µs) | OCR1A | Low | High | Duty (high) |
|:-:|:--|:-:|:--|:--|:-:|
| 1 | 0-256 | 31 | 0-32 | 32-256 | 224/256 = 87.5% |
| 2 | 256-512 | 224 | 256-481 | 481-512 | 31/256 = 12.1% |
| 3 | 512-768 | 31 | 512-544 | 544-768 | 87.5% |
| 4 | 768-1024 | 224 | 768-993 | 993-1024 | 12.1% |

```text
   255|               *               *               *               *
   224|            ***             ***             ***             ***
      |        ****            ****            ****            ****
      |     ***             ***             ***             ***
    31|  ***             ***             ***             ***
     0|**              **              **              **
OC1A 1|  --------------               -  --------------               -
     0|--              --------------- --              ---------------
       0               256             512             768             1024 t (us)
```

The output (pin 19, 0 V / 5 V) is a 256 µs period PWM whose duty cycle alternates between 87.5% and 12.1% every period.

*Note:* edges are given to within one clock (the output changes on the timer clock after the match).
