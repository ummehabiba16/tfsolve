---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "BIOS boot: power-on reset, POST, BIOS picks the boot device, loads the MBR, MBR loads the active partition's boot block/boot loader, the loader loads the kernel, the kernel initialises and starts init."
sources: ["Tanenbaum MOS 4e, ch. 1 (booting the computer)", "Course slides: Introduction, booting"]
---
Steps of booting a BIOS (not UEFI) PC:

1. **Power on / reset:** the CPU starts executing at a fixed address (the reset vector) in the **BIOS** ROM/flash.
2. **POST (power-on self-test):** the BIOS checks the RAM and basic hardware and initialises the devices (keyboard, video, disks).
3. **Choose the boot device:** the BIOS reads the configured boot order (stored in CMOS) and finds the first bootable device.
4. **Load the MBR:** the BIOS reads **sector 0** (the Master Boot Record, 512 bytes, ending with the signature `0x55AA`) of that device into memory (at `0x7C00`) and jumps to it.
5. **MBR program:** it reads the partition table, finds the **active partition** and loads that partition's **boot block** (or a second-stage boot loader such as GRUB).
6. **Boot loader:** it reads the OS **kernel** (and, if needed, an initial RAM disk) from the file system into memory, possibly after showing a menu, and transfers control to it.
7. **Kernel start-up:** the kernel initialises memory management, interrupt handling and device drivers and mounts the root file system.
8. **First process:** the kernel starts the first user process (`init`/`systemd`), which starts the system services and the login prompt.
