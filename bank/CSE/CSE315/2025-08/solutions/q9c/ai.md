---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Mode 10 (phase-correct PWM, TOP = ICR1 = 9999), clk/8 at 4 MHz: f = 4e6/(2 x 8 x 9999) = 25.0 Hz (period 39.996 ms); OC1A is high while TCNT1 < 1999, so duty = 1999/9999 = about 20%."
sources: ["EHP Timer_Part_2 slides 25, 39-43, 47 (mode table, phase correct PWM, COM1A1:0 = 10)", "EHP Timer_Part_2 slides 49-52 (producing a custom waveform)"]
---
**Decode the registers**

- `DDRD = 0b00100000`: PD5 = **OC1A** is an output.
- `TCCR1A = 0b10000010`: COM1A1:0 = **10**, COM1B1:0 = 00, WGM11:10 = **10**.
- `TCCR1B = 0b00010010`: WGM13:12 = **10**, CS12:10 = **010**, so clk/8.
- WGM13:10 = **1010**: **mode 10, Phase Correct PWM, TOP = ICR1** = 9999.
- COM1A1:0 = 10 in phase correct mode: **clear OC1A on compare match when up-counting, set OC1A on compare match when down-counting**.
- `PORTD |= 0b00100000` has no lasting effect: once COM1A is set, the compare unit drives OC1A.

**Timer clock**

$$f_{timer} = \frac{4\text{ MHz}}{8} = 500\text{ kHz},\quad 1\text{ tick} = 2\,\mu s$$

**Waveform.** TCNT1 counts 0 up to 9999 and back down to 0 (a triangle). OC1A is high while TCNT1 < OCR1A = 1999 and low while TCNT1 > 1999.

```text
TCNT1
 9999 |        /\                  /\
      |       /  \                /  \
      |      /    \              /    \
 1999 |----*/------\*----------*/------\*-------  OCR1A
      |   /          \        /          \
    0 |  /            \      /            \
      +--+---+--------+---+--+---+--------+---+--> t
         0  4ms       36  40 44           76  80 ms

OC1A
    1 |--+                   +-+                 +-
      |  |                   | |                 |
    0 |  +-------------------+ +-----------------+
         ^ clear (up-count)  ^ set (down-count)
```

Up-count from 0 to 1999 takes $1999\times2\,\mu s \approx 4$ ms. Down-count from 1999 to 0 at the end of each period also takes about 4 ms. So the high pulse ($\approx 8$ ms) is centred on BOTTOM.

**Frequency**

$$T = 2\times TOP\times t_{tick} = 2\times9999\times2\,\mu s = 39.996\text{ ms}$$

$$f = \frac{f_{clk}}{2\times N\times TOP} = \frac{4\times10^{6}}{2\times8\times9999} = \mathbf{25.0\ Hz}$$

**Duty cycle**

$$\text{Duty} = \frac{2\times OCR1A}{2\times TOP}\times100 = \frac{1999}{9999}\times100 = \mathbf{19.99\% \approx 20\%}$$
