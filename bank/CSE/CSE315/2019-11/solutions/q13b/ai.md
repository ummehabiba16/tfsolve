---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "1 MHz / 8 gives 8 us per tick: elapsed = (50 x 65536 + 1200) x 8 us = 3,278,000 x 8 us = 26.224 s."
sources: ["EHP Timer_Part_1 slides 29-32 (measuring elapsed time with overflow count)"]
---
Assumption: system clock 1 MHz (the paper's default). With prescaler 8, TCNT1 increments every

$$t_{tick} = \frac{8}{1\ \text{MHz}} = 8\ \mu s$$

TCNT1 started at 0, overflowed 50 times (each overflow = 65536 ticks), and ended at 1200:

$$\text{ticks} = 50 \times 65536 + 1200 = 3\,276\,800 + 1200 = 3\,278\,000$$

$$t = 3\,278\,000 \times 8\ \mu s = 26\,224\,000\ \mu s = \mathbf{26.224\ s}$$
