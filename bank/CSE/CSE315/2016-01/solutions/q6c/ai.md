---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) 8 MHz: tick 0.125 us, overflow every 8.192 ms, 4 s / 8.192 ms = 488.28: 488 overflows plus 18432 counts. (ii) 4 MHz / 8: tick 2 us, overflow every 131.072 ms, 4 s / 131.072 ms = 30.52: 30 overflows plus 33920 counts. (iii) 16 MHz / 64: tick 4 us, overflow every 262.144 ms, 50 overflows = 13.1072 s."
sources: ["EHP Timer_Part_1 slides 7, 26-27 (prescaler, overflows needed for a 2 s delay)"]
---
Timer1 is 16 bits, so it overflows every $2^{16} = 65536$ ticks. Tick = prescaler / clock.

**(i) 8 MHz, no prescaler**

$$t_{tick} = \frac{1}{8\ \text{MHz}} = 0.125\ \mu s, \qquad T_{ovf} = 65536 \times 0.125\ \mu s = 8.192\ \text{ms}$$

$$n = \frac{4\ \text{s}}{8.192\ \text{ms}} = \mathbf{488.28}$$

So **488 full overflows** plus $0.28125 \times 65536 = 18432$ more counts (e.g. preload TCNT1 = 65536 - 18432 = 47104 for one extra period, or wait for 489 overflows if a delay of at least 4 s is enough: 4.006 s).

**(ii) 4 MHz, prescaler 8**

$$t_{tick} = \frac{8}{4\ \text{MHz}} = 2\ \mu s, \qquad T_{ovf} = 65536 \times 2\ \mu s = 131.072\ \text{ms}$$

$$n = \frac{4\ \text{s}}{131.072\ \text{ms}} = \mathbf{30.52}$$

So **30 full overflows** plus $0.5176 \times 65536 = 33920$ counts (or 31 overflows = 4.063 s).

**(iii) Time for 50 overflows at 16 MHz, prescaler 64**

$$t_{tick} = \frac{64}{16\ \text{MHz}} = 4\ \mu s, \qquad T_{ovf} = 65536 \times 4\ \mu s = 262.144\ \text{ms}$$

$$t = 50 \times 262.144\ \text{ms} = \mathbf{13.1072\ s}$$
