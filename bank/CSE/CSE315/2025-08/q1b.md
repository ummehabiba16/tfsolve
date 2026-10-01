---
marks: 10
topics: [descriptors, privilege-protection]
kind: analysis
mandatory: true
source: {page: 1}
---
Carefully observe the table below in an 80286 microprocessor and answer the following questions. Your answer **must** have proper justifications.

| Selector Values (in hex) | Descriptor Values (in hex) |
|:-:|:-:|
| 0046 | 00 00 B7 42 54 78 |
| 0017 | 00 00 9B 12 34 56 |
| 0085 | 00 00 D2 95 15 96 |

(i) **Derive** the values of the following segment registers: **CS**, **DS**, and **SS**.

(ii) **Explain** whether the physical address of the code segment is allowed to be accessed.

(iii) **Categorize** which segment's physical address has not been accessed yet?

![Access right byte and descriptor formats for 80286 and 80386 (attached to the paper)](figures/q1b-1.png)
