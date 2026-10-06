---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A 700 MB file cannot fill a 700 MB CD-ROM because the disc also stores file-system structures (volume descriptors, directories) and the raw capacity includes error-correction overhead."
sources: ["Tanenbaum MOS 4e, sec. 4.5.3 (the CD-ROM file system, ISO 9660)"]
---
**Answer: normally no (if "700 MB" is the whole capacity).**

- A CD-ROM stores data in 2048-byte sectors (the 700 MB is the **nominal formatted capacity of the disc**, about $360{,}000$ sectors $\times$ 2048 B $=737$ MB for an 80-minute disc). Every sector also carries synchronisation, header and **error-correcting codes** (ECC/EDC): these are not part of the 2048 bytes of user data, so the user capacity is only what is quoted.
- A file system must be written on the disc: the **ISO 9660** structures take space: a **system area** (16 sectors, 32 KB), **volume descriptors**, the **path table**, the **directory records** with the file's name and location, and padding at the end. The file therefore needs the data **plus** this overhead.
- With contiguous allocation (ISO 9660 stores each file as one contiguous run, starting block and length) the file itself needs 700 MB ($=734{,}003{,}200$ B if MiB): it would fit only if the disc's capacity exceeds 700 MB plus the overhead (an 80-minute disc with 703 MiB would hold it with about 3 MB to spare); a disc whose total capacity is exactly 700 MB **cannot** hold a 700 MB file.

So a file exactly as large as the nominal capacity does not fit; it must be smaller by the file-system overhead. (Multi-extent or multisession discs add even more overhead.)
