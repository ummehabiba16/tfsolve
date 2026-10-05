---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "A (INT0, active low): falling edge, ISC01:00 = 10; B (INT1, active high): rising edge, ISC11:10 = 11; C (INT2, active high): ISC2 = 1. MCUCR = 0b00001110, MCUCSR = 0b01000000, GICR = 0b11100000. Debounce in each ISR: wait ~20 ms, act only if the pin is still pressed, then clear the INTFx flag that the bounces set again. A rotates the ring left, B right, C clears it to 0."
sources: ["EHP ATmega32 Interrupt slides 13-23 (MCUCR, MCUCSR, GICR, GIFR)", "EHP ATMega32 Basic IO slides 28-37 (push buttons, pull-ups)"]
---
**Register settings**

| Switch | Pin | Type | Press = | Setting |
|:--|:--|:--|:--|:--|
| A | INT0 (PD2) | active low (pull-up) | falling edge | ISC01:ISC00 = **10** |
| B | INT1 (PD3) | active high (pull-down) | rising edge | ISC11:ISC10 = **11** |
| C | INT2 (PB2) | active high (pull-down) | rising edge | ISC2 = **1** |

- MCUCR = 0b0000**1110** (sleep bits 0), MCUCSR = 0b0**1**000000, GICR = 0b**111**00000 (INT1, INT0, INT2).
- PD2 gets the internal pull-up (PORTD2 = 1); B and C are assumed to have external pull-down resistors.

**Debouncing.** A bouncing switch produces many edges, so the interrupt flag is set many times for one press. In each ISR:

1. wait about 20 ms (longer than the bounce time);
2. check that the pin is **still** at its pressed level (otherwise it was noise) and only then update the counter;
3. clear that interrupt's flag in GIFR (write 1), because the bounces during the delay have set it again; otherwise the ISR would run a second time.

**Code**

```c
#define F_CPU 1000000UL
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

volatile uint8_t ring = 0x01;

ISR(INT0_vect)                               // A: count up
{
    _delay_ms(20);
    if (!(PIND & (1 << PD2))) {              // still pressed (active low)
        ring = (ring == 0x80 || ring == 0) ? 0x01 : (ring << 1);
        PORTB = ring;
    }
    GIFR = (1 << INTF0);                     // discard bounce edges
}

ISR(INT1_vect)                               // B: count down
{
    _delay_ms(20);
    if (PIND & (1 << PD3)) {                 // still pressed (active high)
        ring = (ring == 0x01 || ring == 0) ? 0x80 : (ring >> 1);
        PORTB = ring;
    }
    GIFR = (1 << INTF1);
}

ISR(INT2_vect)                               // C: reset
{
    _delay_ms(20);
    if (PINB & (1 << PB2)) {
        ring = 0;                            // counter reset to 0 (all LEDs off)
        PORTB = ring;
    }
    GIFR = (1 << INTF2);
}

int main(void)
{
    DDRB  = 0xFF & ~(1 << PB2);              // LEDs on PORTB; PB2 is INT2 input
    DDRD  = 0x00;                            // PD2, PD3 inputs
    PORTD = (1 << PD2);                      // pull-up for active-low switch A
    PORTB = ring;

    MCUCR  = 0b00001110;                     // INT1 rising, INT0 falling
    MCUCSR = 0b01000000;                     // INT2 rising
    GIFR   = 0b11100000;                     // clear old flags
    GICR   = 0b11100000;                     // enable INT1, INT0, INT2
    sei();

    while (1);
}
```

*Notes:* PB2 is both the INT2 input and one of the 8 PORTB LED lines in the question, so that LED cannot also be driven. If the LEDs need all of PORTB, a different port should be used for C's LED or switch; this conflict is in the question itself. After a reset by C (ring = 0), the next A press shows 00000001 and the next B press 10000000.
