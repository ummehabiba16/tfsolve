---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Problems: data is put on the lines before A knows B is ready, and A removes/changes it while STB' is still low, before signalling 'data valid' with STB' rising, so B may latch wrong data; ACK falls (B says 'received') before STB' rises. Correct order: (1) A: STB' low = request; (2) B: ACK high = ready; (3) A: data valid; (4) A: STB' high = data valid, latch it; (5) B: ACK low = data received; (6) A: remove/change data."
sources: ["Hall, Microprocessors and Interfacing, Ch. 9 (double handshake data transfer)"]
---
**Correct double handshake (Hall).** (1) A asks "are you ready?" by lowering $\overline{STB}$. (2) B answers "ready" by raising ACK. (3) A puts the data on the lines and (4) raises $\overline{STB}$ to say "data valid, take it". (5) B reads the data and lowers ACK to say "data received". (6) Only then may A remove or change the data.

**(i) Problems in the given diagram**

1. **Data is placed before B is ready.** The data changes (new byte) **before** $\overline{STB}$ falls, i.e. before A has asked B and before B has raised ACK. In a double handshake A must wait for ACK (ready) before driving the data.
2. **Data is removed too early.** The data changes again **while $\overline{STB}$ is still low**, before A raises $\overline{STB}$. The rising edge of $\overline{STB}$ is the "data valid, latch now" signal, so at that moment the lines already carry the wrong (next) data, and B latches garbage.
3. **ACK falls before $\overline{STB}$ rises.** ACK low means "I have received the data", but B says so before A has even signalled that the data is valid. The two handshake signals are out of order, so neither machine really knows the state of the other.

**(ii) Corrected timing diagram**

```text
           (1)                   (4)
STB'   -----+                     +----------------------
            |_____________________|
                 (2)                   (5)
ACK               +---------------------+
       ___________|                     |________________
Data   ----------------X====================X------------
                      (3)                  (6)
```

| No. | Transition | Initiated by | Meaning |
|:-:|:--|:-:|:--|
| 1 | $\overline{STB}$ high $\to$ low | A | "I have data to send; are you ready?" |
| 2 | ACK low $\to$ high | B | "I am ready to receive." |
| 3 | Data becomes valid | A | A puts the byte on the data lines. |
| 4 | $\overline{STB}$ low $\to$ high | A | "Data is valid; latch it now." |
| 5 | ACK high $\to$ low | B | "I have taken the data." |
| 6 | Data removed / changes | A | A may now remove the byte and start the next transfer. |
