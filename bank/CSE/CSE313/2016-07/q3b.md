---
marks: 10
topics: [fork-process-tree]
kind: analysis
source: {page: 46}
---
Consider the following program:

```c
int main(int argc, char *argv[]) {
    int child = fork();
    int x = 10;
    if(child) {
        x += 10;
    } else {
        child = fork();
        x += 10;
        if(child == 0) {
            x += 10;
        }
    }
    return 0;
}
```

How many different copies of the variable **x** are there? What are their values when their processes finish?
