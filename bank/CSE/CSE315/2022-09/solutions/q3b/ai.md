---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "UCSRA = 0b00000010 (U2X), UCSRB = 0b00001000 (TXEN only), UCSRC = 0b10101100 (async, even parity, 2 stop bits, 7 data bits), UBRR = 1e6/(8 x 3800) - 1 = 31.9 -> 32 (UBRRH = 0, UBRRL = 32), actual 3788 bps (-0.3%) at 1 MHz."
sources: ["EHP Serial Communication slides 25-31 (UBRR formula, double speed, UCSRA/B/C, character size)", "EHP Serial Communication slides 36-37, 52-54 (UART_init examples)"]
---
**Register values** (assumption: system clock 1 MHz, the paper default)

| Register | Value | Bits set |
|:--|:--|:--|
| UCSRA | 0b00000010 | U2X = 1 (double speed), MPCM = 0 |
| UCSRB | 0b00001000 | TXEN = 1 only (RXEN = 0); interrupts off; UCSZ2 = 0 |
| UCSRC | 0b10101100 | URSEL = 1, UMSEL = 0 (async), UPM1:0 = 10 (even), USBS = 1 (2 stop), UCSZ1:0 = 10, UCPOL = 0 |
| UBRRH, UBRRL | 0, 32 | baud rate 3800 bps |

7 data bits: UCSZ2:0 = 010 (UCSZ2 = 0 in UCSRB, UCSZ1:0 = 10 in UCSRC).

**Baud rate.** In double-speed mode the divisor is 8 instead of 16:

$$UBRR = \frac{f_{osc}}{8 \times \text{baud}} - 1 = \frac{10^6}{8 \times 3800} - 1 = 31.89 \approx 32$$

Actual rate $= 10^6 / (8 \times 33) = 3788$ bps, an error of $-0.3\%$ (acceptable).

```c
void UART_init(void)
{
    UCSRA = 0b00000010;   // U2X = 1: double speed
    UCSRB = 0b00001000;   // TXEN = 1: transmitter only, no interrupts
    UCSRC = 0b10101100;   // URSEL=1, async, even parity, 2 stop bits, 7 data bits
    UBRRH = 0;            // URSEL = 0 when writing UBRRH
    UBRRL = 32;           // 1 MHz / (8 x 3800) - 1 = 31.9 -> 32
}
```
