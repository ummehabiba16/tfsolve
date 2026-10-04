---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "PD3 is INT1; release of an active-high switch is a falling edge (ISC11:ISC10 = 10); ISR shifts the ring value left (0x80 -> 0x01), writes PORTB, and calls sei() first so other interrupts can nest."
sources: ["EHP ATmega32 Interrupt slides 13-23 (steps, MCUCR, GICR, INT1 example)", "EHP ATmega32 Interrupt slide 25 (nested interrupts: sei() inside the ISR)", "EHP ATMega32 Basic IO slides 28-35 (pull-down for active-high switch)"]
---
**Analysis**

- PD3 is the **INT1** pin, so the ISR is `ISR(INT1_vect)` and INT1 is enabled with the INT1 bit of GICR.
- The switch is **active-high**: PD3 = 0 when open (external pull-down) and 1 when pressed. *Releasing* it changes PD3 from 1 to 0, a **falling edge**, so ISC11:ISC10 = **10**.
- The ring counter is a single 1 that moves left each time: 0x01, 0x02, ..., 0x80, then back to 0x01.
- **Nested interrupts:** the hardware clears the I-bit of SREG when an ISR is entered, so by default no other interrupt can run inside it. Calling `sei()` at the start of the ISR sets the I-bit again, so another interrupt can execute in the middle of this one. (`ISR(INT1_vect, ISR_NOBLOCK)` does the same.)

**Code**

```c
#include <avr/io.h>
#include <avr/interrupt.h>

volatile uint8_t ring = 0x01;        // shared with the ISR

ISR(INT1_vect)                       // switch on PD3 released
{
    sei();                           // allow other interrupts to nest here
    if (ring == 0x80)
        ring = 0x01;                 // loop back after 10000000
    else
        ring = ring << 1;            // 00000001 -> 00000010 -> ...
    PORTB = ring;                    // show the counter on the LEDs
}

int main(void)
{
    DDRB  = 0xFF;                    // PB0-PB7: LEDs
    DDRD &= ~(1 << PD3);             // PD3 (INT1) input, external pull-down
    PORTB = ring;                    // show 00000001 at start

    MCUCR = (MCUCR & 0b11110011) | (1 << ISC11);  // ISC11:ISC10 = 10, falling edge
    GICR  = (1 << INT1);             // enable INT1
    sei();                           // enable interrupts globally

    while (1);                       // all work is done in the ISR
}
```

*Note:* the switch is assumed to have an external pull-down resistor from PD3 to ground (an active-high switch connects PD3 to +5 V when pressed); the internal pull-up must stay off.
