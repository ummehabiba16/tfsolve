---
marks: 10
topics: [instruction-encoding]
kind: numerical
source: {page: 54}
note: "Printed as 'Suppose a µP have to wait'."
---
Suppose a µP have to wait for at least 1 second before polling on the I/O devices in a Polled I/O based system. For this purpose you are given the following code snippet. (7+3=10)

**Figure for Q.7(a)**

```text
...
    MOV CX, n
DELAY:
    MOV m, CX
    MOV CX, n
DELAY_2:
    LOOP DELAY_2
    MOV CX, m
    LOOP DELAY
...
```

If the µP is running at 10MHz, what should you put as the value of n? What is the actual amount of delay you will achieve with your calculated value of n? You can assume it takes 4 clock cycles to execute a MOV instruction. 17 clock cycles are required to execute a LOOP instruction when it jumps to the target address and 5 clock cycles otherwise.
