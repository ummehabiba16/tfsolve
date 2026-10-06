---
marks: 10
topics: [paging]
kind: numerical
source: {page: 30}
note: "Data size printed as '16,386 bytes' (possibly a typo for 16,384)."
---
A computer provides each process with 65,536 bytes of address space divided into pages of 4096 bytes each. A particular program has a text size of 32,768 bytes, a data size of 16,386 bytes, and a stack size of 15,870 bytes. Will this program fit in the machine's address space? Suppose that instead of 4096 bytes, the page size were 512 bytes, would it then fit? Each page must contain either text, data, or stack, not a mixture of two or three of them.
