---
marks: 15
topics: [risc-cisc]
kind: conceptual
source: {page: 49}
---
Here are two instruction set approaches to add two numbers stored in address @a and @b, and then store the result in address @c. Identify the instruction set approaches with proper reasons. Write three key differences between them. Which one is used in Atmega32?

**Approach i)**

```text
LOAD R1, @a
LOAD R2, @b
ADD R3, R1, R2
STORE R3, @c
```

**Approach ii)**

```text
ADD @c, @a, @b
```
