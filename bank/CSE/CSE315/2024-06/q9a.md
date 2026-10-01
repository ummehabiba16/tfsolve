---
marks: 12
topics: [external-interrupts, push-buttons]
kind: code
mandatory: true
source: {page: 19}
note: "Printed as 'starts form 0'."
---
Suppose, you have an active-low push switch connected to the PD2 pin of an ATMega32, and an active-high push switch is connected to the PD3 pin. Also eight LEDs are connected to PA0-PA7. You want to build an 8-bit counter that will increase by two after the first switch is released, and decrease by two after the second switch is pressed. Kindly assume that the counter starts form 0 and both switches will not be pressed at the same time. The 8-bit counter status will be displayed by the mentioned LEDs. When the counter overflows, it will go back to zero. Please write a C code to implement the above scenario by making use of the external interrupts in ATMega32.
