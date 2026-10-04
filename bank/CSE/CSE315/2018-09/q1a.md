---
marks: 20
topics: [clock-generator]
kind: analysis
source: {page: 58}
---
A system comprising a microprocessor 8086 or 8088, a peripheral device, and a clock generator needs to be designed in such a way that the clock generator feeds both the microprocessor and the peripheral device with 5 MHz clock signals. To ensure it, a hardware designer presents the following design where he applies 15 MHz crystal in between X1 and X2, and another 30 MHz signal to EFI to feed necessary clock signals to both the microprocessor and the peripheral device (not shown in the figure).

Now, you need to answer the following (with other necessary diagrams)-

(i) Does the microprocessor get the intended clock signal? If so, then you need to explain how it is getting the clock signal from corresponding input to the clock generator to the clock input of the microprocessor. If not, then you need to explain why the two clock inputs to the clock generator are not enough or appropriate in supplying the intended clock signal to the microprocessor.

(ii) Does the peripheral device get the intended clock signal? If so, then you need to explain how it is getting the clock signal from corresponding input to the clock generator to the clock input of the peripheral device. If not, then you need to explain why the two clock inputs to the clock generator are not enough or appropriate in supplying the intended clock signal to the peripheral device.

![Figure for Question 1(a): 30 MHz into EFI, 15 MHz crystal on X1/X2, F/C grounded, CSYNC, RES with 10K/10uF/diode reset circuit; 8284A CLK and RESET to the 8086 or 8088, RESET also to system reset](figures/q1a-1.png)
