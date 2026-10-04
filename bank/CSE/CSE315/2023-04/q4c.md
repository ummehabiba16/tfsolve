---
marks: 15
topics: [usart]
kind: analysis
source: {page: 28}
note: "Y is printed as 'A UART sender (Y)' although it is the receiver; 'Briefly explain you answer' as printed."
---
A UART sender (X) is configured with:

`UCSRA = 0b00000000; UCSRB = 0b00001100; UCSRC = 0b10001110; UBRRL = 0x33; UBRRH = 0x00;`

A UART sender (Y) is configured with:

`UCSRA = 0b00000000; UCSRB = 0b00010000; UCSRC = 0b10100110; UBRRL = 0x33; UBRRH = 0x00;`

X has sent a 9-bit data 0b010011001 which has been received by Y. Which of frame, data over run and parity errors will happen at Y? Briefly explain you answer.

**Registers (from Table 1, attached)**

| Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| UCSRA | RXC | TXC | UDRE | FE | DOR | PE | U2X | MPCM |
| UCSRB | RXCIE | TXCIE | UDRIE | RXEN | TXEN | UCSZ2 | RXB8 | TXB8 |
| UCSRC | URSEL | UMSEL | UPM1 | UPM0 | USBS | UCSZ1 | UCSZ0 | UCPOL |

*UCSZ2, UCSZ1, UCSZ0: 000 = 5-bit, 001 = 6-bit, 010 = 7-bit, 011 = 8-bit, 111 = 9-bit. UPM1, UPM0: 00 = No parity, 10 = even parity, 11 = odd parity. USBS: 0 = 1 stop bit, 1 = 2 stop bits.*
