---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "INT0 (PD2, active-low, released = rising edge) adds 2; INT1 (PD3, active-high, pressed = rising edge) subtracts 2; MCUCR = 0b00001111, GICR = INT0|INT1, sei(); a uint8_t counter wraps to 0 on overflow; shown on PORTA."
sources: ["EHP ATmega32 Interrupt slides 13-23 (steps to program an interrupt, MCUCR, GICR, example)", "EHP ATMega32 Basic IO slides 28-36 (push buttons, internal pull-up)"]
---
**Trigger events**

- Switch 1, active-low on PD2 = **INT0**: it reads 1 normally and 0 when pressed. *After it is released* is a **rising edge**: ISC01:ISC00 = 11.
- Switch 2, active-high on PD3 = **INT1**: it reads 0 normally and 1 when pressed. *After it is pressed* is a **rising edge**: ISC11:ISC10 = 11.
- MCUCR = SE SM2 SM1 SM0 ISC11 ISC10 ISC01 ISC00 = 0000 1111.

The counter is `uint8_t`, so $254+2 = 256$ wraps back to 0, as required.

```c
#include <avr/io.h>
#include <avr/interrupt.h>          // STEP 1

volatile uint8_t counter = 0;       // changed in ISRs -> volatile

ISR(INT0_vect)                      // STEP 2: switch 1 released
{
    counter += 2;                   // 8-bit: overflow goes back to 0
    PORTA = counter;
}

ISR(INT1_vect)                      // switch 2 pressed
{
    counter -= 2;
    PORTA = counter;
}

int main(void)
{
    DDRA = 0xFF;                    // PA0-PA7: LEDs
    PORTA = counter;                // show 0 initially

    DDRD &= ~((1<<PD2)|(1<<PD3));   // PD2, PD3 as input
    PORTD |= (1<<PD2);              // internal pull-up for active-low switch
                                    // (active-high switch has an external pull-down)

    MCUCR = 0b00001111;             // STEP 3: INT1 rising, INT0 rising
    GICR = (1<<INT0)|(1<<INT1);     // STEP 4: enable INT0 and INT1
    sei();                          // STEP 5: global interrupt enable

    while(1);
}
```
