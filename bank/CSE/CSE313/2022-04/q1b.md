---
marks: 10
topics: [fork-process-tree]
kind: analysis
source: {page: 25}
params:
  type: fork_loop
  initial_i: 0
  loop_bound: 3
  root: P0
  asks: [process_tree, starting_i_per_node]
---
Consider the code written in C shown in the following figure. Here fork() is an UNIX system call that creates a child process identical to the parent. Executing this code will generate a process tree. Each of the created processes will have its own copy of variable i. Your task is to draw this process tree. At each node of the tree, you have to mention the starting value of i for the corresponding process. Consider that the root process is called P0.

*Code for Question 1(b)*

```c
int i = 0;
int main() {
    for (; i < 3; i++) {
        fork();
    }
    return 0;
}
```
