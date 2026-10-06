---
marks: 10
topics: [fork-process-tree]
kind: code
source: {page: 20}
note: "Printed as 'used combinedly'."
---
A typical OS provides some APIs to create processes. `fork()`, `exec()`, and `wait()` can be used combinedly for that purpose. Write some code that uses these system calls to launch a new child process, have the child executed a program named "hello" (with no arguments), and have the parent wait for the child to complete.
