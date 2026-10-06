---
marks: 10
topics: [symbol-table-management]
kind: diagram
source: {page: 44}
note: "Code printed as shown, including 'fun 1', 'fun 2' and the opening brace on line 10."
---
Draw spaghetti stack interpretation of symbol table for the code snippet. Mention line number in each entry of the spaghetti stack.

```text
 1   int a,b;
 2   int fun 1(int x, int y){
 3       int a,x;
 4       {
 5           int b,y;
 6       }
 7       {
 8           int a, x, y;
 9       }
10   {
11   int fun 2 (int c, int d){
12       int a, b, c;
13   }
```
