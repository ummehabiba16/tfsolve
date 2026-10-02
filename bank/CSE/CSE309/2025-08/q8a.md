---
marks: 15
topics: [garbage-collection, heap-management]
kind: code
source: {page: 7}
note: "Printed as 'attempt of improve'."
---
What are 'temporal locality' and 'spatial locality' in the context of a program execution? How does a garbage collector (GC) attempt of improve these two types of 'locality of reference'? Each garbage collection algorithm starts with a 'root set'. Which objects constitute the 'root set'? Consider below the pseudocode for Cheney's 'copying collector' from your text. Complete the code by defining the function '*LookupNewLocation*'.

```text
 1)  CopyingCollector () {
 2)      for (all objects o in From space) NewLocation(o) = NULL;
 3)      unscanned = free = starting address of To space;
 4)      for (each reference r in the root set)
 5)          replace r with LookupNewLocation(r);
 6)      while (unscanned != free) {
 7)          o = object at location unscanned;
 8)          for (each reference o.r within o)
 9)              o.r = LookupNewLocation(o.r);
10)          unscanned = unscanned + sizeof(o);
         }
     }
```
