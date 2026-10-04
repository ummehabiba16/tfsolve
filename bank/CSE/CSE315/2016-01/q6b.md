---
marks: 10
topics: [external-interrupts]
kind: code
source: {page: 83}
note: "In (iii) 'pressing A will turn LED1 on' is printed (B is meant)."
---
Suppose two **active high** push switches A and B are connected to INT0 and INT1 pin of an ATmega 32 MCU, respectively. Also, Eight LEDs, LED0 - LED7 are connected to PB0 - PB7.

Write a C code using external interrupt to implement the following functionality:

(i) At any instance, only one LED is turned on and initially it is LED0.

(ii) Pressing push switch A will left **rotate** the Led configuration. That is if currently LED2 is on, pressing A will turn LED3 on.

(iii) Pressing push switch B will right **rotate** the LED configuration. That is if currently LED2 is on, pressing A will turn LED1 on.

The three external interrupt vector names are INT0_vect, INT1_vect, and INT2_vect.

The codes for external interrupt events are as follows:

| Code | Interrupt Triggering Events |
|:-:|:--|
| 00 | Low Level |
| 01 | Any Logical Change |
| 10 | Falling Edge |
| 11 | Rising Edge |

Attached sheet: [ATmega32 pinout and list of registers](figures/sheet-1.png).
