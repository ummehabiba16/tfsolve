---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Clear TXC by writing 1 to it, write the character to UDR, then wait until TXC becomes 1 (the whole frame has been shifted out and no new data is waiting)."
sources: ["EHP Serial Communication slides 64-66 (UDRE and TXC flags; TXC must be cleared before each transmission)"]
---
TXC is set when the **entire frame has been shifted out** of the transmit shift register and no new data is waiting. It is **not** cleared automatically by writing UDR (only by its interrupt or by writing a 1 to it), so it must be cleared **before** each transmission; otherwise the flag left from the previous character would make the wait end immediately.

```c
void UART_send(unsigned char data)
{
    UCSRA |= (1 << TXC);               // clear TXC by writing logic 1
    UDR = data;                        // start transmission
    while (!(UCSRA & (1 << TXC)));     // wait until the frame is completely sent
}
```

(Using `|=` also writes back U2X and MPCM unchanged; the other flag bits are read-only or cleared by other means. Polling TXC is slower than polling UDRE, because the next character cannot be loaded until the previous one has fully left the line, but it guarantees the transmission is complete, e.g. before switching an RS-485 driver or entering sleep.)
