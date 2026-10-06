---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "DMA frees the CPU from copying (one interrupt per block) but is slower than the CPU and needs bus arbitration; device-independent I/O software gives uniform interfaces, buffering, error reporting, device allocation and a uniform block size."
sources: ["Tanenbaum MOS 4e, sec. 5.1.4 (DMA) and sec. 5.3.2 (device-independent I/O software)"]
---
**DMA.**

- **Major advantage:** the CPU is not involved in the transfer. Without DMA the CPU is interrupted for every byte or word; with DMA it programs the controller (address, count, direction) and is interrupted **once per block**, so it can run other processes meanwhile.
- **Major disadvantage:** the DMA controller is usually much **slower than the CPU**; if the CPU would otherwise have nothing to do while waiting, it is better to use programmed or interrupt-driven I/O. DMA also needs extra hardware and competes with the CPU for the memory bus (*cycle stealing*), and a controller that cannot drive the device at full speed gains little.

**Functions of device-independent I/O software** (so that applications and drivers are written once, independent of the individual device):

1. **Uniform interfacing for device drivers:** every driver presents the same functions (read, write, ...) to the kernel, so a new driver can be added without changing the OS; also naming of devices and protection (who may access which device).
2. **Buffering:** data is buffered in kernel space when the user buffer is not yet available or when the device delivers data in different unit sizes, to decouple the device speed from the process.
3. **Error reporting:** most errors are handled by the drivers, but programming errors (e.g. writing to an input device) and persistent device errors are reported to the caller by this layer.
4. **Allocating and releasing dedicated devices:** devices that cannot be shared (e.g. a CD recorder) are allocated to one process at a time, with open/close or queued requests.
5. **Device-independent block size:** disks may have different sector sizes, but this layer presents a **uniform logical block size** to the upper layers.
