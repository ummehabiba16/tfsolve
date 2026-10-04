---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "A is active-low on INT0 (PD2): press = falling edge, MCUCR = 0x02. B is active-high on INT2 (PB2): press = rising edge, MCUCSR = 0x40 (ISC2 = 1). GICR = 0x60 (INT0 and INT2). ISR(INT0_vect) count++, ISR(INT2_vect) count--, sei()."
sources: ["EHP ATmega32 Interrupt slides 13-23 (steps, MCUCR/MCUCSR/GICR, ISR macro)", "EHP ATMega32 Basic IO slides 28-35 (pull-up/pull-down, active-low/high)"]
---
**Reading the circuit**

- **Switch A**: between INT0 and ground, with a resistor from INT0 to 5 V (**pull-up**): INT0 = 1 when open, 0 when pressed (**active low**). Pressing gives a **falling edge**.
- **Switch B**: between 5 V and INT2, with a resistor from INT2 to ground (**pull-down**): INT2 = 0 when open, 1 when pressed (**active high**). Pressing gives a **rising edge**.

Using **edge** triggering makes each interrupt fire **only once per press** (a level trigger would fire repeatedly while the switch is held).

**Register values**

| Register | Value | Meaning |
|:--|:-:|:--|
| DDRD | 0x00 | PD2 (INT0) input (external pull-up, so PORTD = 0x00) |
| DDRB | 0x00 | PB2 (INT2) input (external pull-down, so PORTB = 0x00) |
| MCUCR | **0x02** | ISC01:ISC00 = 10: INT0 on falling edge |
| MCUCSR | **0x40** | ISC2 = 1: INT2 on rising edge |
| GICR | **0x60** | INT0 (bit 6) = 1, INT2 (bit 5) = 1 |

**Code**

```c
#include <avr/io.h>
#include <avr/interrupt.h>

volatile uint8_t count = 0;          // 8-bit counter

ISR(INT0_vect)                       // switch A pressed
{
    count++;
}

ISR(INT2_vect)                       // switch B pressed
{
    count--;
}

int main(void)
{
    DDRD = 0x00;                     // PD2 = INT0 input
    DDRB = 0x00;                     // PB2 = INT2 input
    PORTD = 0x00;                    // no internal pull-ups (external resistors)
    PORTB = 0x00;

    MCUCR  = 0x02;                   // INT0: falling edge
    MCUCSR = 0x40;                   // INT2: rising edge (set before enabling INT2)
    GIFR   = 0x60;                   // clear any pending INT0/INT2 flags
    GICR   = 0x60;                   // enable INT0 and INT2
    sei();                           // global interrupt enable

    while (1) {
        // count can be used / displayed here
    }
}
```

*Notes:* MCUCSR is written before INT2 is enabled because changing ISC2 can set the INT2 flag (the data sheet asks to disable INT2, change ISC2, then clear INTF2). Switches are assumed bounce-free.
