---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "DDRA = 0x00 (input), DDRB = 0xFF (output); in an endless loop: PORTB = PINA; _delay_ms(1000)."
sources: ["EHP ATMega32 Basic IO slides 25 (read Port A, write Port B)", "EHP Timer_Part_1 slide 5 (_delay_ms)"]
---
```c
#define F_CPU 1000000UL          // 1 MHz system clock (assumed)
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
    DDRA = 0x00;                 // Port A: input
    DDRB = 0xFF;                 // Port B: output

    while (1) {
        PORTB = PINA;            // read the 8-bit input, send it to Port B
        _delay_ms(1000);         // once every second
    }
}
```

`PINA` (not `PORTA`) holds the levels on the Port A pins. `_delay_ms()` is good enough here; for an exact 1 s period (no drift from the loop body or interrupts) a Timer1 interrupt could be used instead.
