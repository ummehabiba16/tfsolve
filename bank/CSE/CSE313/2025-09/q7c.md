---
marks: 10
topics: [journaling]
---
Bob was studying different kinds of journaling techniques, including data journaling and metadata journaling. He was fascinated to learn about the corner case where the disk may crash during journal writes. To handle such situations, the concept of transaction commit was introduced --- where the TxE block is written only after all previous blocks in the journal transaction are successfully written. However, Bob was concerned that waiting for all previous blocks to be written before committing the transaction would make writes too slow. So, he proposed a new solution:

> *A 32-bit checksum will be computed over all the blocks in the transaction, excluding the TxB (Transaction Begin) and TxE (Transaction End) blocks. This checksum will be stored in both the TxB and TxE blocks. After a crash, the validity of the journal transaction can be verified by computing the checksum of the journaled data and comparing it against the checksums in TxB and TxE.*

Now, Bob knows you are an OS expert. He has come to you to validate his journaling system (6+4=10):

i.  Does the proposed solution have any correctness issues for both data journaling and metadata journaling?

ii. Will the write performance really improve? Are there any hidden drawbacks?
