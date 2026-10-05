---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) UBRR = 4 MHz / (16 x 4800) - 1 = 51.08 -> 51 (0x33), actual 4808 bps (+0.16%). (ii) UCSRA = 0x00, UCSRB = 0x10 (RXEN), UCSRC = 0x86, UBRRH = 0, UBRRL = 51. (iii) loop: wait for RXC, PORTA = UDR, _delay_ms(2000). (iv) Double speed: UBRR = 4 MHz/(8 x 4800) - 1 = 103.2 -> 103 (UBRRL = 0x67) and UCSRA = 0x02 (U2X); the rest is unchanged."
sources: ["EHP Serial Communication slides 25-31, 35-47, 52-54 (UBRR formula, normal and double speed, UART_init, UART_receive)"]
---
**(i) UBRR value** (normal speed, $f_{osc}$ = 4 MHz)

$$UBRR = \frac{f_{osc}}{16 \times \text{baud}} - 1 = \frac{4 \times 10^6}{16 \times 4800} - 1 = 51.08 \approx \mathbf{51} = 0x33$$

Actual baud rate $= 4\times10^6/(16 \times 52) = 4808$ bps (+0.16% error).

**(ii) Initialization**

| Register | Value | Meaning |
|:--|:--|:--|
| UCSRA | 0b00000000 | normal speed |
| UCSRB | 0b00010000 | RXEN = 1 (receive, polling) |
| UCSRC | 0b10000110 | URSEL = 1, async, no parity, 1 stop bit, 8 data bits |
| UBRRH, UBRRL | 0x00, 0x33 | 51 |

```c
void UART_init(void)
{
    UCSRA = 0b00000000;
    UCSRB = 0b00010000;
    UCSRC = 0b10000110;
    UBRRH = 0x00;
    UBRRL = 0x33;          // 51
}
```

**(iii) Program**

```c
#define F_CPU 4000000UL
#include <avr/io.h>
#include <util/delay.h>

unsigned char UART_receive(void)
{
    while ((UCSRA & (1 << RXC)) == 0);   // wait for a received word
    return UDR;
}

int main(void)
{
    DDRA = 0xFF;                         // PORTA output
    UART_init();
    while (1) {
        PORTA = UART_receive();          // receive and show the word
        _delay_ms(2000);                 // sleep 2 seconds
    }
}
```

**(iv) Double-speed mode**

- (i): the divisor becomes 8: $UBRR = \dfrac{4 \times 10^6}{8 \times 4800} - 1 = 103.17 \approx \mathbf{103}$ (0x67), actual 4808 bps.
- (ii): **UCSRA = 0b00000010** (U2X = 1) and **UBRRL = 0x67** (UBRRH = 0). UCSRB and UCSRC are unchanged.
- (iii): no change in the code (only UART_init changes).
