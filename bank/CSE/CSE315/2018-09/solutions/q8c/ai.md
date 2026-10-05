---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Wait for RXC; read UCSRA (status) and UCSRB (RXB8, the 9th bit) before UDR; if FE or PE is set return -1; else return (RXB8 << 8) | UDR."
sources: ["EHP Serial Communication slides 45-47, 57-58 (receiving; read status and RXB8 before UDR, 9-bit reception)"]
---
For 9-bit characters the 9th bit is in **RXB8** (UCSRB bit 1). Reading UDR changes RXB8, FE, DOR and PE, so **UCSRA and UCSRB must be read before UDR**.

```c
unsigned int UART_receive(void)
{
    unsigned char status, resh, resl;

    while (!(UCSRA & (1 << RXC)));       // wait for a received character

    status = UCSRA;                      // error flags (read first)
    resh   = UCSRB;                      // 9th bit is RXB8
    resl   = UDR;                        // low 8 bits (read last)

    if (status & ((1 << FE) | (1 << PE)))
        return -1;                       // frame or parity error

    resh = (resh >> RXB8) & 0x01;        // extract the 9th bit
    return ((unsigned int)resh << 8) | resl;
}
```

*Note:* the return type is `unsigned int`, so `-1` arrives as 0xFFFF; valid 9-bit data are 0x000-0x1FF, so the caller can still tell an error from data.
