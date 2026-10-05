---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Single handshake: sender puts data on the lines (1) and pulses STB' (2); receiver latches it and answers with an ACK pulse (3, 4) meaning 'got it, send the next'. Double handshake: sender lowers STB' to ask 'ready?' (1); receiver raises ACK 'ready' (2); sender puts data (3) and raises STB' 'data valid' (4); receiver lowers ACK 'data received' (5), then the data may be removed."
sources: ["Hall, Microprocessors and Interfacing, Ch. 9 (single and double handshake data transfer)", "Brey, The Intel Microprocessors, Sec. 11-3 (8255 handshake modes)"]
---
**(i) Single handshake I/O**

```text
DATA   ......<======================>
STB'   ----------+     +-----------------------------
                 |_____|
ACK                      +-------+
       __________________|       |___________________
            (1)  (2)     (3)     (4)
```

1. The sender puts a byte on the data lines.
2. It pulses $\overline{STB}$ low to tell the receiver that valid data is present; the receiver latches the data.
3. The receiver answers with an **ACK** pulse, meaning "I have taken the data".
4. When ACK ends the sender may send the next byte.

The sender knows each byte was received, so a slow receiver (e.g. a printer) does not lose data. Used by the 8255 in mode 1.

**(ii) Double handshake I/O**

```text
STB'   ----+                       +-----------------
           |_______________________|
ACK             +-----------------------+
       _________|                       |____________
DATA   ..............<=====================>
           (1)  (2)  (3)           (4)  (5)
```

1. The sender lowers $\overline{STB}$: "I have data, are you ready?"
2. The receiver raises **ACK**: "I am ready."
3. The sender puts the byte on the data lines.
4. The sender raises $\overline{STB}$: "Data is valid, take it." The receiver latches the data.
5. The receiver lowers **ACK**: "Data received." Only now may the sender remove the data and start the next transfer.

Each side confirms every step, so the transfer is reliable even between devices of very different speeds, at the cost of more control steps.
