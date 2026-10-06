---
marks: 10
topics: [vsfs, files-directories]
kind: analysis
source: {page: 23}
---
A program named `test` execute some code and writes some test to the console. The program is executed as:

```bash
./test > /etc/out.txt
```

Now, write down the timeline for read/write operation in the file system. Assume that it is vsfs (very simple file system) and there is no cached value to aid.
