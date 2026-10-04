---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Faults: TIMSK enables the overflow interrupt (bit 2) instead of input capture (bit 5); no sei(); main returns with no while(1); wrong header avr/inttypes.h. For a low-frequency wave also enable TOIE1, count overflows and use period = n x 65536 + ICR1 in a 32-bit variable."
sources: ["EHP Timer_Part_1 slides 29-37 (elapsed time with overflow count, input capture code, exercise for period > 2^16 us)", "EHP Timer_Part_1 slides 23-24 (TIMSK, TIFR)"]
---
**Faults in Figure 1(c)**

1. **Wrong interrupt enabled.** `TIMSK = 0b00000100` sets **TOIE1** (bit 2, overflow). The input capture interrupt is **TICIE1** (bit 5), so `TIMER1_CAPT_vect` never runs. Worse, an overflow interrupt with no ISR jumps to the default handler, which resets the MCU.
2. **Global interrupts are never enabled.** There is no `sei()`, so no ISR can run at all.
3. **`main()` returns immediately.** There is no `while(1)` loop; the program ends right after configuring the timer. An embedded `main()` must never return.
4. **Wrong header.** `<avr/inttypes.h>` does not exist; it is `<inttypes.h>` (or `<stdint.h>`).
5. **Only short periods can be measured.** With no prescaler at 1 MHz, TCNT1 counts 1 µs per tick and overflows after $2^{16}$ µs = 65.536 ms. A **low-frequency** wave (period > 65.536 ms) overflows the timer between two rising edges, so `ICR1` alone is wrong. We must count overflows and keep the period in a 32-bit variable.

**Corrected and modified code** (period in µs, any length up to $2^{32}$ µs)

```c
#include <avr/io.h>
#include <avr/interrupt.h>
#include <inttypes.h>

volatile uint32_t period;            // period in us (1 tick = 1 us)
volatile uint16_t n;                 // overflows since the last rising edge

ISR(TIMER1_OVF_vect) {               // TCNT1 wrapped 0xFFFF -> 0
    n++;
}

ISR(TIMER1_CAPT_vect) {              // rising edge on ICP1 (PD6)
    period = (uint32_t)n * 65536UL + ICR1;
    TCNT1 = 0;                       // start timing the next period
    n = 0;
    PORTB = ~(period >> 8);          // e.g. show bits 15-8 on PORTB (as in slides)
}

int main(void) {
    DDRB = 0xFF;                     // display
    DDRD &= ~(1 << PD6);             // ICP1 input

    TCCR1A = 0b00000000;             // normal mode
    TCCR1B = 0b11000001;             // noise canceller, rising edge, no prescaler
    TIMSK  = 0b00100100;             // TICIE1 (bit 5) + TOIE1 (bit 2)

    n = 0;
    TCNT1 = 0;
    sei();                           // enable interrupts globally
    while (1) { }                    // keep running
    return 0;
}
```

**How it works:** between two rising edges the timer overflows $n$ times and then reaches ICR1, so

$$\text{period} = n \times 65536 + ICR1 \ \text{ticks} = n \times 65536 + ICR1\ \mu s$$

*Notes:*

- Assumption: system clock 1 MHz (paper default) and no prescaler, so 1 tick = 1 µs. Another way to measure a slow wave is a larger prescaler (e.g. clk/256 gives 256 µs per tick and up to 16.7 s without overflow), at the cost of resolution.
- `TCNT1 = 0` is written a few cycles after the capture, so every reading is short by the (constant) interrupt latency, as in the slide code. For exact results keep the timer free-running and subtract the previous ICR1 instead.
