---
marks: 15
topics: [external-interrupts, push-buttons]
kind: code
source: {page: 72}
---
Suppose one active low push switch A and two active high push switches, B and C are connected to INT0, INT1, and INT2 pin of an ATmega32 MCU, respectively. Also, Eight LEDs are connected to PORTB. Write a C code to implement an 8 bit ring counter which counts up when the push switch A is pressed and counts down when B is pressed. Pressing C will reset the counter to 0. The output is shown with the LEDs. Keep in mind that the buttons bounce a lot. Briefly describe how the relevant registers were set and how debouncing was achieved.

The codes for external interrupt events of INT0 and INT1 are as following:

| Code | Interrupt Triggering Events |
|:--|:--|
| 00 | Low Level |
| 01 | Any Logical Change |
| 10 | Falling Edge |
| 11 | Rising Edge |

The code for external interrupt events of external INT2:

| Code | Interrupt Triggering Events |
|:--|:--|
| 0 | Falling Edge |
| 1 | Rising Edge |

**Registers (from Table 1)**

| Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| GICR | INT1 | INT0 | INT2 | - | - | - | IVSEL | IVCE |
| GIFR | INTF1 | INTF0 | INTF2 | - | - | - | - | - |
| MCUCR | SE | SM2 | SM1 | SM0 | ISC11 | ISC10 | ISC01 | ISC00 |
| MCUCSR | JTD | ISC2 | - | JTRF | WDRF | BORF | EXTRF | PORF |

Attached: [Figure 2, ATmega32 pinout](figures/sheet-1.png), [Table 1, list of registers](figures/sheet-2.png).
