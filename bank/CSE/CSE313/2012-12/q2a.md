---
marks: 10
topics: [unix-inodes]
kind: code
source: {page: 67}
---
What is reference count and link count of an inode? [see iput algorithm in Fig. 2]

```text
algorithm iput              /* release (put) access to in-core inode */
input:  pointer to in-core inode
output: none
{
    lock inode if not already locked;
    decrement inode reference count;
    if (reference count == 0)
    {
        if (inode link count == 0)
        {
            free disk blocks for file (algorithm free, section 4.7);
            set file type to 0;
            free inode (algorithm ifree, section 4.6);
        }
        if (file accessed or inode changed or file changed)
            update disk inode;
        put inode on free list;
    }
    release inode lock;
}
```

*Fig 2. iput algorithm*
