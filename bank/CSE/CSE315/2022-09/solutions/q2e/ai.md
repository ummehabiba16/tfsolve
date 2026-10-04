---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Normal mode, prescaler 8 (TCCR1B = 0b00000010), overflow interrupt counts n; elapsed_time = (n x 65536 + TCNT1) x 8 us at 1 MHz."
sources: ["EHP Timer_Part_1 slides 29-32 (measuring elapsed time with overflow count)", "EHP Timer_Part_1 slides 19-23 (TCCR1A/B, clock select, TIMSK)"]
---
**Idea.** At 1 MHz (paper default) with prescaler 8, TCNT1 increments every $8\ \mu s$ and overflows every $65536 \times 8\ \mu s \approx 524$ ms. Count the overflows $n$ in the TOV1 interrupt. At the end

$$\text{elapsed time} = (n \times 65536 + TCNT1) \times 8\ \mu s$$

**Code**

```c
#include <avr/io.h>
#include <avr/interrupt.h>
#include <inttypes.h>

volatile uint32_t n;                 // number of Timer1 overflows

ISR(TIMER1_OVF_vect) {
    n++;
}

int main(void) {
    uint32_t elapsed_time;           // in microseconds
    int i, j;

    TCCR1A = 0b00000000;             // normal mode (WGM13:10 = 0000)
    TCCR1B = 0b00000010;             // CS12:10 = 010: clk/8, increment every 8 clock pulses
    TIMSK  = 0b00000100;             // TOIE1: overflow interrupt

    n = 0;
    TCNT1 = 0;                       // start timing from 0
    sei();

    // ----- code segment to be measured -----
    for (i = 0; i < 100; i++)
        for (j = 0; j < 1000; j++) { ; }
    // ----- end of code segment -----

    cli();                           // stop n from changing while it is read
    elapsed_time = (n * 65536UL + (uint32_t)TCNT1) * 8;   // 1 tick = 8 us
    sei();

    while (1);
}
```

*Note:* assumption: 1 MHz system clock, so one tick = $8/1\,\text{MHz} = 8\ \mu s$. For a clock $f$, multiply by $8 \times 10^6 / f$ instead of 8.
