---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Both switches are active high, so pressing is a rising edge: MCUCR = 0b00000011 (INT0 rising), MCUCSR = 0b01000000 (ISC2 = 1, INT2 rising), GICR = 0b01100000 (INT0, INT2). INT0 ISR rotates the ring left (0x80 -> 0x01), INT2 ISR rotates right (0x01 -> 0x80); PORTA shows the ring."
sources: ["EHP ATmega32 Interrupt slides 13-23 (MCUCR, MCUCSR, GICR, ISR)", "EHP ATMega32 Basic IO slides 28-35 (active-high switch with pull-down)"]
---
**Analysis**

- Switch A on **INT0 (PD2)** and switch B on **INT2 (PB2)** are **active high** (pull-down resistors): pressing changes the pin 0 $\to$ 1, a **rising edge**.
- INT0 rising edge: ISC01:ISC00 = 11. INT2 rising edge: ISC2 = 1.
- Ring counter: one LED on. Count up = move the 1 left (0x80 wraps to 0x01). Count down = move it right (0x01 wraps to 0x80).

**Register values** (don't-care bits = 0)

| Register | Value | Meaning |
|:--|:--|:--|
| MCUCR | 0b00000011 | ISC01:00 = 11: INT0 rising edge |
| MCUCSR | 0b01000000 | ISC2 = 1: INT2 rising edge |
| GICR | 0b01100000 | INT0 = 1, INT2 = 1 |
| GIFR | 0b01100000 | write 1s to clear pending INTF0, INTF2 |
| DDRA | 0b11111111 | LEDs |
| DDRD, DDRB | 0b00000000 | switch inputs |

**Code**

```c
#include <avr/io.h>
#include <avr/interrupt.h>

volatile uint8_t ring = 0x01;

ISR(INT0_vect)                       // switch A: count up
{
    ring = (ring == 0x80) ? 0x01 : (ring << 1);
    PORTA = ring;
}

ISR(INT2_vect)                       // switch B: count down
{
    ring = (ring == 0x01) ? 0x80 : (ring >> 1);
    PORTA = ring;
}

int main(void)
{
    DDRA = 0b11111111;               // LED0-LED7
    DDRD = 0b00000000;               // PD2 = INT0 input
    DDRB = 0b00000000;               // PB2 = INT2 input
    PORTA = ring;                    // show 00000001

    MCUCR  = 0b00000011;             // INT0 on rising edge
    MCUCSR = 0b01000000;             // INT2 on rising edge
    GIFR   = 0b01100000;             // clear pending flags
    GICR   = 0b01100000;             // enable INT0 and INT2
    sei();

    while (1);
}
```

*Notes:* the switches are assumed to have external pull-down resistors and no bounce. ISC2 is set before INT2 is enabled, as the data sheet requires.
