---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "1 us per tick; OC1A is high while TCNT1 < 100, i.e. 200 us around each BOTTOM. ICR1 is not double-buffered, so each new TOP acts at once: in steady state the counter peaks at 200, 300 and 500 (400 and 600 are written while it is counting down) and the waveform repeats every 2000 us with three 200 us pulses: cycles of 400, 600 and 1000 us (duty 50%, 33.3%, 20%); repetition 500 Hz, average pulse rate 1.5 kHz, overall duty 30%."
sources: ["EHP Timer_Part_2 slides 39-47 (phase correct PWM, frequency and duty cycle)", "ATmega32 datasheet, Timer/Counter1 Phase Correct PWM mode (ICR1 not double buffered; f = fclk / (2 N TOP))"]
---
**Basic relations** (1 MHz, no prescaler: 1 tick = 1 µs; phase correct, non-inverting, OCR1A = 100)

- TCNT1 counts 0 $\to$ TOP $\to$ 0. OC1A is cleared at the match on the way up and set at the match on the way down, so **OC1A is high while TCNT1 < 100**: 100 µs before and 100 µs after each BOTTOM, a **200 µs pulse** per cycle.
- With a constant TOP: $T = 2 \times TOP$ µs, $f = 10^6/(2\,TOP)$, duty $= OCR1A/TOP$.

| ICR1 (TOP) | Period | Frequency | Duty cycle |
|:-:|:-:|:-:|:-:|
| 200 | 400 µs | 2500 Hz | 50% |
| 300 | 600 µs | 1667 Hz | 33.3% |
| 400 | 800 µs | 1250 Hz | 25% |
| 500 | 1000 µs | 1000 Hz | 20% |
| 600 | 1200 µs | 833 Hz | 16.7% |

**What actually happens.** Each ICR1 value is kept for only 400 µs, which is shorter than most of the periods above, and in mode 1010 **ICR1 is not double-buffered** (the new TOP is used immediately; only OCR1A is updated at TOP). Simulating the counter tick by tick (loop overhead ignored), it settles into a pattern that repeats every $5 \times 400 = 2000$ µs:

| Time in the 2 ms pattern | TOP in force when the counter turns | Counter cycle | High time | Duty |
|:--|:-:|:-:|:-:|:-:|
| 0-400 µs | 200 (peak at 200 µs) | 400 µs | 200 µs | 50% |
| 400-1000 µs | 300 (peak at 700 µs) | 600 µs | 200 µs | 33.3% |
| 1000-2000 µs | 500 (peak at 1500 µs; 400 is passed while counting up, 600 is written while counting down) | 1000 µs | 200 µs | 20% |

```text
TCNT1                (1 column = 50 us)
    500|                              *                                       *
       |                             * *                                     * *
       |                            *   *                                   *   *
       |                           *     *                                 *     *
    300|              *           *       *                   *           *       *
       |             * *         *         *                 * *         *         *
    200|    *       *   *       *           *       *       *   *       *           *
       |   * *     *     *     *             *     * *     *     *     *             *
OCR 100|  *   *   *       *   *               *   *   *   *       *   *               *
       | *     * *         * *                 * *     * *         * *                 *
      0|*       *           *                   *       *           *                   *
 OC1A 1|--     ---         ---                 ---     ---         ---                 --
      0|  -----   ---------   -----------------   -----   ---------   -----------------
        0       400         1000                2000    2400        3000                4000 us
```

**Result**

- The waveform is periodic with period **2000 µs** (frequency **500 Hz**) and contains **3 pulses** per period, so the average pulse rate is 1.5 kHz.
- Every pulse is 200 µs wide, so the overall duty cycle is $3 \times 200 / 2000 = $ **30%**. Within the pattern the individual cycles have 50%, 33.3% and 20% duty.

*Note:* if each ICR1 value were assumed to last whole cycles (the simple reading), the output would step through the five rows of the first table: 2500 Hz/50%, 1667 Hz/33.3%, 1250 Hz/25%, 1000 Hz/20%, 833 Hz/16.7%. With `_delay_us(400)` the timer cannot complete those cycles, which is why the simulated pattern differs.
