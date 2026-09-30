---
marks: 18
topics: [journaling]
---
(4+4+4+6=18)

i.  **Crash Scenario A:** You are in metadata journaling mode. Crash occurs after data block $D$ is written to disk but before the metadata journal commit record is written. What is the on-disk state after reboot? Is it consistent? Could stale metadata point to new or invalid data?

ii. **Crash Scenario B:** You are in metadata journaling mode. Crash occurs after the metadata commit record is written but before data block $D$ is flushed to disk. What inconsistency can arise?

iii. **Crash Scenario C:** Now assume data journaling mode. Crash occurs after the data block is journaled but before it is written to its home location. Will recovery result in a consistent state? Explain why.

iv. Compare metadata journaling vs. data journaling for performance and durability:

- Which is faster, and why?
- Which guarantees that users will never see garbage data after a crash?
