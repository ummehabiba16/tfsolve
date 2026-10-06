---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Hybrid design: PIO/polling for the small bursts, interrupt coalescing under load, DMA for large transfers, request queues; trade-offs listed."
sources: ["OSTEP ch. 36 (polling, interrupts, DMA, coalescing)", "Tanenbaum MOS 4e, sec. 5.1-5.3"]
---
**Requirements.** (a) *Bursts of many small requests* need low per-request overhead; (b) *very large requests* need the CPU out of the data path.

**Design decisions.**

1. **DMA for large transfers.** The driver gives the DMA engine the buffer address, length and direction; the CPU is free to run other processes and gets one interrupt when the transfer is complete. *Pro:* no CPU time wasted copying data. *Con:* set-up cost of programming the DMA engine, pinned buffers, memory-bandwidth contention.
2. **Programmed I/O (PIO) for small requests.** Programming DMA costs more than copying a few bytes; for tiny requests it is cheaper to write them directly to the device registers. *Pro:* low latency per small request. *Con:* the CPU does the copy, which is fine only for small sizes.
3. **Hybrid polling/interrupts for the bursts.** One interrupt per request would give an *interrupt storm* (and possible receive livelock): the CPU spends all its time in handlers. So the driver uses **interrupt coalescing**: the device waits a little and raises one interrupt for several completed requests; or the driver switches to *polling* when the request rate is high and to interrupts when it is low (two-phase: poll briefly, then sleep). *Pro:* far fewer context switches under load. *Con:* a request may wait longer for its completion (latency), and polling wastes CPU time when the device is slow.
4. **Request queue.** Keep a queue (ring buffer) of requests so the device can be fed continuously, and merge/batch small adjacent requests. *Pro:* better device utilisation. *Con:* more memory and complexity; needs locking.

**Trade-off summary.** The design is a compromise: DMA wins for large sizes, PIO wins for small sizes, coalescing/polling wins for high rates; each adds code complexity and tuning parameters (the thresholds for switching).
