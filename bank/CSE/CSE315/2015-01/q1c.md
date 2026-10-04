---
marks: 20
topics: [push-buttons, avr-io]
kind: code
source: {page: 86}
---
We want to build a simple **Fibonacci counter**. Our counting system is connected with a push button to take pulse input and with 8 LEDs to display current counter value. When the system starts up, our counter will show 0. After successive presses at the push button, the counter will display following sequences,

**1, 1, 2, 3, 5, 8, 13, ...**

-Since we are using only 8-bits for our counter, when the counter overflows it goes to its initial value, i. e., **0**. Using ATmega 16 digital I/O write **a complete C program** to implement this counter system.
