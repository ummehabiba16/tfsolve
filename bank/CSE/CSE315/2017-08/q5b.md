---
marks: 10
topics: [usart]
kind: code
source: {page: 71}
---
Implement a C function void UART_send (unsigned char data) which receives a character as an argument and transmits it using UART by **polling on the TXC bit of UCSRA.**

**UCSRA (from Table 1):** RXC | TXC | UDRE | FE | DOR | PE | U2X | MPCM
