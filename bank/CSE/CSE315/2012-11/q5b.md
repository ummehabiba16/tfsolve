---
marks: 15
topics: [descriptors, privilege-protection]
kind: analysis
source: {page: 93}
---
Suppose DS has the value 000B (in Hex). The following table describes the GDT:

| Entry | Descriptor Value (in Hex) |
|:-:|:-:|
| 0 | — |
| 1 | 0031E110FFFF0000 |
| 2 | 0031E101FFFF0000 |
| 3 | 0031E100FFFF0000 |

The base address stored in GDTR is 0000FFFF.

Now answer the following questions:

(i) What should be the value of the limit field of GDTR?

(ii) Suppose you are using DS as the segment selector (with the value given above) to access a memory location for reading and writing data. Will the instruction execute successfully? Justify your answer.

(iii) Suppose you want to read some data from the GDT. Using the above configuration, would it be possible? Explain.
