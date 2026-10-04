---
marks: 15
topics: [address-decoding]
kind: analysis
source: {page: 43}
---
A memory designer is given a task of designing a memory unit using four sections each of 64K-bit. The overall memory unit needs to be 256K$\times$1. Here, addresses will need to be applied in row and column addresses. First, the row address is applied and a total of 1024 bits get selected from the four sections. Next, the column address is applied to filter 4 bits out of the selected 1024 bits. Finally, the most significant bits of the row and column addresses determine one bit from the filtered-out 4 bits.

To perform the task, the designer designs the following (Figure 2(a)).

![Figure 2(a): A0-A8 with RAS, CAS, WE into row and column latches; a decoder and four 64K arrays (256 x 256), each with a multiplexer, feeding a 4-to-1 MUX to Din/Dout. Notes: 1. Decoder is an 8-line to 256-line decoder. 2. Multiplexer is 256 to 1 line. 3. Multiplexer is 4 to 1 line.](figures/q2a-1.png)

Now, you need to pinpoint in case you find any flaw in the above design. If so, then you need to elaborate and justify how that flaw(s) can be fixed. In case you think that the above design is flawless, you need to explicitly mention that. Unless you mention anything, your answer will be treated as a blank answer.

You need to justify your answer.
