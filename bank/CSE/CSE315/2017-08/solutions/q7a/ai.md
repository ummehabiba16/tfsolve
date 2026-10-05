---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Bugs: wait loop missing '!' (must wait while RXC = 0); UCSRA sets U2X (double speed) -> 0x00; UCSRB enables TXEN instead of RXEN -> 0b00010000; UCSRC has URSEL = 0 (writes UBRRH), no parity, 2 stop bits, 7 bits -> 0b10100110; UBRR wrong -> 8 MHz/(16 x 1200) - 1 = 416 = 0x01A0 (UBRRH = 0x01 written before UBRRL = 0xA0); F_CPU (8 MHz) not defined for _delay_ms."
sources: ["EHP Serial Communication slides 25-31, 35-47 (UBRR, UCSRA/B/C, URSEL, UART_init and UART_receive)"]
---
**Corrected code** (changed lines marked `// FIX`)

```c
#define F_CPU 8000000UL                       // FIX 1: 8 MHz clock for _delay_ms
#include <avr/io.h>
#include <util/delay.h>

unsigned char UART_receive(void){
    while (!(UCSRA & (1<<RXC)));              // FIX 2: wait WHILE no byte received
    return UDR;
}

int main(void)
{
    DDRB = 0xFF;
    UCSRA = 0b00000000;                       // FIX 3: U2X = 0, normal speed
    UCSRB = 0b00010000;                       // FIX 4: RXEN = 1 (receiver), not TXEN
    UCSRC = 0b10100110;                       // FIX 5: URSEL=1, even parity, 1 stop, 8 bits
    UBRRH = 0x01;                             // FIX 6: UBRR = 416 = 0x01A0,
    UBRRL = 0xA0;                             //        high byte first, then low byte

    while(1)
    {
        unsigned char c = UART_receive();
        PORTB = c;
        _delay_ms(1000);
    }
}
```

**The mistakes**

1. **F_CPU not defined.** `_delay_ms()` calculates its loop from F_CPU; without it the default (1 MHz) is assumed, so at 8 MHz the delay would be 8 times too short.
2. **Wrong polling condition.** `while ((UCSRA & (1<<RXC)));` loops while a byte **has** arrived and falls through when none has, so UDR is read before data arrives. It must loop while RXC = 0.
3. **UCSRA = 0b00000010** sets **U2X** (double speed), but normal speed is required.
4. **UCSRB = 0b00001000** enables only the **transmitter (TXEN)**; the program receives, so **RXEN** (bit 4) must be set.
5. **UCSRC = 0b00001100** is wrong in four ways: URSEL (bit 7) = 0, so the write goes to **UBRRH** instead of UCSRC; UPM = 00 (no parity, even parity needs 10); USBS = 1 (2 stop bits, need 1); UCSZ1:0 = 10 (7 bits, need 11 for 8 bits). Correct: URSEL = 1, UMSEL = 0, UPM = 10, USBS = 0, UCSZ1:0 = 11, i.e. **0b10100110**.
6. **Baud rate.** For 1200 bps at 8 MHz, normal speed:

$$UBRR = \frac{8\,000\,000}{16 \times 1200} - 1 = 415.67 \approx 416 = 0x01A0$$

so UBRRH = 0x01, UBRRL = 0xA0 (actual 1199 bps, $-0.08\%$). The given 0x1604 is wrong, and UBRRH can hold only 4 bits. UBRRH must be written **before** UBRRL, because writing UBRRL updates the baud-rate prescaler immediately.
