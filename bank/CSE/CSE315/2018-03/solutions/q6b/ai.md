---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "TCCR1A = 0x00, TCCR1B = 0b10000001 (ICNC = 1, falling edge, normal mode, no prescaler), TIMSK = TICIE1 | TOIE1. Count overflows; at each falling edge period = n x 65536 + ICR1 - previous ICR1 (us); convert to seconds with integer arithmetic and show it with LCD_string()."
sources: ["EHP Timer_Part_1 slides 29-37 (overflow counting, input capture period measurement)", "Section B note of the paper (LCD.h: LCD_init, LCD_string)"]
---
**Settings** (1 MHz, no prescaler: 1 tick = 1 µs)

| Register | Value | Meaning |
|:--|:--|:--|
| TCCR1A | 0b00000000 | normal mode (WGM11:10 = 00) |
| TCCR1B | 0b10000001 | ICNC1 = 1 (noise canceller), ICES1 = 0 (falling edge), WGM13:12 = 00, CS = 001 |
| TIMSK | 0b00100100 | TICIE1 (input capture) and TOIE1 (overflow) interrupts |

The square wave is connected to **ICP1 (PD6)**. Overflows are counted so that periods longer than 65.536 ms can be measured.

```c
#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdio.h>
#include "LCD.h"

volatile uint16_t ovf = 0;          // overflows since the last edge
volatile uint32_t period_us = 0;    // latest period in microseconds
volatile uint8_t  ready = 0;
volatile uint16_t last = 0;         // ICR1 at the previous edge
volatile uint8_t  first = 1;

ISR(TIMER1_OVF_vect) {
    ovf++;
}

ISR(TIMER1_CAPT_vect) {             // falling edge on ICP1
    uint16_t now = ICR1;
    if (!first) {
        period_us = (uint32_t)ovf * 65536UL + now - last;
        ready = 1;
    }
    first = 0;
    last = now;
    ovf = 0;
}

int main(void) {
    char buf[20];
    DDRD &= ~(1 << PD6);            // ICP1 input
    LCD_init();

    TCCR1A = 0b00000000;
    TCCR1B = 0b10000001;
    TIMSK  = 0b00100100;
    sei();

    while (1) {
        if (ready) {
            uint32_t p;
            cli(); p = period_us; ready = 0; sei();
            sprintf(buf, "T=%lu.%06lu s", p / 1000000UL, p % 1000000UL);
            LCD_string(buf);        // period in seconds
        }
    }
}
```

`now - last` is computed in 32 bits, so it also works when ICR1 wrapped past 0 (then $n \times 65536$ makes up the difference). Integer formatting is used because `printf` for floats is not enabled by default on the AVR.

*Note:* an overflow that happens just before the capture may be counted one edge late; for a uniform wave this only affects a reading occasionally and could be fixed by also checking TOV1 inside the capture ISR.
