---
marks: 15
topics: [pins-8086, dma]
kind: analysis
source: {page: 41}
note: "Transcribed as printed: 'Pin 1 and 42' (the 8086 GND pins are 1 and 20), the request/grant pins are printed with overline as 'R0/GT0' and 'R1/GT1' (RQ/GT), and the status pin as 'SSO' with overline."
---
A design involving multiple 8086 processors incorporates the following pin usages –

a. The $MN/\overline{MX}$ pin has been connected to Logic 1.

b. One of the two *GND* pins (Pin 1 and 42) has been connected to Logic 0 retaining the other floating.

c. $\overline{R0}/\overline{GT0}$ and $\overline{R1}/\overline{GT1}$ pins are used as bidirectional lines for requesting and granting DMA operations.

d. $\overline{LOCK}$ pin is used for locking peripherals.

e. Combination of ($IO/\overline{M}$, $DT/\overline{R}$, and $\overline{SSO}$) pins are used for the purposes of memory read/write and I/O read/write.

Now, you need to pinpoint in case you find any of the above usages to be not workable. If so, then you need to elaborate and justify how that usage(s) can be modified to make that workable. In case you think that all of the above usages are workable, you need to explicitly mention that. Unless you mention anything, your answer will be treated as a blank answer.

You need to justify your answer.
