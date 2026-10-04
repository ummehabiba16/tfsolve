---
marks: 10
topics: [push-buttons, avr-io]
kind: code
source: {page: 73}
---
Suppose two active high push switches are connected to PA0 and PA4 of an ATmega32 MCU. Also, eight active low LEDs are connected to PORT B. Write a C code to implement an 8 bit ring counter which counts up when the push switch connected to PA0 is pressed and counts down when the other one is pressed. The output is shown with the LEDs. Use polling approach. Keep in mind that the buttons bounce a lot. Also assume the push switches will not be pressed simultaneously.
