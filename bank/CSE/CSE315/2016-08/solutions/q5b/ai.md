---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) Normal speed: UBRR = 1e6/(16 x 9600) - 1 = 5.51 (5 or 6 gives about 8% error), so use double speed: UBRR = 1e6/(8 x 9600) - 1 = 12.02 -> 12 (9615 bps, 0.16%). (ii) UCSRA = 0b00000010, UCSRB = 0b00001000, UCSRC = 0b10000110, UBRRH = 0, UBRRL = 12. (iii) wait for UDRE, write UDR. (iv) loop: 5 x ('L', 500 ms), 5 x ('R', 200 ms)."
sources: ["EHP Serial Communication slides 25-26, 51-55 (UBRR formula, camera example at 9600 bps with double speed, USART_init, main loop)", "EHP Serial Communication slides 42-44 (send with UDRE polling)"]
---
**(i) UBRR**

Normal speed (U2X = 0):

$$UBRR = \frac{f_{osc}}{16 \times \text{baud}} - 1 = \frac{10^6}{16 \times 9600} - 1 = 5.51$$

Rounding to 5 or 6 gives 10417 or 8929 bps, about 8% error, too much for reliable UART. With **double speed** (U2X = 1):

$$UBRR = \frac{10^6}{8 \times 9600} - 1 = 12.02 \approx \mathbf{12}$$

Actual rate $= 10^6/(8 \times 13) = 9615$ bps, an error of only 0.16%.

**(ii) USART_init**

```c
void USART_init(void)
{
    UCSRA = 0b00000010;   // U2X = 1: double speed
    UCSRB = 0b00001000;   // TXEN = 1: transmitter (only sending is needed), polling
    UCSRC = 0b10000110;   // URSEL = 1, async, no parity, 1 stop bit, 8 data bits
    UBRRH = 0;
    UBRRL = 12;           // 9600 bps at 1 MHz in double-speed mode
}
```

**(iii) USART_send**

```c
void USART_send(unsigned char data)
{
    while ((UCSRA & (1 << UDRE)) == 0);   // wait until the transmit buffer is empty
    UDR = data;                           // send the character
}
```

**(iv) main**

```c
#define F_CPU 1000000UL
#include <avr/io.h>
#include <util/delay.h>
/* USART_init and USART_send as above */

int main(void)
{
    unsigned char i;
    USART_init();
    while (1) {
        for (i = 0; i < 5; i++) {      // rotate left 5 times
            USART_send('L');
            _delay_ms(500);
        }
        for (i = 0; i < 5; i++) {      // rotate right 5 times
            USART_send('R');
            _delay_ms(200);
        }
    }
}
```
