---
marks: 15
topics: [producer-consumer-race]
kind: code
source: {page: 54-55}
---
Assume that a finite number of resources of a single resource type must be managed. Processes may ask for a number of these resources and will return them once finished. As an example, many commercial software packages provide a given number of licenses, indicating the number of applications that may run concurrently. When the application is started, the license count is decremented. When the application is terminated, the license count is incremented. If all licenses are in use, requests to start the application are denied. Such requests will only be granted when an existing license holder terminates the application and a license is returned.

The following program segment is used to manage a finite number of instances of an available resource. The maximum number of resources and the number of available resources are declared as follows:

```c
#define MAX_RESOURCES 5
int available_resources = MAX_RESOURCES;
```

When a process wishes to obtain a number of resources, it invokes the `decrease_count()` function (line numbers 3-13 in the paper):

```c
/* decrease available_resources by count resources */
/* return 0 if sufficient resources available, */
/* otherwise return -1 */
int decrease_count(int count) {
    if (available_resources < count)
        return -1;
    else {
        available_resources -= count;
        return 0;
    }
}
```

When a process wants to return a number of resources, it calls the `increase_count()` function (lines 14-17 in the paper):

```c
/* increase available_resources by count */
void increase_count(int count) {
    available_resources += count;
}
```

The preceding program segment produces race condition.

(i) Identify the data involved in the race condition.

(ii) Mention the line number (or numbers) of the statement (or statements) in the above code which is (or are) responsible for the race condition. *(Line numbers 1-17 are printed on the paper: 1-2 the declarations, 3-5 comments, 6 the `decrease_count` header, 7-8 the `if`/`return -1`, 9 `else {`, 10 `available_resources -= count;`, 11 `return 0;`, 12-13 closing braces, 14 comment, 15 `increase_count` header, 16 `available_resources += count;`, 17 `}`.)*

(iii) Using a single binary semaphore, fix the race condition. You must rewrite the complete code. Make sure that your fixed version of `decrease_count()` returns 0 if sufficient resources are available and -1 otherwise.
