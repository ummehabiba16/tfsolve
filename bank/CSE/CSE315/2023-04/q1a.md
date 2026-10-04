---
marks: 10
topics: [external-interrupts, interrupt-execution]
kind: code
source: {page: 25}
note: "Printed as 'ATmege32' and '000000010' (nine digits) in the ring-counter sequence."
---
Suppose an active-high push switch is connected to the PD3 pin of an ATmege32. Also, eight LEDs are connected to PB0-PB7. Write a C code for an 8-bit ring counter using an interrupt. An 8-bit ring counter counts like 00000001, 000000010, 00000100, ..., 10000000, then loops back to 00000001. Subsequently, display the counter status using LEDs.

- The counter must increment only after you release the switch.

- You are to write the interrupt service routine to allow another interrupt to execute in the middle of the current interrupt.

- You can assume the switches are perfect and do not produce any bouncing.

**Registers (from Table 1, attached)**

| Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| GICR | INT1 | INT0 | INT2 | - | - | - | IVSEL | IVCE |
| MCUCR | - | - | - | - | ISC11 | ISC10 | ISC01 | ISC00 |

*Trigger codes: 00 = low level, 01 = any logical change, 10 = falling, 11 = rising.*

Attached sheet: [Figures and Tables for Section A](figures/sheet-1.png), [ATmega32 pinout](figures/sheet-2.png).
