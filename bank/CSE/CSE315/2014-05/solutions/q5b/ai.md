---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Steps: include avr/interrupt.h; write ISR(INT0_vect); set the trigger in MCUCR (ISC01:ISC00: 00 low level, 01 any change, 10 falling, 11 rising); enable INT0 with GICR bit 6 (INT0 = 1); enable interrupts globally with sei(). Also set PD2 as input (with pull-up if needed)."
sources: ["EHP ATmega32 Interrupt slides 13-23 (steps to program an interrupt in C, MCUCR, GICR, example)"]
---
**Steps to program an external interrupt**

1. Include the header **`<avr/interrupt.h>`**.
2. Write the handler with the **`ISR()`** macro and the vector name, e.g. `ISR(INT0_vect)`; this also places its address in the interrupt vector table.
3. Make the pin an **input** (INT0 = PD2), with the internal pull-up if the source is an active-low switch.
4. **Choose the triggering event** in **MCUCR** (ISC01, ISC00 for INT0).
5. **Enable the specific interrupt** in **GICR** (INT0 bit).
6. **Enable interrupts globally** with **`sei()`**.

**Registers for INT0**

| Register | Bits | Setting |
|:--|:--|:--|
| MCUCR | ISC01 ISC00 (bits 1-0) | 00 = low level, 01 = any logical change, 10 = falling edge, 11 = rising edge |
| GICR | INT0 (bit 6) | 1 = INT0 enabled |
| GIFR | INTF0 (bit 6) | flag, set by the event, cleared on entering the ISR (or by writing 1) |
| SREG | I (bit 7) | set by `sei()` |

**Example: INT0 on the falling edge (switch to ground)**

```c
#include <avr/io.h>
#include <avr/interrupt.h>

ISR(INT0_vect)
{
    PORTB = ~PORTB;                 // action on each falling edge
}

int main(void)
{
    DDRB  = 0xFF;
    DDRD &= ~(1 << PD2);            // PD2 = INT0 input
    PORTD |= (1 << PD2);            // pull-up
    MCUCR = (MCUCR & 0xFC) | (1 << ISC01);   // ISC01:00 = 10, falling edge
    GICR |= (1 << INT0);            // enable INT0
    sei();                          // global enable
    while (1);
}
```
