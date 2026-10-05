---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Button on PD0 (input, internal pull-up, active low), LEDs on PORTB. Poll the button, debounce (20 ms), and on each press move the Fibonacci pair (cur, next): 0, 1, 1, 2, 3, ..., 233; when the next term exceeds 255 restart at 0. Wait for release so each press counts once."
sources: ["EHP ATMega32 Basic IO slides 25-37 (digital I/O, push buttons, internal pull-up)"]
---
**Design (assumptions):** push button on **PD0** to ground, using the **internal pull-up** (active low); 8 LEDs on **PORTB** (active high); 1 MHz clock.

The counter keeps two consecutive Fibonacci terms: `cur` (displayed) and `nxt` (16-bit, to detect overflow). Each press: `cur = nxt; nxt = old cur + old nxt`. When the next term would exceed 255 (after 233 comes 377) the counter returns to 0.

Sequence shown: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 0, 1, 1, ...

```c
#define F_CPU 1000000UL
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
    uint8_t  cur = 0;           // current counter value
    uint16_t nxt = 1;           // next Fibonacci term
    uint16_t sum;

    DDRB  = 0xFF;               // LEDs
    PORTB = cur;                // show 0 at start
    DDRD &= ~(1 << PD0);        // button input
    PORTD |= (1 << PD0);        // internal pull-up: released = 1, pressed = 0

    while (1) {
        if (!(PIND & (1 << PD0))) {           // button pressed
            _delay_ms(20);                    // debounce
            if (!(PIND & (1 << PD0))) {
                if (nxt > 255) {              // 8-bit overflow
                    cur = 0;
                    nxt = 1;
                } else {
                    sum = cur + nxt;
                    cur = (uint8_t)nxt;
                    nxt = sum;
                }
                PORTB = cur;
                while (!(PIND & (1 << PD0))); // wait for release
                _delay_ms(20);
            }
        }
    }
}
```
