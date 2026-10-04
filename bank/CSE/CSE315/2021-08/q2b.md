---
marks: 20
topics: [address-decoding, memory-banks]
kind: diagram
source: {page: 44}
---
The following figure (Figure 2(b)) shows a working circuit that incorporates sixteen 62256, 32K $\times$ 8 static RAMs interfaced to the 8088, beginning at memory location 00000H. This circuit board uses two decoders to select the memory components and a third to select the other decoders for the appropriate memory sections. Sixteen 32K RAMs fill memory from location 00000H through location 7FFFFH, for 512K bytes of memory.

![Figure 2(b): three 74LS244 buffers (A0-A7, A8-A14, WR/RD/A15-A17), 74LS139 (U4) on A18/A19, two 74LS138 decoders (U3, U9) selecting the CS of eight 62256 RAMs each (Bank 0 and Bank 1), 74LS245 data buffer (U5), 74LS20, 74LS00 and 74LS04 gates with IO/M](figures/q2b-1.png)

Now, keeping the memory specifications and address spacing same, you need to use a new microprocessor 80XX instead of 8088. In the new 80XX microprocessor, there is a 16-bit data bus having all other features exactly same as 8088.

You need to show the required change(s) in the above circuit as needed to use 80XX in place of 8088. You need to justify your answer.
