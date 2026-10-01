---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Issues: TCCR1A = 0b00000010 sets WGM11 (not normal mode); TCCR1B = 0b00000001 is no prescaler, not 64; no ISR(TIMER1_OVF_vect) to count overflows; overflow_count not volatile; no sei()/cli(); elapsed_time ignores TCNT1 and the 64 us tick; the empty loop may be optimised away."
sources: ["EHP Timer_Part_1 slides 18-32 (TCCR1A/B, TIMSK, measuring elapsed time code)", "EHP ATmega32 Interrupt slides 13, 24, 27-29 (sei/cli, volatile)"]
---
Compared with the slide's "measuring elapsed time" program:

1. **Line 10, wrong mode.** `TCCR1A = 0b00000010` sets WGM11 = 1. With WGM13:12 = 00 from TCCR1B, WGM13:10 = 0010 is **phase correct PWM, 9-bit** (TOP = 0x1FF), not normal mode. TCNT1 never counts to 0xFFFF, so "overflows" are not $2^{16}$ counts. Fix: `TCCR1A = 0b00000000; // normal mode`.
2. **Line 11, wrong prescaler.** `TCCR1B = 0b00000001` has CS12:10 = 001, which is **no prescaling**, but the prescaler must be **64**: CS12:10 = 011, so `TCCR1B = 0b00000011;`. The timer also starts running as soon as TCCR1B is written, before `TCNT1 = 0`; set the clock bits after resetting the counter.
3. **No overflow ISR.** TIMSK enables TOIE1, but there is no `ISR(TIMER1_OVF_vect){ overflow_count++; }`. Nothing ever increments `overflow_count`, and an enabled interrupt with no handler jumps to the default vector (a reset).
4. **No `sei()`.** Global interrupts are never enabled, so even with an ISR the overflows would not be counted. A `cli()` should stop interrupts after the measured block, before TCNT1 and the count are read.
5. **`overflow_count` is not `volatile`.** It is modified in an ISR and read in main; without volatile the compiler may use a stale value.
6. **Line 26, wrong formula.** It drops the partial count in TCNT1, and it forgets that one tick is $64/1\text{ MHz} = 64\,\mu s$, not 1 µs. Fix:

$$t\,(\mu s) = (n\times65536 + TCNT1)\times64$$

so `elapsed_time = (overflow_count * 65536 + (uint32_t)TCNT1) * 64;`

7. **Empty loop may be removed.** `i` and `j` are not `volatile`, so the optimiser can delete the do-nothing loop entirely and the measured time becomes about 0. (The elapsed time is also never used or output.)

**Corrected code**

```c
#include <avr/io.h>
#include <avr/interrupt.h>
#include <inttypes.h>

volatile uint32_t overflow_count;

ISR(TIMER1_OVF_vect){            // handler for Timer1 overflow interrupt
    overflow_count++;            // increment overflow count
}

int main(void)  {
    uint32_t elapsed_time;
    volatile int i, j;

    TCCR1A = 0b00000000;         // normal mode
    TIMSK  = 0b00000100;         // enable Timer 1 overflow interrupt
    overflow_count = 0;          // reset n
    TCNT1 = 0;                   // reset Timer 1
    TCCR1B = 0b00000011;         // start: prescaler 64, internal clock
    sei();                       // enable interrupts globally

    //----start code----
    for(i=0; i<1000; i++)
        for(j=0; j<1000; j++)
            {;}
    //----end code------

    cli();                       // stop counting overflows
    elapsed_time = (overflow_count * 65536 + (uint32_t)TCNT1) * 64;  // in us
    return 0;
}
```
