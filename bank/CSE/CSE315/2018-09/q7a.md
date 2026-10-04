---
marks: 15
topics: [usart]
kind: code
source: {page: 62}
---
Consider, you are continuously receiving data from a PC using UART in polling approach. The connection details are: Baud rate:9600 bps, no parity (code: 0x0), 1 stop bit (code: 0x0), 8 data bits (code: 0x3), and asynchronous communication (code: 0x0). Assume a clock speed of 8MHz. Write a C code that continuously receives a word from the PC, writes that word to PORTA, and sleeps for 1 second and repeats. Clearly specify the initialization of different registers and necessary calculations of their values.

**Registers (from the attached list)**

| Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| UCSRA | RXC | TXC | UDRE | FE | DOR | PE | U2X | MPCM |
| UCSRB | RXCIE | TXCIE | UDRIE | RXEN | TXEN | UCSZ2 | RXB8 | TXB8 |
| UCSRC | URSEL | UMSEL | UPM1 | UPM0 | USBS | UCSZ1 | UCSZ0 | UCPOL |

Attached sheet: [ATmega32 pinout and list of registers](figures/sheet-1.png).
