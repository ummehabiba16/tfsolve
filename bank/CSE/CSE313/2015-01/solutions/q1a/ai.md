---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "UNIX kernel block diagram (file subsystem and process control subsystem above hardware control); the file subsystem reaches the hardware via the buffer cache and device drivers."
sources: ["Bach, Design of the UNIX Operating System, ch. 2 (fig. 2.1: block diagram of the system kernel)"]
---
![Block diagram of the UNIX system kernel](figures/kernel.png)

**Levels.** User programs and libraries run at *user level* and enter the kernel through the **system call interface** (a trap). The kernel has two main subsystems; below them the **hardware control** layer handles interrupts and machine-dependent details, and the hardware sits at the bottom.

**Subsystems and their interaction**

- **File subsystem:** manages files (allocation, free space, access control, i-nodes) and moves data between the file system and user space. It uses the **buffer cache** to reduce disk accesses, and the **device drivers** (*block* drivers for disks/tapes through the buffer cache, *character* drivers for raw devices and terminals) to talk to the hardware.
- **Process control subsystem:** creation, termination and scheduling of processes; **interprocess communication** (signals, pipes, messages, shared memory), the **scheduler** (which process gets the CPU) and **memory management** (allocation of memory, swapping/paging).
- **Interaction.** The two subsystems interact when a program is loaded for execution: the file subsystem reads the executable into memory, and the process control subsystem allocates memory for it; the memory manager also uses the file subsystem/disk driver to swap processes. The scheduler lets the process control subsystem decide which process runs while the others wait for file-system I/O.

**How the file subsystem interacts with the hardware.**

In the UNIX kernel structure the **file subsystem** is in the upper part of the kernel and talks to the hardware only **through the device drivers**:

1. A system call such as `read` enters the kernel through the **system call interface** and is handled by the file subsystem (algorithms `namei`, `bmap`, ...) that finds which disk block holds the data.
2. For **block devices** (disks, tapes) the request goes through the **buffer cache**: if the block is in the cache the data is copied without disk access; otherwise the file subsystem asks the **block device driver** to read the block into a buffer.
3. The **block device driver** works out the physical position (cylinder, track, sector) and issues commands to the **disk controller** through the **hardware control** layer (interrupt handlers and machine-dependent code).
4. When the transfer finishes, the device raises an **interrupt**; the hardware-control layer calls the driver's interrupt handler, which wakes up the sleeping process (`wakeup`); the kernel then copies the data from the buffer to user space.
5. For **character devices** (terminals, raw disks) the file subsystem calls the **character device driver** directly (raw devices may bypass the buffer cache), again through the hardware control layer.

So the file subsystem is hardware independent: all device specifics are inside the drivers and the hardware-control layer.
