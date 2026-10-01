---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Wrong ISRs/pins (button 1 is INT2 on PB2, button 2 is INT0 on PD2), INT1 enabled instead of INT2, MCUCR unchanged so INT0 is low-level, ISC2 not set, no sei(), count not volatile, no pull-up for the active-low button."
sources: ["EHP ATmega32 Interrupt slides 13-23 (steps, MCUCR/MCUCSR/GICR, example)", "EHP ATmega32 Interrupt slides 27-29 (volatile)", "EHP ATMega32 Basic IO slides 28-36 (push buttons, pull-up/pull-down)"]
---
**Circuit**

```text
               +5V                          ATmega32
                |                     +----------------------+
              [Rpu]  (or internal     |                      |
                |     pull-up)        |                      |
 GND --o  o-----+-------------------->| PD2 (INT0)  PA0 .. PA7|---[R]--|>|-- GND  (x8 LEDs,
     button 2 (active-low)            |                      |                 LED0..LED7)
                                      |                      |
 +5V --o  o-----+-------------------->| PB2 (INT2)           |
     button 1   |                     |                      |
   (active-high)[Rpd]                 +----------------------+
                |
               GND
```

- Button 1 (active-high) on PB2 = INT2, with a pull-down resistor: the pin reads 0 normally and 1 when pressed. *Pressed* is a **rising edge**.
- Button 2 (active-low) on PD2 = INT0, with a pull-up resistor (or the internal pull-up, PORTD2 = 1): the pin reads 1 normally and 0 when pressed. *Released* is a **rising edge**.
- 8 LEDs (with series resistors) on PA0-PA7.

**Issues in Listing 1**

1. **Wrong interrupt for button 1.** Button 1 is on PB2, which is **INT2**, not INT1 (INT1 is PD3). There is no `ISR(INT2_vect)`, and `ISR(INT1_vect)` handles a pin with nothing connected.
2. **Wrong action in the INT0 ISR.** INT0 (PD2) is button 2, which must **decrement**. Line 7 increments.
3. **GICR enables INT0 and INT1** (line 17). It must enable **INT0 and INT2**: `GICR = (1<<INT0)|(1<<INT2);`
4. **Line 18 does nothing.** `MCUCR & 0b11111111` leaves MCUCR unchanged, so ISC01:ISC00 = 00 and **INT0 triggers on low level**. While button 2 is held down, the ISR fires again and again (many decrements), and on *press* rather than release. It must be a rising edge: ISC01:ISC00 = 11.
5. **ISC2 is not set.** INT2's edge is chosen by ISC2 in MCUCSR. The default ISC2 = 0 is a falling edge, which for button 1 means *release*. It must be a rising edge for *press*: `MCUCSR |= (1<<ISC2);`
6. **Global interrupts are never enabled.** There is no `sei()`, so no ISR ever runs.
7. **`count` is not `volatile`.** It is changed only inside ISRs, so the compiler may keep it in a register in the `while(1)` loop and PORTA would never change.
8. **No pull-up for the active-low button.** PD2 floats when the button is open. Enable the internal pull-up (`PORTD |= (1<<PD2);`) or fit an external one. (The active-high button needs an external pull-down.)

**Corrected code**

```c
#include <avr/io.h>
#include <avr/interrupt.h>

volatile uint8_t count;

ISR(INT2_vect){          // button 1 (PB2, active-high): pressed
    count += 1;
}

ISR(INT0_vect){          // button 2 (PD2, active-low): released
    count -= 1;
}

int main(void) {
    DDRA = 0xFF;                     // LEDs
    DDRB &= ~(1<<PB2);               // PB2 input (external pull-down)
    DDRD &= ~(1<<PD2);               // PD2 input
    PORTD |= (1<<PD2);               // internal pull-up for active-low button
    count = 0;

    MCUCR |= (1<<ISC01)|(1<<ISC00);  // INT0: rising edge (release)
    MCUCSR |= (1<<ISC2);             // INT2: rising edge (press)
    GICR = (1<<INT0) | (1<<INT2);    // enable INT0 and INT2
    sei();                           // enable interrupts globally

    while(1) {
        PORTA = count;
    }
}
```
