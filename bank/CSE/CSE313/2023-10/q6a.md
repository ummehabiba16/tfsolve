---
marks: 28
topics: [io-devices, files-directories]
---
The following function writes a sequence of $n$ numbers to a given file descriptor `fd`.

```c
void write_fd(int fd, int n){
    char buf[10];
    for (int i = 0; i < n; i++) {
        itoa(i, buf, 10);
        write(fd, buf, strlen(buf));
    }
}
```

($5\times3+13=28$)

i.  For each of the following possible values of $n$, design a device driver where `write_fd` is called frequently with $n$. Explain your design decisions using illustrative pseudocodes.

(a) always 10

(b) always 1000000

(c) mixture of 10 and 1000000

ii. What is the difference of output from the following two code blocks? Analyze with necessary figures and arguments showing what happens in the kernel.

**Code block 1**

```c
int fd1 = open("file.txt");
int fd2 = open("file.txt");
write_fd(fd1);
write_fd(fd2);
```

**Code block 2**

```c
int fd1 = open("file.txt");
int fd2 = dup(fd1);
write_fd(fd1);
write_fd(fd2);
```
