---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Phase correct PWM, TOP = ICR1 = 1000, prescaler 64 (64 us tick): f = 1 MHz / (2 x 64 x 1000) = 7.8125 Hz (period 128 ms); OC1A high while TCNT1 < 200, duty = 200/1000 = 20% (taking the overwritten register as OCR1A)."
sources: ["EHP Timer_Part_2 slides 39-44, 47 (phase correct PWM)", "ATmega32 datasheet, Timer/Counter1, Phase Correct PWM Mode (f = fclk / (2 N TOP))"]
---
*Note:* the register is printed as OCR1B with an "A" written over the B. Since the output asked about is OC1A, the value is taken as **OCR1A = 200**. Clock 1 MHz (paper default).

**Mode.** WGM = 1010 is **phase correct PWM with TOP = ICR1 = 1000**: TCNT1 counts 0 $\to$ 1000 $\to$ 0. Tick = $64/1\,\text{MHz} = 64\ \mu s$.

**Frequency.** One period is $2 \times TOP$ ticks:

$$T = 2 \times 1000 \times 64\ \mu s = 128\ \text{ms}, \qquad f_{OC1A} = \frac{f_{clk}}{2\,N\,TOP} = \frac{10^6}{2 \times 64 \times 1000} = \mathbf{7.8125\ Hz}$$

**Duty cycle.** OC1A is cleared at the up-count match and set at the down-count match, so it is **high while TCNT1 < 200** (around BOTTOM):

$$t_{high} = 2 \times 200 \times 64\ \mu s = 25.6\ \text{ms}, \qquad D = \frac{OCR1A}{ICR1} = \frac{200}{1000} = \mathbf{20\%}$$

```text
  1000|              ***                           ***
      |            **   **                       **   **
      |         ***       ***                 ***       ***
      |       **             **             **             **
      |    ***                 ***       ***                 ***
   200|  **                       **   **                       **   **
     0|**                           ***                           ***
OC1A 1|---                         -----                         -----
     0|   -------------------------     -------------------------     -
      (1 column = 4.27 ms; OC1A high 25.6 ms of every 128 ms)
```

(If OCR1B = 200 were meant literally, OCR1A would be unknown and OC1A's duty could not be found; OCR1B only affects OC1B.)
