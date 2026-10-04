---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Fast PWM with TOP = OCR1A = 1999, prescaler 8: f = 1 MHz / (8 x 2000) = 62.5 Hz (period 16 ms). Inverting OC1B (set on match, clear at BOTTOM) is low for counts 0-199 and high for 200-1999: duty = 1800/2000 = 90%."
sources: ["EHP Timer_Part_2 slides 31-38 (fast PWM, frequency and duty cycle)", "ATmega32 datasheet, Timer/Counter1, Fast PWM Mode (f = fclk / (N (1 + TOP)))"]
---
**Mode.** WGM = 1111 is **fast PWM with TOP = OCR1A = 1999**: TCNT1 counts 0 $\to$ 1999 and restarts at 0 (single slope). Clock 1 MHz (paper default), prescaler 8: tick = $8\ \mu s$.

**Frequency.** One period is TOP + 1 = 2000 ticks:

$$T = 2000 \times 8\ \mu s = 16\ \text{ms}, \qquad f_{OC1B} = \frac{f_{clk}}{N\,(1 + TOP)} = \frac{10^6}{8 \times 2000} = \mathbf{62.5\ Hz}$$

**Duty cycle.** OC1B is **cleared at BOTTOM** and **set on compare match** with OCR1B = 199 (inverting mode):

- counts 0 to 199 (200 ticks): OC1B **low**;
- counts 200 to 1999 (1800 ticks): OC1B **high**.

$$D = \frac{TOP - OCR1B}{TOP + 1} = \frac{1999 - 199}{2000} = \frac{1800}{2000} = \mathbf{90\%}$$

High time = $1800 \times 8\ \mu s = 14.4$ ms, low time = 1.6 ms.

```text
  1999|              **              **              **
      |            **              **              **
      |         ***             ***             ***
      |       **              **              **
      |    ***             ***             ***
   199|  **              **              **
     0|**              **              **
OC1B 1|  --------------  --------------  --------------
     0|--              --              --
      (1 column = 1 ms; OC1B low 1.6 ms, high 14.4 ms of every 16 ms)
```
