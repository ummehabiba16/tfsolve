---
marks: 10
topics: [memory-banks]
kind: diagram
source: {page: 28}
note: "The table is transcribed as printed: it labels BHE=0, A0=1 as 'Even Bank, D8-D15' and BHE=1, A0=0 as 'Odd bank, D0-D7'."
---
Suppose you want to access memory location 00223h to 00226h using an 8086 µP.

i) Determine the minimum number of required clock cycle(s).

ii) Draw the signals (timing diagram) of $\overline{BHE}$ and **A0** throughout these clock cycles.

| $\overline{BHE}$ | A0 | Accessed Bank(s) | Data Bits |
|:-:|:-:|:-:|:-:|
| 0 | 0 | Both banks | D0-D15 |
| 0 | 1 | Even Bank | D8-D15 |
| 1 | 0 | Odd bank | D0-D7 |
| 1 | 1 | None | None |
