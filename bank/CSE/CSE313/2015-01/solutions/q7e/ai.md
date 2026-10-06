---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Every partition has a boot block so that any partition can hold a bootable OS and the BIOS/MBR can load the boot block of the active partition; the layout of all file systems stays uniform."
sources: ["Tanenbaum MOS 4e, sec. 4.2.1 and ch. 1 (file system layout, booting)"]
---
A disk is divided into **logical partitions**, each of which may hold a different file system and, possibly, a different operating system (multi-boot). Booting works in two stages: the BIOS reads the **MBR** (sector 0 of the disk), whose program finds the **active partition** and loads **that partition's boot block**, which then loads the operating system kernel from the file system in the partition.

Hence **every partition needs its own boot block**:

- any partition might be made **bootable** (or be the one chosen by a boot manager such as GRUB) without reformatting;
- the boot block contains the code that knows the layout of **that** file system and where its kernel is;
- keeping the layout the same for all partitions (boot block, super block, inode list, data blocks) makes the file-system code uniform; a non-bootable partition simply leaves its boot block unused.
