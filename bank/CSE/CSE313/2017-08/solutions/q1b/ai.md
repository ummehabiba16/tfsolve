---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The file subsystem reaches the hardware through the buffer cache and the block device drivers (and directly through character drivers), which sit on the hardware-control layer."
sources: ["Bach, ch. 2 and 3 (system kernel architecture, buffer cache)"]
---
![UNIX kernel structure](figures/kernel.png)

In the UNIX kernel structure the **file subsystem** is in the upper part of the kernel and talks to the hardware only **through the device drivers**:

1. A system call such as `read` enters the kernel through the **system call interface** and is handled by the file subsystem (algorithms `namei`, `bmap`, ...) that finds which disk block holds the data.
2. For **block devices** (disks, tapes) the request goes through the **buffer cache**: if the block is in the cache the data is copied without disk access; otherwise the file subsystem asks the **block device driver** to read the block into a buffer.
3. The **block device driver** works out the physical position (cylinder, track, sector) and issues commands to the **disk controller** through the **hardware control** layer (interrupt handlers and machine-dependent code).
4. When the transfer finishes, the device raises an **interrupt**; the hardware-control layer calls the driver's interrupt handler, which wakes up the sleeping process (`wakeup`); the kernel then copies the data from the buffer to user space.
5. For **character devices** (terminals, raw disks) the file subsystem calls the **character device driver** directly (raw devices may bypass the buffer cache), again through the hardware control layer.

So the file subsystem is hardware independent: all device specifics are inside the drivers and the hardware-control layer.
