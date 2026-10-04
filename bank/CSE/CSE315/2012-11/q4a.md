---
marks: 18
topics: [adc-auto-trigger, usart]
kind: conceptual
source: {page: 92}
---
Suppose you are designing a micro-controller based automated system that takes input from an analog device and sends it to a computer via USART after the necessary conversion is done. The analog device generates analog voltage precisely in every 200 µs and the analog voltage persists for a very brief period of time. Assume that the micro-controller is operating at 1MHz clock rate. You cannot use polling approach in any step of your automated system. Now answer the following: (3+3+3+3+6=18)

(i) Which mode of the ADC is appropriate in this case and why?

(ii) How can you ensure that ADC samples analog voltage precisely in every 200 µs?

(iii) What will be triggering event to start the A-to-D conversions?

(iv) How many ISRs you need to write and what are the purposes of those ISRs?

(v) Write the necessary steps to configure the micro-controller for the automated system. You need to mention the name of the necessary registers and action on the register.
