---
marks: 15
topics: [external-interrupts]
kind: code
source: {page: 62}
---
Suppose two **active high** push switches A and B are connected to INT0 and INT2 pin of an ATmega32 MCU, respectively. Also, eight **active high** LEDs (LED0 – LED7) are connected to PA0 – PA7. Write a C code using external interrupt to implement a ring counter, which counts up upon pressing the switch A and counts down upon pressing the switch B. Use 0 for don't care bits. The three external interrupt vector names are INT0_vect, INT1_vect, and INT2_vect.

The codes for external interrupt events of INT0 and INT1 are as following:

| Code | Interrupt Triggering Events |
|:--|:--|
| 00 | Low Level |
| 01 | Any Logical Change |
| 10 | Falling Edge |
| 11 | Rising Edge |

The codes for external interrupt events of external INT2:

| Code | Interrupt Triggering Events |
|:--|:--|
| 0 | Falling Edge |
| 1 | Rising Edge |

**Registers (from the attached list)**

| Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| GICR | INT1 | INT0 | INT2 | - | - | - | IVSEL | IVCE |
| GIFR | INTF1 | INTF0 | INTF2 | - | - | - | - | - |
| MCUCR | SE | SM2 | SM1 | SM0 | ISC11 | ISC10 | ISC01 | ISC00 |
| MCUCSR | JTD | ISC2 | - | JTRF | WDRF | BORF | EXTRF | PORF |

Attached sheet: [ATmega32 pinout and list of registers](figures/sheet-1.png).
