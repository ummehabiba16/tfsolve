---
author: ai
via: chat
status: unverified
summary: Firmware/BIOS in ROM runs POST, finds a boot device, loads its boot sector, which loads the kernel; the kernel initialises and starts the first process.
sources: [Introduction slides 7-10, 'Tanenbaum, MOS 4e, sec. 1.3.2']
imported_from: tfsolve-questions/data/solutions/2019-20.json
---
1. On power-up the CPU begins executing the BIOS/firmware held in ROM.
2. BIOS runs POST (power-on self-test): checks RAM and devices and builds a device inventory.
3. BIOS picks a boot device from a configured list and reads its first sector (MBR / boot sector) into memory.
4. The boot loader in that sector loads the OS kernel (often via a second-stage loader) into RAM.
5. The kernel initialises its data structures and drivers, starts the first process, and the machine is ready for users.
