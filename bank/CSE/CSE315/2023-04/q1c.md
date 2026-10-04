---
marks: 15
topics: [timer-input-capture]
kind: code
source: {page: 25}
---
The following code (Figure 1(c)) is a faulty code that was designed to measure the period of a high-frequency square wave using TIMER1 input capture. Correct and modify the code to measure the period of a low-frequency square wave.

**Figure 1(c)**

```c
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/inttypes.h>

volatile uint16_t period;

ISR(TIMER1_CAPT_vect) {
    period = ICR1;
    TCNT1 = 0;
}

int main() {
    TCCR1A = 0b00000000;
    TCCR1B = 0b11000001;
    TIMSK  = 0b00000100;
    return 0;
}
```

**Registers (from Table 1, attached)**

| Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| TCCR1A | COM1A1 | COM1A0 | COM1B1 | COM1B0 | FOC1A | FOC1B | WGM11 | WGM10 |
| TCCR1B | ICNC1 | ICES1 | - | WGM13 | WGM12 | CS12 | CS11 | CS10 |
| TIMSK | OCIE2 | TOIE2 | TICIE1 | OCIE1A | OCIE1B | TOIE1 | OCIE0 | TOIE0 |
| TIFR | OCF2 | TOV2 | ICF1 | OCF1A | OCF1B | TOV1 | OCF0 | TOV0 |

*CS12, CS11, CS10: 001 = No prescaling, 010 = clk/8, 011 = clk/64, 100 = clk/256.*

Attached sheet: [Figures and Tables for Section A](figures/sheet-1.png), [ATmega32 pinout](figures/sheet-2.png).
