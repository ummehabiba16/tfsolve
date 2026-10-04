---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "The frame has 9 data bits (UCSZ = 111) but UDR holds only 8; the 9th bit must be written to TXB8 (UCSRB bit 0) before writing UDR. UART_send never sets TXB8, so bit 8 of data is lost (TXB8 stays 0). Fix: clear TXB8, set it if (data & 0x0100), then write UDR."
sources: ["EHP Serial Communication slide 56 (sending 9-bit characters: write the ninth bit to TXB8 before writing UDR)", "EHP Serial Communication slides 42-44 (UART_send with UDRE)"]
---
**The error.** UART_init selects **9-bit characters** (UCSZ2 = 1 in UCSRB and UCSZ1:0 = 11 in UCSRC). UDR is only **8 bits** wide: `UDR = data;` sends only bits 7-0 of `data`. The **ninth bit** of a 9-bit character is taken from **TXB8** (bit 0 of UCSRB), and it must be written **before** the low byte is written to UDR. UART_send never writes TXB8, so bit 8 of every character is always sent as 0 (whatever was left in TXB8) and the receiver gets wrong data.

**Corrected function** (two added lines)

```c
void UART_send(unsigned int data)
{
    while ((UCSRA & (1 << UDRE)) == 0x00);   // wait until the buffer is empty
    UCSRB &= ~(1 << TXB8);                   // added: clear the 9th bit
    if (data & 0x0100) UCSRB |= (1 << TXB8); // added: copy bit 8 of data to TXB8
    UDR = data;                              // low 8 bits; starts transmission
}
```

The order matters: TXB8 is set while the buffer is empty and before UDR is written, so the 9th bit belongs to the same frame as the low byte.
