---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Switch on PD2 = INT0 with internal pull-up; pressing an active-low switch is a falling edge (ISC01:ISC00 = 10). The ISR advances the Fibonacci pair (cur, next): 0, 1, 1, 2, 3, ..., 233, and when the next term would exceed 255 it restarts at 0; PORTA shows cur."
sources: ["EHP ATmega32 Interrupt slides 13-23 (INT0, MCUCR, GICR, sei)", "EHP ATMega32 Basic IO slides 28-36 (active-low switch, internal pull-up)"]
---
**Design**

- PD2 is **INT0**. The switch is **active-low**, so PD2 needs a pull-up (internal: DDRD2 = 0, PORTD2 = 1). Pressing the switch pulls PD2 from 1 to 0, a **falling edge**: ISC01:ISC00 = **10**.
- Keep two terms of the sequence: `cur` (shown on PORTA) and `nxt`. On each press: `cur = nxt`, `nxt = old cur + old nxt`.
- The 8-bit counter **overflows** when the next term exceeds 255 (after 233 comes 377). Then it goes back to 0 and the sequence restarts: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 0, 1, 1, ...

**Code**

```c
#include <avr/io.h>
#include <avr/interrupt.h>

volatile uint8_t  cur = 0;           // value shown on the LEDs
volatile uint16_t nxt = 1;           // next Fibonacci term (16-bit to detect overflow)

ISR(INT0_vect)                       // switch pressed (falling edge on PD2)
{
    if (nxt > 255) {                 // next term does not fit in 8 bits: overflow
        cur = 0;
        nxt = 1;                     // restart 0, 1, 1, 2, ...
    } else {
        uint16_t sum = cur + nxt;
        cur = (uint8_t)nxt;
        nxt = sum;
    }
    PORTA = cur;
}

int main(void)
{
    DDRA  = 0xFF;                    // 8 LEDs on PORTA
    PORTA = cur;                     // show 0

    DDRD  &= ~(1 << PD2);            // PD2 (INT0) input
    PORTD |=  (1 << PD2);            // internal pull-up for the active-low switch

    MCUCR = (MCUCR & 0b11111100) | (1 << ISC01);   // ISC01:00 = 10, falling edge
    GICR  = (1 << INT0);             // enable INT0
    sei();                           // enable interrupts globally

    while (1);                       // everything happens in the ISR
}
```

**Trace:** (cur, nxt) = (0,1) $\to$ (1,1) $\to$ (1,2) $\to$ (2,3) $\to$ (3,5) $\to$ ... $\to$ (144,233) $\to$ (233,377) $\to$ next press: 377 > 255, so (0,1).

*Note:* switch bouncing is ignored (assumed clean); a real switch would need debouncing.
