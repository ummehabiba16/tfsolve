---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) FAT file dates use a 7-bit year since 1980, so dates stop at 2107 (the paper's Y2018 is probably Y2108); (ii) user-level context: process text, data, user stack, shared memory; (iii) device driver: kernel code controlling a device; (iv) device controller: hardware between the device and the bus."
sources: ["Tanenbaum MOS 4e, sec. 4.5.1 and 5.1; Bach, ch. 6"]
---
**(i) The "Y2018 problem" of the MS-DOS file system** (probably meant: the **year-2108 problem**; the question prints "Y2018"). A FAT directory entry stores the date in 16 bits: 5 bits day, 4 bits month and **7 bits for the year counted from 1980**. A 7-bit year can represent only 128 years, **1980 to 2107**; in the year 2108 the field overflows, so file dates would be wrong (like the Y2K problem). (The time field also has only 2-second resolution.) *Ambiguity:* if "Y2018" really is meant, no such limit exists in FAT, so it is taken as a misprint.

**(ii) User-level context of a process in UNIX.** The part of the context that the process itself can access in user mode: the **text** (program code), the **data** (initialised and uninitialised data and heap), the **user stack** and the **shared-memory** regions, i.e. the contents of its virtual address space in user mode.

**(iii) Device driver.** Operating-system **software (kernel code)** that controls one type of device: it translates generic requests (read/write) into device-specific commands, programs the controller's registers, starts DMA, handles the device's interrupts and errors; it hides the device details from the rest of the OS.

**(iv) Device controller.** The **hardware (electronics)** that sits between the device and the system bus (e.g. the disk controller on a card or the chip): it has registers and a buffer, executes the commands sent by the driver, converts the device's signals into bytes/blocks, checks errors (ECC) and raises interrupts when finished.
