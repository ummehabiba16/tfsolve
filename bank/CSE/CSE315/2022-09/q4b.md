---
marks: 10
topics: [external-interrupts, push-buttons]
kind: code
source: {page: 35}
---
You are to design a Fibonacci counter using ATmega32. An active-low switch is connected to PD2. When the switch is pressed, the counter will increase. The counter is an 8-bit number. It starts from 0 and increases like the following sequence: 1, 1, 2, 3, 5, 8 ....When the counter overflows, it goes back to zero. The current value of the counter will be displayed in eight LEDs connected to PORTA. Write a C program to implement this counter using external interrupt.
