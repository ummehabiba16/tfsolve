---
marks: 15
topics: [raid]
---
Alice was studying different RAID systems. She particularly liked RAID level 5 for its all-around performance. However, one aspect she didn't like was that RAID 5 cannot tolerate more than one disk failure. So, she took matters into her own hands and designed a modified RAID level, which she called RAID-5X. As you may recall, in RAID 5, data and parity are striped across all disks. In RAID-5X, the only modification is that **parity blocks are written twice**:

I.  Once in the usual rotating parity position.

II. Again, on a fixed disk dedicated to parity backup.

Now, Alice knows you are an OS expert. She has come to you to validate her system (5+2+8=15).

i.  Will the reliability increase in practice?

ii. What will be the effective capacity of the system?

iii. Analyze the performance under random and sequential read and write workloads.
