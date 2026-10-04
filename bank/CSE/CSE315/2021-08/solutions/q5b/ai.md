---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "PD2 = INT0; releasing an active-high switch is a falling edge (ISC01:ISC00 = 10). ISR(INT0_vect) shifts the ring value left (0x80 -> 0x01) and writes PORTA; GICR = 1<<INT0; sei()."
sources: ["EHP ATmega32 Interrupt slides 13-23 (steps, MCUCR, GICR, INT1 example)", "EHP ATMega32 Basic IO slides 28-35 (pull-down for active-high switch)"]
---
**Analysis**

- PD2 is **INT0**, so the ISR is `ISR(INT0_vect)` and GICR bit INT0 enables it.
- Active-high switch: PD2 = 0 when open (external pull-down), 1 when pressed. **Release** is the change 1 $\to$ 0, a **falling edge**: ISC01:ISC00 = **10** in MCUCR.
- Ring counter: one 1 moving left: 0x01, 0x02, ..., 0x80, then 0x01 again.

```c
#include <avr/io.h>
#include <avr/interrupt.h>

volatile uint8_t ring = 0x01;

ISR(INT0_vect)                       // switch released (falling edge on PD2)
{
    if (ring == 0x80)
        ring = 0x01;                 // loop back
    else
        ring = ring << 1;            // next position
    PORTA = ring;                    // LEDs on PA0-PA7
}

int main(void)
{
    DDRA  = 0xFF;                    // LEDs
    DDRD &= ~(1 << PD2);             // PD2 input (external pull-down)
    PORTA = ring;                    // show 00000001

    MCUCR = (MCUCR & 0b11111100) | (1 << ISC01);   // ISC01:00 = 10, falling edge
    GICR  = (1 << INT0);             // enable INT0
    sei();                           // global interrupt enable

    while (1);
}
```

*Note:* the switch is assumed to have an external pull-down resistor (the internal pull-up must stay off for an active-high switch) and to be bounce-free.
