---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "DDRD = 0x00, DDRB = 0x00, PORTD = PORTB = 0x00; in an endless loop read PIND bit 2 and PINB bit 2 and compare with the previous readings: A 1 -> 0 (pressed) gives count++, B 0 -> 1 (pressed) gives count--, so each press is counted once."
sources: ["EHP ATMega32 Basic IO slides 25-36 (reading PINx, push buttons)", "EHP ATmega32 Interrupt slides 2-4 (polling vs interrupt)"]
---
With polling the CPU reads the pins continuously. To count **only once per press** (not on every loop pass while the switch is held), the program detects the **edge** by comparing each reading with the previous one.

- Switch A (PD2, active low): pressed when it changes **1 $\to$ 0**.
- Switch B (PB2, active high): pressed when it changes **0 $\to$ 1**.

**Register values:** DDRD = **0x00**, DDRB = **0x00** (inputs), PORTD = **0x00**, PORTB = **0x00** (no internal pull-ups; the circuit has external resistors). No interrupt registers are used (GICR = 0x00).

```c
#include <avr/io.h>

int main(void)
{
    uint8_t count = 0;
    uint8_t a, b;
    uint8_t prevA, prevB;

    DDRD  = 0x00;                    // PD2 input (switch A)
    DDRB  = 0x00;                    // PB2 input (switch B)
    PORTD = 0x00;                    // no internal pull-ups
    PORTB = 0x00;

    prevA = PIND & 0x04;             // initial states
    prevB = PINB & 0x04;

    while (1) {
        a = PIND & 0x04;             // PD2
        b = PINB & 0x04;             // PB2

        if (prevA && !a)             // A: 1 -> 0, just pressed
            count++;
        if (!prevB && b)             // B: 0 -> 1, just pressed
            count--;

        prevA = a;
        prevB = b;
    }
}
```

*Note:* switches are assumed bounce-free, as in Q.10(a); a real circuit would add a short debounce delay after a detected edge.
