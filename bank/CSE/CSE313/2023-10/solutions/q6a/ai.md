---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
**(i) Device-driver design for different values of $n$** (i.e., how often/how much data `write_fd` pushes through the descriptor).

**(a) $n$ always small (10):** the function is called frequently but each call only issues 10 tiny `write()`s. Doing one device operation (interrupt + DMA setup) per tiny write is very wasteful relative to the amount of data moved. *Design*: a **buffering driver** -- append each write's bytes into an in-kernel ring buffer; only actually kick off a device transfer (DMA) once the buffer reaches a reasonable size or after a short timeout, coalescing many small writes into one larger, more efficient device operation.

```text
driver_write(buf, len):
    ring_buffer.append(buf, len)
    if ring_buffer.size >= FLUSH_THRESHOLD or timer_expired:
        start_dma(ring_buffer); ring_buffer.clear()
```

**(b) $n$ always huge (1,000,000):** each call already generates a very large volume of small internal writes. Here the workload is heavy and sustained, so in addition to coalescing into a large buffer, it is worth **switching to a polling-based completion model** (or streaming DMA with interrupt coalescing) rather than raising one interrupt per chunk transferred -- because with sustained heavy traffic the CPU can reasonably expect there is always more work, so polling avoids per-transfer interrupt overhead (same reasoning as "high and regular I/O $\to$ polling").

**(c) A mixture of both (10 and 1,000,000):** use an **adaptive/hybrid** driver: default to interrupt-driven, buffered writes (good for the small/bursty case), but dynamically switch to polling mode whenever the instantaneous write rate/queue length crosses a threshold indicating a sustained heavy burst, then switch back to interrupts once the load subsides. This is exactly the design used by real high-performance NIC drivers (e.g. Linux NAPI) to get low latency under light load and high throughput without livelock under heavy load.

**(ii) `open()`+`open()` vs. `open()`+`dup()`.**

**Code block 1** calls `open("file.txt")` *twice*. Each `open()` creates a brand-new entry in the system-wide open-file table, each with *its own independent file offset* starting at 0. So `write_fd(fd1)` advances fd1's own offset while writing \"0123456789\"; then `write_fd(fd2)` starts writing *again from offset 0* (its own, separate, still-zero offset), **overwriting** what fd1 just wrote at the start of the file. The two writes clobber each other rather than accumulate.

**Code block 2** uses `fd2 = dup(fd1)`. `dup()` does *not* create a new open-file-table entry; it creates a new file descriptor in the process's descriptor table that points to the *same* open-file-table entry as `fd1` (and bumps its reference count). Both descriptors therefore **share the same file offset**. `write_fd(fd1)` advances the shared offset while writing; `write_fd(fd2)` then *continues* from wherever that shared offset ended up, so its output is **appended right after** fd1's output -- the file ends up containing both writes concatenated, with no overwriting.

In short: two independent `open()`s $\to$ two independent offsets $\to$ overlapping/overwritten output; `dup()` $\to$ one shared offset $\to$ concatenated output.
