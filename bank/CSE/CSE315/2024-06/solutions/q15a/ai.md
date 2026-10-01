---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Transmit: TXB8 is set and then always cleared (wrong order), and UDRE is not polled. Receive: RXC is not polled, UDR is read before UCSRA/UCSRB (that read clears the status and RXB8), the error test lacks parentheses (always true), and -1 is returned as unsigned."
sources: ["EHP Serial Communication slides 56-58 (sending/receiving 9-bit characters; read status and RXB8 before UDR)", "EHP Serial Communication slides 42-47 (polling UDRE / RXC)"]
---
**USART_Transmit**

1. **Lines 3-7, wrong order.** TXB8 is set if bit 8 is 1, and then line 7 **always clears** it, so the 9th bit is always sent as 0. The comment says "copy the 9th bit", but the clear must come **first**: `UCSRB &= ~(1<<TXB8); if (data & 0x0100) UCSRB |= (1<<TXB8);`
2. **No wait for an empty buffer.** UDRE is not polled before writing UDR (`while(!(UCSRA & (1<<UDRE)));`). If the previous character is still in the buffer, the new data and its TXB8 overwrite it, and TXB8 may be changed while the old character still needs it.

**USART_Receive**

3. **No wait for reception.** RXC is not polled (`while(!(UCSRA & (1<<RXC)));`), so the function may read old or garbage data.
4. **Lines 18-20, wrong read order.** **Reading UDR changes RXB8, FE, DOR and PE.** The status (UCSRA) and the 9th bit (RXB8 in UCSRB) must be read **before** UDR. Here UDR is read first, so `status` and `resh` belong to the **next** character in the buffer.
5. **Line 22, operator precedence.** `status & (1<<FE)|(1<<DOR)|(1<<PE)` is parsed as `(status & (1<<FE)) | (1<<DOR) | (1<<PE)`, which is **always non-zero**. The function would always return $-1$. It needs `status & ((1<<FE)|(1<<DOR)|(1<<PE))`.
6. **Return type.** The function returns `unsigned int`, so $-1$ becomes 0xFFFF. That only works if the caller compares with 0xFFFF; a valid 9-bit value never exceeds 0x01FF, so it is distinguishable but unclear.

**Corrected code**

```c
void USART_Transmit( unsigned int data )
{
    /* Wait for empty transmit buffer */
    while ( !( UCSRA & (1<<UDRE)) );
    /* Copy the 9th bit to TXB8 */
    UCSRB &= ~(1<<TXB8);
    if ( data & 0x0100 )
        UCSRB |= (1<<TXB8);
    /* Put data into buffer, sends the data */
    UDR = data;
}

unsigned int USART_Receive( void )
{
    unsigned char status, resh, resl;
    /* Wait for data to be received */
    while ( !(UCSRA & (1<<RXC)) );
    /* Get status and 9th bit, then data from buffer */
    status = UCSRA;
    resh = UCSRB;
    resl = UDR;
    /* If error, return -1 */
    if ( status & ((1<<FE)|(1<<DOR)|(1<<PE)) )
        return -1;
    /* Filter the 9th bit, then return */
    resh = (resh >> 1) & 0x01;
    return ((resh << 8) | resl);
}
```
