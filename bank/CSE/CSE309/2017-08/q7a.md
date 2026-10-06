---
marks: 8
topics: [yacc, shift-reduce]
kind: analysis
source: {page: 45}
---
For the following grammar how many conflicts will be reported by yacc/bison? Specify the type of each conflict along with reason of its occurrence.

$$a \to b \mid c \mid \text{PLUS} \mid \text{MINUS}$$

$$b \to b\ \text{MINUS}\ b \mid \text{PLUS}$$

$$c \to c\ \text{PLUS}\ c \mid \text{MINUS}$$
