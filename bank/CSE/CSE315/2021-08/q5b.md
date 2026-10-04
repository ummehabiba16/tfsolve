---
marks: 12
topics: [external-interrupts]
kind: code
source: {page: 48}
---
Suppose an active high push switch is connected to PD2 pin of an Atmega32. Also, eight LEDs are connected to PA0-PA7. Write a C code for 8 bit **ring counter** using external interrupt. An 8 bit ring counter counts like 00000001, 00000010, 00000100, ..., 10000000 then loops back to 00000001. Subsequently, display the counter status using LEDs. The counter must count up only after you release the switch.

**Registers (from the attached list)**

| Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| GICR | INT1 | INT0 | INT2 | - | - | - | IVSEL | IVCE |
| MCUCR | - | - | - | - | ISC11 | ISC10 | ISC01 | ISC00 |
| MCUCSR | JTD | ISC2 | - | - | - | - | - | - |

*Trigger codes: 00 = low level, 01 = any logical change, 10 = falling edge, 11 = rising edge. ISC2: 0 = falling edge trigger, 1 = rising edge trigger.*

Attached sheet: [list of registers](figures/sheet-1.png).
