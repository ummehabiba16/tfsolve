---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Frame Error: the first stop bit is received as 0 (stop bit missing). Data OverRun: the receive buffer (2 characters) is full, a character waits in the shift register, and a new start bit arrives. FE and DOR are flags in UCSRA."
sources: ["EHP Serial Communication slides 57, 62-63, 76-77 (FE, DOR, data recovery)"]
---
**Frame Error (FE).** The receiver expects a stop bit (logic 1) at the stop bit time. If the **first stop bit is sampled as 0** (majority vote of the 3 centre samples), the frame is not properly terminated, which usually means a baud-rate mismatch, noise or a break. The second stop bit is ignored by the receiver.

*Detection:* the **FE flag (bit 4 of UCSRA)** is set for that character. It belongs to the character currently in the receive buffer, so it must be read **before** reading UDR.

**Data OverRun Error (DOR).** Data is lost because the receiver is full: the receive buffer UDR (two characters) is full, a new character is waiting in the receive shift register, and **a new start bit is detected**. One or more frames are lost between the last frame read from UDR and the next one.

*Detection:* the **DOR flag (bit 3 of UCSRA)** is set. It means software is not reading UDR fast enough. It is cleared when the received character is read from UDR.
