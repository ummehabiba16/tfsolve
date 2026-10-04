---
marks: 10
topics: [usart]
kind: code
source: {page: 27}
---
The following function (Figure 4(b)) is responsible for receiving 8-bit UART data. However, the function is faulty. Identify the flaws and correct them with brief explanation.

**Figure 4(b)**

```c
unsigned char USART_Receive()
{
    while (!(UCSRA & (1 << UDRE)));
    unsigned char data = UDR;
    unsigned char status = UCSRA;
    if (status & (1 << FE) | (1 << DOR) | (1 << PE)) {
        return ~data;
    }
    return data;
}
```

**Registers (from Table 1, attached)**

| Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| UCSRA | RXC | TXC | UDRE | FE | DOR | PE | U2X | MPCM |
| UCSRB | RXCIE | TXCIE | UDRIE | RXEN | TXEN | UCSZ2 | RXB8 | TXB8 |
| UCSRC | URSEL | UMSEL | UPM1 | UPM0 | USBS | UCSZ1 | UCSZ0 | UCPOL |

*UCSZ2, UCSZ1, UCSZ0: 000 = 5-bit, 001 = 6-bit, 010 = 7-bit, 011 = 8-bit, 111 = 9-bit. UPM1, UPM0: 00 = No parity, 10 = even parity, 11 = odd parity. USBS: 0 = 1 stop bit, 1 = 2 stop bits.*
