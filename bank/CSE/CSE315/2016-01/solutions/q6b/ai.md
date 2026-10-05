---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "A on INT0 and B on INT1 are active high: rising edge for both, MCUCR = 0b00001111; GICR = 0b11000000. Start with PORTB = 0x01; INT0 ISR rotates left (0x80 -> 0x01), INT1 ISR rotates right (0x01 -> 0x80)."
sources: ["EHP ATmega32 Interrupt slides 13-23 (MCUCR, GICR, ISR)"]
---
- Both switches are **active high**, so pressing gives a **rising edge**: ISC01:00 = 11 (INT0) and ISC11:10 = 11 (INT1): **MCUCR = 0b00001111**.
- Enable both: **GICR = 0b11000000** (INT1, INT0).
- Rotate left: LED$k$ $\to$ LED$k+1$ (bit shifted left, 0x80 goes back to 0x01). Rotate right: the opposite.

```c
#include <avr/io.h>
#include <avr/interrupt.h>

volatile uint8_t led = 0x01;          // LED0 on at start

ISR(INT0_vect)                        // switch A: rotate left
{
    led = (led == 0x80) ? 0x01 : (led << 1);
    PORTB = led;
}

ISR(INT1_vect)                        // switch B: rotate right
{
    led = (led == 0x01) ? 0x80 : (led >> 1);
    PORTB = led;
}

int main(void)
{
    DDRB  = 0xFF;                     // LED0-LED7 on PB0-PB7
    PORTB = led;
    DDRD  = 0x00;                     // PD2 (INT0), PD3 (INT1) inputs, external pull-downs

    MCUCR = 0b00001111;               // INT1 and INT0 on rising edge
    GICR  = 0b11000000;               // enable INT1 and INT0
    sei();

    while (1);
}
```

*Note:* the paper's part (iii) says "pressing A" for the right rotation; switch B is meant.
