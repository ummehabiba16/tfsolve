---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "UBRR = 8 MHz / (16 x 9600) - 1 = 51.08 -> 51 (UBRRH = 0, UBRRL = 51; actual 9615 bps, +0.16%). UCSRA = 0x00, UCSRB = 0x10 (RXEN), UCSRC = 0x86 (URSEL, async, no parity, 1 stop, 8 bits). Loop: wait for RXC, PORTA = UDR, _delay_ms(1000)."
sources: ["EHP Serial Communication slides 25-31, 35-41 (UBRR formula, UCSRA/B/C, UART_init example)", "EHP Serial Communication slides 45-47 (UART_receive with RXC polling)"]
---
**Calculations** ($f_{osc}$ = 8 MHz, normal speed U2X = 0)

$$UBRR = \frac{f_{osc}}{16 \times \text{baud}} - 1 = \frac{8 \times 10^6}{16 \times 9600} - 1 = 51.08 \approx 51 = 0x33$$

Actual rate $= 8\times10^6/(16 \times 52) = 9615$ bps, error $+0.16\%$.

| Register | Value | Bits |
|:--|:--|:--|
| UCSRA | 0b00000000 | U2X = 0, MPCM = 0 |
| UCSRB | 0b00010000 | RXEN = 1 (receiver only), no interrupts, UCSZ2 = 0 |
| UCSRC | 0b10000110 | URSEL = 1, UMSEL = 0 (async), UPM = 00 (no parity), USBS = 0 (1 stop), UCSZ1:0 = 11 (8 bits), UCPOL = 0 |
| UBRRH, UBRRL | 0x00, 0x33 | 51 |

**Code**

```c
#define F_CPU 8000000UL
#include <avr/io.h>
#include <util/delay.h>

void UART_init(void)
{
    UCSRA = 0b00000000;          // normal speed
    UCSRB = 0b00010000;          // enable receiver
    UCSRC = 0b10000110;          // async, no parity, 1 stop bit, 8 data bits
    UBRRH = 0x00;
    UBRRL = 0x33;                // 51: 9600 bps at 8 MHz
}

unsigned char UART_receive(void)
{
    while ((UCSRA & (1 << RXC)) == 0);   // wait until a character arrives
    return UDR;
}

int main(void)
{
    DDRA = 0xFF;                 // PORTA output
    UART_init();
    while (1) {
        PORTA = UART_receive();  // receive a word (8-bit character), show on PORTA
        _delay_ms(1000);         // sleep for 1 second
    }
}
```

*Note:* while the program sleeps, characters keep arriving; the USART buffers only two, so a PC sending faster than one character per second will cause data overrun (DOR). "Sleep" is implemented as a 1 s delay.
