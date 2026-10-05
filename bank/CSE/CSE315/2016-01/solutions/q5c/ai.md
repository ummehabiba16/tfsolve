---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "PA0 and PA4 inputs, PORTB output; LEDs are active low so PORTB = ~count. Poll: when PA0 = 1 (debounced ~20 ms) count++, when PA4 = 1 count--, and wait for the switch to be released so each press counts once."
sources: ["EHP ATMega32 Basic IO slides 25-37 (reading PINx, push buttons)"]
---
- PA0 (count up) and PA4 (count down): inputs, **active high** (external pull-down; internal pull-ups off).
- LEDs on PORTB are **active low**: an LED is on when its bit is 0, so the counter is shown as **PORTB = ~count**.
- Each press must change the counter **once**: after detecting a press, wait for the release. A short delay filters contact bounce.

```c
#define F_CPU 1000000UL
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
    uint8_t count = 0;

    DDRA  = 0x00;                  // PA0, PA4 inputs
    PORTA = 0x00;                  // no pull-ups (active-high switches)
    DDRB  = 0xFF;                  // LEDs
    PORTB = ~count;                // all LEDs off for 0

    while (1) {
        if (PINA & (1 << PA0)) {               // up switch pressed
            _delay_ms(20);                     // debounce
            if (PINA & (1 << PA0)) {
                count++;                       // 255 -> 0 wraps naturally
                PORTB = ~count;
                while (PINA & (1 << PA0));     // wait for release
                _delay_ms(20);
            }
        }
        if (PINA & (1 << PA4)) {               // down switch pressed
            _delay_ms(20);
            if (PINA & (1 << PA4)) {
                count--;                       // 0 -> 255 wraps
                PORTB = ~count;
                while (PINA & (1 << PA4));
                _delay_ms(20);
            }
        }
    }
}
```
