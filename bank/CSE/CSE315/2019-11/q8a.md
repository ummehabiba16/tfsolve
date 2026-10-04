---
marks: 5
topics: [interrupts-8086]
kind: analysis
source: {page: 54}
note: "The printed marks line reads (5+5=10) for Q8 as a whole: (a) 5 and (b) 5."
---
What is wrong with the following interrupt handling procedure? In what situation will it work despite the mistake?

![Figure for Q.8(a): main program; 1. Push FLAGS, 2. Clear IF, 3. Clear TF, 4. Push CS, 5. Push IP, 6. Fetch ISR address; Interrupt Service Routine (ISR): PUSH registers ... POP registers, IRET; return: POP CS, POP IP, POP FLAGS](figures/q8a-1.png)
