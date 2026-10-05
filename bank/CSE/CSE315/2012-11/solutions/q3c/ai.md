---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "UDRE interrupt: it keeps firing as long as UDRE = 1 (buffer empty), and writing UDR is the only way to clear UDRE, so the ISR must either write new data to UDR or disable UDRIE when there is nothing more to send; otherwise the CPU is stuck re-entering the ISR. RXC interrupt: it keeps firing while RXC = 1, so the ISR must read UDR (which clears RXC), even if the data is not needed; otherwise a new interrupt occurs as soon as the ISR returns."
sources: ["EHP Serial Communication slides 67-68 (transmission using UDRIE interrupt, reception using RXCIE interrupt)"]
---
**Data Register Empty interrupt (UDRIE / UDRI)**

- The interrupt is executed **as long as UDRE = 1**, i.e. as long as the transmit buffer is empty, not just once.
- UDRE is cleared **only by writing to UDR**.
- **Precaution:** in the UDRE ISR, **either write the next byte to UDR, or disable the interrupt (UDRIE = 0)** when there is no more data to send. Enable UDRIE again only when new data is waiting. Otherwise the ISR re-enters endlessly and the main program never runs.

**Receive Complete interrupt (RXCIE / RXCI)**

- The interrupt is executed **as long as RXC = 1**, i.e. while unread data is in the receive buffer.
- RXC is cleared by **reading UDR**.
- **Precaution:** the RXC ISR **must read UDR** (and read UCSRA status and RXB8 before it, for errors and 9-bit data), even if the byte is to be thrown away. Otherwise a new interrupt occurs as soon as the ISR returns.

(The TXC interrupt has no such problem: its flag is cleared automatically when its ISR runs. Shared buffers between ISRs and main should be `volatile`.)
