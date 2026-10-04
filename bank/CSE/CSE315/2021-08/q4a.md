---
marks: 15
topics: [ppi-8255, transfer-modes]
kind: analysis
source: {page: 46}
---
Programmable Peripheral Interface 82C55 has its timing diagram for Mode 1 (Strobed Input) as follows (Figure 4(a)-1).

![Figure 4(a)-1: Mode 1 strobed input: STB, IBF (Buffer full), INTR (Interrupt requested), RD, Port; 'Data strobed into port', 'Data read by microprocessor'](figures/q4a-1.png)

Its timing diagram for Mode 1 (Strobed Output) is as follows (Figure 4(a)-2).

![Figure 4(a)-2: Mode 1 strobed output: WR, OBF (Buffer full), INTR (Interrupt requested), ACK, Port; 'Data sent to port', 'Data removed from port'](figures/q4a-2.png)

Now, a hardware engineer gives you the following as the timing diagram of 82C55 for Mode 2 (Figure 4(a)-3).

![Figure 4(a)-3: proposed Mode 2 diagram: WR, OBF, INTR, ACK, STB, IBF, Port A, RD; 'Data output (OUT) to port A', 'Data stored in port A', 'Data read from port A', 'Data input (IN) from port A'](figures/q4a-3.png)

You need to pinpoint in case you find any flaw in the above timing diagram for Mode 2, specially for the change in the *INTR* signal in response to the initial down edge of the $\overline{RD}$ signal.

If you find any flaw(s), then you need to elaborate and justify how that flaw(s) can be fixed. In case you think that the above design is flawless, you need to explicitly mention that. Unless you mention anything, your answer will be treated as a blank answer.

You need to justify your answer.
