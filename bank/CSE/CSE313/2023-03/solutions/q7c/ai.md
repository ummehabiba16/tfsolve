---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Track skew offsets sector numbering of adjacent tracks so a sequential read across a track boundary does not miss a rotation; modern disks hide geometry (zones, track buffers, remapping), so a fixed skew is not meaningful."
sources: ["OSTEP ch. 37 (HDDs, track skew)"]
---
**Track skew.** The sector numbers of each track are *shifted* (skewed) relative to the previous track by the number of sectors that pass under the head while the arm moves to the adjacent track.

**Why it was required.** In sequential reading, after the last sector of one track the head must move to the next track (a track-to-track seek). If sector $0$ of the next track were exactly below the head's old position, it would have rotated past during the seek and the disk would have to wait almost a **full rotation** to read it. With the skew, the next sector arrives just as the head settles, so sequential reads across tracks run at full speed.

**Why it is not good for newer disks.**

- Modern disks hide their geometry behind logical block addresses and use **zoned recording**: outer tracks have more sectors than inner ones, so one fixed skew value is wrong for different zones.
- The firmware **remaps** bad sectors and has a **track buffer/cache** that reads whole tracks ahead, so the physical layout that the OS assumed no longer exists.
- Seek and head-switch times differ between drives, so the best skew is drive-specific; the drive's firmware chooses it internally. (SSDs have no tracks at all.)
