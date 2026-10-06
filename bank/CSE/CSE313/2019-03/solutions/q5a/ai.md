---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Abstraction hides complicated hardware details behind a simple interface; the OS provides abstractions such as files, processes and address spaces."
sources: ["Tanenbaum MOS 4e, sec. 1.1.2 (the OS as an extended machine)"]
---
**Abstraction** means presenting a complex thing through a **simple, clean interface** that hides the unimportant (and ugly) details, so that the user of the interface can concentrate on *what* it does rather than *how*.

**Example: the file abstraction.** A disk consists of tracks, sectors, heads and a controller with dozens of commands (seek, read sector, set DMA address, handle errors, ...). An application programmer does not want to deal with that. The OS offers the abstraction of a **file** with a name: `open`, `read`, `write`, `close`. The program writes `write(fd, buf, n)` and the OS (driver, file system) takes care of block allocation, buffering, disk scheduling and error handling, and the same program works on any disk or SSD.

The OS gives similar abstractions for other resources: a **process** (instead of CPU registers and interrupts), an **address space** (instead of physical RAM chunks), a **socket** (instead of the network card). This makes programs simpler, portable and independent of the hardware.
