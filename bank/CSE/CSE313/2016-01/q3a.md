---
marks: 10
topics: [fork-process-tree]
kind: analysis
source: {page: 52}
params:
  type: fork_loop
  initial_i: 0
  loop_bound: 3
  root: Root
  asks: [process_tree, starting_i_per_node]
---
Consider the code written in C shown in the following figure. Here **fork()** is an UNIX system call that creates a child process identical to the parent. Executing this code will generate a process tree. Each of the created process will have its own copy of variable **i**. Your task is to draw this process tree. At each node of the tree you have to mention the starting value of **i** for the corresponding process. The root node is shown in the next figure. Draw the complete process tree appropriately.

```c
#include <stdio.h>
#include <unistd.h>
int i = 0;
int main()
{
    for (; i < 3 ; i++)
        fork();
    return 0;
}
```

*Figure for Q. No. 3(a):* the root node is labelled "Root, i = 0".
