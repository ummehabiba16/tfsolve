---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "X sends 9 data bits, no parity, 2 stop bits; Y expects 8 data bits, even parity, 1 stop bit, same baud. Y reads data 10011001 (0x99), takes X's 9th bit 0 as the parity bit (correct for even parity: four 1s) and X's first stop bit 1 as its stop bit. So no frame, overrun or parity error occurs."
sources: ["EHP Serial Communication slides 18-19 (frame: start, LSB first, parity, stop)", "EHP Serial Communication slides 25-31 (UBRR, UCSRA/B/C, character size)", "EHP Serial Communication slides 60-63 (reception, second stop bit ignored, FE, DOR)"]
---
**Decode the settings**

| | X (sender) | Y (receiver) |
|:--|:--|:--|
| UCSRB | 0b00001100: TXEN = 1, **UCSZ2 = 1** | 0b00010000: RXEN = 1, UCSZ2 = 0 |
| UCSRC | 0b10001110: URSEL = 1, async, UPM = 00 (**no parity**), USBS = 1 (**2 stop bits**), UCSZ1:0 = 11 | 0b10100110: URSEL = 1, async, UPM = 10 (**even parity**), USBS = 0 (**1 stop bit**), UCSZ1:0 = 11 |
| Character size | UCSZ = 111: **9 bits** | UCSZ = 011: **8 bits** |
| UBRR, U2X | 0x0033 = 51, U2X = 0 | 0x0033 = 51, U2X = 0 |

Both use the same baud rate ($1\ \text{MHz}/(16 \times 52) \approx 1200$ bps, assuming the 1 MHz default clock), so the bit times match.

**Frame on the line** (data 0b010011001, LSB first)

| Bit time | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| X sends | start 0 | d0 = 1 | d1 = 0 | d2 = 0 | d3 = 1 | d4 = 1 | d5 = 0 | d6 = 0 | d7 = 1 | d8 = 0 | stop 1 | stop 1 |
| Y reads as | start | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | parity | stop | (idle) |

**Check each error at Y**

- **Data received:** D7..D0 = 1001 1001 = **0x99**. The 9th bit of X (d8 = 0) is taken as the parity bit.
- **Parity error (PE): no.** Even parity: the data 10011001 has **four** 1s (already even), so the parity bit should be **0**. The bit received in the parity position is d8 = **0**, which matches. PE = 0.
- **Frame error (FE): no.** FE is set only if the (first) stop bit is read as 0. Y's stop bit falls on X's first stop bit, which is **1**. FE = 0. (X's second stop bit just looks like an idle line to Y.)
- **Data overrun (DOR): no.** DOR needs the receive buffer to be full (two unread characters) when a third start bit arrives. Only one frame is sent. DOR = 0.

**Answer: none of the three errors happens.** Y receives 0x99 with no error flag, but the 9th data bit sent by X is silently lost (it was used as the parity bit). It only works because that bit happens to equal the even-parity bit; e.g. if X's 9th bit had been 1, Y would report a parity error.
