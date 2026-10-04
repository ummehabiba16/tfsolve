---
marks: 10
topics: [memory-banks]
kind: diagram
source: {page: 52}
note: "Printed as 'using at 8086 µP' and 'Minimum how many clock are required?'."
---
Suppose you want to access memory location 00111H to 00114H using at 8086 µP. Minimum how many clock are required? Draw the signals (timing diagram) of **BHE** and **A0** throughout these clock cycles. (4+6=10)

| $\overline{BHE}$ | A0 | Accessed Bank | Data Bits |
|:-:|:-:|:-:|:-:|
| 0 | 0 | Both banks | D0 - D15 |
| 0 | 1 | Odd bank | D8 - D15 |
| 1 | 0 | Even bank | D0 - D7 |
| 1 | 1 | None | None |
