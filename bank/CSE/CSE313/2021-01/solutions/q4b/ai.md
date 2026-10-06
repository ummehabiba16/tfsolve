---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Cycle stealing moves one word per bus grant; burst mode moves a whole block while holding the bus. Disk power saving: spin down when idle, cache/buffer in memory (flash), lower rotation speed or prefetch to lengthen idle periods."
sources: ["Tanenbaum MOS 4e, sec. 5.1.4 (DMA) and sec. 5.8 (power management: hard disk)"]
---
**Cycle stealing vs burst mode (DMA modes).**

| | Cycle stealing | Burst mode |
|:--|:--|:--|
| Transfer | one word at a time; the DMA controller *steals* a bus cycle from the CPU for each word | the controller tells the device to acquire the bus, transfer a whole **block** (a burst of words) and release the bus |
| Effect on CPU | CPU is delayed by one bus cycle now and then, so it is hardly noticed | CPU (and other devices) may be locked out of the bus for a considerable time |
| Speed | slower for the transfer | faster, more efficient |

**Three techniques to reduce the power consumption of a hard disk.**

1. **Spin down the disk** after a period of inactivity (a timeout); it is spun up again on the next request. The trade-off is the delay and energy of spinning up.
2. **Cache / buffer in main memory (or a flash cache):** reads served from the cache and writes buffered (write-behind) mean the disk does not need to be spun up for every request, so it stays off longer.
3. **Lengthen idle periods:** batch/**prefetch** I/O (and let applications give hints), and/or use a **lower rotation speed** (multi-speed disks), so that requests come in bursts and the disk can sleep in between.
