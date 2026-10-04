---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Flaws: waits on UDRE (transmit flag) instead of RXC; reads UDR before UCSRA, which clears FE/DOR/PE; operator precedence makes the error test always true; returning ~data does not signal an error. Fix: wait for RXC, read UCSRA first, mask with (FE|DOR|PE), report errors separately."
sources: ["EHP Serial Communication slides 45-47 (receiving a character, RXC)", "EHP Serial Communication slides 57-58 (read status before UDR)", "EHP Serial Communication slides 62-64 (FE, DOR, UDRE)"]
---
**Flaws**

1. **Waiting on the wrong flag.** `UDRE` (USART Data Register Empty) is a **transmit** flag: it says the transmit buffer can take a new byte, and it is normally 1. The receiver must wait for **RXC** (Receive Complete), which is set when an unread byte is in the receive buffer. As written, the loop ends at once and UDR is read before any data has arrived.
2. **Status read after the data.** Reading UDR moves the receive FIFO on and **changes FE, DOR and PE** (and RXB8). The status must be read from UCSRA **before** reading UDR, otherwise the error bits belong to the next character (or are cleared).
3. **Operator precedence.** In C, `&` binds tighter than `|`, so
   `status & (1<<FE) | (1<<DOR) | (1<<PE)` means `(status & (1<<FE)) | 0x08 | 0x04`, which is **always non-zero**. Every byte is treated as an error. The mask must be in parentheses: `status & ((1<<FE)|(1<<DOR)|(1<<PE))`.
4. **Returning `~data` is not an error signal.** The complement of a byte is just another valid byte, so the caller cannot tell an error from good data. The error should be reported separately (e.g. return a 16-bit value with an error code, or a status flag).

**Corrected function**

```c
// returns 0..255 for good data, -1 if a frame, overrun or parity error occurred
int USART_Receive(void)
{
    while (!(UCSRA & (1 << RXC)));            // 1. wait until a byte is received
    unsigned char status = UCSRA;             // 2. read status FIRST
    unsigned char data   = UDR;               //    then read the data
    if (status & ((1 << FE) | (1 << DOR) | (1 << PE)))   // 3. correct mask
        return -1;                            // 4. clear error indication
    return data;
}
```
