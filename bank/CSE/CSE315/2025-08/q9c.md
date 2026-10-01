---
marks: 15
topics: [timer-pwm]
kind: analysis
mandatory: true
source: {page: 5}
---
The C code in Listing 2 generates a square wave in the `OC1A` pin of ATMega32 using Timer 1. Analyze the code carefully and evaluate its output. Draw the square wave generated at `OC1A` pin with respect to time. Clearly show how `TCNT1` changes with respect to time. Determine the duty cycle and the frequency of the wave. If you find any necessary information to be missing, assume any appropriate value and clearly mention your assumption.

**Listing 2: C program for question 9(c)**

```c
#include <avr/io.h>
#define F_CPU 4000000

int main(void)  {
    DDRD = 0b00100000;
    PORTD |= 0b00100000;
    TCCR1A = 0b10000010;
    TCCR1B = 0b00010010;

    ICR1 = 9999;
    OCR1A = 1999;

    while(1){;}
}
```
