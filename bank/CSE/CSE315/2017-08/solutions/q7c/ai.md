---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "PA0 and PA4 inputs (external pull-downs), PORTB outputs with active-low LEDs (PORTB = ~ring). Poll: when PA0 reads 1, wait 20 ms, confirm still 1, rotate the ring left, then wait for release and debounce it; PA4 the same rotating right."
sources: ["EHP ATMega32 Basic IO slides 25-37 (PINx polling, push buttons)"]
---
**Approach**

- PA0 (up) and PA4 (down) are inputs; the switches are active high (external pull-down resistors). DDRA = 0x00, PORTA = 0x00.
- The LEDs are **active low**, so an LED is on when its PORTB bit is 0: output **PORTB = ~ring**.
- **Debouncing:** when a press is seen, wait about 20 ms and read again; accept it only if the switch is still pressed. Then wait until the switch is released (and wait 20 ms again), so one press is counted once even though the contact bounces.

```c
#define F_CPU 1000000UL
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
    uint8_t ring = 0x01;

    DDRA  = 0x00;                  // PA0, PA4 inputs
    PORTA = 0x00;                  // no internal pull-ups (active-high switches)
    DDRB  = 0xFF;                  // LEDs
    PORTB = ~ring;                 // active-low LEDs: show 00000001

    while (1) {
        if (PINA & (1 << PA0)) {                   // up switch seems pressed
            _delay_ms(20);                         // debounce
            if (PINA & (1 << PA0)) {               // really pressed
                ring = (ring == 0x80) ? 0x01 : (ring << 1);
                PORTB = ~ring;
                while (PINA & (1 << PA0));         // wait for release
                _delay_ms(20);                     // debounce the release
            }
        }
        if (PINA & (1 << PA4)) {                   // down switch
            _delay_ms(20);
            if (PINA & (1 << PA4)) {
                ring = (ring == 0x01) ? 0x80 : (ring >> 1);
                PORTB = ~ring;
                while (PINA & (1 << PA4));
                _delay_ms(20);
            }
        }
    }
}
```
