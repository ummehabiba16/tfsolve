---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "UBRR = 2e6/(16 x 9600) - 1 = 12.02, so 12: UBRRH = 00000000, UBRRL = 00001100; UCSRA = 00000000; UCSRB = 11011000 (RXCIE, TXCIE, RXEN, TXEN); UCSRC = 10101100 (URSEL, even parity, 2 stop, 7-bit)."
sources: ["EHP Serial Communication slides 25-31 (UBRR, UCSRA, UCSRB, UCSRC, character size table)", "EHP Serial Communication slides 36-37, 67-68 (UART_init example; interrupt-driven Tx/Rx)"]
---
**Baud rate** (normal speed):

$$UBRR = \frac{2\times10^{6}}{16\times9600}-1 = 13.02-1 = 12.02 \approx 12$$

The actual rate is $2\times10^6/(16\times13) = 9615$ bps, a +0.16% error, so normal speed is fine.

| Register | Value (binary) | Meaning |
|:--|:-:|:--|
| UCSRA | 0000 0000 | U2X = 0 normal speed, MPCM = 0 |
| UCSRB | 1101 1000 | RXCIE = 1, TXCIE = 1 (interrupts), UDRIE = 0, RXEN = 1, TXEN = 1, UCSZ2 = 0, RXB8 = TXB8 = 0 |
| UCSRC | 1010 1100 | URSEL = 1, UMSEL = 0 (async), UPM1:0 = 10 (even parity), USBS = 1 (2 stop bits), UCSZ1:0 = 10 (with UCSZ2 = 0: 7-bit), UCPOL = 0 |
| UBRRH | 0000 0000 | URSEL = 0 when writing UBRRH |
| UBRRL | 0000 1100 | 12 |

```c
void USART_init(void){
    UCSRA = 0b00000000;   // normal speed, disable multi-proc
    UCSRB = 0b11011000;   // Rx/Tx complete interrupts, enable Tx and Rx
    UCSRC = 0b10101100;   // async, even parity, 2 stop bits, 7 data bits
    UBRRH = 0b00000000;
    UBRRL = 0b00001100;   // 9600 bps at 2 MHz
    sei();                // global interrupt enable
}
```
