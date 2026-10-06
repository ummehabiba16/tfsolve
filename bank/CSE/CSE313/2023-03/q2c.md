---
marks: 15
topics: [fork-process-tree]
kind: analysis
source: {page: 19}
note: "The scan shows margin line numbers 1-21; the number 11 looks to be skipped (10 is followed by 12). The numbers are not reproduced here."
---
Consider the following program:

```c
int main{
    int count =1;
    int pid = 0, pid2 = 0;
    if ((pid = fork())) {
        count = count + 2;
        printf("%d ", count);
    }

    if (count == 1) {
        count++;
        pid2=fork();
        printf("%d ", count);
    }

    if (pid2) {
        wait(pid2, NULL, 0);
        count = count * 2;
        printf("%d ", count);
    }
}
```

i. How many processes are created during the execution of this program? Explain briefly.

ii. List all the possible outputs of the program.
