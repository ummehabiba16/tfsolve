---
marks: 15
topics: [external-interrupts, push-buttons]
kind: code
mandatory: true
source: {page: 4}
---
The C code in Listing 1 is supposed to be an external interrupt-driven program implementing a counter using an ATMega32. Eight LEDs are connected to PORT A, which represent the current state of the counter in binary format. An active-high push button is connected to the PB2 pin, and an active-low push button is connected to the PD2 pin of ATMega32. The first button should increment the counter by one when it is pressed. The second button should decrement the counter by one when it is released. Draw a circuit diagram showing the connections between all the components. Analyze the C code in Listing 1 and find out all the issues that may prevent the code from achieving the desired outcome as described above. You also have to properly explain the reasoning behind your answer.

**Listing 1: C program for question 9(a)**

```c
#include <avr/io.h>
#include <avr/interrupt.h>

uint8_t count;

ISR(INT0_vect){
    count += 1;
}

ISR(INT1_vect){
    count -= 1;
}

int main(void) {
    DDRA = 0xFF;
    count = 0;
    GICR = (1<<INT0) | (1<<INT1);
    MCUCR = MCUCR & 0b11111111;

    while(1) {
        PORTA = count;
    }
}
```
