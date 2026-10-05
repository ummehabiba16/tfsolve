---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "At 1 MHz, normal speed: UBRR = 1e6/(16 x 4800) - 1 = 12.02 -> 12 (4808 bps, +0.16%). With the usual 8N1 format and both directions: UCSRA = 0x00, UCSRB = 0x18 (RXEN, TXEN), UCSRC = 0x86 (URSEL, async, no parity, 1 stop, 8 bits), UBRRH = 0x00, UBRRL = 0x0C."
sources: ["EHP Serial Communication slides 25-31, 36-41 (UBRR formula, UCSRA/B/C, UART_init example)"]
---
**Baud rate register** (U2X = 0):

$$UBRR = \frac{f_{osc}}{16 \times \text{baud}} - 1 = \frac{10^6}{16 \times 4800} - 1 = 12.02 \approx 12$$

Actual rate $= 10^6/(16 \times 13) = 4808$ bps, error +0.16%.

**Register values** (assumed frame: asynchronous, 8 data bits, no parity, 1 stop bit; transmitter and receiver enabled, polling)

| Register | Value | Meaning |
|:--|:--|:--|
| UCSRA | 0b00000000 = 0x00 | normal speed, no multiprocessor mode |
| UCSRB | 0b00011000 = 0x18 | RXEN = 1, TXEN = 1, no interrupts, UCSZ2 = 0 |
| UCSRC | 0b10000110 = 0x86 | URSEL = 1, async, no parity, 1 stop bit, UCSZ1:0 = 11 (8 bits) |
| UBRRH | 0x00 | |
| UBRRL | 0x0C | 12 |

```c
void USART_init(void)
{
    UCSRA = 0x00;
    UCSRB = 0x18;
    UCSRC = 0x86;
    UBRRH = 0x00;
    UBRRL = 0x0C;     // 4800 bps at 1 MHz
}
```

(Double-speed mode would give UBRR = $10^6/(8 \times 4800) - 1 = 25$ with UCSRA = 0x02, the same 4808 bps.)
