---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Simple I/O (no timing signals), simple strobe I/O (data + strobe), single handshake (strobe + acknowledge), double handshake (request/ready, data, strobe/acknowledge). Keyboard: simple strobe I/O (data valid for a long time, one strobe per key). Dot-matrix printer: handshake I/O (single handshake; it is slow and must say when it has taken each byte)."
sources: ["Hall, Microprocessors and Interfacing, Ch. 9 (parallel data transfer: simple, simple strobe, single handshake, double handshake)", "Brey, The Intel Microprocessors, Sec. 11-3 (8255 strobed I/O, printer interface)"]
---
**1. Simple I/O.** No timing signals: the CPU just reads or writes the port whenever it wants; the data is assumed always valid.

**2. Simple strobe I/O.** The sender puts data on the lines and gives a **strobe** pulse ($\overline{STB}$) to say "data is valid now"; the receiver latches it on the strobe.

**3. Single handshake I/O.** The sender puts data and pulses $\overline{STB}$ (1); the receiver latches it and answers with **ACK** (2), "I have taken it, send the next" (3). The sender waits for ACK before the next byte.

**4. Double handshake I/O.** (1) The sender lowers $\overline{STB}$: "I want to send". (2) The receiver raises ACK: "I am ready". (3) The sender puts the data on the lines (then raises $\overline{STB}$, (4)). (5) The receiver, having read the data, lowers ACK: "data taken". Both sides check each other at every step.

```text
Simple I/O
DATA   ......<================================>
             data valid; read/written any time

Simple strobe I/O
DATA   ......<======================>
STB'   ------------+       +-------------------------
                   |_______|

Single handshake
DATA   ......<======================>
STB'   ----------+     +-----------------------------
                 |_____|
ACK                      +-------+
       __________________|       |___________________
                 (1)     (2)     (3)

Double handshake
STB'   ----+                       +-----------------
           |_______________________|
ACK             +-----------------------+
       _________|                       |____________
DATA   ..............<=====================>
           (1)  (2)  (3)           (4)  (5)
```

| Mode | Advantages | Disadvantages |
|:--|:--|:--|
| Simple I/O | Simplest, no extra lines, fastest | No synchronisation; only for devices that are always ready or always valid (LEDs, switches) |
| Simple strobe | Receiver knows exactly when data is valid; one extra line | Sender does not know if the receiver took the data; a fast sender can overwrite data |
| Single handshake | Transfer is confirmed; works with a slower receiver | Two control lines, slower than strobe; sender must wait for ACK |
| Double handshake | Most reliable: each side confirms readiness and receipt; handles very different speeds | Most control steps, slowest, more complex logic |

**Best mode**

- **(i) Keyboard: simple strobe I/O.** A key press is a rare, slow event; the keyboard encoder puts the key code on the lines and gives a strobe. The data stays valid much longer than the CPU needs to read it, so no acknowledgement is required.
- **(ii) Dot-matrix printer: handshake I/O (single handshake).** The printer is much slower than the CPU and is sometimes busy (moving the head, feeding paper). Each byte must be acknowledged before the next is sent, otherwise characters would be lost; single handshake (8255 mode 1 strobed output with $\overline{ACK}$) is the usual choice, and double handshake is used if even more reliability is needed.

*Note:* "dot matrix" is read as a dot-matrix printer. If an LED dot-matrix display were meant, simple I/O would do, because the display is always ready to accept a new pattern.
